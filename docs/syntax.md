# Syntax

- Overview
- Files
- Comments
- Reserved words
- Identifiers
- Blocks
- Operators

## Overview
Jingle's syntax is influenced by and is designed for users of high-level languages such as Python and Ruby. However, it brings it slightly lower-level in an attempt to make the syntax more streamlined, simple and enjoyable to program and play with.

## Files
All Jingle source files are stored in plain text files with a `.jn` file extension.

## Comments
Line comments begin with `#` and run to the end of the line.
`# This is a comment.`
Block comments begin with `/*` and end with `*/`. Unlike line comments, block comments can span multiple lines.
```
/* This
   is
   a
   block
   comment */
```
Since block comments are detected and treated the same way as typical blocks they can be nested within other block comments.
```
/* Outside /* inside comment */ comment */
```
This feature is very useful as code that already has block comments can still be fully commented out without removing or changing existing comments.

## Reserved words
If you still want to have a feel of the language's style then you can view Jingle's reserved keywords.
```
and   end    nil
as    false  not
bind  fn     or
break for    require
class from   return
const if     this
def   import trait
echo  in     true
elif  is     var
else  let    while
```
Obviously all names of _types_ are reserved keywords, such as `int`, `float`, `bool` etc.

## Identifiers
The naming rules in Jingle are very similar to those of other programming languages. Identifiers start with a letter or underscore and may contain letters, digits or underscores. Case is insensitive.
```
hello
camelCase
PascalCase
_underscore
abc123
CONSTANT_IS_ALL_CAPS
```
Constants usually have all capital identifers but they are not needed. Classes and functions should use PascalCase but variables should use camelCase. Special variables should start with underscores (_).

## Blocks
The syntax of block definition in Jingle is a combination of Python and Ruby. They are started with a colon (:) and ended with the keyword `end`. Blocks can be used in the following: control flow statements, class bodies, function bodies, method bodies and trait bodies. 

Example of a block in an `if` statement.
```
if happy == true && knowIt == true:
   Hands.Clap()
else:
   echo "Sad"
end
```
Blocks that just contain statements implicitly return a value of `nil` when completed. If you wish to make the block return a different value, then you must use a `return` statement. For example, both of these functions return `"It is true"`.
```
if test == true:
   "It is true"
end

if test == true:
   return "It is true"
end
```

## Operators
| Operator        | Symbol          | Literal  |
| -------------   |:---------------:| --------:|
| Grouping | `( )` | None |
| Subscript | `[ ]` | None |
| Method calls | `.` | None |
| Negate | `-` | None |
| Not | `!` | `not` |
| Multiply | `*` | None |
| Divide | `/` | None |
| Modulus | `%` | None |
| Add | `+` | None |
| Minus | `-` | None |
| Inclusive Range | `..` | None |
| Exclusive Range | `...` | None |
| And | `&&` | `and` |
| Or | `||` | `or` |
| Comparison | `<`, `<=`, `>`, `>=` | None |
| Equality | `==`, `!=` | `is`, None |
| Assignment | `=` | None |
