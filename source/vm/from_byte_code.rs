//! Code deserializer.
//!
//! If you wish to be able to load serialized bytecode into your virtual
//! machine to use again.

use std::io::Read;

/// Convert from byte code to a type.
///
/// This trait represents the ability to load your Operands from bytecode.
/// `stack-vm` uses the [`rmp`](https://crates.io/crates/rmp) crate to load
/// bytecode from a MsgPack encoded binary.
///
/// See the [`rmp` docs](https://docs.rs/rmp/0.8.7/rmp/) to find out which
/// functions you can use to write out your types.
pub trait FromByteCode {
    /// Convert from MsgPack to your type.
    ///
    /// This function takes a mutable reference of type `Read` and returns your
    /// operand type.
    ///
    /// ## Example
    ///
    /// ```
    /// # extern crate rmp;
    /// # extern crate stack_vm;
    /// # use stack_vm::FromByteCode;
    /// # use std::io::Read;
    ///
    /// #[derive(PartialEq, Debug)]
    /// struct Operand(i64);
    ///
    /// impl FromByteCode for Operand {
    ///     fn from_byte_code(mut buf: &mut dyn Read) -> Operand {
    ///         let value = rmp::decode::read_int(&mut buf).unwrap();
    ///         Operand(value)
    ///     }
    /// }
    /// # fn main() {
    /// let bytecode = [0xd];
    /// assert_eq!(Operand(13), Operand::from_byte_code(&mut &bytecode[..]));
    /// # }
    /// ```
    fn from_byte_code(_: &mut dyn Read) -> Self;
}

#[cfg(test)]
mod test {
    use super::*;
    use rmp;

    #[derive(PartialEq, Debug)]
    struct Operand(i64);

    impl FromByteCode for Operand {
        fn from_byte_code(mut buf: &mut dyn Read) -> Operand {
            let i = rmp::decode::read_int(&mut buf).unwrap();
            Operand(i)
        }
    }

    #[test]
    fn from_byte_code() {
        let bytecode = [0xd];
        assert_eq!(Operand(13), Operand::from_byte_code(&mut &bytecode[..]));
    }
}
