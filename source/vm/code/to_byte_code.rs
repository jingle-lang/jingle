use crate::to_byte_code::ToByteCode;
use std::io::Write;
use rmp::encode;
use std::fmt;
use super::Code;

impl<T: ToByteCode + fmt::Debug> ToByteCode for Code<T> {
    /// Create bytecode for this `Code`.
    ///
    /// Encodes into a Map of the following format:
    /// ```json
    /// {
    ///     "code" => [ 0, 1, 0, 0, 1, 1, 1, 0 ],
    ///     "data" => [ 123, 456 ],
    ///     "symbols" => [ 0, "push", 1, "add" ],
    ///     "labels" => [ 0, "main" ]
    /// }
    /// ```
    fn to_byte_code(&self, mut buf: &mut dyn Write) {
        // We're creating a 4-element map.
        encode::write_map_len(&mut buf, 4).unwrap();

        // First, the code.
        encode::write_str(&mut buf, "code").unwrap();
        encode::write_array_len(&mut buf, self.code.len() as u32).unwrap();
        for operation in self.code() {
            encode::write_uint(&mut buf, *operation as u64).unwrap();
        }

        // Next, the data.
        encode::write_str(&mut buf, "data").unwrap();
        encode::write_array_len(&mut buf, self.data.len() as u32).unwrap();
        for operand in self.data() {
            operand.to_byte_code(&mut buf);
        }

        // Next, the symbols.
        encode::write_str(&mut buf, "symbols").unwrap();
        encode::write_array_len(&mut buf, (self.symbols.len() * 2) as u32).unwrap();
        for symbol in self.symbols() {
            encode::write_uint(&mut buf, symbol.0 as u64).unwrap();
            encode::write_str(&mut buf, &symbol.1).unwrap();
        }

        // Lastly, the labels.
        encode::write_str(&mut buf, "labels").unwrap();
        encode::write_array_len(&mut buf, (self.labels.len() * 2) as u32).unwrap();
        for label in self.labels() {
            encode::write_uint(&mut buf, label.0 as u64).unwrap();
            encode::write_str(&mut buf, &label.1).unwrap();
        }
    }
}
