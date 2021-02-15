using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    class Parser
    {
        private class ParseError : System.SystemException { }

        private readonly List<Token> tokens;
        private int current = 0;

        public Parser(List<Token> tokens)
        {
            this.tokens = tokens;
        }

        public List<Stmt> parse()
        {
            List<Stmt> statements = new List<Stmt>();
            while (!isAtEnd())
            {
                statements.Add(declaration());
            }
            return statements;
        }

        private Expr expression()
        {
            return assignment();
        }

        private Stmt declaration()
        {
            try
            {
                if (match(TokenType.CLASS))
                    return classDeclaration();
                if (match(TokenType.FN))
                    return function("function");
                if (match(TokenType.VAR))
                    return varDeclaration();
                return statement();
            }
            catch (ParseError error)
            {
                syncrhonize();
                return null;
            }
        }

        private Stmt classDeclaration()
        {
            Token name = consume(TokenType.IDENTIFIER, "Expect class name.");

            Expr.Variable superclass = null;
            if (match(TokenType.LESS))
            {
                consume(TokenType.IDENTIFIER, "Expect superclass name.");
                superclass = new Expr.Variable(previous());
            }

            consume(TokenType.COLON, "Expect '{' before class body.");

            List<Stmt.Function> methods = new List<Stmt.Function>();
            while (!check(TokenType.END) && !isAtEnd())
            {
                methods.Add(function("method"));
            }

            consume(TokenType.END, "Expect '}' after class body.");

            return new Stmt.Class(name, superclass, methods);
        }

        private Stmt statement()
        {
            if (match(TokenType.FOR))
                return forStatement();
            if (match(TokenType.IF))
                return ifStatement();
            if (match(TokenType.ECHO))
                return printStatement();
            if (match(TokenType.RETURN))
                return returnStatement();
            if (match(TokenType.WHILE))
                return whileStatement();
            if (match(TokenType.COLON))
                return new Stmt.Block(block());

            return expressionStatement();
        }

        private Stmt forStatement()
        {
            consume(TokenType.LEFT_PAREN, "Expect '(' after 'for'.");

            Stmt initializer;
            if (match(TokenType.SEMICOLON))
            {
                initializer = null;
            }
            else if (match(TokenType.VAR))
            {
                initializer = varDeclaration();
            }
            else
            {
                initializer = expressionStatement();
            }

            Expr condition = null;
            if (!check(TokenType.SEMICOLON))
            {
                condition = expression();
            }
            consume(TokenType.SEMICOLON, "Expect ';' after loop condition.");

            Expr increment = null;
            if (!check(TokenType.RIGHT_PAREN))
            {
                increment = expression();
            }
            consume(TokenType.RIGHT_PAREN, "Expect ')' after for clauses.");
            Stmt body = statement();

            if (increment != null)
            {
                body = new Stmt.Block(new List<Stmt> { body, new Stmt.Expression(increment) });
            }

            if (condition == null)
                condition = new Expr.Literal(true);
            body = new Stmt.While(condition, body);

            if (initializer != null)
                body = new Stmt.Block(new List<Stmt> { initializer, body });

            return body;
        }

        private Stmt ifStatement()
        {
            //consume(TokenType.LEFT_PAREN, "Expect '(' after 'if'.");
            Expr condition = expression();
            //consume(TokenType.RIGHT_PAREN, "Expect ')' after if condition.");

            Stmt thenBranch = statement();
            Stmt elseBranch = null;
            if (match(TokenType.ELSE))
            {
                elseBranch = statement();
            }

            return new Stmt.If(condition, thenBranch, elseBranch);
        }

        private Stmt printStatement()
        {
            Expr value = expression();
            consume(TokenType.SEMICOLON, "Expect ';' after value.");
            return new Stmt.Echo(value);
        }

        private Stmt returnStatement()
        {
            Token keyword = previous();
            Expr value = null;
            if (!check(TokenType.SEMICOLON))
            {
                value = expression();
            }
            consume(TokenType.SEMICOLON, "Expect ';' after return value.");
            return new Stmt.Return(keyword, value);
        }

        private Stmt varDeclaration()
        {
            Token name = consume(TokenType.IDENTIFIER, "Expect variable name.");

            Expr initializer = null;
            if (match(TokenType.EQUAL))
            {
                initializer = expression();
            }

            consume(TokenType.SEMICOLON, "Expect ';' after variable declaration.");
            return new Stmt.Var(name, initializer);
        }

        private Stmt whileStatement()
        {
            //consume(TokenType.LEFT_PAREN, "Expect '(' after while.");
            Expr condition = expression();
            //consume(TokenType.RIGHT_PAREN, "Expect ')' after condition.");
            Stmt body = statement();

            return new Stmt.While(condition, body);
        }

        private Stmt expressionStatement()
        {
            Expr expr = expression();
            consume(TokenType.SEMICOLON, "Expect ';' after expression.");
            return new Stmt.Expression(expr);
        }

        private Stmt.Function function(string kind)
        {
            Token name = consume(TokenType.IDENTIFIER, "Expect " + kind + " name.");
            consume(TokenType.LEFT_PAREN, "Expect '(' after" + kind + " name.");
            List<Token> parameters = new List<Token>();
            if (!check(TokenType.RIGHT_PAREN))
            {
                do
                {
                    if (parameters.Count >= 255)
                    {
                        error(peek(), "Cannot have more than 255 parameters.");
                    }

                    parameters.Add(consume(TokenType.IDENTIFIER, "Expect parameter name."));
                }
                while (match(TokenType.COMMA));
            }
            consume(TokenType.RIGHT_PAREN, "Expect ')' after parameters.");
            consume(TokenType.COLON, "Expect '{' before" + kind + "body.");
            List<Stmt> body = block();
            return new Stmt.Function(name, parameters, body);
        }

        private List<Stmt> block()
        {
            List<Stmt> statements = new List<Stmt>();

            while (!check(TokenType.END) && !isAtEnd())
            {
                statements.Add(declaration());
            }

            consume(TokenType.END, "Expect '}' after block.");
            return statements;
        }

        private Expr assignment()
        {
            Expr expr = or();

            if (match(TokenType.EQUAL))
            {
                Token equals = previous();
                Expr value = assignment();

                if (expr is Expr.Variable)
                {
                    Token name = ((Expr.Variable)expr).name;
                    return new Expr.Assign(name, value);
                }
                else if (expr is Expr.Get)
                {
                    Expr.Get get = (Expr.Get)expr;
                    return new Expr.Set(get.object_, get.name, value);
                }

                error(equals, "Invalid assignment target.");
            }

            return expr;
        }

        private Expr or()
        {
            Expr expr = and();

            while (match(TokenType.OR))
            {
                Token operator_ = previous();
                Expr right = and();
                expr = new Expr.Logical(expr, operator_, right);
            }

            return expr;
        }

        private Expr and()
        {
            Expr expr = equality();

            while (match(TokenType.AND))
            {
                Token operator_ = previous();
                Expr right = equality();
                expr = new Expr.Logical(expr, operator_, right);
            }

            return expr;
        }

        private Expr equality()
        {
            Expr expr = comparison();

            while (match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL))
            {
                Token operator_ = previous();
                Expr right = comparison();
                expr = new Expr.Binary(expr, operator_, right);
            }

            return expr;
        }

        private Expr comparison()
        {
            Expr expr = addition();

            while (match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL))
            {
                Token operator_ = previous();
                Expr right = addition();
                expr = new Expr.Binary(expr, operator_, right);
            }

            return expr;
        }

        private Expr addition()
        {
            Expr expr = multiplication();

            while (match(TokenType.MINUS, TokenType.PLUS))
            {
                Token operator_ = previous();
                Expr right = multiplication();
                expr = new Expr.Binary(expr, operator_, right);
            }

            return expr;
        }

        private Expr multiplication()
        {
            Expr expr = unary();

            while (match(TokenType.SLASH, TokenType.STAR, TokenType.MODULO))
            {
                Token operator_ = previous();
                Expr right = unary();
                expr = new Expr.Binary(expr, operator_, right);
            }

            return expr;
        }

        private Expr unary()
        {
            if (match(TokenType.BANG, TokenType.MINUS))
            {
                Token operator_ = previous();
                Expr right = unary();
                return new Expr.Unary(operator_, right);
            }

            return call();
        }

        private Expr finishCall(Expr callee)
        {
            List<Expr> arguments = new List<Expr>();
            if (!check(TokenType.RIGHT_PAREN))
            {
                do
                {
                    if (arguments.Count >= 255)
                    {
                        error(peek(), "Cannot have more than 255 arguments.");
                    }
                    arguments.Add(expression());
                }
                while (match(TokenType.COMMA));
            }

            Token paren = consume(TokenType.RIGHT_PAREN, "Expect ')' after arguments");
            return new Expr.Call(callee, paren, arguments);
        }

        private Expr call()
        {
            Expr expr = primary();

            while (true)
            {
                if (match(TokenType.LEFT_PAREN))
                {
                    expr = finishCall(expr);
                }
                else if (match(TokenType.DOT))
                {
                    Token name = consume(TokenType.IDENTIFIER, "Expect property name after '.'.");
                    expr = new Expr.Get(expr, name);
                }
                else
                {
                    break;
                }
            }

            return expr;
        }

        private Expr primary()
        {
            if (match(TokenType.FALSE))
                return new Expr.Literal(false);
            if (match(TokenType.TRUE))
                return new Expr.Literal(true);
            if (match(TokenType.NIL))
                return new Expr.Literal(null);
            if (match(TokenType.NUMBER, TokenType.STRING))
            {
                return new Expr.Literal(previous().literal);
            }

            if (match(TokenType.SUPER))
            {
                Token keyword = previous();
                consume(TokenType.DOT, "Expect '.' after 'super'.");
                Token method = consume(TokenType.IDENTIFIER, "Expect superclass method name.");
                return new Expr.Super(keyword, method);
            }

            if (match(TokenType.THIS))
                return new Expr.This(previous());
            if (match(TokenType.IDENTIFIER))
            {
                return new Expr.Variable(previous());
            }

            if (match(TokenType.LEFT_PAREN))
            {
                Expr expr = expression();
                consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.");
                return new Expr.Grouping(expr);
            }

            throw error(peek(), "Expect expression.");
        }

        private bool match(params TokenType[] types)
        {
            foreach (TokenType type in types)
            {
                if (check(type))
                {
                    advance();
                    return true;
                }
            }
            return false;
        }

        private Token consume(TokenType type, string message)
        {
            if (check(type))
                return advance();

            throw error(peek(), message);
        }

        private bool check(TokenType type)
        {
            if (isAtEnd())
                return false;
            return peek().type == type;
        }

        private Token advance()
        {
            if (!isAtEnd())
                current++;
            return previous();
        }

        private bool isAtEnd()
        {
            return peek().type == TokenType.EOF;
        }

        private Token peek()
        {
            return tokens[current];
        }

        private Token previous()
        {
            return tokens[current - 1];
        }

        private ParseError error(Token token, string message)
        {
            Jingle.Error(token, message);
            return new ParseError();
        }

        private void syncrhonize()
        {
            advance();

            while (!isAtEnd())
            {
                if (previous().type == TokenType.SEMICOLON)
                    return;

                switch (peek().type)
                {
                    case TokenType.CLASS:
                    case TokenType.FN:
                    case TokenType.VAR:
                    case TokenType.FOR:
                    case TokenType.IF:
                    case TokenType.WHILE:
                    case TokenType.ECHO:
                    case TokenType.RETURN:
                        return;
                }

                advance();
            }
        }
    }
}