use crate::from_byte_code::FromByteCode;
use std::io::Read;
use rmp::decode;
use std::fmt;
use super::Code;

impl<T: FromByteCode + fmt::Debug> FromByteCode for Code<T> {
    fn from_byte_code(mut buf: &mut dyn Read) -> Code<T> {
        // We expect a four-element map.
        let map_len = decode::read_map_len(&mut buf).unwrap();
        assert_eq!(map_len, 4);

        // We expect the code section next:
        let section = read_string(&mut buf);
        assert_eq!(section, "code");

        let code_len = decode::read_array_len(&mut buf).unwrap();
        let mut code: Vec<usize> = vec![];
        for _i in 0..code_len {
            code.push(decode::read_int(&mut buf).unwrap());
        }

        // We expect the data section next
        let section = read_string(&mut buf);
        assert_eq!(section, "data");

        let data_len = decode::read_array_len(&mut buf).unwrap();
        let mut data: Vec<T> = vec![];
        for _i in 0..data_len {
            data.push(FromByteCode::from_byte_code(&mut buf));
        }

        // Next, symbols.
        let section = read_string(&mut buf);
        assert_eq!(section, "symbols");

        let symbol_len = decode::read_array_len(&mut buf).unwrap();
        let mut symbols: Vec<(usize, String)> = vec![];
        for _i in 0..symbol_len / 2 {
            let idx = decode::read_int(&mut buf).unwrap();
            let symbol = read_string(&mut buf);
            symbols.push((idx, symbol));
        }

        // Lastly, labels.
        let section = read_string(&mut buf);
        assert_eq!(section, "labels");

        let label_len = decode::read_array_len(&mut buf).unwrap();
        let mut labels: Vec<(usize, String)> = vec![];
        for _i in 0..label_len / 2 {
            let idx = decode::read_int(&mut buf).unwrap();
            let label = read_string(&mut buf);
            labels.push((idx, label));
        }

        Code {
            symbols,
            code,
            data,
            labels
        }
    }
}

fn read_string(mut buf: &mut dyn Read) -> String {
    let len = decode::read_str_len(&mut buf).unwrap();
    let mut strbuf: Vec<u8> = vec![0u8; len as usize];
    buf.read_exact(&mut strbuf).unwrap();
    String::from_utf8(strbuf).unwrap()
}
