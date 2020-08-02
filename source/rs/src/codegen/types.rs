/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 1:58 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use crate::{
    codegen::IRGenerator,
    ir::nodes::{ADTType, AbstractMethod, ClosureType, Function, Type, Variable, ADT},
};
use inkwell::{
    types::{BasicType, BasicTypeEnum, FunctionType, PointerType, StructType},
    values::PointerValue,
    AddressSpace::Generic,
};
use std::{cell::Ref, rc::Rc};

impl IRGenerator {
    /// Converts a `MIRType` to the corresponding LLVM type.
    /// Structs are returned as `PointerType<StructType>`.
    pub fn ir_ty_ptr(&mut self, mir: &Type) -> BasicTypeEnum {
        match mir {
            Type::None => return self.none_const.get_type(),
            Type::Pointer(inner) => return self.ir_ty_ptr(inner).ptr_type(Generic).into(),
            _ => (),
        }
        let ir = self.ir_ty(mir);
        match (ir, mir) {
            // If the type does not need lifecycle (currently only interfaces), then it is passed by value
            (BasicTypeEnum::StructType(_), Type::Adt(adt))
                if !adt.borrow().ty.needs_lifecycle() =>
            {
                ir
            }
            (BasicTypeEnum::StructType(_), Type::Value(_)) => ir,
            (BasicTypeEnum::StructType(struc), _) => struc.ptr_type(Generic).into(),
            _ => ir,
        }
    }

    /// Converts a `MIRType` to the corresponding LLVM type.
    pub fn ir_ty(&mut self, mir: &Type) -> BasicTypeEnum {
        self.ir_ty_full(mir).0
    }

    /// Converts a `MIRType` to the corresponding LLVM type info global struct.
    pub fn ir_ty_info(&mut self, mir: &Type) -> PointerValue {
        self.ir_ty_full(mir).1
    }

    pub fn ir_ty_full(&mut self, mir: &Type) -> (BasicTypeEnum, PointerValue) {
        self.types
            .get(mir)
            .copied()
            .unwrap_or_else(|| self.build_type(mir))
    }

    /// Generates a type, if it was not found in self.types.
    fn build_type(&mut self, ty: &Type) -> (BasicTypeEnum, PointerValue) {
        let ir_ty = match ty {
            // Any is a special case - it is not in self.types
            // as it is considered equal to all other types -
            // this would break the hashmap and result in returning
            // of Any when the type searched for is not Any.
            Type::Any => return (self.none_const.get_type(), self.nullptr()),

            Type::Function(func) => self.build_fn_type(func.borrow()).ptr_type(Generic).into(),

            Type::Closure(closure) => self.build_closure_type(closure),

            Type::ClosureCaptured(captured) => self.build_captured_type(captured).into(),

            Type::Adt(adt) => match adt.borrow().ty {
                ADTType::Class { external } if external => self
                    .build_struct(
                        &adt.borrow().name,
                        adt.borrow().members.iter().map(|(_, m)| &m.type_),
                        false,
                        false,
                    )
                    .into(),

                ADTType::Interface { .. } => self.build_iface_type(adt.borrow()).into(),

                _ => self
                    .build_struct(
                        &adt.borrow().name,
                        adt.borrow().members.iter().map(|(_, m)| &m.type_),
                        true,
                        true,
                    )
                    .into(),
            },

            Type::Pointer(inner) => self.ir_ty(inner).ptr_type(Generic).into(),

            Type::Value(inner) => self.ir_ty(inner),

            _ => panic!(format!("Unknown type '{}' to build", ty)),
        };

        let type_info = self.build_type_info();

        self.types.insert(ty.clone(), (ir_ty, type_info));
        match ir_ty {
            BasicTypeEnum::StructType(struc) if !ty.is_value() => {
                self.types_bw.insert(
                    struc.get_name().unwrap().to_str().unwrap().to_string(),
                    ty.clone(),
                );
            }
            _ => (),
        }
        (ir_ty, type_info)
    }

    /// Generates the struct for captured variables, given a list of them.
    fn build_captured_type(&mut self, captured: &[Rc<Variable>]) -> StructType {
        self.build_struct(
            "closure-captured",
            captured.iter().map(|var| &var.type_),
            true,
            false,
        )
    }

    /// Generates a struct out of an iterator of member types.
    fn build_struct<'a, T: Iterator<Item = &'a Type>>(
        &mut self,
        name: &str,
        body: T,
        refcount: bool,
        type_info: bool,
    ) -> StructType {
        let body: Vec<_> = body.map(|var| self.ir_ty_ptr(&var)).collect();
        self.build_struct_ir(name, body.into_iter(), refcount, type_info)
    }

    fn build_struct_ir<T: Iterator<Item = BasicTypeEnum>>(
        &self,
        name: &str,
        body: T,
        refcount: bool,
        type_info: bool,
    ) -> StructType {
        let first_field = if refcount {
            Some(self.context.i32_type().into())
        } else {
            None
        };
        let second_field = if type_info {
            Some(self.type_info_type.ptr_type(Generic).into())
        } else {
            None
        };

        let struc_val = self.context.opaque_struct_type(name);
        let body: Vec<_> = first_field
            .into_iter()
            .chain(second_field.into_iter())
            .chain(body)
            .collect();
        struc_val.set_body(&body, false);
        struc_val
    }

    /// Generates the struct for a closure, containing a function pointer
    /// and a pointer to captured variables.
    fn build_closure_type(&mut self, closure: &ClosureType) -> BasicTypeEnum {
        let refcount = self.context.i32_type().into();
        let func_ty = self
            .fn_type_from_raw(
                Some(Type::I64).iter().chain(closure.parameters.iter()),
                &closure.ret_type,
                false,
            )
            .ptr_type(Generic)
            .into();
        let captured_ty = self.context.i64_type().into();

        let struc_val = self.context.opaque_struct_type("closure");
        let free_ty = self
            .context
            .void_type()
            .fn_type(&[struc_val.ptr_type(Generic).into()], false)
            .ptr_type(Generic)
            .into();
        struc_val.set_body(&[refcount, func_ty, free_ty, captured_ty], false);
        struc_val.into()
    }

    /// Generates the LLVM `FunctionType` of a MIR function.
    pub fn build_fn_type(&mut self, func: Ref<Function>) -> FunctionType {
        let params = func.parameters.iter().map(|param| &param.type_);
        let variadic = func.ast.as_ref().map_or(false, |a| a.sig.variadic);
        self.fn_type_from_raw(params, &func.ret_type, variadic)
    }

    /// Generates a function type from raw parts - parameters, return type.
    fn fn_type_from_raw<'a, T: Iterator<Item = &'a Type>>(
        &mut self,
        params: T,
        ret_type: &Type,
        variadic: bool,
    ) -> FunctionType {
        let params: Vec<BasicTypeEnum> = params.map(|param| self.ir_ty_ptr(param)).collect();
        if *ret_type == Type::None {
            self.context.void_type().fn_type(&params, variadic)
        } else {
            self.ir_ty_ptr(ret_type).fn_type(&params, variadic)
        }
    }

    /// Generate the type of an interface when used as a standalone type,
    /// which is a struct with 2 pointers (vtable + implementor).
    fn build_iface_type(&mut self, iface: Ref<ADT>) -> StructType {
        let free_method_sig = Some(
            self.context
                .void_type()
                .fn_type(
                    &[self.void_ptr().into(), self.context.bool_type().into()],
                    false,
                )
                .ptr_type(Generic)
                .into(),
        );
        let vtable: Vec<BasicTypeEnum> = free_method_sig
            .into_iter()
            .chain(
                iface
                    .dyn_methods
                    .iter()
                    .map(|(_, method)| self.build_iface_method_type(method)),
            )
            .collect();
        let vtable_struct = self.build_struct_ir("vtable", vtable.into_iter(), false, false);

        self.build_struct_ir(
            &format!("iface-{}", &iface.name),
            vec![
                self.context.i64_type().ptr_type(Generic).into(),
                vtable_struct.ptr_type(Generic).into(),
            ]
            .into_iter(),
            false,
            false,
        )
    }

    fn build_iface_method_type(&mut self, method: &AbstractMethod) -> BasicTypeEnum {
        let params: Vec<BasicTypeEnum> = Some(self.void_ptr().into())
            .into_iter()
            .chain(method.parameters.iter().map(|param| self.ir_ty_ptr(&param)))
            .collect();

        if method.ret_type == Type::None {
            self.context.void_type().fn_type(params.as_slice(), false)
        } else {
            let ret_type = self.ir_ty_ptr(&method.ret_type);
            ret_type.fn_type(params.as_slice(), false)
        }
        .ptr_type(Generic)
        .into()
    }

    fn build_type_info(&self) -> PointerValue {
        let global = self
            .module
            .add_global(self.type_info_type, None, "typeinfo");
        global.set_initializer(
            &self.type_info_type.const_named_struct(&[self
                .context
                .i64_type()
                .const_int(0, false)
                .into()]),
        );
        global.as_pointer_value()
    }

    pub fn void_ptr(&self) -> PointerType {
        self.context.i64_type().ptr_type(Generic)
    }
}
