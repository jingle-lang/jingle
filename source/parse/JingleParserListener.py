# Generated from JingleParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JingleParser import JingleParser
else:
    from JingleParser import JingleParser

# This class defines a complete listener for a parse tree produced by JingleParser.
class JingleParserListener(ParseTreeListener):

    # Enter a parse tree produced by JingleParser#top_level_decl.
    def enterTop_level_decl(self, ctx:JingleParser.Top_level_declContext):
        pass

    # Exit a parse tree produced by JingleParser#top_level_decl.
    def exitTop_level_decl(self, ctx:JingleParser.Top_level_declContext):
        pass


    # Enter a parse tree produced by JingleParser#end_of_statement.
    def enterEnd_of_statement(self, ctx:JingleParser.End_of_statementContext):
        pass

    # Exit a parse tree produced by JingleParser#end_of_statement.
    def exitEnd_of_statement(self, ctx:JingleParser.End_of_statementContext):
        pass


    # Enter a parse tree produced by JingleParser#attributes.
    def enterAttributes(self, ctx:JingleParser.AttributesContext):
        pass

    # Exit a parse tree produced by JingleParser#attributes.
    def exitAttributes(self, ctx:JingleParser.AttributesContext):
        pass


    # Enter a parse tree produced by JingleParser#attribute.
    def enterAttribute(self, ctx:JingleParser.AttributeContext):
        pass

    # Exit a parse tree produced by JingleParser#attribute.
    def exitAttribute(self, ctx:JingleParser.AttributeContext):
        pass


    # Enter a parse tree produced by JingleParser#attribute_list.
    def enterAttribute_list(self, ctx:JingleParser.Attribute_listContext):
        pass

    # Exit a parse tree produced by JingleParser#attribute_list.
    def exitAttribute_list(self, ctx:JingleParser.Attribute_listContext):
        pass


    # Enter a parse tree produced by JingleParser#operator.
    def enterOperator(self, ctx:JingleParser.OperatorContext):
        pass

    # Exit a parse tree produced by JingleParser#operator.
    def exitOperator(self, ctx:JingleParser.OperatorContext):
        pass


    # Enter a parse tree produced by JingleParser#statements.
    def enterStatements(self, ctx:JingleParser.StatementsContext):
        pass

    # Exit a parse tree produced by JingleParser#statements.
    def exitStatements(self, ctx:JingleParser.StatementsContext):
        pass


    # Enter a parse tree produced by JingleParser#block.
    def enterBlock(self, ctx:JingleParser.BlockContext):
        pass

    # Exit a parse tree produced by JingleParser#block.
    def exitBlock(self, ctx:JingleParser.BlockContext):
        pass


    # Enter a parse tree produced by JingleParser#param_list.
    def enterParam_list(self, ctx:JingleParser.Param_listContext):
        pass

    # Exit a parse tree produced by JingleParser#param_list.
    def exitParam_list(self, ctx:JingleParser.Param_listContext):
        pass


    # Enter a parse tree produced by JingleParser#param.
    def enterParam(self, ctx:JingleParser.ParamContext):
        pass

    # Exit a parse tree produced by JingleParser#param.
    def exitParam(self, ctx:JingleParser.ParamContext):
        pass


    # Enter a parse tree produced by JingleParser#expression.
    def enterExpression(self, ctx:JingleParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JingleParser#expression.
    def exitExpression(self, ctx:JingleParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JingleParser#main_expression.
    def enterMain_expression(self, ctx:JingleParser.Main_expressionContext):
        pass

    # Exit a parse tree produced by JingleParser#main_expression.
    def exitMain_expression(self, ctx:JingleParser.Main_expressionContext):
        pass


    # Enter a parse tree produced by JingleParser#unary_expression.
    def enterUnary_expression(self, ctx:JingleParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by JingleParser#unary_expression.
    def exitUnary_expression(self, ctx:JingleParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by JingleParser#operand.
    def enterOperand(self, ctx:JingleParser.OperandContext):
        pass

    # Exit a parse tree produced by JingleParser#operand.
    def exitOperand(self, ctx:JingleParser.OperandContext):
        pass


    # Enter a parse tree produced by JingleParser#literal.
    def enterLiteral(self, ctx:JingleParser.LiteralContext):
        pass

    # Exit a parse tree produced by JingleParser#literal.
    def exitLiteral(self, ctx:JingleParser.LiteralContext):
        pass


    # Enter a parse tree produced by JingleParser#statement.
    def enterStatement(self, ctx:JingleParser.StatementContext):
        pass

    # Exit a parse tree produced by JingleParser#statement.
    def exitStatement(self, ctx:JingleParser.StatementContext):
        pass


    # Enter a parse tree produced by JingleParser#declaration.
    def enterDeclaration(self, ctx:JingleParser.DeclarationContext):
        pass

    # Exit a parse tree produced by JingleParser#declaration.
    def exitDeclaration(self, ctx:JingleParser.DeclarationContext):
        pass


    # Enter a parse tree produced by JingleParser#var_declaration.
    def enterVar_declaration(self, ctx:JingleParser.Var_declarationContext):
        pass

    # Exit a parse tree produced by JingleParser#var_declaration.
    def exitVar_declaration(self, ctx:JingleParser.Var_declarationContext):
        pass


    # Enter a parse tree produced by JingleParser#var_declaration_prefix.
    def enterVar_declaration_prefix(self, ctx:JingleParser.Var_declaration_prefixContext):
        pass

    # Exit a parse tree produced by JingleParser#var_declaration_prefix.
    def exitVar_declaration_prefix(self, ctx:JingleParser.Var_declaration_prefixContext):
        pass


    # Enter a parse tree produced by JingleParser#var_declaration_keyword.
    def enterVar_declaration_keyword(self, ctx:JingleParser.Var_declaration_keywordContext):
        pass

    # Exit a parse tree produced by JingleParser#var_declaration_keyword.
    def exitVar_declaration_keyword(self, ctx:JingleParser.Var_declaration_keywordContext):
        pass


    # Enter a parse tree produced by JingleParser#function_declaration.
    def enterFunction_declaration(self, ctx:JingleParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by JingleParser#function_declaration.
    def exitFunction_declaration(self, ctx:JingleParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by JingleParser#function_declaration_prefix.
    def enterFunction_declaration_prefix(self, ctx:JingleParser.Function_declaration_prefixContext):
        pass

    # Exit a parse tree produced by JingleParser#function_declaration_prefix.
    def exitFunction_declaration_prefix(self, ctx:JingleParser.Function_declaration_prefixContext):
        pass


    # Enter a parse tree produced by JingleParser#class_declaration.
    def enterClass_declaration(self, ctx:JingleParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by JingleParser#class_declaration.
    def exitClass_declaration(self, ctx:JingleParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by JingleParser#class_declaration_prefix.
    def enterClass_declaration_prefix(self, ctx:JingleParser.Class_declaration_prefixContext):
        pass

    # Exit a parse tree produced by JingleParser#class_declaration_prefix.
    def exitClass_declaration_prefix(self, ctx:JingleParser.Class_declaration_prefixContext):
        pass


    # Enter a parse tree produced by JingleParser#trait_declaration.
    def enterTrait_declaration(self, ctx:JingleParser.Trait_declarationContext):
        pass

    # Exit a parse tree produced by JingleParser#trait_declaration.
    def exitTrait_declaration(self, ctx:JingleParser.Trait_declarationContext):
        pass


    # Enter a parse tree produced by JingleParser#trait_declaration_prefix.
    def enterTrait_declaration_prefix(self, ctx:JingleParser.Trait_declaration_prefixContext):
        pass

    # Exit a parse tree produced by JingleParser#trait_declaration_prefix.
    def exitTrait_declaration_prefix(self, ctx:JingleParser.Trait_declaration_prefixContext):
        pass


    # Enter a parse tree produced by JingleParser#trait_block.
    def enterTrait_block(self, ctx:JingleParser.Trait_blockContext):
        pass

    # Exit a parse tree produced by JingleParser#trait_block.
    def exitTrait_block(self, ctx:JingleParser.Trait_blockContext):
        pass


    # Enter a parse tree produced by JingleParser#trait_block_body.
    def enterTrait_block_body(self, ctx:JingleParser.Trait_block_bodyContext):
        pass

    # Exit a parse tree produced by JingleParser#trait_block_body.
    def exitTrait_block_body(self, ctx:JingleParser.Trait_block_bodyContext):
        pass


    # Enter a parse tree produced by JingleParser#property_declaration.
    def enterProperty_declaration(self, ctx:JingleParser.Property_declarationContext):
        pass

    # Exit a parse tree produced by JingleParser#property_declaration.
    def exitProperty_declaration(self, ctx:JingleParser.Property_declarationContext):
        pass


    # Enter a parse tree produced by JingleParser#property_declaration_prefix.
    def enterProperty_declaration_prefix(self, ctx:JingleParser.Property_declaration_prefixContext):
        pass

    # Exit a parse tree produced by JingleParser#property_declaration_prefix.
    def exitProperty_declaration_prefix(self, ctx:JingleParser.Property_declaration_prefixContext):
        pass


    # Enter a parse tree produced by JingleParser#import_declaration.
    def enterImport_declaration(self, ctx:JingleParser.Import_declarationContext):
        pass

    # Exit a parse tree produced by JingleParser#import_declaration.
    def exitImport_declaration(self, ctx:JingleParser.Import_declarationContext):
        pass


    # Enter a parse tree produced by JingleParser#import_name_direct.
    def enterImport_name_direct(self, ctx:JingleParser.Import_name_directContext):
        pass

    # Exit a parse tree produced by JingleParser#import_name_direct.
    def exitImport_name_direct(self, ctx:JingleParser.Import_name_directContext):
        pass


    # Enter a parse tree produced by JingleParser#import_from.
    def enterImport_from(self, ctx:JingleParser.Import_fromContext):
        pass

    # Exit a parse tree produced by JingleParser#import_from.
    def exitImport_from(self, ctx:JingleParser.Import_fromContext):
        pass


    # Enter a parse tree produced by JingleParser#static_var_declaration.
    def enterStatic_var_declaration(self, ctx:JingleParser.Static_var_declarationContext):
        pass

    # Exit a parse tree produced by JingleParser#static_var_declaration.
    def exitStatic_var_declaration(self, ctx:JingleParser.Static_var_declarationContext):
        pass


    # Enter a parse tree produced by JingleParser#static_var_declaration_prefix.
    def enterStatic_var_declaration_prefix(self, ctx:JingleParser.Static_var_declaration_prefixContext):
        pass

    # Exit a parse tree produced by JingleParser#static_var_declaration_prefix.
    def exitStatic_var_declaration_prefix(self, ctx:JingleParser.Static_var_declaration_prefixContext):
        pass


    # Enter a parse tree produced by JingleParser#loop_statement.
    def enterLoop_statement(self, ctx:JingleParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by JingleParser#loop_statement.
    def exitLoop_statement(self, ctx:JingleParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by JingleParser#for_statement.
    def enterFor_statement(self, ctx:JingleParser.For_statementContext):
        pass

    # Exit a parse tree produced by JingleParser#for_statement.
    def exitFor_statement(self, ctx:JingleParser.For_statementContext):
        pass


    # Enter a parse tree produced by JingleParser#while_statement.
    def enterWhile_statement(self, ctx:JingleParser.While_statementContext):
        pass

    # Exit a parse tree produced by JingleParser#while_statement.
    def exitWhile_statement(self, ctx:JingleParser.While_statementContext):
        pass


    # Enter a parse tree produced by JingleParser#control_statement.
    def enterControl_statement(self, ctx:JingleParser.Control_statementContext):
        pass

    # Exit a parse tree produced by JingleParser#control_statement.
    def exitControl_statement(self, ctx:JingleParser.Control_statementContext):
        pass


    # Enter a parse tree produced by JingleParser#if_statement.
    def enterIf_statement(self, ctx:JingleParser.If_statementContext):
        pass

    # Exit a parse tree produced by JingleParser#if_statement.
    def exitIf_statement(self, ctx:JingleParser.If_statementContext):
        pass


    # Enter a parse tree produced by JingleParser#else_statement.
    def enterElse_statement(self, ctx:JingleParser.Else_statementContext):
        pass

    # Exit a parse tree produced by JingleParser#else_statement.
    def exitElse_statement(self, ctx:JingleParser.Else_statementContext):
        pass


