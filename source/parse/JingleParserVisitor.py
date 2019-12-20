# Generated from JingleParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JingleParser import JingleParser
else:
    from JingleParser import JingleParser

# This class defines a complete generic visitor for a parse tree produced by JingleParser.

class JingleParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JingleParser#top_level_decl.
    def visitTop_level_decl(self, ctx:JingleParser.Top_level_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#end_of_statement.
    def visitEnd_of_statement(self, ctx:JingleParser.End_of_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#attributes.
    def visitAttributes(self, ctx:JingleParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#attribute.
    def visitAttribute(self, ctx:JingleParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#attribute_list.
    def visitAttribute_list(self, ctx:JingleParser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#operator.
    def visitOperator(self, ctx:JingleParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#statements.
    def visitStatements(self, ctx:JingleParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#block.
    def visitBlock(self, ctx:JingleParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#param_list.
    def visitParam_list(self, ctx:JingleParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#param.
    def visitParam(self, ctx:JingleParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#expression.
    def visitExpression(self, ctx:JingleParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#main_expression.
    def visitMain_expression(self, ctx:JingleParser.Main_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#unary_expression.
    def visitUnary_expression(self, ctx:JingleParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#operand.
    def visitOperand(self, ctx:JingleParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#literal.
    def visitLiteral(self, ctx:JingleParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#statement.
    def visitStatement(self, ctx:JingleParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#declaration.
    def visitDeclaration(self, ctx:JingleParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#var_declaration.
    def visitVar_declaration(self, ctx:JingleParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#var_declaration_prefix.
    def visitVar_declaration_prefix(self, ctx:JingleParser.Var_declaration_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#var_declaration_keyword.
    def visitVar_declaration_keyword(self, ctx:JingleParser.Var_declaration_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#function_declaration.
    def visitFunction_declaration(self, ctx:JingleParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#function_declaration_prefix.
    def visitFunction_declaration_prefix(self, ctx:JingleParser.Function_declaration_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#class_declaration.
    def visitClass_declaration(self, ctx:JingleParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#class_declaration_prefix.
    def visitClass_declaration_prefix(self, ctx:JingleParser.Class_declaration_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#trait_declaration.
    def visitTrait_declaration(self, ctx:JingleParser.Trait_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#trait_declaration_prefix.
    def visitTrait_declaration_prefix(self, ctx:JingleParser.Trait_declaration_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#trait_block.
    def visitTrait_block(self, ctx:JingleParser.Trait_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#trait_block_body.
    def visitTrait_block_body(self, ctx:JingleParser.Trait_block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#property_declaration.
    def visitProperty_declaration(self, ctx:JingleParser.Property_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#property_declaration_prefix.
    def visitProperty_declaration_prefix(self, ctx:JingleParser.Property_declaration_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#import_declaration.
    def visitImport_declaration(self, ctx:JingleParser.Import_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#import_name_direct.
    def visitImport_name_direct(self, ctx:JingleParser.Import_name_directContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#import_from.
    def visitImport_from(self, ctx:JingleParser.Import_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#static_var_declaration.
    def visitStatic_var_declaration(self, ctx:JingleParser.Static_var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#static_var_declaration_prefix.
    def visitStatic_var_declaration_prefix(self, ctx:JingleParser.Static_var_declaration_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#loop_statement.
    def visitLoop_statement(self, ctx:JingleParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#for_statement.
    def visitFor_statement(self, ctx:JingleParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#while_statement.
    def visitWhile_statement(self, ctx:JingleParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#control_statement.
    def visitControl_statement(self, ctx:JingleParser.Control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#if_statement.
    def visitIf_statement(self, ctx:JingleParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#else_statement.
    def visitElse_statement(self, ctx:JingleParser.Else_statementContext):
        return self.visitChildren(ctx)



del JingleParser