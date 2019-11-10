require "rubygems"
require "parser"
require "nodes"

require "llvm/core"
require "llvm/execution_engine"
require "llvm/transforms/scalar"

LLVM.init_x86

class LLVMCompiler

  PCHAR = LLVM.Pointer(LLVM::Int8) # equivalent to *char in C
  INT   = LLVM::Int # equivalent to int in C

  attr_reader :locals

  def initialize(mod=nil, function=nil)
    @module = mod || LLVM::Module.new("awesome")
    
    @locals = {} # To track local names during compilation
    
    @function = function ||
                @module.functions.named("main") || # Default the function to `main`
                @module.functions.add("main", [], LLVM.Void)
    
    @builder = LLVM::Builder.new # Prepare a builder to build code.
    @builder.position_at_end(@function.basic_blocks.append)
    
    @engine = LLVM::JITCompiler.new(@module) # The machine code compiler.
  end

  def preamble
    fun = @module.functions.add("puts", [PCHAR], INT)
    fun.linkage = :external
  end
  
  # Always finish the function with a `return`.
  def finish
    @builder.ret_void
  end

  def new_string(value)
    @builder.global_string_pointer(value)
  end

  def new_number(value)
    LLVM::Int(value)
  end
  
  def call(name, args=[])
    function = @module.functions.named(name)
    @builder.call(function, *args)
  end

  def assign(name, value)
    ptr = @builder.alloca(value.type) # Allocate memory.
    @builder.store(value, ptr) # Store the value in the allocated memory.
    @locals[name] = ptr # Keep track of where we stored the local.
  end
  
  def load(name)
    ptr = @locals[name]
    @builder.load(ptr, name) # Load back the value stored for that local.
  end

  def function(name)
    func = @module.functions.add(name, [], LLVM.Void)
    compiler = LLVMCompiler.new(@module, func)
    yield compiler
    compiler.finish
  end

  def optimize
    @module.verify! # Verify the code is valid.
    pass_manager = LLVM::PassManager.new(@engine)
    pass_manager.mem2reg! # Promote memory to machine registers.
  end

  def run
    @engine.run_function(@function)
  end

  def dump
    @module.dump
  end
end

class Nodes
  def llvm_compile(compiler)
    nodes.map { |node| node.llvm_compile(compiler) }.last
  end
end

class NumberNode
  def llvm_compile(compiler)
    compiler.new_number(value)
  end
end

class StringNode
  def llvm_compile(compiler)
    compiler.new_string(value)
  end
end

class CallNode
  def llvm_compile(compiler)
    raise "Receiver not supported for compilation" if receiver
    
    compiled_arguments = arguments.map { |arg| arg.llvm_compile(compiler) }
    compiler.call(method, compiled_arguments)
  end
end

class GetLocalNode
  def llvm_compile(compiler)
    compiler.load(name)
  end
end

class SetLocalNode
  def llvm_compile(compiler)
    compiler.assign(name, value.llvm_compile(compiler))
  end
end

class DefNode
  def llvm_compile(compiler)
    raise "Parameters not supported for compilation" if !params.empty?
    compiler.function(name) do |function|
      body.llvm_compile(function)
    end
  end
end
