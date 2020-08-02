/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 1:50 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::rc::Rc;

use crate::{
    ast,
    ast::{
        declaration::{FuncSignature, FunctionParam, Variable as ASTVar, Visibility},
        literal::Closure,
        Expression as ASTExpr, Literal, Type as ASTType,
    },
    error::Res,
    scanner::token::{TType, Token},
    ir::{
        generator::{
            builder::Context,
            passes::declaring_globals::{generate_mir_fn, insert_global_and_type},
            AssociatedMethod, ForLoop, MIRGenerator, intrinsics::INTRINSICS
        },
        nodes::{catch_up_passes, ADTType, Expr, Type, Variable, ADT},
        result::ToMIRResult,
        MutRc,
    },
};
use either::Either::Right;

/// This impl contains all code of the generator that directly
/// produces expressions.
/// This is split into its own file for readability reasons;
/// a 1500-line file containing everything is difficult to navigate.
impl MIRGenerator {
    pub fn expression(&mut self, expression: &ASTExpr) -> Res<Expr> {
        match expression {
            ASTExpr::Assignment { name, value } => self.assignment(name, value),

            ASTExpr::Binary {
                left,
                operator,
                right,
            } => self.binary(left, operator, right),

            ASTExpr::Block(expressions, _) => self.block(expressions),

            ASTExpr::Break(expr, tok) => self.break_(expr, tok),

            ASTExpr::Call { callee, arguments } => self.call(callee, arguments),

            ASTExpr::For {
                condition,
                body,
                else_b,
            } => self.for_(condition, body, else_b),

            ASTExpr::Get { object, name } => self.get(object, name),

            ASTExpr::GetGeneric { name, .. } => {
                Err(self.err(name, "Can only call generic methods directly"))
            }

            ASTExpr::GetStatic { object, name } => self.get_static(object, name, true),

            ASTExpr::If {
                condition,
                then_branch,
                else_branch,
            } => self.if_(condition, then_branch, else_branch),

            ASTExpr::IndexGet {
                indexed,
                index,
                bracket,
            } => self.index_get(indexed, index, bracket),

            ASTExpr::IndexSet {
                indexed,
                index,
                value,
            } => self.index_set(indexed, index, value),

            ASTExpr::Literal(literal, token) => self.literal(literal, token),

            ASTExpr::Return(val, err_tok) => self.return_(val, err_tok),

            ASTExpr::Set {
                object,
                name,
                value,
            } => self.set(object, name, value),

            ASTExpr::Unary { operator, right } => self.unary(operator, right),

            ASTExpr::Variable(var) => self.var(var),

            ASTExpr::VarWithGenerics { name, generics } => self.var_with_generics(name, generics),

            ASTExpr::Switch {
                value,
                branches,
                else_branch,
            } => self.switch(value, branches, else_branch),

            ASTExpr::VarDef(var) => self.var_def(var),
        }
    }

    fn assignment(&mut self, name: &Token, value: &ASTExpr) -> Res<Expr> {
        let var = self.find_var(&name).or_err(
            &self.builder.path,
            name,
            &format!("Variable '{}' is not defined", name.lexeme),
        )?;
        let value = self.expression(value)?;
        let value = self.try_cast(value, &var.type_);
        let val_ty = value.get_type();

        if val_ty == var.type_ && var.mutable {
            Ok(Expr::store(&var, value, false))
        } else if var.mutable {
            Err(self.err(
                &name,
                &format!("Variable {} is a different type", name.lexeme),
            ))
        } else {
            Err(self.err(
                &name,
                &format!("Variable {} is not assignable (val)", name.lexeme),
            ))
        }
    }

    fn binary(&mut self, left: &ASTExpr, operator: &Token, right: &ASTExpr) -> Res<Expr> {
        let left = self.expression(left)?;

        // Account for an edge case with simple enums, where `A:A` incorrectly gets
        // turned into a regular value instead of a type get.
        let right = match right {
            ASTExpr::GetStatic { object, name } if operator.t_type == TType::Is => {
                self.get_static(object, name, false)
            }
            _ => self.expression(right),
        }?;

        self.binary_mir(left, operator, right)
    }

    fn binary_mir(&mut self, left: Expr, operator: &Token, mut right: Expr) -> Res<Expr> {
        let left_ty = left.get_type();
        let right_ty = right.get_type();

        if (left_ty.is_int() && right_ty.is_int())
            || left_ty.is_float() && right_ty.is_float()
            || (operator.t_type == TType::Is && right_ty.is_type())
        {
            if operator.t_type == TType::And || operator.t_type == TType::Or {
                Ok(Self::binary_logic(left, operator.t_type, right))
            } else {
                let (_, left, right) = self.try_unify_type(left, right);
                Ok(Expr::binary(left, operator.t_type, right))
            }
        } else {
            let method_var = self
                .get_operator_overloading_method(operator.t_type, &left_ty, &mut right)
                .or_err(
                    &self.builder.path,
                    operator,
                    "No implementation of operator found for types.",
                )?;

            let mut expr = Expr::call(Expr::load(&method_var), vec![left, right]);
            if operator.t_type == TType::BangEqual {
                expr = Expr::unary(expr, TType::Bang);
            }
            Ok(expr)
        }
    }

    /// Logic operators need special treatment for shortcircuiting behavior
    fn binary_logic(left: Expr, operator: TType, right: Expr) -> Expr {
        if operator == TType::And {
            // a and b --> if (a) b else false
            Expr::if_(left, right, Expr::Literal(Literal::Bool(false)), true)
        } else {
            // a or b --> if (a) true else b
            Expr::if_(left, Expr::Literal(Literal::Bool(true)), right, true)
        }
    }

    fn block(&mut self, expressions: &[ASTExpr]) -> Res<Expr> {
        if expressions.is_empty() {
            return Ok(Expr::none_const());
        }

        self.begin_scope();
        let exprs = expressions
            .iter()
            .map(|e| self.expression(e))
            .collect::<Res<_>>()?;
        self.end_scope();

        Ok(Expr::Block(exprs))
    }

    fn break_(&mut self, expr: &Option<Box<ASTExpr>>, err_tok: &Token) -> Res<Expr> {
        if self.current_loop.is_none() {
            return Err(self.err(err_tok, "Break is only allowed in loops."));
        }

        let expr = expr
            .as_ref()
            .map(|expr| {
                let expression = self.expression(&expr)?;
                self.get_or_create_loop_var(&expression.get_type())?;
                Ok(expression)
            })
            .transpose()?;

        Ok(Expr::break_(expr))
    }

    fn call(&mut self, callee: &ASTExpr, arguments: &[ASTExpr]) -> Res<Expr> {
        let mut args = arguments
            .iter()
            .map(|a| self.expression(a))
            .collect::<Res<Vec<_>>>()?;

        match callee {
            // Method call while a `this` member is still uninitialized
            ASTExpr::Get { name, .. } | ASTExpr::GetGeneric { name, .. }
                if !self.uninitialized_this_members.is_empty() =>
            {
                Err(self.err(
                    name,
                    "Cannot call methods in constructors until all class members are initialized.",
                ))
            }

            // Method call
            ASTExpr::Get { object, name } | ASTExpr::GetGeneric { object, name, .. } => {
                let (object, field) = self.get_field(object, name)?;
                let func = field.right().or_err(
                    &self.builder.path,
                    name,
                    "Class members cannot be called.",
                )?;
                let obj_ty = object.get_type();
                args.insert(0, object);

                match (callee, func) {
                    // Regular method call
                    (ASTExpr::Get { .. }, AssociatedMethod::Fn(func)) => {
                        self.check_func_args_(&func.type_, &mut args, arguments, name, true)?;
                        Ok(Expr::call(Expr::load(&func), args))
                    }

                    // Interface method call
                    (ASTExpr::Get { .. }, AssociatedMethod::IFace(index)) => {
                        let adt = obj_ty.as_adt().borrow();
                        let params = &adt.dyn_methods.get_index(index).unwrap().1.parameters;
                        self.check_func_args(
                            // 'params' need to have the 'this' parameter, this is the result...
                            Some(obj_ty.clone()).iter().chain(params.iter()),
                            &mut args,
                            arguments,
                            false,
                            name,
                            true,
                        )?;

                        Ok(Expr::call_dyn(obj_ty.as_adt(), index, args))
                    }

                    // Proto method call with inferred generics
                    (ASTExpr::Get { name, .. }, AssociatedMethod::Proto(ref proto)) => proto
                        .try_infer_call(
                            self,
                            args,
                            arguments,
                            name,
                            Rc::clone(&proto),
                            obj_ty.context(),
                            None,
                        ),

                    // Proto method call with explicit generics
                    (ASTExpr::GetGeneric { params, .. }, AssociatedMethod::Proto(ref proto)) => {
                        let proto_args = params
                            .iter()
                            .map(|ty| self.builder.find_type(&ty))
                            .collect::<Res<Vec<Type>>>()?;

                        let func = proto.build_with_parent_context(
                            proto_args,
                            &self.module,
                            name,
                            Rc::clone(&proto),
                            &obj_ty.context().unwrap_or_else(Context::default),
                        )?;
                        let func_rc = self
                            .builder
                            .module
                            .borrow()
                            .find_global(&func.as_function().borrow().name)
                            .unwrap();
                        self.check_func_args_(&func, &mut args, arguments, name, true)?;

                        Ok(Expr::call(Expr::load(&func_rc), args))
                    }

                    // Generic parameters on something else, invalid
                    _ => Err(self.err(name, "This method does not take generic parameters")),
                }
            }

            // Prototype call with inferred types
            // TODO: Kinda ugly double find call
            ASTExpr::Variable(tok)
                if self.module.borrow().find_prototype(&tok.lexeme).is_some() =>
            {
                let proto = self.module.borrow().find_prototype(&tok.lexeme).unwrap();
                proto.try_infer_call(self, args, arguments, tok, Rc::clone(&proto), None, None)
            }

            // Enum prototype call with inferred types
            // TODO: Kinda ugly
            ASTExpr::GetStatic { object, name }
                if object.is_variable()
                    && self
                        .module
                        .borrow()
                        .find_prototype(&object.get_token().lexeme)
                        .is_some() =>
            {
                let proto = self
                    .module
                    .borrow()
                    .find_prototype(&object.get_token().lexeme)
                    .unwrap();
                proto.try_infer_call(
                    self,
                    args,
                    arguments,
                    object.get_token(),
                    Rc::clone(&proto),
                    None,
                    Some(&name.lexeme),
                )
            }

            // Can be either a constructor or function call
            _ => {
                let callee_mir = self.expression(callee)?;
                let callee_type = callee_mir.get_type();

                if let Some(constructors) = callee_type.get_constructors() {
                    let constructor: &Rc<Variable> = constructors
                        .iter()
                        .find(|constructor| {
                            let constructor = constructor.type_.as_function().borrow();
                            // If args count and types match
                            (constructor.parameters.len() - 1 == args.len())
                                && constructor
                                    .parameters
                                    .iter()
                                    .skip(1)
                                    .zip(args.iter_mut())
                                    .all(|(param, arg)| arg.get_type().can_cast_to(&param.type_))
                        })
                        .or_err(
                            &self.builder.path,
                            callee.get_token(),
                            "No matching constructor found for arguments.",
                        )?;

                    {
                        let constructor = constructor.type_.as_function().borrow();
                        for (param, arg) in
                            constructor.parameters.iter().skip(1).zip(args.iter_mut())
                        {
                            self.try_cast_in_place(arg, &param.type_)
                        }
                    }

                    Ok(Expr::alloc_type(callee_type, constructor, args))
                } else {
                    self.check_func_args_(
                        &callee_type,
                        &mut args,
                        arguments,
                        callee.get_token(),
                        false,
                    )?;
                    Ok(Expr::call(callee_mir, args))
                }
            }
        }
    }

    fn for_(
        &mut self,
        condition: &ASTExpr,
        body: &ASTExpr,
        else_b: &Option<Box<ASTExpr>>,
    ) -> Res<Expr> {
        let prev_loop = std::mem::replace(&mut self.current_loop, Some(ForLoop::default()));

        let cond = self.expression(condition)?;
        if cond.get_type() != Type::Bool {
            return Err(self.err(condition.get_token(), "For condition must be a boolean."));
        }

        let body = self.expression(body)?;
        let body_type = body.get_type();
        self.get_or_create_loop_var(&body_type)?;

        let (else_, result_store) = if let Some(else_b) = else_b {
            let else_val = self.expression(&else_b)?;
            if else_val.get_type() == body_type {
                (
                    Some(else_val),
                    Some(self.get_or_create_loop_var(&body_type)?),
                )
            } else {
                (Some(else_val), None)
            }
        } else {
            (None, None)
        };

        self.current_loop = prev_loop;
        Ok(Expr::loop_(cond, body, else_, result_store))
    }

    fn get(&mut self, object: &ASTExpr, name: &Token) -> Res<Expr> {
        let (object, field) = self.get_field(object, name)?;
        let field = field.left().or_err(
            &self.builder.path,
            name,
            "Cannot get class method (must be called)",
        )?;

        if self.uninitialized_this_members.contains(&field) {
            return Err(self.err(name, "Cannot get uninitialized class member."));
        }
        Ok(Expr::struct_get(object, &field))
    }

    // See `binary` for info on `allow_simple`
    fn get_static(&mut self, object: &ASTExpr, name: &Token, allow_simple: bool) -> Res<Expr> {
        let obj = self.expression(object)?;
        if let Type::Type(ty) = obj.get_type() {
            if let ADTType::Enum { cases, .. } = &ty.as_adt().borrow().ty {
                if let Some(case) = cases.get(&name.lexeme) {
                    match ADT::get_singleton_inst(case) {
                        Some(inst) if allow_simple => Ok(inst),
                        _ => Ok(Expr::type_get(Type::Adt(Rc::clone(case)))),
                    }
                } else {
                    Err(self.err(name, "Unknown enum case."))
                }
            } else {
                Err(self.err(name, "Static access is only supported on enum types."))
            }
        } else {
            Err(self.err(name, "Static access is not supported on values."))
        }
    }

    fn if_(
        &mut self,
        condition: &ASTExpr,
        then_branch: &ASTExpr,
        else_branch: &Option<Box<ASTExpr>>,
    ) -> Res<Expr> {
        let cond = self.expression(condition)?;
        if cond.get_type() != Type::Bool {
            return Err(self.err(condition.get_token(), "If condition must be a boolean"));
        }

        self.begin_scope(); // scope for smart casts if applicable
        let mut then_block = self.smart_casts(&cond);
        then_block.push(self.expression(then_branch)?);
        let then_val = Expr::Block(then_block);
        self.end_scope();

        let else_val = else_branch
            .as_ref()
            .map_or(Ok(Expr::none_const()), |else_branch| {
                self.expression(&else_branch)
            })?;
        let then_ty = then_val.get_type();
        let else_ty = else_val.get_type();

        let (phi_type, then_val, else_val) = self.try_unify_type(then_val, else_val);
        let phi = phi_type.is_some() && (then_ty != Type::None || else_ty != Type::None);

        Ok(Expr::if_(cond, then_val, else_val, phi))
    }

    fn smart_casts(&mut self, condition: &Expr) -> Vec<Expr> {
        let mut casts = Vec::new();
        self.find_casts(&mut casts, condition);
        casts
    }

    fn find_casts(&mut self, list: &mut Vec<Expr>, expr: &Expr) {
        if let Expr::Binary {
            left,
            operator,
            right,
        } = expr
        {
            match operator {
                TType::And => {
                    self.find_casts(list, &left);
                    self.find_casts(list, &right);
                }

                TType::Is if left.is_var_get() => {
                    let ty = (&**right.get_type().as_type()).clone();
                    let var = self.define_variable(
                        &Token::generic_identifier(left.as_var_get().name.to_string()),
                        false,
                        ty,
                    );
                    list.push(Expr::store(
                        &var,
                        Expr::cast((**left).clone(), &right.get_type().as_type()),
                        true,
                    ));
                }

                _ => (),
            }
        }
    }

    fn index_get(&mut self, indexed: &ASTExpr, index: &ASTExpr, bracket: &Token) -> Res<Expr> {
        let obj = self.expression(indexed)?;
        let index = self.expression(index)?;
        self.binary_mir(obj, bracket, index)
    }

    fn index_set(
        &mut self,
        indexed: &ASTExpr,
        ast_index: &ASTExpr,
        ast_value: &ASTExpr,
    ) -> Res<Expr> {
        let obj = self.expression(indexed)?;
        let mut index = self.expression(ast_index)?;
        let value = self.expression(ast_value)?;
        let method = self
            .get_operator_overloading_method(TType::RightBracket, &obj.get_type(), &mut index)
            .or_err(
                &self.builder.path,
                ast_index.get_token(),
                "No implementation of operator found for types.",
            )?;

        if value.get_type() == method.type_.as_function().borrow().parameters[2].type_ {
            Ok(Expr::call(Expr::load(&method), vec![obj, index, value]))
        } else {
            Err(self.err(ast_value.get_token(), "Setter is of wrong type."))
        }
    }

    fn literal(&mut self, literal: &Literal, token: &Token) -> Res<Expr> {
        match literal {
            Literal::Array(arr) => self.array_literal(arr.as_ref().left().unwrap()),
            Literal::Closure(closure) => self.closure(closure, token),
            _ => Ok(Expr::Literal(literal.clone())),
        }
    }

    fn array_literal(&mut self, literal: &[ASTExpr]) -> Res<Expr> {
        let mut values_mir = Vec::new();
        let mut ast_values = literal.iter();
        let first = self.expression(ast_values.next().unwrap())?;
        let elem_type = first.get_type();

        values_mir.push(first);
        for value in ast_values {
            let mir_val = self.expression(value)?;

            if mir_val.get_type() != elem_type {
                return Err(self.err(
                    value.get_token(),
                    &format!(
                        "Type of array value ({}) does not match rest of array ({}).",
                        mir_val.get_type(),
                        elem_type
                    ),
                ));
            }

            values_mir.push(mir_val);
        }

        let array_type = INTRINSICS.with(|i| i.borrow().get_array_type(elem_type, None))?;
        let array_type = array_type.as_adt();
        let push_method = {
            let arr = array_type.borrow();
            Rc::clone(arr.methods.get(&Rc::new("push".to_string())).unwrap())
        };

        let constructor = &array_type.borrow().constructors[0];
        let array = Expr::alloc_type(
            Type::Adt(Rc::clone(&array_type)),
            constructor,
            vec![Expr::Literal(Literal::I64(values_mir.len() as u64))],
        );

        for value in values_mir {
            self.insert_at_ptr(Expr::call(
                Expr::load(&push_method),
                vec![array.clone(), value],
            ))
        }

        Ok(array)
    }

    fn closure(&mut self, closure: &Closure, token: &Token) -> Res<Expr> {
        let mut name = token.clone();
        name.lexeme = Rc::new(format!("closure-{}:{}", token.line, token.index));
        let ast_func = ast::Function {
            sig: FuncSignature {
                name: name.clone(),
                visibility: Visibility::Public,
                generics: None,
                return_type: closure.ret_ty.clone(),
                parameters: closure
                    .parameters
                    .iter()
                    .map(|p| FunctionParam {
                        type_: p.type_.as_ref().unwrap().clone(),
                        name: p.name.clone(),
                    })
                    .collect(),
                variadic: false,
            },
            body: Some(closure.body.clone()),
        };

        let mut gen = Self::for_closure(self);
        let function = generate_mir_fn(
            &gen.builder,
            Right(ast_func),
            String::clone(&name.lexeme),
            Some(FunctionParam::this_param(&Token::generic_identifier(
                "i64".to_string(),
            ))),
        )?;
        let global = Variable::new(false, Type::Function(Rc::clone(&function)), &name.lexeme);
        insert_global_and_type(&gen.module, &global);

        catch_up_passes(&mut gen, &Type::Function(Rc::clone(&function)))?;
        let closure_data = gen.end_closure(self);

        let captured = Rc::new(closure_data.captured);
        function.borrow_mut().parameters[0] = Variable::new(
            false,
            Type::ClosureCaptured(Rc::clone(&captured)),
            &Rc::new("CLOSURE-CAPTURED".to_string()),
        );

        let expr = Expr::construct_closure(&global, captured);
        let var = self.define_variable(
            &Token::generic_identifier("closure-literal".to_string()),
            false,
            expr.get_type(),
        );
        Ok(Expr::store(&var, expr, true))
    }

    fn return_(&mut self, val: &Option<Box<ASTExpr>>, err_tok: &Token) -> Res<Expr> {
        let value = val
            .as_ref()
            .map(|v| self.expression(&*v))
            .transpose()?
            .unwrap_or_else(Expr::none_const);

        let ret_type = self.cur_fn().borrow().ret_type.clone();
        let value = self.cast_or_none(value, &ret_type).or_err(
            &self.builder.path,
            err_tok,
            "Return expression in function has wrong type",
        )?;

        Ok(Expr::ret(value))
    }

    fn set(&mut self, object: &ASTExpr, name: &Token, value: &ASTExpr) -> Res<Expr> {
        let (object, field) = self.get_field(object, name)?;
        let field = field
            .left()
            .or_err(&self.builder.path, name, "Cannot set class method")?;
        let value = self.expression(value)?;
        let value = self.try_cast(value, &field.type_);

        if value.get_type() != field.type_ {
            return Err(self.err(name, "Class member is a different type"));
        }
        if !field.mutable && !self.uninitialized_this_members.contains(&field) {
            return Err(self.err(name, "Cannot set immutable class member"));
        }

        let first_set = self.uninitialized_this_members.remove(&field);
        Ok(Expr::struct_set(object, field.index, value, first_set))
    }

    fn unary(&mut self, operator: &Token, right: &ASTExpr) -> Res<Expr> {
        let right = self.expression(right)?;
        let ty = right.get_type();

        match operator.t_type {
            TType::Bang if ty != Type::Bool => {
                Err(self.err(operator, "'!' can only be used on boolean values"))
            }

            TType::Minus if !(ty.is_signed_int() || ty.is_float()) => Err(self.err(
                operator,
                "'-' can only be used on signed integers and floats",
            )),

            _ => Ok(()),
        }?;

        Ok(Expr::unary(right, operator.t_type))
    }

    fn var(&mut self, var: &Token) -> Res<Expr> {
        if let Some(var) = self.find_var(&var) {
            Ok(Expr::load(&var))
        } else {
            self.module
                .borrow()
                .find_type(&var.lexeme)
                .map(Expr::type_get)
                .or_err(
                    &self.builder.path,
                    var,
                    &format!("Variable '{}' is not defined", var.lexeme),
                )
        }
    }

    fn var_with_generics(&mut self, name: &Token, generics: &[ASTType]) -> Res<Expr> {
        let ty = self.builder.find_type(&ASTType::Generic {
            token: name.clone(),
            types: Vec::from(generics),
        })?;

        if let Type::Function(func) = ty {
            Ok(Expr::load(
                &self
                    .module
                    .borrow()
                    .find_global(&func.borrow().name)
                    .unwrap(),
            ))
        } else {
            Ok(Expr::type_get(ty))
        }
    }

    fn switch(
        &mut self,
        ast_value: &ASTExpr,
        branches: &[(ASTExpr, ASTExpr)],
        else_branch: &Option<Box<ASTExpr>>,
    ) -> Res<Expr> {
        let value = self.expression(ast_value)?;
        let cond_type = value.get_type();

        let mut cases = Vec::with_capacity(branches.len());

        let mut iter = branches.iter();
        let first = iter.next();
        if first.is_none() {
            // There are no branches, just return else branch or nothing
            return else_branch
                .as_ref()
                .map_or(Ok(Expr::none_const()), |br| self.expression(br));
        }

        let (first_cond, mut first_val) =
            self.switch_branch(value.clone(), &cond_type, first.unwrap())?;
        let mut first_ty = first_val.get_type();
        for branch in iter {
            let (cond, mut branch_val) = self.switch_branch(value.clone(), &cond_type, branch)?;

            if first_ty != Type::None {
                let result = self.try_unify_type(first_val, branch_val);
                first_ty = result.0.unwrap_or(Type::None);
                first_val = result.1;
                branch_val = result.2;
            } else if branch_val.get_type() != first_ty {
                first_ty = Type::None
            }

            cases.push((cond, branch_val))
        }

        // TODO: Deduplicate this...
        let mut else_br = else_branch
            .as_ref()
            .map(|e| self.expression(e))
            .transpose()?;
        if let Some(branch_val) = &else_br {
            if first_ty != Type::None {
                let result = self.try_unify_type(first_val, else_br.unwrap());
                first_ty = result.0.unwrap_or(Type::None);
                first_val = result.1;
                else_br = Some(result.2);
            } else if branch_val.get_type() != first_ty {
                first_ty = Type::None
            }
        }

        cases.insert(0, (first_cond, first_val));
        if else_br.is_none() && !self.can_omit_else(&cond_type, &cases) {
            first_ty = Type::None
        }
        Ok(Expr::switch(cases, else_br, first_ty))
    }

    fn switch_branch(
        &mut self,
        value: Expr,
        cond_type: &Type,
        branch: &(ASTExpr, ASTExpr),
    ) -> Res<(Expr, Expr)> {
        // See note on `binary` about this
        let br_cond = match &branch.0 {
            ASTExpr::GetStatic { object, name } => self.get_static(object, name, false),
            _ => self.expression(&branch.0),
        }?;
        let br_type = br_cond.get_type();
        if &br_type != cond_type && !br_type.is_type() {
            return Err(self.err(
                branch.0.get_token(),
                "Branches of match must be of same type as the value compared.",
            ));
        }

        // Small hack to get a token that gives the user
        // a useful error without having to add complexity
        // to binary_mir()
        let mut optok = branch.0.get_token().clone();
        optok.t_type = if br_type.is_type() {
            TType::Is
        } else {
            TType::EqualEqual
        };
        let cond = self.binary_mir(value, &optok, br_cond)?;

        self.begin_scope();
        let mut branch_list = self.smart_casts(&cond);
        branch_list.push(self.expression(&branch.1)?);
        let branch_val = Expr::Block(branch_list);
        self.end_scope();

        Ok((cond, branch_val))
    }

    /// If a when expression can safely give a value even when an else branch is missing.
    /// Only true when switching on enum type with every case present.
    fn can_omit_else(&self, value_ty: &Type, switch_cases: &[(Expr, Expr)]) -> bool {
        let adt = if let Type::Adt(adt) = value_ty {
            adt
        } else {
            return false;
        };
        let adt = adt.borrow();
        let cases = if let ADTType::Enum { cases } = &adt.ty {
            cases
        } else {
            return false;
        };
        let mut cases: Vec<&MutRc<ADT>> = cases.values().collect();

        for (cond, _) in switch_cases.iter() {
            let (op, right) = if let Expr::Binary {
                operator, right, ..
            } = cond
            {
                (operator, right)
            } else {
                panic!("Invalid match condition")
            };

            if *op != TType::Is {
                return false;
            };
            let ty = right.get_type();
            let ty = ty.as_type().as_adt();
            let i = cases.iter().position(|c| Rc::ptr_eq(c, &ty));
            if let Some(i) = i {
                cases.remove(i);
            }
        }
        cases.is_empty()
    }

    fn var_def(&mut self, var: &ASTVar) -> Res<Expr> {
        let init = self.expression(&var.initializer)?;
        let type_ = init.get_type();
        if type_.is_assignable() {
            let var = self.define_variable(&var.name, var.mutable, type_);
            Ok(Expr::store(&var, init, true))
        } else {
            Err(self.err(
                &var.initializer.get_token(),
                &format!("Cannot assign type '{}' to a variable.", type_),
            ))
        }
    }
}
