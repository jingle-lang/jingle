/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/14/19 2:34 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

extern crate test;

use std::env;
use std::path::PathBuf;
use test::Bencher;

static GENERIC_TEST: &str = "class_generic_instantiation.jn";

fn get_benchmark(name: &'static str) -> PathBuf {
    let mut test_path = env::current_dir().expect("Couldn't get current dir.");
    test_path.push("tests");
    test_path.push("benchmark");
    test_path.push(name);
    test_path
}

#[bench]
fn generic_classes_parse(b: &mut Bencher) {
    let path = vec![get_benchmark(GENERIC_TEST)];
    b.iter(|| super::parse_source(path.clone()));
}

#[bench]
fn generic_classes_mir(b: &mut Bencher) {
    let path = vec![get_benchmark(GENERIC_TEST)];
    b.iter(|| {
        let ast = super::parse_source(path.clone()).ok().unwrap();
        super::compile_mir(ast)
    });
}
