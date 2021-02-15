using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    class Resolver : Expr.Visitor<object>, Stmt.Visitor<object>
    {
        private readonly Interpreter interpreter;
        private readonly List<Dictionary<string, bool>> scopes = new List<Dictionary<string, bool>>();
        private FunctionType currentFunction = FunctionType.NONE;

        public Resolver(Interpreter interpreter)
        {
            this.interpreter = interpreter;
        }

        private enum FunctionType
        {
            NONE,
            FUNCTION,
            INITIALIZER,
            METHOD
        }

        private enum ClassType
        {
            NONE,
            CLASS,
            SUBCLASS
        }

        private ClassType currentClass = ClassType.NONE;

        public void resolve(List<Stmt> statements)
        {
            foreach (Stmt statement in statements)
            {
                resolve(statement);
            }
        }

        public object visitBlockStmt(Stmt.Block stmt)
        {
            beginScope();
            resolve(stmt.statements);
            endScope();
            return null;
        }

        public object visitClassStmt(Stmt.Class stmt)
        {
            ClassType enclosingClass = currentClass;
            currentClass = ClassType.CLASS;

            declare(stmt.name);
            define(stmt.name);

            if (stmt.superclass != null && stmt.name.lexeme.Equals(stmt.superclass.name.lexeme))
            {
                Jingle.Error(stmt.superclass.name, "A class cannot inherit from itself.");
            }

            if (stmt.superclass != null)
            {
                currentClass = ClassType.SUBCLASS;
                resolve(stmt.superclass);
            }

            if (stmt.superclass != null)
            {
                beginScope();
                scopes[scopes.Count - 1].Add("super", true);
            }

            beginScope();
            scopes[scopes.Count - 1].Add("this", true);

            foreach (Stmt.Function method in stmt.methods)
            {
                FunctionType declaration = FunctionType.METHOD;
                if (method.name.lexeme.Equals("init"))
                {
                    declaration = FunctionType.INITIALIZER;
                }
                resolveFunction(method, declaration);
            }

            endScope();

            if (stmt.superclass != null)
                endScope();

            currentClass = enclosingClass;
            return null;
        }

        public object visitExpressionStmt(Stmt.Expression stmt)
        {
            resolve(stmt.expression);
            return null;
        }

        public object visitFunctionStmt(Stmt.Function stmt)
        {
            declare(stmt.name);
            define(stmt.name);

            resolveFunction(stmt, FunctionType.FUNCTION);
            return null;
        }

        public object visitIfStmt(Stmt.If stmt)
        {
            resolve(stmt.condition);
            resolve(stmt.thenBranch);
            if (stmt.elseBranch != null)
                resolve(stmt.elseBranch);
            return null;
        }

        public object visitEchoStmt(Stmt.Echo stmt)
        {
            resolve(stmt.expression);
            return null;
        }

        public object visitReturnStmt(Stmt.Return stmt)
        {
            if (currentFunction == FunctionType.NONE)
            {
                Jingle.Error(stmt.keyword, "Cannot return from top-level code.");
            }

            if (stmt.value != null)
            {
                if (currentFunction == FunctionType.INITIALIZER)
                {
                    Jingle.Error(stmt.keyword, "Cannot return a value from an initializer.");
                }

                resolve(stmt.value);
            }

            return null;
        }


        public object visitVarStmt(Stmt.Var stmt)
        {
            declare(stmt.name);
            if (stmt.initializer != null)
            {
                resolve(stmt.initializer);
            }
            define(stmt.name);
            return null;
        }

        public object visitWhileStmt(Stmt.While stmt)
        {
            resolve(stmt.condition);
            resolve(stmt.body);
            return null;
        }

        public object visitAssignExpr(Expr.Assign expr)
        {
            resolve(expr.value);
            resolveLocal(expr, expr.name);
            return null;
        }

        public object visitBinaryExpr(Expr.Binary expr)
        {
            resolve(expr.left);
            resolve(expr.right);
            return null;
        }

        public object visitCallExpr(Expr.Call expr)
        {
            resolve(expr.callee);

            foreach (Expr argument in expr.arguments)
            {
                resolve(argument);
            }

            return null;
        }

        public object visitGetExpr(Expr.Get expr)
        {
            resolve(expr.object_);
            return null;
        }

        public object visitGroupingExpr(Expr.Grouping expr)
        {
            resolve(expr.expression);
            return null;
        }

        public object visitLiteralExpr(Expr.Literal expr)
        {
            return null;
        }

        public object visitLogicalExpr(Expr.Logical expr)
        {
            resolve(expr.left);
            resolve(expr.right);
            return null;
        }

        public object visitSetExpr(Expr.Set expr)
        {
            resolve(expr.value);
            resolve(expr.object_);
            return null;
        }

        public object visitSuperExpr(Expr.Super expr)
        {
            if (currentClass == ClassType.NONE)
            {
                Jingle.Error(expr.keyword, "Cannot use 'super' outside of a class.");
            }
            else if (currentClass != ClassType.SUBCLASS)
            {
                Jingle.Error(expr.keyword, "Cannot use 'super' in a class with no superclass.");
            }

            resolveLocal(expr, expr.keyword);
            return null;
        }

        public object visitThisExpr(Expr.This expr)
        {
            if (currentClass == ClassType.NONE)
            {
                Jingle.Error(expr.keyword, "Cannot use 'this' outside of a class.");
                return null;
            }

            resolveLocal(expr, expr.keyword);
            return null;
        }


        public object visitUnaryExpr(Expr.Unary expr)
        {
            resolve(expr.right);
            return null;
        }

        public object visitVariableExpr(Expr.Variable expr)
        {
            if (scopes.Count > 0 && scopes[scopes.Count - 1].ContainsKey(expr.name.lexeme))
            {
                if (scopes[scopes.Count - 1][expr.name.lexeme] == false)
                    Jingle.Error(expr.name, "Cannot read local variable in its own initializer.");
            }

            resolveLocal(expr, expr.name);
            return null;
        }

        private void resolve(Stmt stmt)
        {
            stmt.accept(this);
        }

        private void resolve(Expr expr)
        {
            expr.accept(this);
        }

        private void resolveFunction(Stmt.Function function, FunctionType type)
        {
            FunctionType enclosingFunction = currentFunction;
            currentFunction = type;

            beginScope();
            foreach (Token param in function.params_)
            {
                declare(param);
                define(param);
            }
            resolve(function.body);
            endScope();
            currentFunction = enclosingFunction;
        }

        private void beginScope()
        {
            scopes.Add(new Dictionary<string, bool>());
        }

        private void endScope()
        {
            scopes.RemoveAt(scopes.Count - 1);
        }

        private void declare(Token name)
        {
            if (scopes.Count < 1)
                return;

            Dictionary<string, bool> scope = scopes[scopes.Count - 1];

            if (scope.ContainsKey(name.lexeme))
            {
                Jingle.Error(name, "Variable with this name already declared in this scope.");
            }
            else
            {
                scope.Add(name.lexeme, false);
            }
        }

        private void define(Token name)
        {
            if (scopes.Count < 1)
                return;
            scopes[scopes.Count - 1][name.lexeme] = true;
        }

        private void resolveLocal(Expr expr, Token name)
        {
            for (int i = scopes.Count - 1; i >= 0; i--)
            {
                if (scopes[i].ContainsKey(name.lexeme))
                {
                    interpreter.resolve(expr, scopes.Count - 1 - i);
                    return;
                }
            }
        }
    }
}