/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 3:28 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use crate::{
    ast::Literal,
    codegen::{IRGenerator, LoopData, PtrEqRc},
    scanner::token::TType,
    ir::{
        get_iface_impls,
        nodes::{ADTType, Expr, Function, Type, Variable, ADT},
        MutRc,
    },
};
use inkwell::{
    types::{AnyTypeEnum, BasicType, BasicTypeEnum, PointerType, StructType},
    values::{BasicValueEnum, PointerValue},
    AddressSpace::Generic,
    FloatPredicate, IntPredicate,
};
use std::rc::Rc;

impl IRGenerator {
    pub fn expression(&mut self, expression: &Expr) -> BasicValueEnum {
        if self.builder.get_insert_block().is_none() {
            return self.none_const;
        }

        match expression {
            Expr::AllocInst {
                ty,
                constructor,
                constructor_args,
                heap,
            } => self.alloc_inst(ty, constructor, constructor_args, heap.get()),

            Expr::Binary {
                left,
                operator,
                right,
            } => {
                let left = self.expression(left);
                if operator == &TType::Is {
                    let ty_info_ptr = self.ir_ty_info(right.get_type().as_type());
                    let left_ptr = self.get_type_info_field(left.into_pointer_value());
                    let left_ptr = self.load_ptr(left_ptr).into_pointer_value();

                    let left_int =
                        self.builder
                            .build_ptr_to_int(left_ptr, self.context.i64_type(), "conv");
                    let right_int =
                        self.builder
                            .build_ptr_to_int(ty_info_ptr, self.context.i64_type(), "conv");
                    self.builder
                        .build_int_compare(IntPredicate::EQ, left_int, right_int, "ident")
                        .into()
                } else {
                    let right = self.expression(right);
                    self.binary(left, *operator, right)
                }
            }

            Expr::Block(exprs) => {
                self.push_locals();

                let mut val = self.none_const;
                for expr in exprs {
                    val = self.expression(expr);
                }

                self.pop_locals_lift(val);
                val
            }

            Expr::Break(value) => {
                if self.loop_data.as_ref().unwrap().phi_nodes.is_some() {
                    let node = (self.expression(value), self.last_block());
                    self.loop_data
                        .as_mut()
                        .unwrap()
                        .phi_nodes
                        .as_mut()
                        .unwrap()
                        .push(node);
                }
                self.builder
                    .build_unconditional_branch(&self.loop_data.as_ref().unwrap().end_block);
                self.builder.clear_insertion_position();
                self.none_const
            }

            Expr::Call { callee, arguments } => {
                let callee = self.expression(callee);
                let (ptr, first_arg) = self.function_from_callee(callee);
                self.build_call(ptr, arguments.iter(), first_arg)
            }

            Expr::CallDyn {
                index, arguments, ..
            } => self.call_dyn(*index, arguments),

            Expr::Cast { object, to } => self.cast(object, to),

            Expr::ConstructClosure {
                function,
                global,
                captured,
            } => self.construct_closure(function, global, captured),

            Expr::Free(expr) => {
                let ptr = self.expression(expr).into_pointer_value();
                self.builder.build_free(ptr);
                self.none_const
            }

            Expr::If {
                condition,
                then,
                else_,
                phi,
            } => self.if_(condition, then, else_, *phi),

            Expr::Literal(literal) => self.literal(literal),

            Expr::Loop {
                condition,
                body,
                else_,
                result_store,
            } => self.loop_(condition, body, else_, result_store),

            Expr::ModifyRefCount { object, dec } => self.modify_ref_count(object, *dec),

            Expr::Return(value) => {
                let value = self.expression(value);
                self.increment_refcount(value, false);
                self.decrement_all_locals();

                if value.get_type() == self.none_const.get_type() {
                    self.builder.build_return(None);
                } else {
                    self.builder.build_return(Some(&value));
                }

                self.builder.clear_insertion_position();
                self.none_const
            }

            Expr::StructGet {
                object,
                index,
                val_ty,
            } => {
                let struc = self.expression(object);
                let ptr = self.struct_gep(struc.into_pointer_value(), *index);
                self.load_ptr_mir(ptr, val_ty)
            }

            Expr::StructSet {
                object,
                index,
                value,
                first_set,
            } => {
                let struc = self.expression(object);
                let ptr = self.struct_gep(struc.into_pointer_value(), *index);
                let value = self.expression(value);
                self.build_store(ptr, value, *first_set);
                value
            }

            // This expression cannot be used in a meaningful way - all
            // possible uses are transformed in MIR already.
            Expr::TypeGet(_) => self.none_const,

            Expr::Unary { right, operator } => self.unary(right, *operator),

            Expr::VarGet(var) => self.load_ptr_mir(self.get_variable(var), &var.type_),

            Expr::VarStore {
                var,
                value,
                first_store,
            } => {
                let var = self.get_variable(var);
                let val = self.expression(value);
                self.build_store(var, val, *first_store);
                if *first_store {
                    self.locals().push((var.into(), true));
                }

                val
            }

            Expr::Switch { cases, else_, phi } => self.switch(cases, else_, phi.is_some()),
        }
    }

    fn alloc_inst(
        &mut self,
        ty: &MutRc<ADT>,
        constructor: &Rc<Variable>,
        constructor_args: &[Expr],
        heap: bool,
    ) -> BasicValueEnum {
        let ir_ty = self.ir_ty(&Type::Adt(ty.clone()));
        let alloc = self.create_alloc(ir_ty, heap);
        self.maybe_init_type_info(ty, alloc);
        self.build_alloc_and_init(
            alloc,
            self.get_variable(&ty.borrow().instantiator.as_ref().unwrap()),
            self.get_variable(&constructor),
            constructor_args,
        )
    }

    fn maybe_init_type_info(&mut self, ty: &MutRc<ADT>, alloc: PointerValue) {
        if ty.borrow().ty.needs_lifecycle() && ty.borrow().ty.has_refcount() {
            let gep = unsafe { self.builder.build_struct_gep(alloc, 1, "tygep") };
            let val = self.ir_ty_info(&Type::Adt(Rc::clone(ty)));
            self.builder.build_store(gep, val);
        }
    }

    fn build_alloc_and_init(
        &mut self,
        alloc: PointerValue,
        instantiator: PointerValue,
        constructor: PointerValue,
        constructor_args: &[Expr],
    ) -> BasicValueEnum {
        self.increment_refcount(alloc.into(), true);
        self.builder
            .build_call(instantiator, &[alloc.into()], "inst");

        let mut arguments: Vec<BasicValueEnum> = constructor_args
            .iter()
            .map(|a| self.expression(a))
            .collect();
        for arg in &arguments {
            self.increment_refcount(*arg, false);
        }
        arguments.insert(0, alloc.into());
        self.builder.build_call(constructor, &arguments, "constr");
        for arg in arguments.iter().skip(1) {
            self.decrement_refcount(*arg, false);
        }

        self.locals().push((alloc.into(), true));
        alloc.into()
    }

    fn binary(
        &self,
        left: BasicValueEnum,
        operator: TType,
        right: BasicValueEnum,
    ) -> BasicValueEnum {
        match (left, right) {
            (BasicValueEnum::IntValue(left), BasicValueEnum::IntValue(right)) => {
                BasicValueEnum::IntValue(match operator {
                    TType::Plus => self.builder.build_int_add(left, right, "add"),
                    TType::Minus => self.builder.build_int_sub(left, right, "sub"),
                    TType::Star => self.builder.build_int_mul(left, right, "mul"),
                    TType::Slash => self.builder.build_int_signed_div(left, right, "div"),
                    TType::Modulo => self.builder.build_int_signed_rem(left, right, "rem"),
                    TType::And => self.builder.build_and(left, right, "and"),
                    TType::Or => self.builder.build_or(left, right, "or"),
                    _ => {
                        self.builder
                            .build_int_compare(get_predicate(operator), left, right, "cmp")
                    }
                })
            }

            (BasicValueEnum::FloatValue(left), BasicValueEnum::FloatValue(right)) => {
                BasicValueEnum::FloatValue(match operator {
                    TType::Plus => self.builder.build_float_add(left, right, "add"),
                    TType::Minus => self.builder.build_float_sub(left, right, "sub"),
                    TType::Star => self.builder.build_float_mul(left, right, "mul"),
                    TType::Slash => self.builder.build_float_div(left, right, "div"),
                    TType::Modulo => self.builder.build_float_rem(left, right, "rem"),
                    _ => {
                        return BasicValueEnum::IntValue(self.builder.build_float_compare(
                            get_float_predicate(operator),
                            left,
                            right,
                            "cmp",
                        ))
                    }
                })
            }

            // One of the operators is `Any`, so it will branch away; return whatever
            _ => self.context.bool_type().const_int(0, false).into(),
        }
    }

    fn function_from_callee(
        &mut self,
        callee: BasicValueEnum,
    ) -> (PointerValue, Option<BasicValueEnum>) {
        let ptr = callee.into_pointer_value();
        match ptr.get_type().get_element_type() {
            // Regular function call
            AnyTypeEnum::FunctionType(_) => (ptr, None),

            // Closure call with captured as first arg
            AnyTypeEnum::StructType(_) => (
                self.load_ptr(self.struct_gep(ptr, 0)).into_pointer_value(),
                Some(self.load_ptr(self.struct_gep(ptr, 2))),
            ),

            _ => panic!("Invalid callee"),
        }
    }

    fn call_dyn(&mut self, index: usize, arguments: &[Expr]) -> BasicValueEnum {
        let mut arguments = arguments.iter();

        let iface_struct = self.expression(arguments.next().unwrap());
        let vtable_ptr = self
            .builder
            .build_extract_value(iface_struct.into_struct_value(), 1, "vtable")
            .unwrap()
            .into_pointer_value();

        // The '+1' is required to account for the 'free' method that is
        // added to all vtables in IR.
        let method_ptr = self
            .load_ptr(self.struct_gep(vtable_ptr, index + 1))
            .into_pointer_value();

        let implementor_ptr = self
            .builder
            .build_extract_value(iface_struct.into_struct_value(), 0, "impl")
            .unwrap()
            .into_pointer_value();
        self.build_call(method_ptr, arguments, Some(implementor_ptr.into()))
    }

    fn build_call<'a, T: Iterator<Item = &'a Expr>>(
        &mut self,
        ptr: PointerValue,
        arguments: T,
        first_arg: Option<BasicValueEnum>,
    ) -> BasicValueEnum {
        let arguments: Vec<BasicValueEnum> = first_arg
            .into_iter()
            .chain(arguments.map(|a| self.expression(a)))
            .collect();

        for arg in &arguments {
            self.increment_refcount(*arg, false);
        }

        let ret = self
            .builder
            .build_call(ptr, &arguments, "call")
            .try_as_basic_value();
        let ret = ret.left().unwrap_or(self.none_const);
        self.locals().push((ret, false));

        for arg in &arguments {
            self.decrement_refcount(*arg, false);
        }

        ret
    }

    fn cast(&mut self, object: &Expr, to: &Type) -> BasicValueEnum {
        match to {
            _ if to.is_int() => {
                let obj = self.expression(object);
                let cast_ty = self.ir_ty(to).into_int_type();
                self.builder
                    .build_int_cast(obj.into_int_value(), cast_ty, "cast")
                    .into()
            }

            _ if to.is_float() => {
                let obj = self.expression(object);
                let cast_ty = self.ir_ty(to).into_float_type();
                self.builder
                    .build_float_cast(obj.into_float_value(), cast_ty, "cast")
                    .into()
            }

            Type::Adt(adt) => {
                if let ADTType::Interface { .. } = adt.borrow().ty {
                    self.cast_to_interface(object, to)
                } else {
                    // This should be an enum cast;
                    // simply a bitcast is sufficient
                    let obj = self.expression(object);
                    let cast_ty = self.ir_ty_ptr(to);
                    self.builder.build_bitcast(obj, cast_ty, "cast")
                }
            }

            _ => panic!("Invalid cast"),
        }
    }

    fn cast_to_interface(&mut self, object: &Expr, to: &Type) -> BasicValueEnum {
        let obj = self.expression(object);
        let iface_ty = self.ir_ty(to).into_struct_type();
        let vtable_ty = iface_ty.get_field_types()[1]
            .as_pointer_type()
            .get_element_type()
            .into_struct_type();

        let vtable = self.get_vtable(&object.get_type(), to, vtable_ty);
        let store = self.create_alloc(iface_ty.into(), false);
        self.write_struct(store, [self.coerce_to_void_ptr(obj), vtable].iter());
        self.builder.build_load(store, "ifaceload")
    }

    /// Returns the vtable of the interface implementor given.
    /// Will generate functions as needed to fill the vtable.
    fn get_vtable(
        &mut self,
        implementor: &Type,
        iface: &Type,
        vtable: StructType,
    ) -> BasicValueEnum {
        let field_tys = vtable.get_field_types();
        let mut field_tys = field_tys.iter();
        let impls = get_iface_impls(&implementor).unwrap();
        let impls = impls.borrow();
        let methods_iter = self
            .get_free_function(&implementor)
            .into_iter()
            .chain(
                impls.interfaces[iface]
                    .methods
                    .iter()
                    .map(|(_, method)| self.functions[&PtrEqRc::new(method)])
                    .map(|f| f.as_global_value().as_pointer_value()),
            )
            .map(|func| {
                self.builder.build_bitcast(
                    func,
                    *field_tys.next().unwrap().as_pointer_type(),
                    "funccast",
                )
            });
        let methods = methods_iter.collect::<Vec<_>>();
        let global = self.module.add_global(vtable, None, "vtable");
        global.set_initializer(&vtable.const_named_struct(&methods));
        global.as_pointer_value().into()
    }

    fn get_free_function(&self, ty: &Type) -> Option<PointerValue> {
        Some(match ty {
            Type::Adt(adt) if adt.borrow().destructor.is_some() => self.functions
                [&PtrEqRc::new(&adt.borrow().destructor.as_ref().unwrap())]
                .as_global_value()
                .as_pointer_value(),
            _ => self.void_ptr().const_zero(),
        })
    }

    fn construct_closure(
        &mut self,
        function: &MutRc<Function>,
        global: &Rc<Variable>,
        captured: &Rc<Vec<Rc<Variable>>>,
    ) -> BasicValueEnum {
        let func_ptr = self.cast_first_param_to_i64(self.get_variable(global));

        let captured_ty = self.ir_ty(&Type::ClosureCaptured(Rc::clone(captured)));
        let captured_vals = self.create_captured_values(captured_ty, captured);
        let captured_vals = self
            .builder
            .build_ptr_to_int(captured_vals, self.context.i64_type(), "captcast")
            .into();

        let ty = self.ir_ty(&function.borrow().to_closure_type());
        let free_ptr =
            self.create_closure_free(ty.ptr_type(Generic), captured_ty.ptr_type(Generic));

        let alloc = self.create_alloc(ty, true);
        self.write_struct(alloc, [func_ptr, free_ptr.into(), captured_vals].iter());
        alloc.into()
    }

    /// Takes a `PointerValue<FunctionValue>` and casts its type
    /// to have the first parameter type be replaced with i64.
    fn cast_first_param_to_i64(&self, val: PointerValue) -> BasicValueEnum {
        let func_ty = val.get_type().get_element_type().into_function_type();
        let mut params = func_ty.get_param_types();
        params[0] = self.context.i64_type().into();
        let func_ty = if let Some(ret_type) = func_ty.get_return_type() {
            ret_type.fn_type(&params, false)
        } else {
            self.context.void_type().fn_type(&params, false)
        };
        self.builder
            .build_bitcast(val, func_ty.ptr_type(Generic), "bc")
    }

    fn create_captured_values(
        &mut self,
        ty: BasicTypeEnum,
        captured: &[Rc<Variable>],
    ) -> PointerValue {
        let alloc = self.create_alloc(ty, true);
        for (i, var) in captured.iter().enumerate() {
            let value = self.load_ptr(self.get_variable(var));
            self.build_store(self.struct_gep(alloc, i), value, true);
        }
        alloc
    }

    /// Builds the free function of a given closure.
    fn create_closure_free(
        &mut self,
        closure_ty: PointerType,
        captured_ty: PointerType,
    ) -> PointerValue {
        let func = self.module.add_function(
            "free-closure",
            self.context
                .void_type()
                .fn_type(&[closure_ty.into()], false),
            None,
        );
        let closure = func.get_first_param().unwrap().into_pointer_value();
        let old_builder = std::mem::replace(&mut self.builder, self.context.create_builder());

        let entry_bb = func.append_basic_block("entry");
        let dealloc_bb = func.append_basic_block("dealloc");
        let end_bb = func.append_basic_block("end");

        self.builder.position_at_end(&entry_bb);
        let refcount = unsafe { self.builder.build_struct_gep(closure, 0, "rcgep") };
        let refcount = self.builder.build_load(refcount, "rcload").into_int_value();
        let rc_is_0 = self.builder.build_int_compare(
            IntPredicate::EQ,
            refcount,
            self.context.i32_type().const_int(0, false),
            "rc_is_0",
        );
        self.builder
            .build_conditional_branch(rc_is_0, &dealloc_bb, &end_bb);

        self.builder.position_at_end(&dealloc_bb);
        let captured = unsafe { self.builder.build_struct_gep(closure, 3, "captgep") };
        let captured_int = self
            .builder
            .build_load(captured, "captload")
            .into_int_value();
        let captured = self
            .builder
            .build_int_to_ptr(captured_int, captured_ty, "captcast");
        for (i, _) in captured_ty
            .get_element_type()
            .into_struct_type()
            .get_field_types()
            .iter()
            .enumerate()
        {
            let val = unsafe { self.builder.build_struct_gep(captured, i as u32, "Cgep") };
            self.decrement_refcount(self.load_ptr(val), false)
        }
        self.builder.build_free(captured);
        self.builder.build_free(closure);
        self.builder.build_unconditional_branch(&end_bb);

        self.builder.position_at_end(&end_bb);
        self.builder.build_return(None);

        self.builder = old_builder;
        func.as_global_value().as_pointer_value()
    }

    fn if_(&mut self, cond: &Expr, then: &Expr, else_: &Expr, phi: bool) -> BasicValueEnum {
        let cond = self.expression(cond);
        let then_bb = self.append_block("then");
        let else_bb = self.append_block("else");
        let cont_bb = self.append_block("cont");

        self.builder
            .build_conditional_branch(cond.into_int_value(), &then_bb, &else_bb);

        self.position_at_block(then_bb);
        self.push_locals();
        let then_val = self.expression(then);
        let then_bb = self.last_block();
        if phi {
            self.pop_locals_remove(then_val);
        } else {
            self.pop_dec_locals()
        }
        self.builder.build_unconditional_branch(&cont_bb);

        self.position_at_block(else_bb);
        self.push_locals();
        let else_val = self.expression(else_);
        let else_bb = self.last_block();
        if phi {
            self.pop_locals_remove(else_val);
        } else {
            self.pop_dec_locals()
        }
        self.builder.build_unconditional_branch(&cont_bb);

        self.position_at_block(cont_bb);
        if phi {
            self.build_phi(&[(then_val, then_bb), (else_val, else_bb)])
        } else {
            self.none_const
        }
    }

    fn loop_(
        &mut self,
        condition: &Expr,
        body: &Expr,
        else_: &Expr,
        result_store: &Option<Rc<Variable>>,
    ) -> BasicValueEnum {
        let loop_bb = self.append_block("for-loop");
        let else_bb = self.append_block("for-else");
        let cont_bb = self.append_block("for-cont");

        let prev_loop = std::mem::replace(
            &mut self.loop_data,
            Some(LoopData {
                end_block: cont_bb,
                phi_nodes: if result_store.is_some() {
                    Some(vec![])
                } else {
                    None
                },
            }),
        );

        let cond = self.expression(condition).into_int_value();
        self.builder
            .build_conditional_branch(cond, &loop_bb, &else_bb);

        self.position_at_block(loop_bb);
        self.push_locals();
        let body = self.expression(body);
        let loop_end_bb = self.last_block();
        if let Some(result_store) = result_store {
            self.build_store(self.get_variable(result_store), body, false);
        }
        self.pop_dec_locals();
        let cond = self.expression(condition).into_int_value();
        let phi_node = if let Some(result_store) = result_store {
            Some(self.load_ptr(self.get_variable(result_store)))
        } else {
            None
        };
        self.builder
            .build_conditional_branch(cond, &loop_bb, &cont_bb);

        self.position_at_block(else_bb);
        self.push_locals();
        let else_val = self.expression(else_);
        let else_bb = self.last_block();
        self.pop_dec_locals();
        self.builder.build_unconditional_branch(&cont_bb);

        self.position_at_block(cont_bb);
        let loop_data = std::mem::replace(&mut self.loop_data, prev_loop).unwrap();
        if result_store.is_some() {
            let mut phi_nodes = loop_data.phi_nodes.unwrap();
            phi_nodes.push((phi_node.unwrap(), loop_end_bb));
            phi_nodes.push((else_val, else_bb));
            self.build_phi(&phi_nodes)
        } else {
            self.none_const
        }
    }

    fn modify_ref_count(&mut self, object: &Expr, dec: bool) -> BasicValueEnum {
        let object = self.expression(object);
        if dec {
            self.decrement_refcount(object, false); // TODO: is false correct?
        } else {
            self.increment_refcount(object, false);
        }
        object
    }

    fn literal(&mut self, literal: &Literal) -> BasicValueEnum {
        match literal {
            Literal::Any | Literal::None => self.none_const,
            Literal::Bool(value) => self
                .context
                .bool_type()
                .const_int(*value as u64, false)
                .into(),

            Literal::I8(num) | Literal::U8(num) => {
                self.context.i8_type().const_int(*num as u64, false).into()
            }
            Literal::I16(num) | Literal::U16(num) => {
                self.context.i16_type().const_int(*num as u64, false).into()
            }
            Literal::I32(num) | Literal::U32(num) => {
                self.context.i32_type().const_int(*num as u64, false).into()
            }
            Literal::I64(num) | Literal::U64(num) => {
                self.context.i64_type().const_int(*num as u64, false).into()
            }

            Literal::F32(num) => self.context.f32_type().const_float((*num).into()).into(),
            Literal::F64(num) => self.context.f64_type().const_float(*num).into(),

            Literal::String(string) => {
                // If the builder's insert position is not set, creating a global string pointer
                // will segfault (https://github.com/TheDan64/inkwell/issues/32)
                // This is usually only the case when a return expression unset the position
                // earlier, in which case the actual value doesn't matter anyway.
                if self.builder.get_insert_block().is_none() {
                    self.none_const
                } else {
                    let const_str = self.builder.build_global_string_ptr(&string, "str");
                    let string_builder = self
                        .module
                        .get_function("std::intrinsics:build_string_literal")
                        .unwrap();
                    let st = self
                        .builder
                        .build_call(
                            string_builder,
                            &[
                                const_str.as_pointer_value().into(),
                                self.context
                                    .i64_type()
                                    .const_int((string.len() + 1) as u64, false)
                                    .into(),
                            ],
                            "str",
                        )
                        .try_as_basic_value()
                        .left()
                        .unwrap();
                    self.locals().push((st, false));
                    st
                }
            }

            _ => panic!("unknown literal"),
        }
    }

    fn unary(&mut self, right: &Expr, operator: TType) -> BasicValueEnum {
        let expr = self.expression(right);
        match expr {
            BasicValueEnum::IntValue(int) => match operator {
                TType::Bang => self.builder.build_not(int, "unarynot"),
                TType::Minus => self.builder.build_int_neg(int, "unaryneg"),
                _ => panic!("Invalid unary operator"),
            }
            .into(),

            BasicValueEnum::FloatValue(float) => {
                self.builder.build_float_neg(float, "unaryneg").into()
            }

            _ => panic!("Invalid unary operator"),
        }
    }

    fn switch(
        &mut self,
        cases: &[(Expr, Expr)],
        else_: &Option<Box<Expr>>,
        phi: bool,
    ) -> BasicValueEnum {
        let cond = self.context.bool_type().const_int(1, false);
        let end_bb = self.append_block("switch-end");

        let mut phi_nodes = Vec::with_capacity(cases.len());
        let mut next_bb = self.append_block("switch-case-false");
        // If the else block is missing, the last block becomes the 'default', so don't compile it in the loop
        for (br_cond, branch) in cases.iter().take(cases.len() - else_.is_none() as usize) {
            let case_bb = self.append_block("switch-case");

            self.push_locals();
            let br_cond = self.expression(br_cond).into_int_value();
            self.pop_dec_locals();
            let cmp = self
                .builder
                .build_int_compare(IntPredicate::EQ, cond, br_cond, "switch-cmp");
            self.builder
                .build_conditional_branch(cmp, &case_bb, &next_bb);

            self.position_at_block(case_bb);
            self.push_locals();
            let value = self.expression(branch);
            if phi {
                self.pop_locals_remove(value)
            } else {
                self.pop_dec_locals()
            };
            phi_nodes.push((value, self.last_block()));
            self.builder.build_unconditional_branch(&end_bb);

            self.position_at_block(next_bb);
            next_bb = self.append_block("switch-case-false");
        }
        // Next case is 'else', this BB is not needed
        next_bb.remove_from_function().unwrap();

        // If the last case falls though, do the else case
        let else_ = else_
            .as_ref()
            .map(|e| &**e)
            .or_else(|| cases.last().map(|l| &l.1))
            .unwrap();
        self.push_locals();
        let else_val = self.expression(else_);
        if phi {
            self.pop_locals_remove(else_val)
        } else {
            self.pop_dec_locals()
        };
        let else_end_bb = self.last_block();
        self.builder.build_unconditional_branch(&end_bb);
        phi_nodes.push((else_val, else_end_bb));

        self.position_at_block(end_bb);
        if phi {
            self.build_phi(&phi_nodes)
        } else {
            self.none_const
        }
    }
}

fn get_predicate(tok: TType) -> IntPredicate {
    match tok {
        TType::Greater => IntPredicate::SGT,
        TType::GreaterEqual => IntPredicate::SGE,
        TType::Less => IntPredicate::SLT,
        TType::LessEqual => IntPredicate::SLE,
        TType::EqualEqual => IntPredicate::EQ,
        TType::BangEqual => IntPredicate::NE,
        _ => panic!("invalid tok"),
    }
}

fn get_float_predicate(tok: TType) -> FloatPredicate {
    match tok {
        TType::Greater => FloatPredicate::OGT,
        TType::GreaterEqual => FloatPredicate::OGE,
        TType::Less => FloatPredicate::OLT,
        TType::LessEqual => FloatPredicate::OLE,
        TType::EqualEqual => FloatPredicate::OEQ,
        TType::BangEqual => FloatPredicate::ONE,
        _ => panic!("invalid tok"),
    }
}
