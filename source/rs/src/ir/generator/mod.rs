/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 7:26 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{
    collections::{HashMap, HashSet},
    mem,
    rc::Rc,
};

use either::Either;
use indexmap::IndexMap;

use crate::{
    ast,
    ast::{
        declaration::{Constructor, Function as ASTFunc},
        expression::Expression as ASTExpr,
    },
    error::Res,
    scanner::token::{TType, Token},
    ir::{
        generator::{builder::MIRBuilder, intrinsics::INTRINSICS},
        get_iface_impls,
        nodes::{ADTMember, ADTType, Expr, Function, Prototype, Type, Variable},
        result::ToMIRResult,
        MModule, MutRc, IFACE_IMPLS,
    },
    Error,
};

pub mod builder;
pub mod gen_expr;
pub mod intrinsics;
pub mod module;
pub mod passes;

pub type Environment = HashMap<Rc<String>, Rc<Variable>>;

/// The `MIRGenerator` turns a list of declarations produced by the parser
/// into their MIR representation.
///
/// MIR is an intermediate format between the AST and LLVM IR.
///
/// The generator not only generates MIR, but also checks the code
/// for correctness (type-checking, scoping, etc.).
pub struct MIRGenerator {
    /// The module that the generator is linked to.
    pub module: MutRc<MModule>,

    /// The builder used to build the MIR.
    pub builder: MIRBuilder,

    /// The current insertion position.
    position: Option<Pointer>,

    /// An environment is a scope that variables live in.
    /// This field is used like a stack.
    /// See the begin_scope and end_scope functions for more info.
    environments: Vec<Environment>,

    /// The current loop, if in one.
    current_loop: Option<ForLoop>,

    /// All class members that are not initialized yet.
    /// This is only used when generating constructors to check
    /// that all constructors don't access uninitialized fields,
    /// and initialize all fields when finished.
    ///
    /// Because of this, calling is_empty() on this set
    /// can be used to determine if 'this' is fully
    /// initialized yet and if methods can be used.
    ///
    /// TODO: The code checking for illegal uninitialized access
    /// does not validate that the object the access occurs on is 'this'.
    /// Because of this, accesses of members on other objects of the same type
    /// (that ARE initialized) will be considered illegal.
    uninitialized_this_members: HashSet<Rc<ADTMember>>,

    /// Closure-related data, if compiling a closure.
    closure_data: Option<ClosureData>,
}

impl MIRGenerator {
    /// Fill a function's body.
    /// The AST given must be from a function inside the module.
    pub fn generate_function(
        &mut self,
        func: &ASTFunc,
        override_fn: Option<&MutRc<Function>>,
    ) -> Res<()> {
        // Don't have to generate anything for external functions
        // which do not have a body
        let body = match func.body.as_ref() {
            None => return Ok(()),
            Some(body) => body,
        };

        let function = override_fn.cloned().unwrap_or_else(|| {
            self.module
                .borrow()
                .find_type(&func.sig.name.lexeme)
                .unwrap()
                .as_function()
                .clone()
        });
        self.prepare_function(&function, func.sig.name.line)?;
        let body = self.expression(body)?;

        let ret_type = function.borrow().ret_type.clone();
        let body = self.try_cast(body, &ret_type);
        match () {
            _ if ret_type == Type::None => self.insert_at_ptr(body),
            _ if ret_type == body.get_type() => self.insert_at_ptr(Expr::ret(body)),
            _ => Err(self.err(
                &func.sig.name,
                &format!(
                    "Function return type ({}) does not match body type ({}).",
                    ret_type,
                    body.get_type()
                ),
            ))?,
        };

        self.end_scope();
        Ok(())
    }

    /// Generate all constructors of the given ADT.
    /// ADT should already be defined in MIR.
    pub fn generate_constructors(
        &mut self,
        adt: &ast::ADT,
        constructors: &[ast::Constructor],
    ) -> Res<()> {
        let adt_rc = self
            .module
            .borrow()
            .find_type(&adt.name.lexeme)
            .unwrap()
            .as_adt()
            .clone();

        for (constructor, mir_fn) in constructors.iter().zip(
            adt_rc
                .borrow()
                .constructors
                .iter()
                .map(|v| v.type_.as_function()),
        ) {
            self.prepare_function(
                mir_fn,
                constructor.parameters.get(0).map_or(0, |l| l.0.line),
            )?;
            self.set_uninitialized_members(constructor, &adt_rc.borrow().members);
            if let Some(body) = &constructor.body {
                let body = self.expression(body)?;
                self.insert_at_ptr(body);
            }
            self.end_scope();
            self.check_no_uninitialized(&adt.name)?;
        }

        self.uninitialized_this_members.clear();
        Ok(())
    }

    fn set_uninitialized_members(
        &mut self,
        constructor: &Constructor,
        class_mems: &IndexMap<Rc<String>, Rc<ADTMember>>,
    ) {
        self.uninitialized_this_members.clear();
        for (name, mem) in class_mems.iter() {
            let initialized = constructor
                .parameters
                .iter()
                .filter(|p| p.1.is_none())
                .any(|p| &p.0.lexeme == name);
            if !initialized && !mem.has_default_value {
                self.uninitialized_this_members.insert(Rc::clone(&mem));
            }
        }
    }

    fn check_no_uninitialized(&mut self, err_tok: &Token) -> Res<()> {
        if self.uninitialized_this_members.is_empty() {
            Ok(())
        } else {
            Err(self.err(
                err_tok,
                "Cannot have uninitialized fields after constructor.",
            ))
        }
    }

    /// Will append an 'entry' block to the fn and set the pointer at
    /// that location, then insert all parameters as variables.
    fn prepare_function(&mut self, function: &MutRc<Function>, err_line: usize) -> Res<()> {
        let func = function.borrow();

        self.set_pointer(Rc::clone(function));
        self.begin_scope();
        for param in &func.parameters {
            self.insert_variable(&param, false, err_line)?;
        }

        Ok(())
    }

    /// Defines a new variable. It is put into the variable list in the current function
    /// and placed in the topmost scope.
    fn define_variable(&mut self, token: &Token, mutable: bool, ty: Type) -> Rc<Variable> {
        let def = Variable::new(mutable, ty, &token.lexeme);
        self.add_function_variable(Rc::clone(&def));
        self.insert_variable(&def, true, token.line).unwrap_or(());
        def
    }

    /// Inserts a variable into the topmost scope.
    /// Note that the variable does NOT get added to the function!
    fn insert_variable(
        &mut self,
        var: &Rc<Variable>,
        allow_redefine: bool,
        line: usize,
    ) -> Res<()> {
        let cur_env = self.environments.last_mut().unwrap();
        let was_defined = cur_env
            .insert(Rc::clone(&var.name), Rc::clone(&var))
            .is_some();
        if was_defined && !allow_redefine {
            let mut tok = Token::generic_identifier((*var.name).clone());
            tok.line = line;
            return Err(self.err(
                &tok,
                &format!(
                    "Cannot redefine variable '{}' in the same scope.",
                    &var.name
                ),
            ));
        }

        Ok(())
    }

    /// Will insert the variable into the current function.
    pub fn add_function_variable(&mut self, variable: Rc<Variable>) {
        self.cur_fn()
            .borrow_mut()
            .insert_var(Rc::clone(&variable.name), variable);
    }

    /// Searches all scopes for a variable, starting at the top.
    fn find_var(&mut self, token: &Token) -> Option<Rc<Variable>> {
        for env in self.environments.iter().rev() {
            if let Some(var) = env.get(&token.lexeme) {
                return Some(Rc::clone(var));
            }
        }

        if let Some(closure_data) = &mut self.closure_data {
            for env in closure_data.outer_env.iter().rev() {
                if let Some(var) = env.get(&token.lexeme) {
                    closure_data.captured.push(Rc::clone(var));
                    return Some(Rc::clone(var));
                }
            }
        }

        self.module.borrow().find_global(&token.lexeme)
    }

    /// Returns the variable of the current loop or creates it if it does not exist yet.
    /// This variable stores the value of the last loop iteration.
    fn get_or_create_loop_var(&mut self, type_: &Type) -> Res<Rc<Variable>> {
        let var = self.cur_loop().result_var.clone().unwrap_or_else(|| {
            self.define_variable(
                &Token::generic_identifier("for-body".to_string()),
                true,
                type_.clone(),
            )
        });
        self.cur_loop().result_var = Some(Rc::clone(&var));

        if &var.type_ == type_ {
            Ok(var)
        } else {
            Err(Error::new(
                &Token::generic_token(TType::Break),
                "MIR",
                "Break expressions and for body must have same type".to_string(),
                &self.builder.path,
            ))
        }
    }

    /// Returns a field of the given expression/object,
    /// where a field can be either a member or an associated method.
    fn get_field(
        &mut self,
        object: &ASTExpr,
        name: &Token,
    ) -> Res<(Expr, Either<Rc<ADTMember>, AssociatedMethod>)> {
        let object = self.expression(object)?;
        let ty = object.get_type();

        if let Type::Adt(adt) = &ty {
            let adt = adt.borrow();
            let field = adt.members.get(&name.lexeme);
            if let Some(field) = field {
                return Ok((object, Either::Left(Rc::clone(field))));
            }
        }

        Self::find_associated_method(&ty, name)
            .map(|m| (object, Either::Right(m)))
            .or_err(&self.builder.path, name, "Unknown field or method.")
    }

    /// Check a function call's arguments for correctness,
    /// possibly adding a cast if required.
    fn check_func_args<'a, T: Iterator<Item = &'a Type>>(
        &mut self,
        mut parameters: T,
        args: &mut Vec<Expr>,
        ast_args: &[ASTExpr],
        allow_variadic: bool,
        err_tok: &Token,
        is_method: bool,
    ) -> Res<()> {
        let para_len = parameters.size_hint().0;
        if para_len > args.len() || (para_len < args.len() && !allow_variadic) {
            return Err(self.err(
                err_tok,
                &format!(
                    "Incorrect amount of function arguments. (Expected {}; got {})",
                    parameters.size_hint().0,
                    args.len()
                ),
            ));
        }

        // Sometimes, methods need their "this" arg to be cast (enum case calling a parent func for example)
        // Since parameters are an iterator it needs to be done now
        if is_method {
            // Remove the "this" argument to get ownership using swap_remove, last arg is now
            // swapped into index 0
            let arg = self.try_cast(args.swap_remove(0), parameters.next().unwrap());
            // Put "this" arg at the end and swap them again
            let this_index = args.len();
            args.push(arg);
            args.swap(0, this_index);
            // (This is done since it does not need any copying)
        }

        for ((argument, parameter), ast) in args
            .iter_mut()
            .skip(is_method as usize)
            .zip(parameters)
            .zip(ast_args.iter())
        {
            // The mem::replace usage temporarily swaps out the argument with none_const
            // to get the ownership cast_or_none requires
            let arg_type = argument.get_type();
            let arg = self
                .cast_or_none(mem::replace(argument, Expr::none_const()), &parameter)
                .or_err(
                    &self.builder.path,
                    ast.get_token(),
                    &format!(
                        "Call argument is the wrong type (was {}, expected {})",
                        arg_type, parameter
                    ),
                )?;
            mem::replace(argument, arg);
        }

        Ok(())
    }

    /// Same as above, but takes a function instead.
    /// `func` should be `Type::Function` or `Type::Closure`, otherwise returns an error.
    pub fn check_func_args_(
        &mut self,
        func: &Type,
        args: &mut Vec<Expr>,
        ast_args: &[ASTExpr],
        err_tok: &Token,
        is_method: bool,
    ) -> Res<()> {
        match func {
            Type::Function(func) => self.check_func_args(
                func.borrow().parameters.iter().map(|p| &p.type_),
                args,
                ast_args,
                func.borrow().ast.as_ref().map_or(false, |a| a.sig.variadic),
                err_tok,
                is_method,
            ),

            Type::Closure(closure) => self.check_func_args(
                closure.parameters.iter(),
                args,
                ast_args,
                false,
                err_tok,
                is_method,
            ),

            _ => Err(self.err(err_tok, "This cannot be called.")),
        }
    }

    /// Searches for an associated method on a type. Can be either an interface
    /// method or a class method.
    fn find_associated_method(ty: &Type, name: &Token) -> Option<AssociatedMethod> {
        let method = if let Type::Adt(adt) = &ty {
            let adt = adt.borrow();
            adt.methods
                .get(&name.lexeme)
                .cloned()
                .map(AssociatedMethod::Fn)
                .or_else(|| {
                    adt.proto_methods
                        .get(&name.lexeme)
                        .cloned()
                        .map(AssociatedMethod::Proto)
                })
                .or_else(|| {
                    adt.dyn_methods
                        .get_full(&name.lexeme)
                        .map(|(i, _, _)| AssociatedMethod::IFace(i))
                })
        } else {
            None
        };

        method.or_else(|| {
            IFACE_IMPLS
                .with(|impls| impls.borrow().get(&ty).cloned())?
                .borrow()
                .methods
                .get(&name.lexeme)
                .cloned()
                .map(AssociatedMethod::Fn)
        })
    }

    /// Returns the method that corresponds to the operator given (operator overloading).
    /// Returns None if the given class does not implement overloading.
    fn get_operator_overloading_method(
        &self,
        op: TType,
        left_ty: &Type,
        right: &mut Expr,
    ) -> Option<Rc<Variable>> {
        let proto = INTRINSICS.with(|i| i.borrow().get_op_iface(op))?;
        let iface_impls = get_iface_impls(left_ty)?;
        let iface_impls = iface_impls.borrow();

        for im in iface_impls.interfaces.values() {
            match im.iface.borrow().ty {
                ADTType::Interface { proto: Some(ref p) } if Rc::ptr_eq(&proto, &p) => {
                    let method = im.methods.get_index(0).unwrap().1;
                    let ty = &method.type_.as_function().borrow().parameters[1].type_;
                    self.try_cast_in_place(right, ty);
                    if *ty == right.get_type() {
                        return Some(method).cloned();
                    }
                }
                _ => (),
            }
        }
        None
    }

    /// Will cast value to ty, if needed.
    /// If the cast is not possible, returns None.
    fn cast_or_none(&self, value: Expr, ty: &Type) -> Option<Expr> {
        let value = self.try_cast(value, ty);
        if &value.get_type() == ty {
            Some(value)
        } else {
            None
        }
    }

    /// Checks if the value is of the given type ty.
    /// Will do casts if needed to make the types match;
    /// returns the new expression that should be used in case a cast happened.
    /// If there is no way to make `value.get_type() == ty`,
    /// this function just returns value unmodified.
    fn try_cast(&self, value: Expr, ty: &Type) -> Expr {
        let val_ty = value.get_type();
        if val_ty.can_cast_to(ty) {
            Expr::maybe_cast(value, &val_ty, ty)
        } else {
            value
        }
    }

    /// Same as above but utilizing `std::mem::replace` to only
    /// require a mutable reference at the cost of a slight performance penalty.
    /// Returns if the cast was successful.
    fn try_cast_in_place(&self, value_ref: &mut Expr, ty: &Type) {
        let value = mem::replace(value_ref, Expr::none_const());
        mem::replace(value_ref, self.try_cast(value, ty));
    }

    /// Will try to make left and right be of the same type.
    /// Return value is `(NewType, left, right)`.
    /// If both are already the same type, this will just return the original type.
    /// If they cannot be made to match, it returns None as type.
    fn try_unify_type(&self, mut left: Expr, mut right: Expr) -> (Option<Type>, Expr, Expr) {
        let left_ty = left.get_type();
        let right_ty = right.get_type();

        match (&left_ty, &right_ty) {
            _ if left_ty == right_ty => return (Some(left_ty), left, right),

            // Number cast
            _ if (left_ty.is_int() && right_ty.is_int())
                || left_ty.is_float() && right_ty.is_float() =>
            {
                let right = self.try_cast(right, &left_ty);
                return (Some(left_ty), left, right);
            }

            // Can be either interface and implementor, enum cases or enum and a case
            (Type::Adt(_), Type::Adt(_)) => {
                left = self.try_cast(left, &right_ty);
                right = self.try_cast(right, &left_ty);
                let left_ty = left.get_type();
                let right_ty = right.get_type();

                if left_ty == right_ty {
                    return (Some(left_ty), left, right);
                } else if let (
                    ADTType::EnumCase { parent: p1, .. },
                    ADTType::EnumCase { parent: p2, .. },
                ) = (
                    &left_ty.as_adt().borrow().ty,
                    &right_ty.as_adt().borrow().ty,
                ) {
                    if Rc::ptr_eq(p1, p2) {
                        let ty = Type::Adt(Rc::clone(&p1));
                        return (
                            Some(ty.clone()),
                            Expr::cast(left, &ty),
                            Expr::cast(right, &ty),
                        );
                    }
                }
            }

            // Can only be interface/implementor
            (Type::Adt(adt), _) | (_, Type::Adt(adt)) => {
                let ty = Type::Adt(Rc::clone(&adt));
                left = self.try_cast(left, &ty);
                right = self.try_cast(right, &ty);

                if left.get_type() == right.get_type() {
                    return (Some(left_ty), left, right);
                }
            }

            _ => (),
        }

        (None, left, right)
    }

    /// Creates a new scope. A new scope is created for every function and block,
    /// in addition to the bottom global scope.
    ///
    /// # Example
    /// (global scope #1)
    /// func main() {       <- new scope (#2) for the class main
    ///     var a = 5       <- a now in scope #2
    ///     {               <- new scope (#3)
    ///         var b = 1   <- b now in scope #3
    ///     }               <- scope #3 gets removed, along with b
    /// }                   <- scope #2 gets removed, along with a
    fn begin_scope(&mut self) {
        self.environments.push(HashMap::new());
    }

    /// Removes the topmost scope.
    fn end_scope(&mut self) {
        self.environments.pop();
    }

    /// Inserts the given expression at the current insertion pointer.
    pub fn insert_at_ptr(&mut self, expr: Expr) {
        let func = self.cur_fn();
        let mut func = func.borrow_mut();
        func.exprs.push(expr)
    }

    /// Sets the insertion pointer.
    /// Insertion is always at the end of a function.
    pub fn set_pointer(&mut self, function: MutRc<Function>) {
        self.position = Some(Pointer { function })
    }

    /// Returns the function of the insertion pointer.
    pub fn cur_fn(&self) -> MutRc<Function> {
        self.position.as_ref().unwrap().function.clone()
    }

    /// Switch the module this generator is operating on.
    /// Doing this will cause everything related to the currently generating code
    /// to be reset.
    pub fn switch_module(&mut self, module: &MutRc<MModule>) {
        self.module = Rc::clone(module);
        self.builder.switch_module(&module);
        self.position = None;
        self.environments.clear();
        self.current_loop = None;
        self.uninitialized_this_members.clear();
    }

    fn cur_loop(&mut self) -> &mut ForLoop {
        self.current_loop.as_mut().unwrap()
    }

    pub fn err(&self, tok: &Token, msg: &str) -> Error {
        Error::new(tok, "MIR", msg.to_string(), &self.builder.path)
    }

    pub fn new(builder: MIRBuilder) -> Self {
        MIRGenerator {
            module: Rc::clone(&builder.module),
            builder,
            position: None,
            environments: Vec::with_capacity(5),
            current_loop: None,
            uninitialized_this_members: HashSet::with_capacity(10),
            closure_data: None,
        }
    }

    /// Produces a `MIRGenerator` usable for generating a closure literal,
    /// temporarily making the outer generator unusable.
    /// It takes the outer environments to allow for capturing variables,
    /// and also records some other required closure data.
    /// This data is then retried with `self.end_closure`.
    pub fn for_closure(outer: &mut MIRGenerator) -> Self {
        MIRGenerator {
            module: Rc::clone(&outer.module),
            builder: MIRBuilder::with_context(&outer.module, outer.builder.context.clone()),
            position: None,
            environments: vec![HashMap::with_capacity(3)],
            current_loop: None,
            uninitialized_this_members: HashSet::new(),
            closure_data: Some(ClosureData {
                outer_env: mem::replace(&mut outer.environments, vec![]),
                captured: Vec::with_capacity(3),
            }),
        }
    }

    /// Ends closure compilation and restores the outer generator,
    /// returning recorded info about the compiled closure.
    pub fn end_closure(self, outer: &mut MIRGenerator) -> ClosureData {
        let mut closure_data = self.closure_data.unwrap();
        outer.environments = mem::replace(&mut closure_data.outer_env, vec![]);
        closure_data
    }
}

/// A pointer is the location the generator is inserting into.
pub struct Pointer {
    /// The function inserting into
    pub function: MutRc<Function>,
}

/// All data of a loop.
#[derive(Default)]
struct ForLoop {
    /// The alloca of the for loop result. Can be None for loops that return None type.
    result_var: Option<Rc<Variable>>,
}

/// All types of associated methods on a type.
pub enum AssociatedMethod {
    // A simple method that can be called normally
    Fn(Rc<Variable>),
    // A dynamic method (this is the index of the method.)
    IFace(usize),
    // A prototype that needs its types inferred.
    Proto(Rc<Prototype>),
}

/// Data required for closure compilation.
pub struct ClosureData {
    /// All environments in the function that the closure literal
    /// is being compiled in.
    pub outer_env: Vec<HashMap<Rc<String>, Rc<Variable>>>,
    /// All variables inside the outer environments that are used
    /// inside the closure and therefore 'captured'
    pub captured: Vec<Rc<Variable>>,
}
