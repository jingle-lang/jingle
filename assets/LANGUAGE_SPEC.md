# OUTDATED! Do not use until updated!
# Jingle Language Specification
## Introduction
Welcome to the Jingle programming language specification.

## Table of contents
- [Grammar](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#grammar)
- [Language Elements](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#language-elements)
  - [Reserved Keywords](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#reserved-keywords)
  - [Naming Convention](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#naming-convention)
- [Code Elements](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#code-elements)
  - [Comments](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#comments)
  - [Imports](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#imports)
- [Control Flow](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#control-flow)
  - [If Statements](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#if-statements)
- [Types](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#types)
  - [Strings](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#strings)
  - [Integers](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#integers)
- [Variables](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#variables)

## Grammar
If you wish to have a look at the grammar, it is in EBNF form designed for ANTLR in [source/grammars](https://github.com/jingle-lang/jingle/tree/master/source/grammars).

## Language Elements
### Reserved Keywords
Jingle uses the following keywords. These keywords cannot be used as identifiers.
```
var    else  import  elif
return class require true
if     let   break   false
else   def   for     while
fn     trait con     as
```

## Code elements
### Comments
Comments are designed as in-file documentation. Comments can be defined using the `//` character sequence. You can also make multi-line comments using the `/*` opener and `*/` closer.

### Imports
You can use methods and variables from other Jingle source files by using imports. You can import local files by using the `require` keyword. This is only used for files that are in the same project. You can import packages by using the `import` keyword. This will import the stated package from the packages directory.

## Control Flow
### If Statements
If statements are used to execute code dependent on different conditions which are specified using a boolean operator. If statements have 2 branches, 'if' or 'else'. If the expression is true, the 'if' branch is executed. If the expression is false, the 'else' branch is executed.

```
a = 10
b = 100
if a > b:
  echo("a is bigger")
elif a == b:
  echo("a and b are equal")
else:
  echo("b is bigger")
end
```

## Types
Information on various types in the Jingle language.
### Integers
Integer literals are whole numbers. They are practically identical to integers you would find in any other programming languages. They are referred to with the keywords `integer` or `int`.

Examples of integers include:
```
var version = 2
var age = 15
var testScore = 56
```

### Floats
Floats are decimal numbers. They are double precision floats like doubles or reals. They are referred to with the keywords `float` or `flt`.

```
var chance = 25.7
var numDifference = 61.24412
echo(7/2) #=> prints 3.5
```


### Strings
String literals are essentially pieces of text. They are practically identical to strings that you would find in any other programming language. However, Jingle's strings currently do not support Unicode characters such as emojis, but this is being worked on. They are referred to with the keywords `string` or `str`.

Examples of strings include:
```
var name = "Tom"
var planet = "Earth"
var language = "Jingle"
```

You can do string interpolation with `#{expression}` Example: `"Hello there #{name}!" `

## Variables
Jingle has 4 variable types which all have their own declaration statements. There are variables and locals which are weakly typed, which means their type can be changed at runtime, and constants which are static which means that their value cannot be changed which means their type cannot be changed.

```
// Variables

var random = 15
// This can later turn into any other type due to weak typing.
var random = "15"

// Constants

const pi = 3.14
// These are constants which cannot change value.
const gravity = 9.8

// Locals

// Local variables can only be created inside a code block and can only be accessed from that same block.

fn helloWorld:
  var message = "World"
  echo("Hello #{message}") => Outputs "Hello World"
end
  
echo("Hello #{message}") => Returns error because message is not defined as a global variable, only as a local variable.
```
Let variables are strongly typed so their type cannot be changed at runtime. Let variables also do not have type inference while all other variable types do.
```
let int random = 15
let int random = 14
// Allowed

let int random = 15
let str random = "15"
// Not Allowed
```
