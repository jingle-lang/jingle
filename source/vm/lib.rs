//! # stack-vm
//!
//! This crate implements a generic stack machine for which you provide the
//! operands and the instructions and this crate provides the rest of the
//! infrastructure required to run it.
//!
//! It also provides a simple instruction builder which you can use to generate
//! your program.
//!
//! Stack machines are computers which use an operand stack to perform the
//! evaluation of postfix expressions.  Every computer architecture has it's
//! own instruction set which is the basic set of operations that the computer
//! can perform.
//!
//! Instructions usually describe basic arithmetic operations, I/O, jumps, etc.
//!
//! ## Computer Architecture
//!
//! The architecture of a computer system is how the various logic components
//! are connected together in order to execute the instructions and produce
//! side-effects (useful outcomes).
//!
//! There are two main ways to organise a computer architecture:
//! * *Von Neumann* - in which the program data and instructions are stored in
//!   the same memory.
//! * *Harvard* - in which the program data and instructions are stored in
//!   separate memory sections.
//!
//! The bulk of modern processors are Von Neumann type machines.
//!
//! We can also classify our machines by the way that they store intermediate
//! values:
//! * *Accumulator* - the most basic form of processor where only a single
//!   register is used to store the results of computation.
//! * *Stack* - stack machines use an operand stack to push and pop results
//!   off the top of.
//! * *Register* - register machines use a number of named (or numbered)
//!   registers to store values or pass arguments.
//!
//! Most modern processors are register machines, although interestingly both
//! register and stack machines can be used to emulate their cousin.
//!
//! ## Instruction Sets
//!
//! The instruction set is the definition of the machine.  Without instructions
//! your machine can't *do* anything.  They are the fundamental building blocks
//! of your computer, so you need to think this through before building it.
//!
//! This virtual machine uses Rust functions as instructions rather than
//! transistors and logic gates, but the effect is the same.
//!
//! In order to generate your instructions you need to create a bunch of Rust
//! functions which conform to the `stack_vm::InstructionFn` signature.
//!
//! For example:
//!
//! ```
//! use stack_vm::Machine;
//! type Operand = i64;
//!
//! fn push(machine: &mut Machine<Operand>, args: &[usize]) {
//!     let arg = machine.get_data(args[0]).clone();
//!     machine.operand_push(arg);
//! }
//! ```
//!
//! Once you have finished defining your instructions you can use them to build
//! a `stack_vm::InstructionTable`, where every instruction is identified by
//! it's `op_code`, `name` and `arity`.
//!
//! * `op_code` a positive integer which uniquely identifies this instruction.
//!   This is manually entered rather than auto-generated from insert order
//!   so that you can maintain as much compatibility between versions of your
//!   VM as possible.
//!
//! * `name` a string used to identify this instruction; mainly for debugging.
//!
//! * `arity` the number of arguments your instruction expects *from program
//!   data*.  This is not the number of operands your function needs off the
//!   operand stack.  This is used so that you can place constant data into
//!   the program at compile time.
//!
//! ```
//! use stack_vm::{Instruction, InstructionTable, Machine};
//! type Operand = i64;
//!
//! fn push(machine: &mut Machine<Operand>, args: &[usize]) {
//!     let arg = machine.get_data(args[0]).clone();
//!     machine.operand_push(arg);
//! }
//!
//! fn add(machine: &mut Machine<Operand>, _args: &[usize]) {
//!     let rhs = machine.operand_pop().clone();
//!     let lhs = machine.operand_pop().clone();
//!     machine.operand_push(lhs + rhs);
//! }
//!
//! let mut instruction_table = InstructionTable::new();
//! instruction_table.insert(Instruction::new(0, "push", 1, push));
//! instruction_table.insert(Instruction::new(1, "add",  0, add));
//! ```
//!
//! ## Code generation
//!
//! One your instruction set is defined then you can use the
//! `stack_vm::Builder` object to build a representation that the VM can
//! execute.
//!
//! For example, to push two integers on the stack and add them:
//!
//! ```
//! use stack_vm::{Instruction, InstructionTable, Machine, Builder};
//! type Operand = i64;
//!
//! fn push(machine: &mut Machine<Operand>, args: &[usize]) {
//!     let arg = machine.get_data(args[0]).clone();
//!     machine.operand_push(arg);
//! }
//!
//! fn add(machine: &mut Machine<Operand>, _args: &[usize]) {
//!     let rhs = machine.operand_pop().clone();
//!     let lhs = machine.operand_pop().clone();
//!     machine.operand_push(lhs + rhs);
//! }
//!
//! let mut instruction_table = InstructionTable::new();
//! instruction_table.insert(Instruction::new(0, "push", 1, push));
//! instruction_table.insert(Instruction::new(1, "add",  0, add));
//!
//! let mut builder: Builder<Operand> = Builder::new(&instruction_table);
//! builder.push("push", vec![3 as Operand]);
//! builder.push("push", vec![4 as Operand]);
//! builder.push("add", vec![]);
//! ```
//!
//! This will result in the following code:
//!
//! ```text
//! @0 = 3
//! @1 = 4
//!
//! .main:
//!   push @0
//!   push @1
//!   add
//! ```
//!
//! ## Running your program
//!
//! Once you have the instructions and code generated then you can put them
//! together with the `stack_vm::Machine` to execute it.
//!
//! ```
//! use stack_vm::{Instruction, InstructionTable, Machine, Builder, WriteManyTable, Code};
//! type Operand = i64;
//!
//! fn push(machine: &mut Machine<Operand>, args: &[usize]) {
//!     let arg = machine.get_data(args[0]).clone();
//!     machine.operand_push(arg);
//! }
//!
//! fn add(machine: &mut Machine<Operand>, _args: &[usize]) {
//!     let rhs = machine.operand_pop().clone();
//!     let lhs = machine.operand_pop().clone();
//!     machine.operand_push(lhs + rhs);
//! }
//!
//! let mut instruction_table = InstructionTable::new();
//! instruction_table.insert(Instruction::new(0, "push", 1, push));
//! instruction_table.insert(Instruction::new(1, "add",  0, add));
//!
//! let mut builder: Builder<Operand> = Builder::new(&instruction_table);
//! builder.push("push", vec![3 as Operand]);
//! builder.push("push", vec![4 as Operand]);
//! builder.push("add", vec![]);
//!
//! let constants: WriteManyTable<Operand> = WriteManyTable::new();
//! let mut machine = Machine::new(Code::from(builder), &constants, &instruction_table);
//! machine.run();
//! assert_eq!(machine.operand_pop(), 7);
//! ```
//!
//! ## Calling functions:
//!
//! Functions are executed by having the machine jump to another label within
//! the code and continue executing from there.
//!
//! Every time the machine jumps it creates a new call frame, which allows it
//! to store and retrieve local variables without clobbering their parent
//! call context.  It also contains the return address, meaning that when you
//! ask the machine to return it will know which address in the code to go back
//! to after removing the frame.
//!
//! You can find an example of function calling in this package's acceptance
//! tests.

extern crate rmp;

mod builder;
mod code;
mod frame;
mod from_byte_code;
mod instruction;
mod instruction_table;
mod machine;
mod stack;
mod table;
mod to_byte_code;
mod write_many_table;
mod write_once_table;

pub use crate::builder::Builder;
pub use crate::code::Code;
pub use crate::frame::Frame;
pub use crate::from_byte_code::FromByteCode;
pub use crate::instruction::{Instruction, InstructionFn};
pub use crate::instruction_table::InstructionTable;
pub use crate::machine::Machine;
pub use crate::stack::Stack;
pub use crate::table::Table;
pub use crate::to_byte_code::ToByteCode;
pub use crate::write_many_table::WriteManyTable;
pub use crate::write_once_table::WriteOnceTable;

#[cfg(test)]
mod acceptance;
