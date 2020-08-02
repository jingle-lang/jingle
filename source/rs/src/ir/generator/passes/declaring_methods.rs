/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 7:27 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{collections::HashSet, rc::Rc};

use either::Either::Left;

use crate::{
    ast,
    ast::{
        declaration::{Constructor, FuncSignature, FunctionParam, Visibility},
        Type as ASTType,
    },
    error::{Error, Res},
    scanner::token::Token,
    ir::{
        generator::{
            builder::MIRBuilder,
            passes::{declaring_globals::create_function, ModulePass, PassType},
            MIRGenerator,
        },
        nodes::{ADTType, AbstractMethod, Expr, ProtoAST, Prototype, Type, Variable, ADT},
        result::ToMIRResult,
        MutRc,
    },
};
use std::cell::RefCell;

/// This pass defines all methods on classes and interfaces.
pub struct DeclareMethods();

impl ModulePass for DeclareMethods {
    fn get_type(&self) -> PassType {
        PassType::Type
    }

    fn run_type(&self, gen: &mut MIRGenerator, ty: Type) -> Result<(), Error> {
        if let Type::Adt(adt) = ty {
            if adt.borrow().ty.needs_lifecycle() {
                declare_lifecycle_methods(&mut gen.builder, &adt)?;
            }
            declare_user_methods(&mut gen.builder, &adt)?;

            // TODO: This is a little ugly... it works i guess?
            if let ADTType::Enum { cases } = &adt.borrow().ty {
                for case in cases.values() {
                    let mut case = case.borrow_mut();
                    case.methods.reserve(adt.borrow().methods.len());
                    for method in &adt.borrow().methods {
                        case.methods
                            .insert(Rc::clone(method.0), Rc::clone(method.1));
                    }
                    for method in &adt.borrow().proto_methods {
                        case.proto_methods
                            .insert(Rc::clone(method.0), Rc::clone(method.1));
                    }
                }
            }
        }
        Ok(())
    }
}

fn declare_lifecycle_methods(builder: &mut MIRBuilder, adt: &MutRc<ADT>) -> Res<()> {
    let ast = Rc::clone(&adt.borrow().ast);
    let this_param = FunctionParam::this_param(&ast.name);

    let init_fn_sig = get_instantiator_fn_sig(&ast, this_param.clone());
    adt.borrow_mut().instantiator =
        Some(create_function(builder, Left(&init_fn_sig), false, None)?);
    let free_fn_sig = get_destructor_fn_sig(&ast, this_param);
    adt.borrow_mut().destructor = Some(create_function(builder, Left(&free_fn_sig), false, None)?);
    Ok(())
}

fn declare_user_methods(builder: &mut MIRBuilder, adt: &MutRc<ADT>) -> Res<()> {
    let ast = Rc::clone(&adt.borrow().ast);
    let this_param = FunctionParam::this_param(&ast.name);

    // Do all user-defined methods
    for method in ast.methods.iter().filter(|m| m.body.is_some()) {
        if method.sig.generics.is_some() {
            adt.borrow_mut().proto_methods.insert(
                Rc::clone(&method.sig.name.lexeme),
                generic_method(builder, method, &this_param)?,
            );
        } else {
            let mir_method =
                create_function(builder, Left(&method.sig), false, Some(this_param.clone()))?;
            adt.borrow_mut()
                .methods
                .insert(Rc::clone(&method.sig.name.lexeme), mir_method);
        }
    }

    if let Some(constructors) = ast.constructors() {
        declare_constructors(builder, &adt, &ast, &this_param, constructors)?;
    }

    // Do all abstract/dyn methods
    // This somewhat confusing filter_map simply iterates over all sigs on fns that do not have a body.
    for method in ast
        .methods
        .iter()
        .filter_map(|m| m.body.as_ref().ok_or(&m.sig).err())
    {
        let ret_type = match method.return_type.as_ref() {
            Some(ty) => builder.find_type(ty)?,
            None => Type::None,
        };

        let mut parameters = Vec::with_capacity(method.parameters.len());
        for param in &method.parameters {
            parameters.push(builder.find_type(&param.type_)?);
        }

        let dupe = adt.borrow_mut().dyn_methods.insert(
            Rc::clone(&method.name.lexeme),
            AbstractMethod {
                name: Rc::clone(&method.name.lexeme),
                parameters,
                ret_type,
                has_default_impl: false,
            },
        );

        if dupe.is_some() {
            return Err(Error::new(
                &method.name,
                "MIR",
                format!("Method with name {} already defined", method.name.lexeme),
                &builder.path,
            ));
        }
    }

    Ok(())
}

fn generic_method(
    builder: &mut MIRBuilder,
    method: &ast::Function,
    this_param: &FunctionParam,
) -> Res<Rc<Prototype>> {
    let name = Rc::new(format!("{}-{}", this_param.type_, method.sig.name.lexeme));
    builder
        .module
        .borrow_mut()
        .try_reserve_name_rc(&name, &method.sig.name, true)?;

    let mut ast = method.clone();
    ast.sig.parameters.insert(0, this_param.clone());

    let call_parameters = ast.sig.parameters.clone();
    let proto = Rc::new(Prototype {
        name: Rc::clone(&name),
        instances: Default::default(),
        impls: RefCell::new(vec![]),
        module: Rc::clone(&builder.module),
        ast: ProtoAST::Function(Rc::new(ast)),
        call_parameters: vec![(call_parameters, None)],
    });

    builder
        .module
        .borrow_mut()
        .protos
        .insert(name, Rc::clone(&proto));

    Ok(proto)
}

/// Returns signature of the ADT instantiator.
fn get_instantiator_fn_sig(adt: &ast::ADT, this_param: FunctionParam) -> FuncSignature {
    let fn_name = Token::generic_identifier(format!("create-{}-instance", &adt.name.lexeme));
    FuncSignature {
        name: fn_name,
        visibility: Visibility::Public,
        generics: None,
        return_type: None,
        parameters: vec![this_param],
        variadic: false,
    }
}

/// Returns signature of the ADT destructor.
fn get_destructor_fn_sig(adt: &ast::ADT, this_param: FunctionParam) -> FuncSignature {
    let fn_name = Token::generic_identifier(format!("free-{}-instance", &adt.name.lexeme));
    FuncSignature {
        name: fn_name,
        visibility: Visibility::Public,
        generics: None,
        return_type: None,
        parameters: vec![
            this_param,
            FunctionParam {
                type_: ASTType::Ident(Token::generic_identifier("Bool".to_string())),
                name: Token::generic_identifier("refcount_is_0".to_string()),
            },
        ],
        variadic: false,
    }
}

fn declare_constructors(
    builder: &mut MIRBuilder,
    adt: &MutRc<ADT>,
    ast: &ast::ADT,
    this_param: &FunctionParam,
    constructors: &[Constructor],
) -> Res<()> {
    // Do all constructors
    let mut constructor_parameter_list = HashSet::with_capacity(constructors.len());

    let default = maybe_default_constructor(&ast);
    let iter = constructors.iter().chain(default.iter()).enumerate();
    for (i, constructor) in iter {
        let sig = get_constructor_sig(builder, &ast, constructor, &this_param, i)?;
        let mir_var = create_function(builder, Left(&sig), false, None)?;
        let mir_fn = mir_var.type_.as_function();
        let mut mir_fn = mir_fn.borrow_mut();
        mir_fn.exprs = insert_constructor_setters(builder, &ast, constructor, &mir_fn.parameters)?;
        adt.borrow_mut().constructors.push(Rc::clone(&mir_var));

        let params = mir_fn
            .parameters
            .iter()
            .skip(1)
            .map(|p| &p.type_)
            .cloned()
            .collect::<Vec<Type>>();
        if !constructor_parameter_list.insert(params) {
            return Err(Error::new(
                &ast.name,
                "MIR",
                "Class contains constructors with duplicate signatures.".to_string(),
                &builder.path,
            ));
        }
    }

    Ok(())
}

/// Returns the MIR function signature of a constructor.
fn get_constructor_sig(
    builder: &mut MIRBuilder,
    adt: &ast::ADT,
    constructor: &Constructor,
    this_arg: &FunctionParam,
    index: usize,
) -> Res<FuncSignature> {
    let name = Token::generic_identifier(format!("{}-constructor-{}", &adt.name.lexeme, index));
    let mut parameters = constructor
        .parameters
        .iter()
        .map(|(name, ty)| {
            let type_ = ty
                .clone()
                .or_else(|| {
                    get_field_by_name(adt, name)
                        .map(|(_, ty)| ty)
                        .and_then(|t| t)
                })
                .or_err(
                    &builder.path,
                    name,
                    "Cannot infer type of field with default value (specify type explicitly.)",
                )?;
            Ok(FunctionParam {
                type_,
                name: name.clone(),
            })
        })
        .collect::<Res<Vec<FunctionParam>>>()?;
    parameters.insert(0, this_arg.clone());
    Ok(FuncSignature {
        name,
        visibility: constructor.visibility,
        generics: None,
        return_type: None,
        parameters,
        variadic: false,
    })
}

fn get_field_by_name(adt: &ast::ADT, name: &Token) -> Option<(usize, Option<ASTType>)> {
    adt.members()
        .unwrap()
        .iter()
        .enumerate()
        .find(|(_, mem)| mem.name.lexeme == name.lexeme)
        .map(|(i, mem)| (i, mem.ty.clone()))
}

/// Insert all constructor 'setter' parameters into the entry
/// block of the MIR function.
fn insert_constructor_setters(
    builder: &mut MIRBuilder,
    adt: &ast::ADT,
    constructor: &Constructor,
    mir_fn_params: &[Rc<Variable>],
) -> Res<Vec<Expr>> {
    let mut block = Vec::new();
    for (index, (param, _)) in constructor
        .parameters
        .iter()
        .enumerate()
        .filter(|(_, (_, ty))| ty.is_none())
    {
        let (field_index, _) =
            get_field_by_name(adt, param).or_err(&builder.path, param, "Unknown class field.")?;
        block.push(Expr::struct_set(
            Expr::load(&mir_fn_params[0]),
            field_index,
            Expr::load(&mir_fn_params[index + 1]),
            true,
        ))
    }
    block.push(Expr::none_const());
    Ok(block)
}

/// Will return a default constructor with no parameters
/// should the ADT not contain a constructor and
/// all members have default values.
fn maybe_default_constructor(adt: &ast::ADT) -> Option<Constructor> {
    let no_uninitialized_members = !adt
        .members()
        .unwrap()
        .iter()
        .any(|v| v.initializer.is_none());
    if adt.constructors().unwrap().is_empty() && no_uninitialized_members {
        Some(Constructor {
            parameters: vec![],
            visibility: Visibility::Public,
            body: None,
        })
    } else {
        None
    }
}
