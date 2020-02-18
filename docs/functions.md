## Functions
- Overview
- Invoking functions
- Function parameters
- Returning values
- Closures
- Block Arguments?

### Overview
Just like any other modern programming language, Jingle contains functions. Jingle's functions are first-class, similar to other languages which means that it can be passed as an argument. Functions in Jingle are also treated as objects like everything else.

Functions are defined with the following syntax:

fn <-name of function-> (<-optional parameters->):
  <-function body->
end

A simple example of a function is below.

fn sayString(string):
  echo "Hello #{string}!"
  echo "The string is #{string}."
end

Another example below:

fn addNums(num1, num2):
  finalNum = num1 + num2
  echo "#{num1} + #{num2} is #{finalNum}"
end
