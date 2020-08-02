/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 3:28 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use crate::{
    codegen::{IRGenerator, PtrEqRc},
    ir::nodes::{Type, Variable},
};
use inkwell::{
    basic_block::BasicBlock,
    types::{AnyTypeEnum, BasicType, BasicTypeEnum},
    values::{BasicValue, BasicValueEnum, PointerValue},
    AddressSpace::Generic,
};
use std::rc::Rc;

impl IRGenerator {
    /// Force any type to be turned into a void pointer.
    pub fn coerce_to_void_ptr(&self, ty: BasicValueEnum) -> BasicValueEnum {
        let target = self.void_ptr();
        match ty {
            BasicValueEnum::PointerValue(ptr) => self.builder.build_bitcast(ptr, target, "bc"),

            BasicValueEnum::IntValue(int) => {
                let num = self
                    .builder
                    .build_int_z_extend(int, self.context.i64_type(), "extend");
                self.builder
                    .build_int_to_ptr(num, target, "inttoptr")
                    .into()
            }

            BasicValueEnum::FloatValue(flt) => self.coerce_to_void_ptr(self.builder.build_bitcast(
                flt,
                self.context.i64_type(),
                "flttoint",
            )),

            _ => panic!("Cannot coerce to void ptr: {:?}", ty),
        }
    }

    /// Returns the IR pointer of the variable.
    /// Can also be used for globals, although variables are
    /// searched for first.
    pub fn get_variable(&self, var: &Rc<Variable>) -> PointerValue {
        let wrap = PtrEqRc::new(var);
        self.variables
            .get(&wrap)
            .cloned()
            .unwrap_or_else(|| self.functions[&wrap].as_global_value().as_pointer_value())
    }

    /// Write a set of values to a given struct.
    pub fn write_struct<'a, T: Iterator<Item = &'a BasicValueEnum>>(
        &self,
        location: PointerValue,
        values: T,
    ) {
        for (i, value) in values.enumerate() {
            let slot = self.struct_gep(location, i);
            self.build_store(slot, *value, true);
        }
    }

    /// Loads a pointer, turning it into a value.
    /// Does not load structs or functions, since they are only ever used as pointers.
    pub fn load_ptr(&self, ptr: PointerValue) -> BasicValueEnum {
        match ptr.get_type().get_element_type() {
            AnyTypeEnum::FunctionType(_) => BasicValueEnum::PointerValue(ptr),
            AnyTypeEnum::StructType(str)
                if str
                    .get_name()
                    .map_or(true, |n| !n.to_str().unwrap().starts_with("iface")) =>
            {
                ptr.into()
            }
            _ => self.builder.build_load(ptr, "var"),
        }
    }

    /// Similar to the function above, but with MIR type info.
    /// This is sometimes required to prevent unintentionally loading
    /// a value, for example when dealing with primitive pointers.
    pub fn load_ptr_mir(&self, ptr: PointerValue, mir_ty: &Type) -> BasicValueEnum {
        match (ptr.get_type().get_element_type(), mir_ty) {
            (AnyTypeEnum::IntType(_), Type::Pointer(_)) => ptr.into(),
            (AnyTypeEnum::PointerType(inner), Type::Pointer(_))
                if inner.get_element_type().is_struct_type() =>
            {
                ptr.into()
            }
            _ => self.load_ptr(ptr),
        }
    }

    /// Perform a struct GEP with some additional safety checks.
    /// The index will be offset by one should the struct contain a refcount field,
    /// so callers do not need to account for this.
    pub fn struct_gep(&self, ptr: PointerValue, index: usize) -> PointerValue {
        assert!(ptr.get_type().get_element_type().is_struct_type());

        // Account for the reference count field, should it be present
        let index = index as u32 + self.get_struct_offset(ptr);

        assert!(
            ptr.get_type()
                .get_element_type()
                .as_struct_type()
                .count_fields()
                > index
        );

        unsafe { self.builder.build_struct_gep(ptr, index as u32, "gep") }
    }

    pub fn get_type_info_field(&self, ptr: PointerValue) -> PointerValue {
        unsafe { self.builder.build_struct_gep(ptr, 1, "gep") }
    }

    pub fn get_struct_offset(&self, ptr: PointerValue) -> u32 {
        let elem_ty = ptr.get_type().get_element_type();
        let struct_type = elem_ty.as_struct_type();
        let mut i = 0;

        // Account for the reference count field, should it be present
        i +=
            (struct_type.get_field_type_at_index(i) == Some(self.context.i32_type().into())) as u32;
        // Account for the type info field, should it be present
        i += (struct_type.get_field_type_at_index(i)
            == Some(self.type_info_type.ptr_type(Generic).into())) as u32;

        i
    }

    /// Creates a new stack allocation instruction in the entry block of the function.
    /// The alloca is kept empty.
    pub fn create_alloc(&self, ty: BasicTypeEnum, heap: bool) -> PointerValue {
        let builder = self.context.create_builder();

        let (builder, ptr) = if heap {
            let malloc = self
                .module
                .get_function("malloc")
                .unwrap()
                .as_global_value()
                .as_pointer_value();
            let malloc_ty = ty
                .ptr_type(Generic)
                .fn_type(&[self.context.i32_type().into()], false);
            let malloc = self
                .builder
                .build_bitcast(malloc, malloc_ty.ptr_type(Generic), "malloccast")
                .into_pointer_value();

            let i = self.context.i32_type();
            let ty_size = unsafe {
                self.builder.build_gep(
                    ty.ptr_type(Generic).const_null(),
                    &[i.const_int(1, false)],
                    "size",
                )
            };
            let ty_size = self.builder.build_ptr_to_int(ty_size, i, "sizeint").into();

            (
                &self.builder,
                self.builder
                    .build_call(malloc, &[ty_size], "malloc")
                    .try_as_basic_value()
                    .left()
                    .unwrap()
                    .into_pointer_value(),
            )
        } else {
            let entry = self
                .builder
                .get_insert_block()
                .unwrap()
                .get_parent()
                .unwrap()
                .get_first_basic_block()
                .unwrap();

            match entry.get_first_instruction() {
                Some(first_instr) => builder.position_before(&first_instr),
                None => builder.position_at_end(&entry),
            }

            (&builder, builder.build_alloca(ty, "tmpalloc"))
        };

        if ty.is_struct_type()
            && ty.as_struct_type().get_field_type_at_index(0)
                == Some(self.context.i32_type().into())
        {
            // Initialize the refcount to 0
            let rc = unsafe { builder.build_struct_gep(ptr, 0, "rcinit") };
            let value = if heap {
                0
            } else {
                2_147_483_648 /* first bit 1, rest 0; used to differentiate heap/stack vars */
            };
            builder.build_store(rc, self.context.i32_type().const_int(value, false));
        }
        ptr
    }

    pub fn locals(&mut self) -> &mut Vec<(BasicValueEnum, bool)> {
        self.locals.last_mut().unwrap()
    }

    pub fn push_locals(&mut self) {
        self.locals.push(Vec::with_capacity(5))
    }

    pub fn pop_dec_locals(&mut self) {
        let locals = self.locals.pop().unwrap();
        self.decrement_locals(&locals)
    }

    pub fn pop_locals_lift(&mut self, lift: BasicValueEnum) {
        let locals = self.locals.pop().unwrap();

        if !locals.is_empty() {
            self.increment_refcount(lift, false);
            self.locals().push((lift, false));
        }

        self.decrement_locals(&locals);
    }

    pub fn pop_locals_remove(&mut self, lift: BasicValueEnum) {
        let locals = self.locals.pop().unwrap();
        self.increment_refcount(lift, false);
        self.decrement_locals(&locals);
    }

    pub fn decrement_all_locals(&self) {
        for locals in &self.locals {
            self.decrement_locals(locals);
        }
    }

    fn decrement_locals(&self, locals: &[(BasicValueEnum, bool)]) {
        if self.builder.get_insert_block().is_some() {
            for (local, is_ptr) in locals {
                self.decrement_refcount(*local, *is_ptr);
            }
        }
    }

    pub fn nullptr(&self) -> PointerValue {
        self.context.i64_type().ptr_type(Generic).const_null()
    }

    pub fn build_phi(&mut self, nodes: &[(BasicValueEnum, BasicBlock)]) -> BasicValueEnum {
        let nodes = nodes
            .iter()
            .filter(|(v, _)| v.get_type() != self.none_const.get_type())
            .collect::<Vec<_>>();

        match nodes.len() {
            0 => self.none_const,
            1 => {
                self.locals().push((nodes[0].0, false));
                nodes[0].0
            }
            _ => {
                let ty = nodes[0].0.get_type();
                let nodes = nodes
                    .iter()
                    .map(|(v, b)| (v as &dyn BasicValue, b))
                    .collect::<Vec<_>>();
                let phi = self.builder.build_phi(ty, "phi");
                phi.add_incoming(&nodes);
                self.locals().push((phi.as_basic_value(), false));
                phi.as_basic_value()
            }
        }
    }
}
