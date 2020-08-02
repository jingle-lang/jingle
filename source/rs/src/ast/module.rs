/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:50 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{
    fmt::{Display, Error, Formatter},
    rc::Rc,
};

use crate::{
    ast::declaration::{Function, IFaceImpl, ADT},
    scanner::token::Token,
};

/// The path of the module. For example, the file 'std/collections/array.gel'
/// would have ["std", "collections", "array"] here.
#[derive(Clone, Debug, Default, PartialOrd, PartialEq, Eq, Hash)]
pub struct ModulePath(pub Vec<Rc<String>>);

impl Display for ModulePath {
    fn fmt(&self, f: &mut Formatter) -> Result<(), Error> {
        write!(
            f,
            "{}",
            self.0
                .iter()
                .map(|rc| (&**rc).clone())
                .collect::<Vec<String>>()
                .join("::")
        )
    }
}

/// A module, containing all code inside it.
/// A module in AST is simply a file.
#[derive(Debug, Default)]
pub struct Module {
    pub path: Rc<ModulePath>,
    pub src: Rc<String>,

    pub adts: Vec<ADT>,
    pub iface_impls: Vec<IFaceImpl>,
    pub functions: Vec<Function>,
    pub imports: Vec<Import>,
    pub exports: Vec<Import>,
}

impl Module {
    pub fn new(path: &ModulePath, src: &Rc<String>) -> Self {
        Self {
            path: Rc::new(path.clone()),
            src: Rc::clone(src),
            ..Self::default()
        }
    }
}

#[derive(Debug, Clone)]
pub struct Import {
    pub path: Rc<ModulePath>,
    pub symbol: Token,
}
