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

    # Optimizations
    mod.verify()
    pmb = llvm.create_pass_manager_builder()
    pmb.opt_level = 2
    pmb.size_level = 1
    pm = llvm.create_module_pass_manager()
    pmb.populate(pm)
    pm.add_constant_merge_pass()
    pm.add_dead_arg_elimination_pass()
    pm.add_function_attrs_pass()
    pm.add_global_dce_pass()
    pm.add_global_optimizer_pass()
    pm.add_ipsccp_pass()
    pm.add_dead_code_elimination_pass()
    pm.add_dead_arg_elimination_pass()
    pm.add_cfg_simplification_pass()
    pm.add_gvn_pass()
    pm.add_instruction_combining_pass()
    pm.add_licm_pass()
    pm.add_sccp_pass()
    pm.add_sroa_pass()
    pm.add_type_based_alias_analysis_pass()
    pm.add_basic_alias_analysis_pass()
    mod.verify()
    pm.run(mod)

    engine = llvm.create_mcjit_compiler(mod, target_machine)

    # Execute the main() function
    #
    main_ptr = engine.get_function_address('main')
    main_func = ctypes.CFUNCTYPE(None)(main_ptr)
    main_func()

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
