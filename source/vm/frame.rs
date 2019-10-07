//! A call frame.
//!
//! Used internally by the `Machine` to keep track of call scope.

use crate::write_many_table::WriteManyTable;
use crate::table::Table;

/// A call frame.
///
/// Contains:
/// * A `WriteManyTable` for storage of local variables.
/// * A return address - the instruction pointer for the machine to return to
///   when returning from this call.
#[derive(Debug)]
pub struct Frame<T> {
    locals: WriteManyTable<T>,
    pub return_address: usize
}

impl<T> Frame<T> {
    /// Creates a new call frame with the specified return address.
    pub fn new(return_address: usize) -> Frame<T> {
        Frame {
            locals: WriteManyTable::new(),
            return_address
        }
    }

    /// Return a reference to the specified local variable.
    pub fn get_local(&self, name: &str) -> Option<&T> {
        self.locals.get(name)
    }

    /// Set the value of a local variable.
    pub fn set_local(&mut self, name: &str, value: T) {
        self.locals.insert(name, value);
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn new_has_locals() {
        let frame: Frame<usize> = Frame::new(0);
        assert!(frame.locals.is_empty())
    }
}
