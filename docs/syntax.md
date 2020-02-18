# Syntax

- Overview
- Files
- Comments
- Reserved words
- Identifiers
- Newlines
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
and   end     nil
as    false   not
bind  fn      or
break for     require
class from    return
const if      this
def   import  trait
echo  in      true
elif  is      var
else  let     while
```
Obviously all names of _types_ are reserved keywords, such as `int`, `float`, `bool` etc.
