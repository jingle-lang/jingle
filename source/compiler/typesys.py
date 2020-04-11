# typesys.py
'''
Jingle Type System
================
This file implements basic features of the Jingle type system.  There is
a lot of flexibility possible here, but the best strategy might be to
not overthink the problem.  At least not at first.  Here are the
minimal basic requirements:

1. Types have names (e.g., 'int', 'float', 'string')
2. Types have to be comparable. (e.g., int != float).
3. Types support different operators (e.g., +, -, *, /, etc.)

'''

ARITHM_BIN_OPS = ["+", "-", "*", "/"]
ARITHM_UNARY_OPS = ["+", "-"]

REL_BIN_OPS = ["<", "<=", ">", ">=", "==", "!="]

BOOL_BIN_OPS = ["&&", "||", "==", "!="]
BOOL_UNARY_OPS = ["!"]

class Type():
    """Base class for our type system"""

    @classmethod
    def binop_type(cls, op, right_type):
        """Returns the type of applying the binary operator with the current
        type and the type of the right operand, or returns None if the
        operation is not valid"""
        return None

    @classmethod
    def unaryop_type(cls, op):
        """Returns the type of applying the unary operator to the current type"""
        return None

    @classmethod
    def get_by_name(cls, type_name):
        for type_cls in cls.__subclasses__():
            if type_cls.name == type_name:
                return type_cls

        return None

class FloatType(Type):
    name = "float"

    @classmethod
    def binop_type(cls, op, right_type):
        if issubclass(right_type, FloatType):
            if op in ARITHM_BIN_OPS:
                return FloatType
            elif op in REL_BIN_OPS:
                return BoolType

        return None

    @classmethod
    def unaryop_type(cls, op):
        if op in ARITHM_UNARY_OPS:
            return FloatType

        return None

class IntType(Type):
    name = "int"

    @classmethod
    def binop_type(cls, op, right_type):
        if issubclass(right_type, IntType):
            if op in ARITHM_BIN_OPS:
                return IntType
            elif op in REL_BIN_OPS:
                return BoolType

        return None

    @classmethod
    def unaryop_type(cls, op):
        if op in ARITHM_UNARY_OPS:
            return IntType

        return None

class CharType(Type):
    name = "char"

    @classmethod
    def binop_type(cls, op, right_type):
        if issubclass(right_type, CharType):
            if op in REL_BIN_OPS:
                return BoolType

        return None

#class StringType(Type):
#    name = "str"

#    @classmethod
#    def binop_type(cls, op, right_type):
#        if issubclass(right_type, StringType):
#            if op in REL_BIN_OPS:
#                return BoolType

#        return None


class BoolType(Type):
    name = "bool"

    @classmethod
    def binop_type(cls, op, right_type):
        if issubclass(right_type, BoolType) and op in BOOL_BIN_OPS:
                return BoolType

        return None

    @classmethod
    def unaryop_type(cls, op):
        if op in BOOL_UNARY_OPS:
            return BoolType

        return None
