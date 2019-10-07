//! A function-calling example.
//!
//! This module cntains an example of a machine with function calling
//! behaviour.
//!
//! This is achieved by storing labels in the builder and jumping to those
//! parts of the code during execution.
//!
//! Labels are stored as strings in the builder, so your operand type must have
//! the ability to store strings so that we can use them to find the right
//! label later on.

use super::super::*;

/// Our operand type.  An enum to contain multiple types.
#[derive(Clone, Debug, PartialEq)]
enum Operand {
    I(i64),
    S(String),
}

impl Operand {
    fn to_i(&self) -> Option<i64> {
        match self {
            Operand::I(i) => Some(*i),
            _ => None,
        }
    }

    fn to_s(&self) -> Option<&str> {
        match self {
            Operand::S(ref s) => Some(s),
            _ => None,
        }
    }
}

/// Pushes an piece of data from the data section onto the operand stack.
fn push(machine: &mut Machine<Operand>, args: &[usize]) {
    let arg = machine.get_data(args[0]).clone();
    machine.operand_push(arg)
}

/// Pops two operands off the top of the stack, adds them together and
/// pushes the result back onto the stack.
fn add(machine: &mut Machine<Operand>, _args: &[usize]) {
    let rhs = machine.operand_pop().to_i().unwrap();
    let lhs = machine.operand_pop().to_i().unwrap();
    machine.operand_push(Operand::I(lhs + rhs));
}

/// Takes the name of a label from the data section and asks the interpreter
/// to jump to it.
fn call(machine: &mut Machine<Operand>, args: &[usize]) {
    let label = machine.get_data(args[0]).clone();
    machine.call(label.to_s().unwrap());
}

/// Ask the interpreter to perform a return.
fn ret(machine: &mut Machine<Operand>, _args: &[usize]) {
    machine.ret();
}

/// Generate an instruction table using the instructions outlined above.
fn instruction_table() -> InstructionTable<Operand> {
    let mut it = InstructionTable::new();
    it.insert(Instruction::new(0, "push", 1, push));
    it.insert(Instruction::new(1, "add", 0, add));
    it.insert(Instruction::new(2, "call", 1, call));
    it.insert(Instruction::new(3, "ret", 0, ret));
    it
}

impl From<i64> for Operand {
    fn from(i: i64) -> Self {
        Operand::I(i)
    }
}

impl<'a> From<&'a str> for Operand {
    fn from(s: &'a str) -> Self {
        Operand::S(s.to_string())
    }
}

#[test]
fn example() {
    let it = instruction_table();
    let mut builder: Builder<Operand> = Builder::new(&it);
    builder.push("push", vec![Operand::from(3)]);
    builder.push("push", vec![Operand::from(4)]);
    builder.push("call", vec![Operand::from("add_fun")]);
    builder.push("ret", vec![]);
    builder.label("add_fun");
    builder.push("add", vec![]);
    builder.push("ret", vec![]);
    let constants: WriteManyTable<Operand> = WriteManyTable::new();
    let mut machine: Machine<Operand> = Machine::new(Code::from(builder), &constants, &it);
    machine.run();
    let result = machine.operand_pop().to_i().unwrap();
    assert_eq!(result, 7);
}
