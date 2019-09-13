// Generated from JingleParser.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link JingleParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface JingleParserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link JingleParser#jingleFile}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitJingleFile(JingleParser.JingleFileContext ctx);
	/**
	 * Visit a parse tree produced by {@link JingleParser#line}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLine(JingleParser.LineContext ctx);
	/**
	 * Visit a parse tree produced by the {@code varDeclarationStatement}
	 * labeled alternative in {@link JingleParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarDeclarationStatement(JingleParser.VarDeclarationStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code assignmentStatement}
	 * labeled alternative in {@link JingleParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentStatement(JingleParser.AssignmentStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code displayStatement}
	 * labeled alternative in {@link JingleParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDisplayStatement(JingleParser.DisplayStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link JingleParser#display}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDisplay(JingleParser.DisplayContext ctx);
	/**
	 * Visit a parse tree produced by {@link JingleParser#varDeclaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarDeclaration(JingleParser.VarDeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link JingleParser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(JingleParser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by the {@code decimalLiteral}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecimalLiteral(JingleParser.DecimalLiteralContext ctx);
	/**
	 * Visit a parse tree produced by the {@code minusExpression}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMinusExpression(JingleParser.MinusExpressionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code intLiteral}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntLiteral(JingleParser.IntLiteralContext ctx);
	/**
	 * Visit a parse tree produced by the {@code parenExpression}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParenExpression(JingleParser.ParenExpressionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code binaryOperation}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinaryOperation(JingleParser.BinaryOperationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code typeConversion}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeConversion(JingleParser.TypeConversionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code varReference}
	 * labeled alternative in {@link JingleParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarReference(JingleParser.VarReferenceContext ctx);
	/**
	 * Visit a parse tree produced by the {@code integer}
	 * labeled alternative in {@link JingleParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInteger(JingleParser.IntegerContext ctx);
	/**
	 * Visit a parse tree produced by the {@code decimal}
	 * labeled alternative in {@link JingleParser#dataType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecimal(JingleParser.DecimalContext ctx);
}