// Generated from JingleParser.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link JingleParser}.
 */
public interface JingleParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link JingleParser#jingleFile}.
	 * @param ctx the parse tree
	 */
	void enterJingleFile(JingleParser.JingleFileContext ctx);
	/**
	 * Exit a parse tree produced by {@link JingleParser#jingleFile}.
	 * @param ctx the parse tree
	 */
	void exitJingleFile(JingleParser.JingleFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link JingleParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(JingleParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link JingleParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(JingleParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by the {@code varDeclarationStatement}
	 * labeled alternative in {@link JingleParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclarationStatement(JingleParser.VarDeclarationStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code varDeclarationStatement}
	 * labeled alternative in {@link JingleParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclarationStatement(JingleParser.VarDeclarationStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignmentStatement}
	 * labeled alternative in {@link JingleParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(JingleParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignmentStatement}
	 * labeled alternative in {@link JingleParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(JingleParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code displayStatement}
	 * labeled alternative in {@link JingleParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterDisplayStatement(JingleParser.DisplayStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code displayStatement}
	 * labeled alternative in {@link JingleParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitDisplayStatement(JingleParser.DisplayStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link JingleParser#display}.
	 * @param ctx the parse tree
	 */
	void enterDisplay(JingleParser.DisplayContext ctx);
	/**
	 * Exit a parse tree produced by {@link JingleParser#display}.
	 * @param ctx the parse tree
	 */
	void exitDisplay(JingleParser.DisplayContext ctx);
	/**
	 * Enter a parse tree produced by {@link JingleParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclaration(JingleParser.VarDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link JingleParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclaration(JingleParser.VarDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link JingleParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(JingleParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link JingleParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(JingleParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code decimalLiteral}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterDecimalLiteral(JingleParser.DecimalLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code decimalLiteral}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitDecimalLiteral(JingleParser.DecimalLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code minusExpression}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMinusExpression(JingleParser.MinusExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code minusExpression}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMinusExpression(JingleParser.MinusExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intLiteral}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIntLiteral(JingleParser.IntLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intLiteral}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIntLiteral(JingleParser.IntLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenExpression}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterParenExpression(JingleParser.ParenExpressionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenExpression}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitParenExpression(JingleParser.ParenExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code binaryOperation}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterBinaryOperation(JingleParser.BinaryOperationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code binaryOperation}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitBinaryOperation(JingleParser.BinaryOperationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code typeConversion}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterTypeConversion(JingleParser.TypeConversionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code typeConversion}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitTypeConversion(JingleParser.TypeConversionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code varReference}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterVarReference(JingleParser.VarReferenceContext ctx);
	/**
	 * Exit a parse tree produced by the {@code varReference}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitVarReference(JingleParser.VarReferenceContext ctx);
	/**
	 * Enter a parse tree produced by the {@code integer}
	 * labeled alternative in {@link JingleParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterInteger(JingleParser.IntegerContext ctx);
	/**
	 * Exit a parse tree produced by the {@code integer}
	 * labeled alternative in {@link JingleParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitInteger(JingleParser.IntegerContext ctx);
	/**
	 * Enter a parse tree produced by the {@code decimal}
	 * labeled alternative in {@link JingleParser#dataType}.
	 * @param ctx the parse tree
	 */
	void enterDecimal(JingleParser.DecimalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code decimal}
	 * labeled alternative in {@link JingleParser#dataType}.
	 * @param ctx the parse tree
	 */
	void exitDecimal(JingleParser.DecimalContext ctx);
}