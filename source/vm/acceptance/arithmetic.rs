//! An Arithmetic Machine.
//!
//! This module contains an example of a basic calculator and tests which
//! verify it's output.

use super::super::*;
use std::f64;

/// Pushes an piece of data from the data section onto the operand stack.
fn push(machine: &mut Machine<f64>, args: &[usize]) {
    let arg = *machine.get_data(args[0]);
    machine.operand_push(arg);
}

/// Pops two operands off the top of the stack, adds them together and
/// pushes the result back onto the stack.
fn add(machine: &mut Machine<f64>, _args: &[usize]) {
    let rhs = machine.operand_pop();
    let lhs = machine.operand_pop();
    machine.operand_push(lhs + rhs);
}

/// Pops two operands off the top of the stack, subtracts the first from the
/// second and pushes the result back onto the stack.
fn sub(machine: &mut Machine<f64>, _args: &[usize]) {
    let rhs = machine.operand_pop();
    let lhs = machine.operand_pop();
    machine.operand_push(lhs - rhs);
}

/// Pops two operands off the top of the stack, divides the first from the
/// second and pushes the result back onto the stack.
fn div(machine: &mut Machine<f64>, _args: &[usize]) {
    let rhs = machine.operand_pop();
    let lhs = machine.operand_pop();
    machine.operand_push(lhs / rhs);
}

/// Pops two operands off the top of the stack, multiples them together and
/// pushes the result back onto the stack.
fn mult(machine: &mut Machine<f64>, _args: &[usize]) {
    let rhs = machine.operand_pop();
    let lhs = machine.operand_pop();
    machine.operand_push(lhs * rhs);
}

/// Build an instruction table based on the instructions outlined above.
fn instruction_table() -> InstructionTable<f64> {
    let mut it = InstructionTable::new();
    it.insert(Instruction::new(0, "push", 1, push));
    it.insert(Instruction::new(1, "add", 0, add));
    it.insert(Instruction::new(2, "sub", 0, sub));
    it.insert(Instruction::new(3, "div", 0, div));
    it.insert(Instruction::new(4, "mult", 0, mult));
    it
}

#[test]
fn addition_example() {
    let it = instruction_table();
    let mut builder: Builder<f64> = Builder::new(&it);
    builder.push("push", vec![2.0]);
    builder.push("push", vec![3.0]);
    builder.push("add", vec![]);
    builder.push("push", vec![4.0]);
    builder.push("add", vec![]);
    let constants: WriteManyTable<f64> = WriteManyTable::new();
    let mut machine = Machine::new(Code::from(builder), &constants, &it);
    machine.run();
    let result = machine.operand_pop();
    assert!(result - 9.0 < f64::EPSILON);
}

#[test]
fn subtraction_example() {
    let it = instruction_table();
    let mut builder: Builder<f64> = Builder::new(&it);
    builder.push("push", vec![3.0]);
    builder.push("push", vec![4.0]);
    builder.push("add", vec![]);
    builder.push("push", vec![2.0]);
    builder.push("sub", vec![]);
    let constants: WriteManyTable<f64> = WriteManyTable::new();
    let mut machine = Machine::new(Code::from(builder), &constants, &it);
    machine.run();
    let result = machine.operand_pop();
    assert!(result - 5.0 < f64::EPSILON);
}

#[test]
fn division_example() {
    let it = instruction_table();
    let mut builder: Builder<f64> = Builder::new(&it);
    builder.push("push", vec![3.0]);
    builder.push("push", vec![4.0]);
    builder.push("div", vec![]);
    let constants: WriteManyTable<f64> = WriteManyTable::new();
    let mut machine = Machine::new(Code::from(builder), &constants, &it);
    machine.run();
    let result = machine.operand_pop();
    assert!(result - 0.75 < f64::EPSILON);
}

#[test]
fn multiplication_example() {
    let it = instruction_table();
    let mut builder: Builder<f64> = Builder::new(&it);
    builder.push("push", vec![3.0]);
    builder.push("push", vec![4.0]);
    builder.push("mult", vec![]);
    let constants: WriteManyTable<f64> = WriteManyTable::new();
    let mut machine = Machine::new(Code::from(builder), &constants, &it);
    machine.run();
    let result = machine.operand_pop();
    assert!(result - 12.0 < f64::EPSILON);
}
