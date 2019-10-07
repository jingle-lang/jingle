use super::Code;
use std::fmt;

impl<T: fmt::Debug> fmt::Debug for Code<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut result = String::new();

        // Write out constant data into the header.
        for i in 0..self.data.len() {
            result.push_str(&format!("@{} = {:?}\n", i, self.data[i]));
        }

        // Loop through the code and print out useful stuff.
        let mut ip = 0;
        let len = self.code.len();
        loop {
            // If this IP has a label, then print it out.
            for label in self.labels() {
                if ip == label.0 {
                    result.push_str(&format!("\n.{}:\n", label.1));
                    break;
                }
            }

            if ip == len {
                break;
            }

            let op_code = self.code[ip];
            let arity = self.code[ip + 1];
            ip += 2;

            // Print this instruction's name
            for symbol in self.symbols() {
                if op_code == symbol.0 {
                    result.push_str(&format!("\t{}", symbol.1));
                    break;
                }
            }

            for _i in 0..arity {
                let const_idx = self.code[ip];
                ip += 1;
                result.push_str(&format!(" @{}", const_idx));
            }
            result.push_str("\n");
        }

        write!(f, "{}", result)
    }
}
