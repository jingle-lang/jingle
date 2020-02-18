# Functions
- [Overview](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#overview)
- [Invoking functions](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#invoking-functions)
- [Function parameters](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#function-parameters)
- [Returning values](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#returning-values)
- [_Closures?_](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#closures)
- [_Block Arguments?_](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#block-arguments)

## Overview
Just like any other modern programming language, Jingle contains functions. Jingle's functions are _first-class_, similar to other languages which means that it can be passed as an _argument_. Functions in Jingle are also treated as _objects_ like everything else.

Functions are defined with the following _syntax_:
```
fn <-name of function-> (<-optional parameters->):
  <-function body->
end
```
## Invoking functions
Now that we know how to define functions, we need to be able to invoke it. Functions can be called from the scope that they are defined in. For example:
```
fn MyFunction: # this function is declared globally, so it can be accessed globally.
  echo "Hello!"
end

MyFunction()

class MyClass: # a globally declared class
  fn ScopedFunction:
    echo "Scope matters!"
  end
end

ScopedFunction() # Error: function or method does not exist

MyClass.ScopedFunction() # this function is declared inside of the class so must be invoked as a class method
```
## Function parameters
In some cases functions may not need parameters but most of the time, functions are useless unless you can pass _values_ to them. So far, every function shown does not accept or require parameters. If your function requires parameters, you add them in a parentheses-delimited _list_ between the function's name and start of the function body (:).
```
fn NameIs(name):
  echo "My name is #{name}"
end

NameIs("Johnny") # prints out => "Johnny"
```
There is theoretically no limit on the amount of parameters a function can have, shown here in a function with 6 parameters:
```
fn PersonProfile(firstName, lastName, job, dayBirth, monthBirth, yearBirth):
  echo "#{firstName} #{lastName} works as a #{job} and was born on #{monthBirth} #{dayBirth}, #{yearBirth}"
end

PersonProfile("John", "Stevenson", "Programmer", "18", "February", "1998") # prints out => "John Stevenson works as a Programmer and was born on 18 February, 1998"
```
## Returning values
The body of a function is a _block_. If the block is a single expression then the implicit returned value of the function is that of the single expression. Otherwise, the block will return _`nil`_ by default. Explicit returning of values is defined using a `return` statement. For example, these 2 functions both do the same thing:
```
fn Func:
  "value"
end

fn Func:
  return "value"
end
```
## _Closures?_
Closures in Jingle are still being designed.

## _Block arguments?_
Block arguments in Jingle are still being designed.
