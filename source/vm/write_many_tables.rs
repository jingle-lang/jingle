//! A key/value table using strings as keys.

use crate::table::Table;
use std::collections::HashMap;

/// A table which allows values to be overwritten.
/// Useful for your language's local variables, etc.
///
/// ```
/// use stack_vm::{WriteManyTable, Table};
/// let mut table: WriteManyTable<usize> = WriteManyTable::new();
/// assert!(table.is_empty());
///
/// table.insert("example", 13);
/// assert!(!table.is_empty());
///
/// assert!(table.contains_key("example"));
///
/// let value = *table.get("example").unwrap();
/// assert_eq!(value, 13);
///
/// table.insert("example", 14);
/// assert!(table.contains_key("example"));
///
/// let value = *table.get("example").unwrap();
/// assert_eq!(value, 14);
/// ```
#[derive(Debug, Default)]
pub struct WriteManyTable<T>(HashMap<String, T>);

impl<T> WriteManyTable<T> {
    /// Return a new, empty `WriteManyTable`.
    pub fn new() -> WriteManyTable<T> {
        WriteManyTable(HashMap::new())
    }
}

impl<T> Table for WriteManyTable<T> {
    type Item = T;

    fn insert(&mut self, name: &str, value: T) {
        let name = String::from(name);
        self.0.insert(name, value);
    }

    fn is_empty(&self) -> bool {
        self.0.is_empty()
    }

    fn contains_key(&self, name: &str) -> bool {
        self.0.contains_key(name)
    }

    fn get(&self, name: &str) -> Option<&T> {
        self.0.get(name)
    }
}
#[cfg(test)]
mod test {
    use super::*;
    use crate::table::Table;

    #[test]
    fn new() {
        let write_many_table: WriteManyTable<usize> = WriteManyTable::new();
        assert!(write_many_table.is_empty())
    }

    #[test]
    fn insert() {
        let mut write_many_table: WriteManyTable<usize> = WriteManyTable::new();
        write_many_table.insert("example", 13);
        assert!(!write_many_table.is_empty());
        assert_eq!(*write_many_table.get("example").unwrap(), 13);
    }

    #[test]
    fn insert_is_mutable() {
        let mut write_many_table: WriteManyTable<usize> = WriteManyTable::new();
        write_many_table.insert("example", 13);
        assert_eq!(*write_many_table.get("example").unwrap(), 13);
        write_many_table.insert("example", 14);
        assert_eq!(*write_many_table.get("example").unwrap(), 14);
    }
}
