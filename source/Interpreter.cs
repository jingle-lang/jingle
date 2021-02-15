using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    class Interpreter : Expr.Visitor<object>, Stmt.Visitor<object>
    {
        public readonly Environment globals = new Environment();
        private Environment environment;
        private readonly Dictionary<Expr, int> locals = new Dictionary<Expr, int>();


        public Interpreter()
        {
            this.environment = globals;
            globals.define("timer", new Builtins.clockFunction());
            globals.define("gets", new Builtins.inputFunction());
            globals.define("str", new Builtins.toStringFunction());
            globals.define("num", new Builtins.toNumberFunction());
            globals.define("len", new Builtins.lengthFunction());
            globals.define("version", new Builtins.versionFunction());
            globals.define("sqrt", new Builtins.sqrtFunction());
            globals.define("random", new Builtins.randomFunction());
            globals.define("round", new Builtins.roundFunction());
            //globals.define("chr", new Builtins.toAsciiFunction());
            //globals.define("ord", new Builtins.fromAsciiFunction());
        }

        public void interpret(List<Stmt> statements)
        {
            try
            {
                foreach (Stmt statement in statements)
                {
                    execute(statement);
                }
            }
            catch (RuntimeError error)
            {
                Jingle.runtimeError(error);
            }
        }

        private object evaluate(Expr expr)
        {
            return expr.accept(this);
        }

        private void execute(Stmt stmt)
        {
            stmt.accept(this);
        }

        public void resolve(Expr expr, int depth)
        {
            locals.Add(expr, depth);
        }

        public void executeBlock(List<Stmt> statments, Environment environment)
        {
            Environment previous = this.environment;
            try
            {
                this.environment = environment;
                foreach (Stmt statement in statments)
                {
                    execute(statement);
                }
            }
            finally
            {
                this.environment = previous;
            }
        }

        public object visitBlockStmt(Stmt.Block stmt)
        {
            executeBlock(stmt.statements, new Environment(environment));
            return null;
        }

        public object visitClassStmt(Stmt.Class stmt)
        {
            object superclass = null;
            if (stmt.superclass != null)
            {
                superclass = evaluate(stmt.superclass);
                if (!(superclass is JingleClass))
                {
                    throw new RuntimeError(stmt.superclass.name, "Superclass must be a class.");
                }
            }

            environment.define(stmt.name.lexeme, null);

            if (stmt.superclass != null)
            {
                environment = new Environment(environment);
                environment.define("super", superclass);
            }

            Dictionary<string, JingleFunc> methods = new Dictionary<string, JingleFunc>();
            foreach (Stmt.Function method in stmt.methods)
            {
                JingleFunc function = new JingleFunc(method, environment, method.name.lexeme.Equals("init"));
                methods.Add(method.name.lexeme, function);
            }

            JingleClass jnclass = new JingleClass(stmt.name.lexeme, (JingleClass)superclass, methods);

            if (superclass != null)
            {
                environment = environment.enclosing;
            }
            environment.assign(stmt.name, jnclass);
            return null;
        }

        public object visitExpressionStmt(Stmt.Expression stmt)
        {
            evaluate(stmt.expression);
            return null;
        }

        public object visitFunctionStmt(Stmt.Function stmt)
        {
            JingleFunc function = new JingleFunc(stmt, environment, false);
            environment.define(stmt.name.lexeme, function);
            return null;
        }


        public object visitIfStmt(Stmt.If stmt)
        {
            if (isTruthy(evaluate(stmt.condition)))
            {
                execute(stmt.thenBranch);
            }
            else if (stmt.elseBranch != null)
            {
                execute(stmt.elseBranch);
            }
            return null;
        }

        public object visitEchoStmt(Stmt.Echo stmt)
        {
            object value = evaluate(stmt.expression);
            System.Console.WriteLine(stringify(value));
            return null;
        }

        public object visitReturnStmt(Stmt.Return stmt)
        {
            object value = null;
            if (stmt.value != null)
                value = evaluate(stmt.value);

            throw new Return(value);
        }

        public object visitVarStmt(Stmt.Var stmt)
        {
            object value = null;
            if (stmt.initializer != null)
            {
                value = evaluate(stmt.initializer);
            }

            environment.define(stmt.name.lexeme, value);
            return null;
        }

        public object visitWhileStmt(Stmt.While stmt)
        {
            while (isTruthy(evaluate(stmt.condition)))
            {
                execute(stmt.body);
            }
            return null;
        }

        public object visitAssignExpr(Expr.Assign expr)
        {
            object value = evaluate(expr.value);

            int distance;
            if (locals.ContainsKey(expr))
            {
                distance = locals[expr];
                environment.assignAt(distance, expr.name, value);
            }
            else
            {
                globals.assign(expr.name, value);
            }
            return value;
        }

        public object visitBinaryExpr(Expr.Binary expr)
        {
            object left = evaluate(expr.left);
            object right = evaluate(expr.right);

            switch (expr.operator_.type)
            {
                case TokenType.BANG_EQUAL:
                    return !isEqual(left, right);
                case TokenType.EQUAL_EQUAL:
                    return isEqual(left, right);
                case TokenType.GREATER:
                    checkNumberOperands(expr.operator_, left, right);
                    return (double)left > (double)right;
                case TokenType.GREATER_EQUAL:
                    checkNumberOperands(expr.operator_, left, right);
                    return (double)left >= (double)right;
                case TokenType.LESS:
                    checkNumberOperands(expr.operator_, left, right);
                    return (double)left < (double)right;
                case TokenType.LESS_EQUAL:
                    checkNumberOperands(expr.operator_, left, right);
                    return (double)left <= (double)right;
                case TokenType.MINUS:
                    checkNumberOperands(expr.operator_, left, right);
                    return (double)left - (double)right;
                case TokenType.PLUS:
                    if (left is double && right is double)
                    {
                        return (double)left + (double)right;
                    }
                    if (left is string && right is string)
                    {
                        return (string)left + (string)right;
                    }
                    throw new RuntimeError(expr.operator_, "Operands must be two numbers or two strings.");
                case TokenType.SLASH:
                    checkNumberOperands(expr.operator_, left, right);
                    return (double)left / (double)right;
                case TokenType.STAR:
                    checkNumberOperands(expr.operator_, left, right);
                    return (double)left * (double)right;
                case TokenType.MODULO:
                    checkNumberOperands(expr.operator_, left, right);
                    return (double)left % (double)right;
            }

            return null;
        }

        public object visitCallExpr(Expr.Call expr)
        {
            object callee = evaluate(expr.callee);

            List<object> arguments = new List<object>();
            foreach (Expr argument in expr.arguments)
            {
                arguments.Add(evaluate(argument));
            }

            if (!(callee is CallableFunc))
            {
                throw new RuntimeError(expr.paren, "Can only call functions and classes.");
            }

            CallableFunc function = (CallableFunc)callee;
            if (arguments.Count != function.arity())
            {
                throw new RuntimeError(expr.paren, "Expected " + function.arity() + " arguments but got " + arguments.Count + ".");
            }


            return function.call(this, arguments);
        }

        public object visitGetExpr(Expr.Get expr)
        {
            object object_ = evaluate(expr.object_);
            if (object_ is Instance)
            {
                return ((Instance)object_).get(expr.name);
            }

            throw new RuntimeError(expr.name, "Only instances have properties.");
        }

        public object visitGroupingExpr(Expr.Grouping expr)
        {
            return evaluate(expr.expression);
        }

        public object visitLiteralExpr(Expr.Literal expr)
        {
            return expr.value;
        }

        public object visitLogicalExpr(Expr.Logical expr)
        {
            object left = evaluate(expr.left);

            if (expr.operator_.type == TokenType.OR)
            {
                if (isTruthy(left))
                    return left;
            }
            else
            {
                if (!isTruthy(left))
                    return left;
            }

            return evaluate(expr.right);
        }

        public object visitSetExpr(Expr.Set expr)
        {
            object object_ = evaluate(expr.object_);

            if (!(object_ is Instance))
            {
                throw new RuntimeError(expr.name, "Only instances have fields.");
            }

            object value = evaluate(expr.value);
            ((Instance)object_).set(expr.name, value);
            return value;
        }


        public object visitSuperExpr(Expr.Super expr)
        {
            int distance = locals[expr];
            JingleClass superclass = (JingleClass)environment.getAt(distance, "super");

            Instance object_ = (Instance)environment.getAt(distance - 1, "this");

            JingleFunc method = superclass.findMethod(expr.method.lexeme);

            if (method == null)
            {
                throw new RuntimeError(expr.method, "Undefined property '" + expr.method.lexeme + "'.");
            }

            return method.bind(object_);
        }

        public object visitThisExpr(Expr.This expr)
        {
            return lookUpVariable(expr.keyword, expr);
        }

        public object visitUnaryExpr(Expr.Unary expr)
        {
            object right = evaluate(expr.right);

            switch (expr.operator_.type)
            {
                case TokenType.BANG:
                    return !isTruthy(right);
                case TokenType.MINUS:
                    checkNumberOperand(expr.operator_, right);
                    return -(double)right;
            }

            return null;
        }

        public object visitVariableExpr(Expr.Variable expr)
        {
            return lookUpVariable(expr.name, expr);
        }

        private object lookUpVariable(Token name, Expr expr)
        {
            int distance;
            if (locals.ContainsKey(expr))
            {
                distance = locals[expr];
                return environment.getAt(distance, name.lexeme);
            }
            else
            {
                return globals.get(name);
            }
        }

        private void checkNumberOperand(Token operator_, object operand)
        {
            if (operand is double)
                return;
            throw new RuntimeError(operator_, "Operand must be a number.");
        }

        private void checkNumberOperands(Token operator_, object left, object right)
        {
            if (left is double && right is double)
                return;
            throw new RuntimeError(operator_, "Operands must be numbers.");
        }

        private bool isTruthy(object object_)
        {
            if (object_ == null)
                return false;
            if (object_ is bool)
                return (bool)object_;
            return true;
        }

        private bool isEqual(object a, object b)
        {
            if (a == null && b == null)
                return true;
            if (a == null)
                return false;

            return a.Equals(b);
        }

        private string stringify(object object_)
        {
            if (object_ == null)
                return "nil";

            if (object_ is double)
            {
                string text = object_.ToString();
                if (text.EndsWith(".0"))
                {
                    text = text.Substring(0, text.Length - 2);
                }
                return text;
            }

            if (object_ is bool)
            {
                if ((bool)object_)
                    return "true";
                else
                    return "false";
            }

            return object_.ToString();
        }

    }
}