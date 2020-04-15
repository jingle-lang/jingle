# ircode.py

from collections import ChainMap
from llvmlite.ir import Constant, ArrayType, IntType
from . import ast

IR_TYPE_MAPPING = {
    'Int': 'I',
    'Float': 'F',
    'Char': 'B',
    'Str': 'S',
    'Bool': 'I'
}

OP_CODES = ChainMap(
    {
        'mov': 'MOV',
        '+': 'ADD',
        '-': 'SUB',
        '*': 'MUL',
        '/': 'DIV',
        '%': 'MOD',
        '&&': 'AND',
        '||': 'OR',
        'echo': 'PRINT',
        'store': 'STORE',
        'var': 'VAR',
        'alloc': 'ALLOC', # Local allocation (inside functions)
        'load': 'LOAD',
        'label': 'LABEL',
        'cbranch': 'CBRANCH', # Conditional branch
        'branch': 'BRANCH', # Unconditional branch,
        'call': 'CALL',
        'ret': 'RET'
    },
    dict.fromkeys(['<', '>', '<=', '>=', '==', '!='], "CMP")
)

def get_op_code(operation, type_name=None):
    op_code = OP_CODES[operation]
    suffix = "" if not type_name else IR_TYPE_MAPPING[type_name]

    return f"{op_code}{suffix}"


class Function():
    """This represents a function with its list of IR instructions"""

    def __init__(self, func_name, parameters, return_type):
        self.name = func_name
        self.parameters = parameters
        self.return_type = return_type

        self.code = []

    def append(self, ir_instruction):
        self.code.append(ir_instruction)

    def __iter__(self):
        return self.code.__iter__()

    def __repr__(self):
        params = [f"{pname}:{ptype}" for pname, ptype in self.parameters]
        return f"{self.name}({params}) -> {self.return_type}"


class GenerateCode(ast.NodeVisitor):
    '''
    Node visitor class that creates 3-address encoded instruction sequences.
    '''
    def __init__(self):
        # counter for registers
        self.register_count = 0

        # counter for block labels
        self.label_count = 0

        # Special function to collect all global statements
        init_function = Function("__jn_init", [], IR_TYPE_MAPPING['Int'])

        self.functions = [ init_function ]

        # The generated code (list of tuples)
        self.code = init_function.code

        # This flag indicates if the current code being visited is in global
        # scope, or not
        self.global_scope = True

    def new_register(self):
         '''
         Creates a new temporary register
         '''
         self.register_count += 1
         return f'R{self.register_count}'

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    # You must implement visit_Nodename methods for all of the other
    # AST nodes.  In your code, you will need to make instructions
    # and append them to the self.code list.
    #
    # A few sample methods follow.  You may have to adjust depending
    # on the names and structure of your AST nodes.

    def visit_IntegerLiteral(self, node):
        target = self.new_register()
        op_code = get_op_code('mov', 'Int')
        self.code.append((op_code, node.value, target))
        # Save the name of the register where the value was placed
        node.register = target

    def visit_FloatLiteral(self, node):
        target = self.new_register()
        op_code = get_op_code('mov', 'Float')
        self.code.append((op_code, node.value, target))
        node.register = target

    def visit_CharLiteral(self, node):
        target = self.new_register()
        op_code = get_op_code('mov', 'Char')
        # We treat chars as their ascii value
        self.code.append((op_code, ord(node.value), target))
        # This is just to remember where the literal was put in
        node.register = target

    def visit_StringLiteral(self, node):
        target = self.new_register()
        op_code = get_op_code('mov', 'Str')

        #str_data =  bytearray((node.value + "\x00").encode('utf-8'))
        #str_data_array = ArrayType(IR_TYPE_MAPPING['Char'], len(node.value))
        #node.value = str_data_array

        node.value = int(''.join(str(ord(c)) for c in node.value))
        self.code.append((op_code, node.value, target))
        node.register = target

    def visit_BoolLiteral(self, node):
        target = self.new_register()
        op_code = get_op_code('mov', 'Bool')
        # We treat chars as their ascii value
        value = 1 if node.value == "True" else 0
        self.code.append((op_code, value, target))
        # This is just to remember where the literal was put in
        node.register = target

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
        operator = node.op

        op_code = get_op_code(operator, node.left.type.name)

        target = self.new_register()
        if op_code.startswith('CMP'):
            inst = (op_code, operator, node.left.register, node.right.register, target)
        else:
            inst = (op_code, node.left.register, node.right.register, target)

        self.code.append(inst)
        node.register = target

    def visit_UnaryOp(self, node):
        self.visit(node.right)
        operator = node.op

        if operator == "-":
            sub_op_code = get_op_code(operator, node.type.name)
            mov_op_code = get_op_code('mov', node.type.name)

            # To account for the fact that the machine code does not support
            # unary operations, we must load a 0 into a new register first
            zero_target = self.new_register()
            zero_inst = (mov_op_code, 0, zero_target)
            self.code.append(zero_inst)

            target = self.new_register()
            inst = (sub_op_code, zero_target, node.right.register, target)
            self.code.append(inst)
            node.register = target
        elif operator == "!":
            # This is the boolean NOT operator
            mov_op_code = get_op_code('mov', node.type.name)
            one_target = self.new_register()
            one_inst = (mov_op_code, 1, one_target)
            self.code.append(one_inst)

            target = self.new_register()
            inst = ('XOR', one_target, node.right.register, target)
            self.code.append(inst)
            node.register = target
        else:
            # The plus unary operator produces no extra code
            node.register = node.right.register

    def visit_EchoStatement(self, node):
        self.visit(node.value)
        op_code = get_op_code('echo', node.value.type.name)
        inst = (op_code, node.value.register)
        self.code.append(inst)

    def visit_ReadLocation(self, node):
        op_code = get_op_code('load', node.location.type.name)
        register = self.new_register()
        inst = (op_code, node.location.name, register)
        self.code.append(inst)
        node.register = register

    def visit_WriteLocation(self, node):
        self.visit(node.value)
        op_code = get_op_code('store', node.location.type.name)
        inst = (op_code, node.value.register, node.location.name)
        self.code.append(inst)

    def visit_ConstDeclaration(self, node):
        self.visit(node.value)

        # First we must declare the variable
        op_code = get_op_code('var', node.type.name)
        inst = (op_code, node.name)
        self.code.append(inst)

        op_code = get_op_code('store', node.type.name)
        inst = (op_code, node.value.register, node.name)
        self.code.append(inst)

    def visit_VarDeclaration(self, node):
        self.visit(node.datatype)

        # The variable declaration depends on the scope
        op_code = get_op_code('var' if self.global_scope else 'alloc', node.type.name)
        def_inst = (op_code, node.name)

        if node.value:
            self.visit(node.value)
            self.code.append(def_inst)
            op_code = get_op_code('store', node.type.name)
            inst = (op_code, node.value.register, node.name)
            self.code.append(inst)
        else:
            self.code.append(def_inst)

    def visit_IfStatement(self, node):
        self.visit(node.condition)

        # Generate labels for both branches
        f_label = self.new_label()
        t_label = self.new_label()
        merge_label = self.new_label()
        lbl_op_code = get_op_code('label')

        # Insert the CBRANCH instruction
        cbranch_op_code = get_op_code('cbranch')
        self.code.append((cbranch_op_code, node.condition.register, t_label, f_label))

        # Now, the code for the true branch
        self.code.append((lbl_op_code, t_label))
        self.visit(node.true_block)
        # And we must go to the merge label
        branch_op_code = get_op_code('branch')
        self.code.append((branch_op_code, merge_label))

        # Generate label for false block
        self.code.append((lbl_op_code, f_label))
        self.visit(node.false_block)
        self.code.append((branch_op_code, merge_label))

        # Now we insert the merge label
        self.code.append((lbl_op_code, merge_label))

    def visit_WhileStatement(self, node):
        # Generate labels for while handling
        top_label = self.new_label() # This label is before the condition evaluation
        start_label = self.new_label() # This label is just after the condition
        merge_label = self.new_label() # This label is for exiting the loop
        lbl_op_code = get_op_code('label')
        branch_op_code = get_op_code('branch')

        # Insert the CBRANCH instruction
        # This is required because LLVM requires that each block ends with a
        # BRANCH
        self.code.append((branch_op_code, top_label))
        # Now begins the block with the CBRANCH
        self.code.append((lbl_op_code, top_label))
        self.visit(node.condition) # Generate the CMP instruction
        cbranch_op_code = get_op_code('cbranch')
        self.code.append((cbranch_op_code, node.condition.register, start_label, merge_label))

        # Now, the code for the true branch
        self.code.append((lbl_op_code, start_label))
        self.visit(node.body)
        # And we must go to the merge label

        self.code.append((branch_op_code, top_label))

        # Now we insert the merge label
        self.code.append((lbl_op_code, merge_label))

    def visit_FuncDeclaration(self, node):
        # Generate a new function object to collect the code
        func = Function(node.name,
                        [(p.name, IR_TYPE_MAPPING[p.datatype.type.name])
                         for p in node.params],
                        IR_TYPE_MAPPING[node.datatype.type.name])
        self.functions.append(func)

        if func.name == "main":
            func.name = "__jn_main"

        # And switch the current function to the new one
        old_code = self.code
        self.code = func.code

        # Now, generate the new function code
        self.global_scope = False # Turn off global scope
        self.visit(node.body)
        self.global_scope = True # Turn back on global scope

        # And, finally, switch back to the original function we were at
        self.code = old_code

    def visit_FuncCall(self, node):
        self.visit(node.arguments)
        target = self.new_register()
        op_code = get_op_code('call')
        registers = [arg.register for arg in node.arguments]
        self.code.append((op_code, node.name, *registers, target))
        node.register = target

    def visit_ReturnStatement(self, node):
        self.visit(node.value)
        op_code = get_op_code('ret')
        self.code.append((op_code, node.value.register))
        node.register = node.value.register

# ----------------------------------------------------------------------
#                          TESTING/MAIN PROGRAM
# ----------------------------------------------------------------------

def compile_ircode(source):
    '''
    Generate intermediate code from source.
    '''
    from .parser import parse
    from .checker import check_program
    from .errors import errors_reported

    ast = parse(source)
    check_program(ast)

    # If no errors occurred, generate code
    if not errors_reported():
        gen = GenerateCode()
        gen.visit(ast)
        return gen.functions
    else:
        return []

def main():
    import sys

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 -m gone.ircode filename\n")
        raise SystemExit(1)

    source = open(sys.argv[1]).read()
    code = compile_ircode(source)

    for f in code:
        print(f'{"::"*5} {f} {"::"*5}')
        for instruction in f.code:
            print(instruction)
        print("*"*30)

if __name__ == '__main__':
    main()
