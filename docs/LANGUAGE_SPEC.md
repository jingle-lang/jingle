# Jingle Language Specification
## Introduction
Welcome to the Jingle programming language specification.

## Table of contents
- [Grammar](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#grammar)
- [Code Elements](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#code-elements)
  - [Comments](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#comments)
- [Control Flow](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#control-flow)
  - [If Statements](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#if-statements)
- [Types](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#types)
  - [Strings](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#strings)
  - [Integers](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#integers)
- [Variables](https://github.com/jingle-lang/jingle/blob/master/docs/LANGUAGE_SPEC.md#variables)

## Grammar
If you wish to have a look at the grammar, it is in EBNF form designed for ANTLR in [source/grammars](https://github.com/jingle-lang/jingle/tree/master/source/grammars).

## Code elements
### Comments
Comments are designed as in-file documentation. Comments can be defined using the `//` character sequence. You can also make multi-line comments using the `/*` opener and `*/` closer.

## Control Flow
### If Statements
if

## Types
Information on various types in the Jingle language.
### Integers
Integer literals are whole numbers. They are practically identical to integers you would find in any other programming languages. They are referred to with the keywords `integer` or `int`.

Examples of integers include:
```
var version = 2
display: ("You are running version #{version}.")
var age = 15
display: ("I am #{age} years old.")
```
### Strings
String literals are essentially pieces of text. They are practically identical to strings that you would find in any other programming language. However, Jingle's strings currently do not support Unicode characters such as Emojis, but this is being worked on. They are referred to with the keywords `string` or `str`.

Examples of strings include:
```
var name = "Tom"
var world = "World"
display: ("Hello #{world}!")
```

You can do string interpolation with `#{expression}` Example: `"Hello there #{name}!" `

## Variables
Jingle has 4 variable types which all have their own declaration statements. There are variables, constants and locals which are all weakly typed, which means their type can be changed at runtime, obviously excluding constants. Let variables are strongly typed so their type cannot be changed at runtime. Let variables also do not have type inference while all other variable types do.

Examples:
```
var random = 15
// This can later turn into any other type due to weak typing.
var random = "15"
// This is the same with and locals.
local index = 5
local index = "5"

// However lets must have their type strictly defined. The value can change but the type cannot.

let int random = 15
let int random = 14
// Allowed

let int random = 15
let str random = "15"
// Not Allowed
```
