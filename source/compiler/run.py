# run.py
#
# Runs a Jingle program in a LLVM JIT.   This requires that the
# Jingle runtime support library (jnruntime.c) be compiled into a shared
# object and placed in the same directory as this file.

import os
import os.path
import ctypes
import llvmlite.binding as llvm

_path = os.path.dirname(__file__)

def run(llvm_ir):
    # Load the runtime
    if os.name != 'nt':
        ctypes._dlopen(os.path.join(_path, 'jnruntime.so'), ctypes.RTLD_GLOBAL)
    else:
        ctypes._dlopen(os.path.join(_path, 'jnruntime.dll'), ctypes.RTLD_GLOBAL)

    # Initialize LLVM
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()

    engine = llvm.create_mcjit_compiler(mod, target_machine)

    # Execute the main() function
    #
    main_ptr = engine.get_function_address('main')
    main_func = ctypes.CFUNCTYPE(None)(main_ptr)
    main_func()

    # Modify the above code to execute the Jingle __init() function
    # that initializes global variables.  Then add code below
    # that executes the Jingle main() function.

    # llvmlite.binding.load_library_permanently(filename)

def main():
    from .errors import errors_reported
    from .llvmgen import compile_llvm
    import sys

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 -m jingle.run filename\n")
        raise SystemExit(1)

    source = open(sys.argv[1]).read()
    llvm_code = compile_llvm(source)
    if not errors_reported():
        run(llvm_code)

if __name__ == '__main__':
    main()
