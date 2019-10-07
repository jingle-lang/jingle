//! A simple trait for interacting with various types of table used internally.

/// # Table
///
/// A simple trait used for accessing table-like objects.
///
/// This trait is used internally for the machine's constant table.  As long as
/// your table type implements this trait then you'll be cool.  Meaning you can
/// choose whatever language semantics you want with regards constants.
pub trait Table {
    /// The type for items stored and retrieved from the table.
    type Item;

    /// Insert a value into the table using a string key.
    fn insert(&mut self, name: &str, value: Self::Item);

    /// Is the table empty or not?
    fn is_empty(&self) -> bool;

    /// Does the table contain the key or not?
    fn contains_key(&self, name: &str) -> bool;

    /// Retrieve a reference to a value stored in the table by key.
    fn get(&self, name: &str) -> Option<&Self::Item>;
}
