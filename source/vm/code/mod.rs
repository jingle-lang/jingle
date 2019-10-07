//! Code
//!
//! This module represents a hunk of code ready to be executed by the VM.
//! Code can be created in one of two ways:
//!
//! * From an instance of a `Builder`.
//! * From dumped bytecode.
//!
//! ## Creating code from a Builder:
//!
//! ```
//! # use stack_vm::{Machine, Instruction, InstructionTable, Code, Builder};
//!
//! #[derive(Debug, PartialEq)]
//! struct Operand(i64);
//!
//! fn example_noop(_machine: &mut Machine<Operand>, _args: &[usize]) {}
//!
//! # fn main() {
//! let mut instruction_table = InstructionTable::new();
//! instruction_table.insert(Instruction::new(1, "push", 1, example_noop));
//!
//! let mut builder: Builder<Operand> = Builder::new(&instruction_table);
//! builder.push("push", vec![Operand(13)]);
//! builder.push("push", vec![Operand(14)]);
//!
//! Code::from(builder);
//! # }
//! ```
//!
//! ## Creating code from bytecode
//!
//! Loading bytecode is pretty straight-forward.  Note that you must implement
//! `FromByteCode` for your Operand type however.
//!
//! ```
//! # extern crate stack_vm;
//! # extern crate rmp;
//! # use stack_vm::{Code, FromByteCode};
//! # use std::io::Read;
//!
//! #[derive(Debug)]
//! struct Operand(i64);
//!
//! impl FromByteCode for Operand {
//!     fn from_byte_code(mut buf: &mut Read) -> Operand {
//!         let value = rmp::decode::read_int(&mut buf).unwrap();
//!         Operand(value)
//!     }
//! }
//!
//! # fn main() {
//! let bytecode: [u8; 30] = [132, 164, 99, 111, 100, 101, 144, 164, 100, 97, 116, 97, 144, 167, 115, 121, 109, 98, 111, 108, 115, 144, 166, 108, 97, 98, 101, 108, 115, 144];
//! let _code: Code<Operand> = Code::from_byte_code(&mut &bytecode[..]);
//! # }
//! ```
//!
//! ## Dumping code to bytecode
//!
//! Dumping your code to bytecode is also very straight-forward.  You will need
//! to implement the `ToByteCode` trait on your Operand type.
//!
//! ```
//! # extern crate rmp;
//! # extern crate stack_vm;
//! # use stack_vm::{Code, ToByteCode};
//! # use std::io::Write;
//!
//! #[derive(Debug, PartialEq)]
//! struct Operand(i64);
//!
//! impl ToByteCode for Operand {
//!     fn to_byte_code(&self, mut buf: &mut Write) {
//!         rmp::encode::write_sint(&mut buf, self.0).unwrap();
//!     }
//! }
//!
//! # fn main() {
//! let code: Code<Operand> = Code::empty();
//! let mut bytecode: Vec<u8> = vec![];
//! code.to_byte_code(&mut bytecode);
//! assert_eq!(&bytecode[..], [132, 164, 99, 111, 100, 101, 144, 164, 100, 97, 116, 97, 144, 167, 115, 121, 109, 98, 111, 108, 115, 144, 166, 108, 97, 98, 101, 108, 115, 144]);
//! # }
//! ```

use crate::builder::Builder;
use crate::table::Table;
use std::convert::From;
use std::fmt;
mod debug;
mod from_byte_code;
mod to_byte_code;

/// A structure containing runnable or dumpable code.
///
/// See the module-level docs for more details.
pub struct Code<T> {
    pub symbols: Vec<(usize, String)>,
    pub code: Vec<usize>,
    pub data: Vec<T>,
    pub labels: Vec<(usize, String)>,
}

impl<T: fmt::Debug> Code<T> {
    /// Create an empty code.
    ///
    /// Not useful for anything except tests and documentation.
    pub fn empty() -> Code<T> {
        Code {
            symbols: vec![],
            code: vec![],
            data: vec![],
            labels: vec![],
        }
    }

    /// Retrieve a list of all symbols in the code.
    ///
    /// This is a list of tuples containing op codes and instruction names.
    pub fn symbols(&self) -> &[(usize, String)] {
        self.symbols.as_slice()
    }

    /// Retrieve a list of instructions in the code.
    ///
    /// This is the executable source program of the code.  It is a simple
    /// format based around the following:
    ///
    /// ```text
    /// | Op Code | No of args | Args ...         |
    /// | 0x01    | 0x03       | 0x01, 0x02, 0x03 |
    /// ```
    pub fn code(&self) -> &[usize] {
        self.code.as_slice()
    }

    /// Retrieve the constant data compiled into the code.
    pub fn data(&self) -> &[T] {
        self.data.as_slice()
    }

    /// Retrieve a list of labels used in the program.
    ///
    /// Returns a list of tuples containing the IP of the label and the name of
    /// the label.
    pub fn labels(&self) -> &[(usize, String)] {
        self.labels.as_slice()
    }

    /// Returns the IP for a given label.
    ///
    /// This function is used within the `Machine` to perform jumps.
    pub fn get_label_ip(&self, name: &str) -> Option<usize> {
        for label in self.labels.as_slice() {
            if label.1 == name {
                return Some(label.0);
            }
        }
        None
    }
}

impl<'a, T: fmt::Debug + PartialEq> From<Builder<'a, T>> for Code<T> {
    /// Convert a `Builder` into `Code`.
    ///
    /// This function consumes the builder and returns a `Code`.
    fn from(builder: Builder<T>) -> Code<T> {
        let symbols = builder.instruction_table.symbols();
        let code = builder.instructions;
        let data = builder.data;
        let mut labels = vec![];
        for key in builder.labels.keys() {
            let idx = builder.labels.get(&key).unwrap();
            labels.push((*idx, key.clone()));
        }
        labels.sort_by(|lhs, rhs| lhs.0.cmp(&rhs.0));

        Code {
            symbols,
            code,
            data,
            labels,
        }
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use crate::from_byte_code::FromByteCode;
    use crate::instruction::Instruction;
    use crate::instruction_table::InstructionTable;
    use crate::machine::Machine;
    use crate::to_byte_code::ToByteCode;
    use rmp::{decode, encode};
    use std::io::{Read, Write};

    impl ToByteCode for usize {
        fn to_byte_code(&self, mut buf: &mut dyn Write) {
            encode::write_uint(&mut buf, *self as u64).unwrap();
        }
    }

    impl FromByteCode for usize {
        fn from_byte_code(mut buf: &mut dyn Read) -> usize {
            decode::read_int(&mut buf).unwrap()
        }
    }

    fn noop(_machine: &mut Machine<usize>, _args: &[usize]) {}

    fn example_instruction_table() -> InstructionTable<usize> {
        let mut it = InstructionTable::new();
        it.insert(Instruction::new(0, "noop", 0, noop));
        it.insert(Instruction::new(1, "push", 1, noop));
        it.insert(Instruction::new(2, "pop", 0, noop));
        it
    }

    #[test]
    fn from_builder() {
        let it = example_instruction_table();
        let mut builder: Builder<usize> = Builder::new(&it);
        builder.push("push", vec![13]);
        builder.push("push", vec![14]);
        let code: Code<usize> = Code::from(builder);

        assert_eq!(code.symbols().len(), 3);
        assert_eq!(code.symbols()[0], (0 as usize, "noop".to_string()));
        assert_eq!(code.symbols()[1], (1 as usize, "push".to_string()));
        assert_eq!(code.symbols()[2], (2 as usize, "pop".to_string()));

        assert_eq!(code.code(), [1, 1, 0, 1, 1, 1]);
        assert_eq!(code.data(), [13, 14]);
        assert_eq!(code.labels().len(), 1);
        assert_eq!(code.labels()[0], (0 as usize, "main".to_string()));
    }

    #[test]
    fn get_label_ip() {
        let it = example_instruction_table();
        let builder: Builder<usize> = Builder::new(&it);
        let code: Code<usize> = Code::from(builder);
        assert_eq!(code.get_label_ip("main").unwrap(), 0);
    }

    #[test]
    fn debug_formatter() {
        let it = example_instruction_table();
        let mut builder: Builder<usize> = Builder::new(&it);
        builder.push("noop", vec![]);
        builder.push("push", vec![123]);
        builder.push("push", vec![456]);
        builder.label("some_function");
        builder.push("pop", vec![]);
        let code = Code::from(builder);

        let actual = format!("{:?}", code);
        let expected = "@0 = 123
@1 = 456

.main:
\tnoop
\tpush @0
\tpush @1

.some_function:
\tpop
";
        assert_eq!(actual, expected);
    }

    #[test]
    fn to_byte_code() {
        let it = example_instruction_table();
        let mut builder: Builder<usize> = Builder::new(&it);
        builder.push("noop", vec![]);
        builder.push("push", vec![123]);
        builder.push("push", vec![456]);
        builder.label("some_function");
        builder.push("pop", vec![]);
        let code = Code::from(builder);
        let mut actual: Vec<u8> = vec![];
        code.to_byte_code(&mut actual);
        let expected = [
            132, 164, 99, 111, 100, 101, 154, 0, 0, 1, 1, 0, 1, 1, 1, 2, 0, 164, 100, 97, 116, 97,
            146, 123, 205, 1, 200, 167, 115, 121, 109, 98, 111, 108, 115, 150, 0, 164, 110, 111,
            111, 112, 1, 164, 112, 117, 115, 104, 2, 163, 112, 111, 112, 166, 108, 97, 98, 101,
            108, 115, 148, 0, 164, 109, 97, 105, 110, 8, 173, 115, 111, 109, 101, 95, 102, 117,
            110, 99, 116, 105, 111, 110,
        ];
        assert_eq!(&actual[..], &expected[..]);
    }

    #[test]
    fn from_byte_code() {
        let bytecode: [u8; 82] = [
            132, 164, 99, 111, 100, 101, 154, 0, 0, 1, 1, 0, 1, 1, 1, 2, 0, 164, 100, 97, 116, 97,
            146, 123, 205, 1, 200, 167, 115, 121, 109, 98, 111, 108, 115, 150, 0, 164, 110, 111,
            111, 112, 1, 164, 112, 117, 115, 104, 2, 163, 112, 111, 112, 166, 108, 97, 98, 101,
            108, 115, 148, 0, 164, 109, 97, 105, 110, 8, 173, 115, 111, 109, 101, 95, 102, 117,
            110, 99, 116, 105, 111, 110,
        ];
        let code: Code<usize> = Code::from_byte_code(&mut &bytecode[..]);
        assert_eq!(
            code.code,
            [0x0, 0x0, 0x1, 0x1, 0x0, 0x1, 0x1, 0x1, 0x2, 0x0]
        );
        assert_eq!(code.data, [123, 456]);
        assert_eq!(
            code.symbols,
            [
                (0 as usize, "noop".to_string()),
                (1 as usize, "push".to_string()),
                (2 as usize, "pop".to_string())
            ]
        );
        assert_eq!(
            code.labels,
            [
                (0 as usize, "main".to_string()),
                (8 as usize, "some_function".to_string())
            ]
        )
    }
}
