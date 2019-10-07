//! Code serializer.
//!
//! If you wish to dump compiled bytecode from your virtual machine for loading
//! again later then you need to implement this trait for your Operand type.

use std::io::Write;

/// Convert from operands to byte code.
///
/// This trait represents the ability to dump your Operands to bytecode.
/// `stack-vm` uses the [`rmp`](https://crates.io/crates/rmp) crate to store
/// bytecode as a MsgPack encoded binary.  As long as you return a valid vector
/// of messagepack bytes it'll be inserted into the output during the
/// serialization run.
///
/// See the [`rmp` docs](https://docs.rs/rmp/0.8.7/rmp/) to find out which
/// functions you can use to write out your types.
///
/// Being MsgPack means that you can encode your Operand in any way you require,
/// for example as a single integer, or a map of keys and values provided that
/// you write just a single MsgPack value.
pub trait ToByteCode {
    /// Convert your type to MsgPack.
    ///
    /// This function takes a mutable reference of type `Write` into which you
    /// write your MsgPack encoded value.
    ///
    /// ## Example
    ///
    /// ```
    /// # extern crate rmp;
    /// # extern crate stack_vm;
    /// # use stack_vm::ToByteCode;
    /// # use std::io::Write;
    ///
    /// #[derive(PartialEq, Debug)]
    /// struct Operand(i64);
    ///
    /// impl ToByteCode for Operand {
    ///     fn to_byte_code(&self, mut buf: &mut dyn Write) {
    ///         rmp::encode::write_sint(&mut buf, self.0).unwrap();
    ///     }
    /// }
    /// # fn main() {
    /// let op = Operand(13);
    /// let mut buf: Vec<u8> = vec![];
    /// op.to_byte_code(&mut buf);
    /// assert_eq!(&buf[..], [0xd]);
    /// # }
    /// ```
    fn to_byte_code(&self, _: &mut dyn Write);
}

#[cfg(test)]
mod test {
    use super::*;
    use rmp;

    struct Operand(i64);

    impl ToByteCode for Operand {
        fn to_byte_code(&self, mut buf: &mut dyn Write) {
            rmp::encode::write_sint(&mut buf, self.0).unwrap();
        }
    }

    #[test]
    fn to_byte_code() {
        let op = Operand(13);
        let mut buf: Vec<u8> = vec![];
        op.to_byte_code(&mut buf);
        assert_eq!(&buf[..], [0xd]);
    }
}
