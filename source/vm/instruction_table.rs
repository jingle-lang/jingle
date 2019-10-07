//! An instruction table.
//!
//! Stores the instructions of your machine and allows them to be retrieved
//! by name or op code.

use crate::instruction::Instruction;
use std::collections::HashMap;
use std::fmt;

/// The instruction table.
///
/// Implemented as a `HashMap` behind the scenes.
#[derive(Debug, Default)]
pub struct InstructionTable<T: fmt::Debug>(HashMap<usize, Instruction<T>>);

impl<T: fmt::Debug> InstructionTable<T> {
    /// Create a new empty instruction table.
    pub fn new() -> InstructionTable<T> {
        InstructionTable(HashMap::new())
    }

    /// Retrieve an instruction by looking up it's op code.
    pub fn by_op_code(&self, op_code: usize) -> Option<&Instruction<T>> {
        self.0.get(&op_code)
    }

    /// Retrieve an instruction by looking up it's name.
    pub fn by_name(&self, name: &str) -> Option<&Instruction<T>> {
        self.0.values().find(|ref instr| instr.name == name)
    }

    /// Insert an instruction into the table.
    pub fn insert(&mut self, instr: Instruction<T>) {
        self.0.insert(instr.op_code, instr);
    }

    /// Returns `true` if the instruction table is empty.
    pub fn is_empty(&self) -> bool {
        self.0.is_empty()
    }

    /// Returns a list of symbols for use in the `Code` struct.
    ///
    /// Generates a vector of tuples containing the op code and the name of
    /// each instruction.
    pub fn symbols(&self) -> Vec<(usize, String)> {
        let mut result = vec![];
        self.0.keys().for_each(|ref key| {
            let instr = &self.0[key];
            result.push((instr.op_code, instr.name.clone()));
        });
        result.sort_by(|lhs, rhs| lhs.0.cmp(&rhs.0));
        result
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use crate::machine::Machine;

    fn noop(_machine: &mut Machine<usize>, _args: &[usize]) {}

    #[test]
    fn new() {
        let table: InstructionTable<usize> = InstructionTable::new();
        assert!(table.is_empty())
    }

    #[test]
    fn insert() {
        let mut table: InstructionTable<usize> = InstructionTable::new();
        assert!(table.is_empty());
        table.insert(Instruction::new(0, "NOOP", 0, noop));
        assert!(!table.is_empty());
    }

    #[test]
    fn by_op_code() {
        let mut table: InstructionTable<usize> = InstructionTable::new();
        table.insert(Instruction::new(0, "NOOP", 0, noop));
        let instr = table.by_op_code(0).unwrap();
        assert_eq!(instr.name, "NOOP");
    }

    #[test]
    fn by_name() {
        let mut table: InstructionTable<usize> = InstructionTable::new();
        table.insert(Instruction::new(0, "NOOP", 0, noop));
        let instr = table.by_name("NOOP").unwrap();
        assert_eq!(instr.op_code, 0);
    }
}
