/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/28/19 1:12 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{cell::RefCell, collections::HashMap, rc::Rc};

use crate::{
    ast,
    ast::{
        declaration::{FunctionParam, GenericParam},
        ADTMember, Constructor, Expression,
    },
    error::{Error, Res},
    scanner::token::Token,
    ir::{
        generator::{
            builder::{Context, MIRBuilder},
            module::DONE_PASSES,
            passes::{
                declaring_globals::{generate_mir_fn, insert_global_and_type},
                declaring_iface_impls::declare_impl,
            },
            MIRGenerator,
        },
        get_iface_impls,
        nodes::{ADTType, Expr, Type, Variable, ADT},
        result::ToMIRResult,
        MModule, MutRc,
    },
};
use either::Either::Right;
use indexmap::map::IndexMap;

type CallParameters = (Vec<FunctionParam>, Option<EnumInfo>);
/// This is for special handling on enums -
/// they contain all child case constructors, with `EnumInfo`
/// containing `(CaseName, CaseConstructorIndex)`.
/// For non-enums, it's just always `None`.
type EnumInfo = (Rc<String>, usize);

/// A prototype that ADTs or functions can be instantiated from.
/// This prototype is kept in AST form,
/// as all other MIR codegen would have to handle lots of
/// edge cases and be aware of prototypes otherwise.
///
/// Instead of that, prototypes are simply compiled on demand -
/// whenever they are instanced by using them somewhere,
/// the MIR generator takes the AST and generates it like
/// a regular node, with the generic parameters substituted
/// for their arguments.
///
/// The mayor drawback of this is that prototypes will
/// not produce compiler errors when not instanced,
/// but this is a small drawback compared to the complexity
/// of handling prototypes another way.
/// (Also, this missing check does not lead to unsound compiled code -
/// not producing unsound code is the most important reason of type checking.)
///
/// Another drawback is of course performance, as instancing during IR
/// instead of MIR would allow for less work to be done.
/// TODO: Potentially move instancing to IR for better performance
#[derive(Debug, Clone)]
pub struct Prototype {
    /// The name of the type.
    /// For ADT: user given name
    /// For functions: $module:$fnName
    pub name: Rc<String>,
    pub instances: RefCell<HashMap<Vec<Type>, Type>>,
    pub impls: RefCell<Vec<(ast::IFaceImpl, MutRc<MModule>)>>,
    pub module: MutRc<MModule>,
    pub ast: ProtoAST,
    /// A list of all possible argument types to call this prototype.
    /// Used for type inference; kept in memory since
    /// constructors make looking it up not free.
    pub call_parameters: Vec<CallParameters>,
}

impl Prototype {
    /// Build this prototype with the given arguments, returning a type.
    /// `err_tok` should be a token used for error reporting, `self_ref`
    /// should be this prototype itself.
    /// `instancing_module` is a reference to the module that is
    /// instancing this prototype (which is not always the one the prototype is in
    /// because of imports).
    pub fn build(
        &self,
        arguments: Vec<Type>,
        instancing_module: &MutRc<MModule>,
        err_tok: &Token,
        self_ref: Rc<Prototype>,
    ) -> Res<Type> {
        self.build_with_parent_context(arguments, instancing_module, err_tok, self_ref, &Context::default())
    }

    pub fn build_with_parent_context(
        &self,
        arguments: Vec<Type>,
        instancing_module: &MutRc<MModule>,
        err_tok: &Token,
        self_ref: Rc<Prototype>,
        context: &Context,
    ) -> Res<Type> {
        if let Some(inst) = self.instances.borrow().get(&arguments) {
            return Ok(inst.clone());
        }

        let name = get_name(&self.name, &arguments);
        let ty = self.ast.create_mir(&name, &arguments, instancing_module, self_ref, context)?;
        let mut generator = MIRGenerator::new(MIRBuilder::new(&self.module));

        self.module
            .borrow_mut()
            .types
            .insert(Rc::clone(&name), ty.clone());
        instancing_module
            .borrow_mut()
            .imports
            .types
            .insert(Rc::clone(&name), ty.clone());

        generator.builder.context = ty.context().unwrap();
        check_generic_arguments(
            &mut generator,
            self.ast.get_parameters(),
            &arguments,
            err_tok,
        )?;
        self.instances.borrow_mut().insert(arguments, ty.clone());
        attach_impls(&mut generator.builder, &ty, &name, &self.impls.borrow())?;

        // Enums require special handling because of their child cases
        if ty.is_adt() && ty.as_adt().borrow().ty.is_enum() {
            let adt = ty.as_adt();
            // Insert every child case into the module as well
            for case in adt.borrow().ty.cases().values() {
                self.module
                    .borrow_mut()
                    .types
                    .insert(Rc::clone(&case.borrow().name), Type::Adt(Rc::clone(case)));
            }

            // Run all passes on the enum and its cases, making sure they are done in lockstep
            let len = DONE_PASSES.with(|d| d.borrow().len());
            for i in 0..len {
                catch_up_pass(&mut generator, ty.clone(), i)?;
                for case in adt.borrow().ty.cases().values() {
                    catch_up_pass(&mut generator, Type::Adt(Rc::clone(case)), i)?;
                }
            }
        } else {
            // If it's not an enum, just catch up all passes and it's done
            catch_up_passes(&mut generator, &ty)?;
        }

        Ok(ty)
    }

    /// Will take arguments of a call invocation on this prototype
    /// and try to infer types from the arguments.
    /// Return value is the expression of the finished call.
    pub fn try_infer_call(
        &self,
        gen: &mut MIRGenerator,
        mut arguments: Vec<Expr>,
        ast_args: &[Expression],
        err_tok: &Token,
        self_ref: Rc<Prototype>,
        parent_context: Option<Context>,
        enum_case: Option<&Rc<String>>,
    ) -> Res<Expr> {
        let mut index = 0;
        let mut search_res = None;
        let mut enum_info = None;
        for (i, call) in self.call_parameters.iter().enumerate().filter(|(_, p)| {
            p.0.len() == arguments.len() && p.1.as_ref().map(|e| &e.0) == enum_case
        }) {
            index = i;
            search_res = self
                .ast
                .get_parameters()
                .iter()
                .map(|param| self.resolve_param(param, &call.0, &arguments))
                .collect::<Option<Vec<Type>>>();
            if search_res.is_some() {
                enum_info = call.1.clone();
                break;
            }
        }

        let ty_args = search_res.or_err(
            &self.module.borrow().path,
            err_tok,
            "Cannot infer types (please specify explicitly).",
        )?;

        let ty = self.build_with_parent_context(
            ty_args,
            &gen.module,
            err_tok,
            self_ref,
            &parent_context.unwrap_or_else(Context::default),
        )?;

        match &ty {
            Type::Function(func) => {
                gen.check_func_args_(&ty, &mut arguments, ast_args, err_tok, false)?;

                let fn_load = Expr::load(
                    &self
                        .module
                        .borrow()
                        .find_global(&func.borrow().name)
                        .unwrap(),
                );

                Ok(Expr::call(fn_load, arguments))
            }

            Type::Adt(adt) => {
                let adt_borrow = adt.borrow();
                if let ADTType::Enum { cases } = &adt_borrow.ty {
                    let info = enum_info.unwrap();
                    let case = cases.get(&info.0).cloned().or_err(
                        &self.module.borrow().path,
                        err_tok,
                        "Unknown case.",
                    )?;
                    let constructor = Rc::clone(&case.borrow().constructors[info.1]);
                    Ok(Expr::alloc_type(Type::Adt(case), &constructor, arguments))
                } else {
                    drop(adt_borrow); // Required to make destructor run early and borrowck happy
                    let constructor = Rc::clone(&adt.borrow().constructors[index]);
                    Ok(Expr::alloc_type(ty, &constructor, arguments))
                }
            }

            _ => panic!("Unexpected prototype instance type"),
        }
    }

    fn resolve_param(
        &self,
        param: &GenericParam,
        call_params: &[FunctionParam],
        arguments: &[Expr],
    ) -> Option<Type> {
        let goal = ast::Type::Ident(param.name.clone());

        for (param, mir) in call_params.iter().zip(arguments.iter()) {
            if let Some(ty) = self.match_param(&param.type_, mir.get_type(), &goal) {
                return Some(ty);
            }
        }

        None
    }

    fn match_param(&self, param: &ast::Type, mir: Type, goal: &ast::Type) -> Option<Type> {
        match &param {
            ast::Type::Ident(_) if goal == param => Some(mir),

            ast::Type::Pointer(inner) if goal == &**inner => {
                if let Type::Pointer(mir) = mir {
                    Some(*mir)
                } else {
                    Some(Type::Value(Box::new(mir)))
                }
            }

            ast::Type::Value(inner) if goal == &**inner => {
                // This is required since primitives do not actually get wrapped in MIR
                // (See MIRBuilder::find_type)
                if let Type::Value(mir) = mir {
                    Some(*mir)
                } else {
                    Some(mir)
                }
            }

            ast::Type::Array(inner) if goal == &**inner => Some(
                mir.context()
                    .unwrap()
                    .type_aliases
                    .values()
                    .next()
                    .unwrap()
                    .clone(),
            ),

            ast::Type::Closure {
                params, ret_type, ..
            } => {
                let mir = mir.into_closure();

                // Try recursively resolving parameters
                for (ty, mir) in params.iter().zip(mir.parameters.iter()) {
                    if let Some(ty) = self.match_param(ty, mir.clone(), &goal) {
                        return Some(ty);
                    }
                }

                // Try resolving return type
                ret_type
                    .as_ref()
                    .and_then(|ret_type| self.match_param(ret_type, mir.ret_type.clone(), &goal))
            }

            ast::Type::Generic { types, .. } => {
                let context = mir.context().unwrap();
                // Try recursively resolving, might be a parameter of
                // type Proto<Other<T>> for example and T should be inferred from that
                for (ty, mir) in types.iter().zip(context.type_aliases.values()) {
                    if let Some(ty) = self.match_param(ty, mir.clone(), &goal) {
                        return Some(ty);
                    }
                }
                None
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, EnumIsA)]
pub enum ProtoAST {
    ADT(Rc<ast::ADT>),
    Function(Rc<ast::Function>),
}

impl ProtoAST {
    fn get_parameters(&self) -> &[GenericParam] {
        match self {
            ProtoAST::ADT(a) => a.generics.as_ref().unwrap(),
            ProtoAST::Function(f) => f.sig.generics.as_ref().unwrap(),
        }
    }

    // TODO: I am so, so sorry for making this abomination
    pub fn get_call_parameters(&self) -> Result<Vec<CallParameters>, (String, Token)> {
        match self {
            ProtoAST::ADT(adt) => {
                if let (Some(constructors), Some(members)) = (adt.constructors(), adt.members()) {
                    constructors
                        .iter()
                        .map(|c| self.constructor_to_call_format(c, members.iter(), None))
                        .collect::<Result<_, _>>()
                } else if let ast::ADTType::Enum { cases, variables } = &adt.ty {
                    cases
                        .iter()
                        .flat_map(|case| {
                            let members = case.members().unwrap();
                            case.constructors()
                                .unwrap()
                                .iter()
                                .enumerate()
                                .map(move |(c_i, c)| {
                                    self.constructor_to_call_format(
                                        c,
                                        variables.iter().chain(members.iter()),
                                        Some((case.case_name(), c_i)),
                                    )
                                })
                        })
                        .collect::<Result<_, _>>()
                } else {
                    Ok(vec![])
                }
            }

            ProtoAST::Function(func) => Ok(vec![(func.sig.parameters.clone(), None)]),
        }
    }

    fn constructor_to_call_format<'a, T: Iterator<Item = &'a ADTMember>>(
        &self,
        constructor: &Constructor,
        mut members: T,
        enum_info: Option<EnumInfo>,
    ) -> Result<CallParameters, (String, Token)> {
        Ok((
            constructor
                .parameters
                .iter()
                .map(|(name, ty)| {
                    Ok({
                        FunctionParam {
                            type_: {
                                if let Some(ty) = ty {
                                    Ok(ty.clone())
                                } else {
                                    members
                                        .find(|i| i.name.lexeme == name.lexeme)
                                        .ok_or((
                                            format!("Unknown member '{}'.", name.lexeme),
                                            name.clone(),
                                        ))?
                                        .ty
                                        .clone()
                                        .ok_or((
                                            format!("Missing type on member '{}'.", name.lexeme),
                                            name.clone(),
                                        ))
                                }
                            }?,
                            name: name.clone(),
                        }
                    })
                })
                .collect::<Result<_, (String, Token)>>()?,
            enum_info,
        ))
    }

    fn create_mir(
        &self,
        name: &Rc<String>,
        arguments: &[Type],
        instancing_module: &MutRc<MModule>,
        self_ref: Rc<Prototype>,
        context: &Context,
    ) -> Res<Type> {
        Ok(match self {
            ProtoAST::ADT(ast) => {
                let mut ast = (**ast).clone();
                ast.replace_proto_name(&name);

                let context = get_context(context, ast.generics.as_ref().unwrap(), arguments);
                let adt = ADT::from_ast(ast, context, Some(self_ref));
                Type::Adt(adt)
            }

            ProtoAST::Function(ast) => {
                let mut ast = (**ast).clone();
                ast.sig.name.lexeme = Rc::clone(&name);

                let builder = MIRBuilder::with_context(
                    &self_ref.module,
                    get_context(context, ast.sig.generics.as_ref().unwrap(), arguments),
                );
                let mir_fn = generate_mir_fn(&builder, Right(ast), String::clone(name), None)?;
                let global = Variable::new(false, Type::Function(Rc::clone(&mir_fn)), name);
                insert_global_and_type(&builder.module, &global);
                instancing_module
                    .borrow_mut()
                    .imports
                    .globals
                    .insert(Rc::clone(&global.name), Rc::clone(&global));

                Type::Function(mir_fn)
            }
        })
    }
}

fn get_name(name: &String, args: &[Type]) -> Rc<String> {
    let mut arg_names = args[0].to_string();
    for arg in args.iter().skip(1) {
        arg_names = format!("{}, {}", arg_names, arg);
    }
    Rc::new(format!("{}<{}>", name, arg_names))
}

fn get_context(context: &Context, params: &[GenericParam], args: &[Type]) -> Context {
    Context {
        type_aliases: Rc::new(
            params
                .iter()
                .map(|p| Rc::clone(&p.name.lexeme))
                .zip(args.iter().cloned())
                .chain(IndexMap::clone(&context.type_aliases).into_iter())
                .collect(),
        ),
    }
}

fn check_generic_arguments(
    gen: &mut MIRGenerator,
    parameters: &[GenericParam],
    arguments: &[Type],
    err_tok: &Token,
) -> Result<(), Error> {
    if parameters.len() != arguments.len() {
        return Err(gen.err(
            err_tok,
            &format!(
                "Wrong amount of generic arguments (expected {}; got {})",
                parameters.len(),
                arguments.len()
            ),
        ));
    }

    // for each param with a bound
    for (param, bound, arg) in parameters
        .iter()
        .zip(arguments.iter())
        .filter_map(|(param, arg)| param.bound.as_ref().map(|bound| (param, bound, arg)))
    {
        if arg.has_marker(&bound) {
            continue; // Valid marker, all good
        }

        let iface = gen.builder.find_type(bound);
        if let (Ok(iface), Some(impls)) = (iface, get_iface_impls(arg)) {
            if impls.borrow().interfaces.contains_key(&iface) {
                continue; // Valid interface bound, all good
            }
        }

        // Not a valid bound!
        return Err(gen.err(
            err_tok,
            &format!(
                "Generic argument '{}' does not fulfill bound '{}' on parameter '{}'.",
                arg, bound, param.name.lexeme
            ),
        ));
    }

    Ok(())
}

fn attach_impls(
    builder: &mut MIRBuilder,
    ty: &Type,
    name: &Rc<String>,
    impls: &[(ast::IFaceImpl, MutRc<MModule>)],
) -> Res<()> {
    for (im, module) in impls {
        builder.switch_module(module);
        let mut ast = im.clone();
        let mut tok = ast.implementor.get_token().clone();
        tok.lexeme = Rc::clone(&name);
        ast.implementor = ast::Type::Ident(tok);
        declare_impl(ast, builder, Some(ty.clone()))?;
    }
    Ok(())
}

pub fn catch_up_passes(gen: &mut MIRGenerator, ty: &Type) -> Res<()> {
    let module = Rc::clone(&gen.module);
    let len = DONE_PASSES.with(|d| d.borrow().len());
    for i in 0..len {
        gen.switch_module(&module);
        DONE_PASSES.with(|d| d.borrow()[i].run_type(gen, ty.clone()))?
    }
    Ok(())
}

fn catch_up_pass(gen: &mut MIRGenerator, ty: Type, i: usize) -> Res<()> {
    let module = Rc::clone(&gen.module);
    gen.switch_module(&module);
    DONE_PASSES.with(|d| d.borrow()[i].run_type(gen, ty))
}
