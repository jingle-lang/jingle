# Functions
- [Overview](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#overview)
- [Invoking functions](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#invoking-functions)
- [Function parameters](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#function-parameters)
- [Returning values](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#returning-values)
- [Closures](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#closures)
- [_Block Arguments?_](https://github.com/jingle-lang/jingle/blob/master/docs/functions.md#block-arguments)

## Overview
Just like any other modern programming language, Jingle contains functions. Jingle's functions are first-class, similar to other languages which means that it can be passed as an argument. Functions in Jingle are also treated as objects like everything else.

Functions are defined with the following syntax:
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
In some cases functions may not need parameters but most of the time, functions are useless unless you can pass values to them. 
