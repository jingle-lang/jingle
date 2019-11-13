import ctypes

import llvmlite.binding as llvm

from source.compiler.jinglec import codegen
from source.parser.JingleLexer import *
from source.parser.JingleParser import *
from source.parser.JingleParserVisitor import *

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

class Binder:
    def __init__(self, code):
        parser = parser()
        compiler = codegen()

        tree = parser.parse(code)
        self.ir = str(compiler.compile(tree))
        self._type_map = compiler._fun_types
        self.engine = self.get_engine()
        self.mod = self.compile_ir(self.ir)

    @classmethod
    def from_file(cls, file):
        with open(file) as f:
            code = f.read()
        return cls(code)

    def compile_ir(self, llvm_ir):
        mod = llvm.parse_assembly(llvm_ir)
        mod.verify()
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()
        return mod

    @staticmethod
    def get_engine():
        target = llvm.Target.from_default_triple()
        target_machine = target.create_target_machine()
        backing_mod = llvm.parse_assembly("")
        engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
        return engine

    def __getattr__(self, attr):
        function = self.engine.get_function_address(attr)
        vmtype_decl = self._type_map[attr]
        ret = get_ctype(vmtype_decl.return_type)
        args = [get_ctype(arg) for arg in vmtype_decl.args]
        return ctypes.CFUNCTYPE(ret, *args)(function)
