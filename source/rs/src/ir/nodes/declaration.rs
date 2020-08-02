/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 2:53 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{
    collections::HashMap,
    fmt::{Display, Error, Formatter},
    hash::{Hash, Hasher},
    rc::Rc,
};

use indexmap::IndexMap;

use crate::{
    ast,
    ir::{
        generator::builder::Context,
        mutrc_new,
        nodes::{ClosureType, Expr, Prototype, Type},
        MModule, MutRc,
    },
};
use std::cell::Cell;

/// A general purpose class used for all user-defined data structures.
/// The ty field inside is used for further specialization.
#[derive(Debug)]
pub struct ADT {
    /// The name of the ADT.
    pub name: Rc<String>,
    /// All members of the underlying ADT struct.
    pub members: IndexMap<Rc<String>, Rc<ADTMember>>,
    /// All methods of this ADT that can be called by the user
    /// using get/receiver syntax (adt.method(p1, p2) --compile-> method(adt, p1, p2))
    pub methods: HashMap<Rc<String>, Rc<Variable>>,
    /// See [AbstractMethod].
    /// Used only for interfaces, currently.
    pub dyn_methods: IndexMap<Rc<String>, AbstractMethod>,
    /// Methods with generic parameters.
    pub proto_methods: HashMap<Rc<String>, Rc<Prototype>>,

    /// An internal function that creates an instance of the ADT
    /// and populates all fields with a user-given default value.
    /// When the user wants to create an instance by calling a constructor,
    /// this function is called first, followed by one of the constructor methods.
    ///
    /// Note that not all ADT have this function since not all are intended to be
    /// user-instantiated (for example interfaces or closure capture ADTs)
    pub instantiator: Option<Rc<Variable>>,
    /// All constructors of the ADT, if any. They are simply methods
    /// with special constraints to enforce safety.
    /// Only call on instances produced by the instantiator function.
    ///
    /// Note that not all ADT have this function since not all are intended to be
    /// user-instantiated (for example interfaces or closure capture ADTs)
    pub constructors: Vec<Rc<Variable>>,
    /// An internal function that is called when the refcount is decremented.
    /// The only other parameter is a boolean indicating if the object is no longer
    /// reachable and needs to be deallocated. If it is true, it will first decrement
    /// all members first, then call free(). If not, it'll do nothing.
    ///
    /// Note that not all ADT have this function since not all are intended to be
    /// garbage-collected.
    pub destructor: Option<Rc<Variable>>,

    /// The context to be used inside this ADT.
    pub context: Context,

    pub ast: Rc<ast::ADT>,
    pub ty: ADTType,
}

impl ADT {
    /// TODO: Enum edge case is rather ugly
    pub fn from_ast(
        mut ast: ast::ADT,
        context: Context,
        proto: Option<Rc<Prototype>>,
    ) -> MutRc<ADT> {
        let mut enum_cases: Option<Vec<ast::ADT>> = None;
        let (mem_size, method_size, dyn_size, const_size, ty) = match &mut ast.ty {
            ast::ADTType::Class {
                variables,
                constructors,
                external,
            } => (
                variables.len(),
                ast.methods.len(),
                0,
                constructors.len(),
                ADTType::Class {
                    external: *external,
                },
            ),

            ast::ADTType::Interface => (0, 0, ast.methods.len(), 0, ADTType::Interface { proto }),

            ast::ADTType::Enum {
                variables,
                ref mut cases,
            } => {
                enum_cases = Some(std::mem::replace(cases, vec![]));
                (
                    variables.len(),
                    ast.methods.len(),
                    0,
                    0,
                    ADTType::Enum {
                        cases: HashMap::new(),
                    },
                )
            }

            ast::ADTType::EnumCase {
                variables,
                constructors,
                ..
            } => (
                variables.len(), // TODO: check parent
                ast.methods.len(),
                0,
                constructors.len(),
                ADTType::Generic,
            ),
        };

        let adt = mutrc_new(ADT {
            name: Rc::clone(&ast.name.lexeme),
            members: IndexMap::with_capacity(mem_size),
            methods: HashMap::with_capacity(method_size),
            dyn_methods: IndexMap::with_capacity(dyn_size),
            proto_methods: HashMap::new(),
            instantiator: None,
            constructors: Vec::with_capacity(const_size),
            destructor: None,
            context: context.clone(),
            ast: Rc::new(ast),
            ty,
        });

        if let Some(cases) = enum_cases {
            adt.borrow_mut().ty = ADTType::Enum {
                cases: cases
                    .into_iter()
                    .map(|c| {
                        let (case_name, no_body) =
                            if let ast::ADTType::EnumCase {
                                case_name, no_body, ..
                            } = &c.ty
                            {
                                (case_name, *no_body)
                            } else {
                                panic!()
                            };
                        (
                            Rc::clone(&case_name),
                            Self::enum_parent(
                                Self::from_ast(c, context.clone(), None),
                                no_body && mem_size == 0,
                                &adt,
                            ),
                        )
                    })
                    .collect(),
            }
        }

        adt
    }

    fn enum_parent(child: MutRc<ADT>, simple: bool, parent: &MutRc<ADT>) -> MutRc<ADT> {
        child.borrow_mut().ty = ADTType::EnumCase {
            parent: Rc::clone(parent),
            simple,
        };
        child
    }

    pub fn get_singleton_inst(inst: &MutRc<ADT>) -> Option<Expr> {
        if let ADTType::EnumCase {
            simple: no_body, ..
        } = &inst.borrow().ty
        {
            if *no_body {
                Some(Expr::alloc_type(
                    Type::Adt(Rc::clone(inst)),
                    &inst.borrow().constructors[0],
                    vec![],
                ))
            } else {
                None
            }
        } else {
            None
        }
    }
}

impl Display for ADT {
    fn fmt(&self, f: &mut Formatter) -> Result<(), Error> {
        writeln!(f, "adt {} {{\n", self.name)?;
        for (name, member) in self.members.iter() {
            writeln!(
                f,
                "    {} {}: {}",
                if member.mutable { "var" } else { "val" },
                name,
                member.type_
            )?;
        }
        writeln!(f)?;
        for func in self.methods.values() {
            func.type_.as_function().borrow().display(f, "    ")?;
        }
        writeln!(f, "}}")
    }
}

/// The exact type of ADT.
/// Can also contain type-specific data.
#[derive(Debug, EnumIsA)]
pub enum ADTType {
    /// A generic ADT that is just a bunch of members.
    /// Used for things like interface vtables.
    Generic,

    /// A class definition.
    Class {
        // If this class is external (see gelix docs for more info)
        external: bool,
    },

    /// An enum definition.
    Interface {
        /// The prototype this interface was built from, if any.
        /// Only used for some intrinsics.
        proto: Option<Rc<Prototype>>,
    },

    /// An enum, with unknown case.
    Enum {
        /// All cases.
        /// TODO: Copying all members and methods for each case is inefficient,
        /// ideally EnumCase and Enum would be merged somehow
        cases: HashMap<Rc<String>, MutRc<ADT>>,
    },

    /// An enum with known case.
    EnumCase { parent: MutRc<ADT>, simple: bool },
}

impl ADTType {
    /// If this type needs lifecycle methods (instantiator/destructor).
    /// Also used to determine if the type should have its members generated.
    pub fn needs_lifecycle(&self) -> bool {
        self.is_class() || self.is_enum_case() || self.is_enum()
    }

    /// If this type has a refcount and typeinfo field. Currently true for everything but
    /// extern classes.
    pub fn has_refcount(&self) -> bool {
        match self {
            ADTType::Class { external } => !external,
            _ => true,
        }
    }

    /// Returns the cases of an enum type.
    /// Use on any other type will result in a panic.
    pub fn cases(&self) -> &HashMap<Rc<String>, MutRc<ADT>> {
        if let ADTType::Enum { cases } = self {
            cases
        } else {
            unreachable!();
        }
    }
}

/// A member of an ADT struct.
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct ADTMember {
    /// If this member can be reassigned from user code.
    pub mutable: bool,
    /// If this type is visible to user code.
    /// Used to hide interface vtables for example.
    pub visible: bool,
    /// The type of the member.
    pub type_: Type,
    /// The index of the member inside the ADT struct.
    pub index: usize,
    /// If this member has a default value.
    /// This is used for some ADTs to check user constructors
    /// initialize all members before the constructor returns.
    pub has_default_value: bool,
}

/// An implementation of an interface.
#[derive(Debug)]
pub struct IFaceImpl {
    pub implementor: Type,
    pub iface: MutRc<ADT>,
    /// Note: These methods are the same order as the ones on the interface.
    pub methods: IndexMap<Rc<String>, Rc<Variable>>,
    /// Note: This is the module that the impl block is in.
    pub module: MutRc<MModule>,
    pub ast: Rc<ast::IFaceImpl>,
}

/// A struct representing all interfaces implemented by a type.
/// A simple map of interfaces is not enough, as it does not
/// prevent naming collisions.
#[derive(Debug)]
pub struct IFaceImpls {
    pub implementor: Type,
    /// Key is the implemented interface, value the impl.
    /// Key isn't an interface directly due to needed
    /// Hash and Eq traits that only [Type] implements.
    pub interfaces: HashMap<Type, IFaceImpl>,
    pub methods: HashMap<Rc<String>, Rc<Variable>>,
}

/// An abstract method (currently only on interfaces.)
/// Used for dynamic dispatch methods, where the exact
/// method is not known at compile time.
#[derive(Debug)]
pub struct AbstractMethod {
    pub name: Rc<String>,
    pub parameters: Vec<Type>,
    pub ret_type: Type,
    // TODO: Is this obsolete? probably
    pub has_default_impl: bool,
}

impl Display for AbstractMethod {
    fn fmt(&self, f: &mut Formatter) -> Result<(), Error> {
        write!(f, "func {}(", self.name)?;

        let mut params = self.parameters.iter();
        params.next().map(|param| write!(f, "{}", param));
        for param in params {
            write!(f, ", {}", param)?;
        }

        writeln!(f, ")")
    }
}

/// A function.
#[derive(Debug)]
pub struct Function {
    /// The name of the function, with its module before it ($mod:$func)
    /// The only functions with no name change are external functions
    pub name: String,
    /// All parameters needed to call this function.
    pub parameters: Vec<Rc<Variable>>,
    /// A list of expressions that make up the func, executed in order.
    pub exprs: Vec<Expr>,
    /// All variables declared inside that need alloca in IR.
    pub variables: HashMap<Rc<String>, Rc<Variable>>,
    /// The return type of the function; Type::None if omitted.
    pub ret_type: Type,
    /// The context to be used inside this declaration.
    pub context: Context,
    /// The AST the function was compiled from.
    /// This is only present on functions that were
    /// compiled from AST functions;
    /// things like methods have None here.
    pub ast: Option<Rc<ast::Function>>,
    /// If this function has been looked at by the
    /// GC, in particular if all escaping variables have been marked.
    pub gc_inspected: bool,
}

impl Function {
    /// Inserts a variable into the functions allocation table.
    /// Returns the name of it (should be used since a change can be needed due to colliding names).
    pub fn insert_var(&mut self, mut name: Rc<String>, var: Rc<Variable>) -> Rc<String> {
        if self.variables.contains_key(&name) {
            name = Rc::new(format!("{}-{}", name, self.variables.len()));
        }
        self.variables.insert(Rc::clone(&name), var);
        name
    }

    /// Returns the corresponding closure type for this function.
    /// Will not include the first parameter containing captures.
    pub fn to_closure_type(&self) -> Type {
        Type::Closure(Rc::new(ClosureType {
            // Skip the first parameter, which is the parameter for captured variables.
            parameters: self
                .parameters
                .iter()
                .skip(1)
                .map(|p| p.type_.clone())
                .collect(),
            ret_type: self.ret_type.clone(),
        }))
    }

    fn display(&self, f: &mut Formatter, space: &'static str) -> Result<(), Error> {
        write!(f, "{}func {}(", space, self.name)?;

        let mut params = self.parameters.iter();
        params.next().map(|param| {
            write!(
                f,
                "{}: {} (esc: {})",
                param.name,
                param.type_,
                param.escapes.get()
            )
        });
        for param in params {
            write!(
                f,
                ", {}: {}  (esc: {})",
                param.name,
                param.type_,
                param.escapes.get()
            )?;
        }

        writeln!(f, ") {{")?;
        for (name, var) in &self.variables {
            writeln!(
                f,
                "{}{} {}: {} (esc: {}) (local: {})",
                space,
                if var.mutable { "var" } else { "val" },
                name,
                var.type_,
                var.escapes.get(),
                var.as_local.get()
            )?;
        }
        if !self.variables.is_empty() {
            writeln!(f)?;
        }
        for expr in &self.exprs {
            writeln!(f, "{}    {}", space, expr)?;
        }
        writeln!(f, "{}}}", space)
    }
}

impl PartialEq for Function {
    fn eq(&self, other: &Self) -> bool {
        self.name == other.name
    }
}

impl Hash for Function {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.name.hash(state)
    }
}

impl Display for Function {
    fn fmt(&self, f: &mut Formatter) -> Result<(), Error> {
        self.display(f, "")
    }
}

/// A variable. Used for function variables as well as for referencing functions.
#[derive(Debug, Default, Clone)]
pub struct Variable {
    /// If the variable can be mutated after inital set.
    pub mutable: bool,
    /// The type stored by the variable.
    pub type_: Type,
    /// The user-chosen name of the variable.
    pub name: Rc<String>,
    /// If the variable leaves the function and 'escapes' -
    /// if so, all values need to be heap-allocated.
    pub escapes: Cell<bool>,
    /// If this variable should be considered a local inside IR.
    /// If true, it will have it's refcounter decreased once
    /// its surrounding scope exits. True for all variables
    /// except those created in loops, which require special handling.
    pub as_local: Cell<bool>,
}

impl Variable {
    pub fn new(mutable: bool, type_: Type, name: &Rc<String>) -> Rc<Variable> {
        Rc::new(Variable {
            mutable,
            type_,
            name: Rc::clone(name),
            escapes: Cell::new(false),
            as_local: Cell::new(true),
        })
    }
}

impl Hash for Variable {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.name.hash(state)
    }
}
