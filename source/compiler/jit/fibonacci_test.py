from __future__ import print_function
from llvmlite import ir
import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int64

"""
Generate fibonacci function:
f(n) = 1 if n <= 1 else f(n-1) + f(n-2)
"""
# Create a 64bit wide int type
int_type = ir.IntType(64);
# Create a int -> int function
fn_int_to_int_type = ir.FunctionType( int_type, [int_type] )

module = ir.Module( name="m_fibonacci_example" )

# Create the Fibonacci function and block
fn_fib = ir.Function( module, fn_int_to_int_type, name="fn_fib" )
fn_fib_block = fn_fib.append_basic_block( name="fn_fib_entry" )

# Create the builder for the fibonacci code block
builder = ir.IRBuilder( fn_fib_block )

# Access the function argument
fn_fib_n, = fn_fib.args
# Const values for int(1) and int(2)
const_1 = ir.Constant(int_type,1);
const_2 = ir.Constant(int_type,2);

# Create inequality comparison instruction
fn_fib_n_lteq_1 = builder.icmp_signed(cmpop="<=", lhs=fn_fib_n, rhs=const_1 )


# Create the base case
# Using the if_then helper to create the branch instruction and 'then' block if
# the predicate (fn_fib_n_lteq_1) is true ( ie if n <= 1 then ... )
with builder.if_then( fn_fib_n_lteq_1 ):
  # Simply return 1 if n <= 1
  builder.ret( const_1 )


# This is where the recursive case is created
# _temp1= n - 1
fn_fib_n_minus_1 = builder.sub( fn_fib_n, const_1 )
# _temp2 = n - 2
fn_fib_n_minus_2 = builder.sub( fn_fib_n, const_2 )

# Call fibonacci( n - 1 )\
# arguments in a list, in positional order
call_fn_fib_n_minus_1 = builder.call( fn_fib, [fn_fib_n_minus_1] );
# Call fibonacci( n - 2 )
call_fn_fib_n_minus_2 = builder.call( fn_fib, [fn_fib_n_minus_2] );

# Add the resulting call values
fn_fib_rec_res =  builder.add( call_fn_fib_n_minus_1, call_fn_fib_n_minus_2 )

# Return the result of the addition
builder.ret( fn_fib_rec_res )

# Print the generated LLVM asm code
print( module )

"""
Execute generated code.
"""
# initialize the LLVM machine
# These are all required (apparently)
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Create engine and attach the generated module
# Create a target machine representing the host
target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()
# And an execution engine with an empty backing module
backing_mod = llvm.parse_assembly("")
engine = llvm.create_mcjit_compiler(backing_mod, target_machine)

# Parse our generated module
mod = llvm.parse_assembly( str( module ) )
mod.verify()
# Now add the module and make sure it is ready for execution
engine.add_module(mod)
engine.finalize_object()

# Look up the function pointer (a Python int)
func_ptr = engine.get_function_address("fn_fib")

# Run the function via ctypes
c_fn_fib = CFUNCTYPE(c_int64, c_int64)(func_ptr)

# Test our function for n in 0..50
for n in xrange(0,50+1):
  result = c_fn_fib(n)
  print( "c_fn_fib({0}) = {1}".format
