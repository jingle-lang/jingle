/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 3:26 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use crate::{
    codegen::IRGenerator,
    ir::{
        nodes::{Type, ADT},
        MutRc,
    },
};
use inkwell::{
    types::{AnyTypeEnum, BasicType, StructType},
    values::{BasicValueEnum, IntValue, PointerValue, StructValue},
    AddressSpace::Generic,
    IntPredicate,
};

impl IRGenerator {
    /// Build a store; will do required refcount modification.
    pub fn build_store(&self, ptr: PointerValue, value: BasicValueEnum, is_null: bool) {
        if !is_null {
            self.decrement_refcount(ptr.into(), true);
        }
        self.builder.build_store(ptr, value);
        self.increment_refcount(ptr.into(), true);
    }

    /// Increment the refcount of a value.
    /// is_ptr specifies if the value is a pointer or a value in
    /// the context of the MIR type system.
    pub fn increment_refcount(&self, value: BasicValueEnum, is_ptr: bool) {
        if let Some(val) = self.get_rc_value(value, is_ptr) {
            self.mod_refcount(val, false)
        }
    }

    /// Decrement the refcount of a value, and check if it needs to be freed
    /// is_ptr specifies if the value is a pointer or a value in
    /// the context of the MIR type system.
    pub fn decrement_refcount(&self, value: BasicValueEnum, is_ptr: bool) {
        if let Some(val) = self.get_rc_value(value, is_ptr) {
            self.mod_refcount(val, true)
        }
    }

    /// Returns a modified version of the value ready for modifying the refcount,
    /// should the value be refcounted.
    /// is_ptr specifies if the value is a pointer or a value in
    /// the context of the MIR type system.
    fn get_rc_value(&self, value: BasicValueEnum, is_ptr: bool) -> Option<BasicValueEnum> {
        if value.get_type() == self.none_const.get_type().ptr_type(Generic).into() {
            return None;
        }

        match value {
            BasicValueEnum::PointerValue(ptr) => match ptr.get_type().get_element_type() {
                AnyTypeEnum::PointerType(_) if is_ptr => {
                    self.get_rc_value(self.load_ptr(ptr), false)
                }
                AnyTypeEnum::StructType(struc) if Self::needs_gc(struc) => Some(self.load_ptr(ptr)),
                _ => None,
            },

            BasicValueEnum::StructValue(struc) if Self::needs_gc(struc.get_type()) => Some(value),

            _ => None,
        }
    }

    /// Checks if a given struct needs to be GC'd.
    fn needs_gc(struc: StructType) -> bool {
        !struc
            .get_name()
            .map_or(true, |name| name.to_str().unwrap().starts_with("vtable"))
    }

    fn mod_refcount(&self, value: BasicValueEnum, decrement: bool) {
        match value {
            BasicValueEnum::StructValue(struc)
                if struc.get_name().to_str().unwrap().starts_with("iface") =>
            {
                self.mod_refcount_iface(struc, decrement)
            }
            BasicValueEnum::PointerValue(ptr) => {
                let ty = ptr.get_type().get_element_type().into_struct_type();
                match &self
                    .types_bw
                    .get(ty.get_name().unwrap().to_str().unwrap())
                    .unwrap()
                {
                    Type::Adt(adt) => self.mod_refcount_adt(ptr, adt, decrement),
                    Type::Closure(_) => self.mod_refcount_closure(ptr, decrement),
                    Type::Value(_) => (),
                    _ => panic!("Cannot mod refcount on this"),
                }
            }
            _ => (),
        }
    }

    fn mod_refcount_adt(&self, ptr: PointerValue, adt: &MutRc<ADT>, decrement: bool) {
        if !adt.borrow().ty.has_refcount() {
            return;
        }
        if let Some(destructor) = &adt.borrow().destructor {
            let func = self.get_variable(destructor);
            let refcount = unsafe { self.builder.build_struct_gep(ptr, 0, "rcgep") };
            let refcount = self.write_new_refcount(refcount, decrement);
            if decrement {
                self.build_maybe_free(refcount, &mut |this, pred| {
                    this.builder
                        .build_call(func, &[ptr.into(), pred.into()], "free");
                })
            }
        }
    }

    fn mod_refcount_iface(&self, struc: StructValue, decrement: bool) {
        let func = if decrement {
            self.module.get_function("jingle_dec_ref_iface")
        } else {
            self.module.get_function("jingle_inc_ref_iface")
        }
        .unwrap();

        let int_ty = self.context.i64_type();
        let first = self
            .builder
            .build_extract_value(struc, 0, "extr")
            .unwrap()
            .into_pointer_value();
        let second = self
            .builder
            .build_extract_value(struc, 1, "extr")
            .unwrap()
            .into_pointer_value();
        self.builder.build_call(
            func,
            &[
                self.builder.build_ptr_to_int(first, int_ty, "cast").into(),
                self.builder.build_ptr_to_int(second, int_ty, "cast").into(),
            ],
            "rc",
        );
    }

    fn mod_refcount_closure(&self, ptr: PointerValue, decrement: bool) {
        let refcount = unsafe { self.builder.build_struct_gep(ptr, 0, "rcgep") };
        self.write_new_refcount(refcount, decrement);
        if decrement {
            let free_fn = self.struct_gep(ptr, 1);
            let free_fn = self.load_ptr(free_fn);
            self.builder
                .build_call(free_fn.into_pointer_value(), &[ptr.into()], "rccheck");
        }
    }

    fn write_new_refcount(&self, refcount: PointerValue, decrement: bool) -> IntValue {
        let rc = self.builder.build_load(refcount, "rcload").into_int_value();
        let added = self.context.i32_type().const_int(1, false);
        let new_rc = if decrement {
            self.builder.build_int_sub(rc, added, "rcdec")
        } else {
            self.builder.build_int_add(rc, added, "rcinc")
        };
        self.builder.build_store(refcount, new_rc);
        new_rc
    }

    /// Will insert a free check at the current insert position.
    /// `free_closure` should generate the code that runs when the value
    /// is to be freed.
    fn build_maybe_free(
        &self,
        refcount: IntValue,
        free_closure: &mut dyn FnMut(&IRGenerator, IntValue),
    ) {
        let value_is_0 = self.builder.build_int_compare(
            IntPredicate::EQ,
            refcount,
            self.context.i32_type().const_int(0, false),
            "rccond",
        );
        free_closure(self, value_is_0);
    }
}
