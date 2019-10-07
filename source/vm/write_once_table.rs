//! A key/value table using strings as keys.

use crate::table::Table;
use std::collections::HashMap;

/// A table which does not allow values to be overwritten.
/// Useful for your languages constants, etc.
///
/// ```
/// use stack_vm::{WriteOnceTable, Table};
/// let mut table: WriteOnceTable<usize> = WriteOnceTable::new();
/// assert!(table.is_empty());
///
/// table.insert("example", 13);
/// assert!(!table.is_empty());
///
/// assert!(table.contains_key("example"));
///
/// let value = *table.get("example").unwrap();
/// assert_eq!(value, 13);
/// ```
///
/// ```should_panic
/// use stack_vm::{WriteOnceTable, Table};
/// let mut table: WriteOnceTable<usize> = WriteOnceTable::new();
/// table.insert("example", 13);
/// table.insert("example", 14);
/// ```
#[derive(Debug, Default)]
pub struct WriteOnceTable<T>(HashMap<String, T>);

impl<T> WriteOnceTable<T> {
    /// Return a new, empty `WriteOnceTable`.
    pub fn new() -> WriteOnceTable<T> {
        WriteOnceTable(HashMap::new())
    }

    fn already_exists_guard(&self, name: &str) {
        if self.0.contains_key(name) {
            panic!("Error: redefining constant {} not allowed.", name);
        }
    }

    pub fn keys(&self) -> Vec<String> {
        let mut result = vec![];
        self.0.keys().for_each(|ref k| result.push(k.to_string()));
        result
    }
}

impl<T> Table for WriteOnceTable<T> {
    type Item = T;

    fn insert(&mut self, name: &str, value: T) {
        self.already_exists_guard(name);
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
        let write_once_table: WriteOnceTable<usize> = WriteOnceTable::new();
        assert!(write_once_table.is_empty())
    }

    #[test]
    fn insert() {
        let mut write_once_table: WriteOnceTable<usize> = WriteOnceTable::new();
        write_once_table.insert("example", 13);
        assert!(!write_once_table.is_empty());
        assert_eq!(*write_once_table.get("example").unwrap(), 13);
    }

    #[test]
    #[should_panic(expected = "redefining constant")]
    fn insert_uniq() {
        let mut write_once_table: WriteOnceTable<usize> = WriteOnceTable::new();
        write_once_table.insert("example", 13);
        assert_eq!(*write_once_table.get("example").unwrap(), 13);
        write_once_table.insert("example", 13);
    }
}
