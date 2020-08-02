/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 1:58 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{
    cell::RefMut,
    collections::HashMap,
    hash::{Hash, Hasher},
    path::Path,
    rc::Rc,
};

use inkwell::{
    basic_block::BasicBlock,
    builder::Builder,
    context::Context,
    module::Module,
    types::{BasicType, BasicTypeEnum},
    values::{BasicValueEnum, FunctionValue, PointerValue},
};

use crate::ir::{
    nodes::{Function, Type, Variable},
    MModule, MutRc,
};
use inkwell::{passes::PassManager, types::StructType, AddressSpace::Generic};

mod gc;
mod gen_expr;
mod intrinsics;
mod types;
mod values;

/// A generator that creates LLVM IR out of Gelix mid-level IR (MIR).
///
/// Will panic when encountering invalid code; this should not happen however thanks to the
/// `MIRGenerator` validating the MIR it generates.
pub struct IRGenerator {
    context: Context,
    builder: Builder,
    module: Module,
    mpm: PassManager<Module>,

    /// The currently compiled function.
    function: Option<FunctionValue>,

    /// All variables in the currently compiled function.
    /// Note that not all variables are valid - they are kept after going out of scope.
    /// This is not an issue since the MIR generator checked against this already.
    variables: HashMap<PtrEqRc<Variable>, PointerValue>,
    /// All local stores in this function that need their refcount
    /// to be decremented when the function returns.
    /// This also includes locally declared variables.
    /// This is a vector to account for local variables that are not available
    /// during all parts of the function - locals declared inside of an if clause for example.
    ///
    /// The `bool` specifies if the value is a pointer or a value in
    /// the context of the MIR type system.
    locals: Vec<Vec<(BasicValueEnum, bool)>>,
    /// All blocks in the current function.
    blocks: Vec<BasicBlock>,
    last_block: Option<BasicBlock>,

    /// All functions.
    functions: HashMap<PtrEqRc<Variable>, FunctionValue>,
    /// All types (classes/interfaces/structs) that are available.
    /// The GlobalValue is a pointer to a static struct containing type
    /// information. All values have a pointer to this struct in them.
    types: HashMap<Type, (BasicTypeEnum, PointerValue)>,
    /// A map of types based on their names in IR to allow for backwards lookup.
    types_bw: HashMap<String, Type>,

    /// A constant that is used for expressions that don't produce a value but are required to,
    /// like return or break expressions.
    none_const: BasicValueEnum,
    /// The type for type info that is baked into every value
    type_info_type: StructType,

    /// Needed state about the current loop, if compiling one.
    loop_data: Option<LoopData>,
}

impl IRGenerator {
    /// Generates IR. Will process all MIR modules given.
    pub fn generate(mut self, mir: Vec<MutRc<MModule>>) -> Module {
        for module in &mir {
            let module = module.borrow_mut();
            for function in module.globals.values() {
                self.declare_function(function);
            }
        }

        let intrinsics_module = mir.iter().find(|m| {
            let module = m.borrow();
            **module.path.0[0] == *"std" && **module.path.0[1] == *"intrinsics"
        });
        self.fill_intrinsic_functions(intrinsics_module.unwrap());

        for module in mir {
            let module = module.borrow_mut();
            for function in module.globals.values() {
                self.function(&function);
            }
        }

        self.module
            .verify()
            .map_err(|e| {
                self.module.print_to_file(Path::new("invalid_code.ll")).unwrap_or(());
                println!("The compiler generated invalid code, which can be found in the 'invalid_code.ll'.");
                println!("This is a bug, and should be reported (please include the code when doing so).");
                println!("The error message reported by LLVM:\n");
                println!("{}\n", e.to_string().replace("\\n", "\n"));
                std::process::exit(1);
            })
            .unwrap();
        self.mpm.run_on(&self.module);
        self.module
    }

    /// Declares a function. All functions must be declared before generating
    /// code; as a reference to an undeclared function is otherwise possible
    /// (and leads to a panic)
    fn declare_function(&mut self, func: &Rc<Variable>) {
        let func_ty = func.type_.as_function();
        let fn_ty = self.build_fn_type(func_ty.borrow());
        let func_val = self
            .module
            .add_function(&func_ty.borrow().name, fn_ty, None);
        self.functions.insert(PtrEqRc::new(&func), func_val);
    }

    /// Generates a function, should it have a body.
    fn function(&mut self, func_var: &Rc<Variable>) {
        let func_ty = func_var.type_.as_function();
        let func = func_ty.borrow_mut();
        if !func.exprs.is_empty() {
            let func_val = self.functions[&PtrEqRc::new(&func_var)];
            self.function_body(func, func_val);
        }
    }

    /// Generates a function's body.
    fn function_body(&mut self, func: RefMut<Function>, func_val: FunctionValue) {
        self.function = Some(func_val);
        self.blocks.clear();

        self.prepare_function(&func, func_val);

        for (name, var) in &func.variables {
            let alloc_ty = self.ir_ty_ptr(&var.type_);
            let alloca = self.builder.build_alloca(alloc_ty, &name);
            self.variables.insert(PtrEqRc::new(var), alloca);
        }

        for expr in &func.exprs {
            self.expression(expr);
        }

        // Build a return if the end of the function is an implicit return
        if self.builder.get_insert_block().is_some() {
            self.decrement_all_locals();
            self.builder.build_return(None);
        }

        self.variables.clear();
    }

    /// Given a function, will do steps needed to allow code generation, starting
    /// with resetting function-specific state.
    /// It inserts the entry BB in IR, and build all parameter alloca.
    /// self.builder will be positioned after the entry alloca after calling this method.
    /// Returns the entry basic block.
    fn prepare_function(&mut self, func: &RefMut<Function>, func_val: FunctionValue) {
        self.blocks.clear();
        self.variables.clear();
        self.locals.clear();
        self.locals.push(Vec::with_capacity(3));

        let entry_bb = self.context.append_basic_block(&func_val, "entry");
        self.blocks.push(entry_bb);

        self.position_at_block(entry_bb);
        self.build_parameter_alloca(&func, func_val);
    }

    fn build_parameter_alloca(&mut self, func: &RefMut<Function>, func_val: FunctionValue) {
        for (arg, arg_val) in func.parameters.iter().zip(func_val.get_param_iter()) {
            if let Type::ClosureCaptured(captured) = &arg.type_ {
                // If this is the first arg on a closure containing all captured variables,
                // 'unpack' them and create separate entries for each in self.variables
                // so they can be used like regular variables.
                let arg_val = *arg_val.as_pointer_value();
                for (i, var) in captured.iter().enumerate() {
                    let field = self.struct_gep(arg_val, i);
                    self.variables.insert(PtrEqRc::new(var), field);
                }
            } else if let BasicValueEnum::PointerValue(ptr) = arg_val {
                // If the type of the function parameter is a pointer (aka a struct or function),
                // creating an alloca isn't needed; the pointer can be used directly.
                self.variables.insert(PtrEqRc::new(arg), ptr);
            } else {
                let alloc = self.builder.build_alloca(arg_val.get_type(), &arg.name);
                self.builder.build_store(alloc, arg_val);
                self.variables.insert(PtrEqRc::new(arg), alloc);
            }
        }
    }

    fn position_at_block(&mut self, block: BasicBlock) {
        self.last_block = Some(block);
        self.builder.position_at_end(&block)
    }

    pub fn append_block(&mut self, name: &'static str) -> BasicBlock {
        let bb = self
            .context
            .append_basic_block(&self.function.unwrap(), name);
        self.blocks.push(bb);
        bb
    }

    pub fn last_block(&self) -> BasicBlock {
        self.last_block.unwrap()
    }

    pub fn new() -> IRGenerator {
        let context = Context::create();
        let module = context.create_module("main");
        let builder = context.create_builder();

        let mpm = PassManager::create(());
        mpm.add_instruction_combining_pass();
        mpm.add_reassociate_pass();
        mpm.add_basic_alias_analysis_pass();
        mpm.add_instruction_combining_pass();
        mpm.add_reassociate_pass();

        let none_const = context
            .struct_type(&[BasicTypeEnum::IntType(context.bool_type())], true)
            .const_named_struct(&[BasicValueEnum::IntValue(
                context.bool_type().const_int(0, false),
            )]);

        let mut types = HashMap::with_capacity(50);
        let null_ptr = context.i64_type().ptr_type(Generic).const_null();
        Self::insert_primitive(
            &mut types,
            Type::None,
            none_const.get_type().into(),
            null_ptr,
        );
        Self::insert_primitive(&mut types, Type::Bool, context.bool_type().into(), null_ptr);

        Self::insert_primitive(&mut types, Type::I8, context.i8_type().into(), null_ptr);
        Self::insert_primitive(&mut types, Type::I16, context.i16_type().into(), null_ptr);
        Self::insert_primitive(&mut types, Type::I32, context.i32_type().into(), null_ptr);
        Self::insert_primitive(&mut types, Type::I64, context.i64_type().into(), null_ptr);
        Self::insert_primitive(&mut types, Type::U8, context.i8_type().into(), null_ptr);
        Self::insert_primitive(&mut types, Type::U16, context.i16_type().into(), null_ptr);
        Self::insert_primitive(&mut types, Type::U32, context.i32_type().into(), null_ptr);
        Self::insert_primitive(&mut types, Type::U64, context.i64_type().into(), null_ptr);

        Self::insert_primitive(&mut types, Type::F32, context.f32_type().into(), null_ptr);
        Self::insert_primitive(&mut types, Type::F64, context.f64_type().into(), null_ptr);

        let type_info_type = context.struct_type(&[context.i64_type().into()], false);

        IRGenerator {
            context,
            module,
            builder,
            mpm,
            function: None,

            variables: HashMap::with_capacity(10),
            locals: Vec::with_capacity(10),
            blocks: Vec::with_capacity(10),
            last_block: None,

            types,
            types_bw: HashMap::with_capacity(50),
            functions: HashMap::with_capacity(10),

            type_info_type,
            none_const: none_const.into(),
            loop_data: None,
        }
    }

    fn insert_primitive(
        types: &mut HashMap<Type, (BasicTypeEnum, PointerValue)>,
        ty: Type,
        ir: BasicTypeEnum,
        null_ptr: PointerValue,
    ) {
        types.insert(ty.clone(), (ir, null_ptr));
        types.insert(
            Type::Pointer(Box::new(ty)),
            (ir.ptr_type(Generic).into(), null_ptr),
        );
    }
}

pub struct LoopData {
    /// The block to jump to using break expressions;
    /// the block at the end of the loop.
    pub end_block: BasicBlock,
    pub phi_nodes: Option<Vec<(BasicValueEnum, BasicBlock)>>,
}

/// A Rc that can be compared by checking for pointer equality.
/// Used as a `HashMap` key to allow unique keys with the same data.
#[derive(Debug)]
pub struct PtrEqRc<T: Hash>(Rc<T>);

impl<T: Hash> PtrEqRc<T> {
    pub fn new(rc: &Rc<T>) -> PtrEqRc<T> {
        PtrEqRc(Rc::clone(rc))
    }
}

impl<T: Hash> PartialEq for PtrEqRc<T> {
    fn eq(&self, other: &Self) -> bool {
        Rc::ptr_eq(&self.0, &other.0)
    }
}

impl<T: Hash> Eq for PtrEqRc<T> {}

impl<T: Hash> Hash for PtrEqRc<T> {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.0.hash(state)
    }
}
