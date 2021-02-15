using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    public abstract class Expr
    {
        public interface Visitor<R>
        {
            R visitAssignExpr(Assign expr);
            R visitBinaryExpr(Binary expr);
            R visitCallExpr(Call expr);
            R visitGetExpr(Get expr);
            R visitGroupingExpr(Grouping expr);
            R visitLiteralExpr(Literal expr);
            R visitLogicalExpr(Logical expr);
            R visitSetExpr(Set expr);
            R visitSuperExpr(Super expr);
            R visitThisExpr(This expr);
            R visitUnaryExpr(Unary expr);
            R visitVariableExpr(Variable expr);
        }

        public abstract R accept<R>(Visitor<R> visitor);

        public class Assign : Expr
        {
            public Assign(Token name, Expr value)
            {
                this.name = name;
                this.value = value;
            }

            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitAssignExpr(this);
            }

            public readonly Token name;
            public readonly Expr value;
        }

        public class Binary : Expr
        {
            public Binary(Expr left, Token operator_, Expr right)
            {
                this.left = left;
                this.operator_ = operator_;
                this.right = right;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitBinaryExpr(this);
            }

            public readonly Expr left;
            public readonly Token operator_;
            public readonly Expr right;
        }

        public class Call : Expr
        {
            public Call(Expr callee, Token paren, List<Expr> arguments)
            {
                this.callee = callee;
                this.paren = paren;
                this.arguments = arguments;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitCallExpr(this);
            }

            public readonly Expr callee;
            public readonly Token paren;
            public readonly List<Expr> arguments;
        }

        public class Get : Expr
        {
            public Get(Expr object_, Token name)
            {
                this.object_ = object_;
                this.name = name;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitGetExpr(this);
            }

            public readonly Expr object_;
            public readonly Token name;
        }

        public class Grouping : Expr
        {
            public Grouping(Expr expression)
            {
                this.expression = expression;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitGroupingExpr(this);
            }

            public readonly Expr expression;
        }

        public class Literal : Expr
        {
            public Literal(object value)
            {
                this.value = value;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitLiteralExpr(this);
            }

            public readonly object value;
        }

        public class Logical : Expr
        {
            public Logical(Expr left, Token operator_, Expr right)
            {
                this.left = left;
                this.operator_ = operator_;
                this.right = right;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitLogicalExpr(this);
            }

            public readonly Expr left;
            public readonly Token operator_;
            public readonly Expr right;
        }

        public class Set : Expr
        {
            public Set(Expr object_, Token name, Expr value)
            {
                this.object_ = object_;
                this.name = name;
                this.value = value;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitSetExpr(this);
            }

            public readonly Expr object_;
            public readonly Token name;
            public readonly Expr value;
        }

        public class Super : Expr
        {
            public Super(Token keyword, Token method)
            {
                this.keyword = keyword;
                this.method = method;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitSuperExpr(this);
            }

            public readonly Token keyword;
            public readonly Token method;
        }

        public class This : Expr
        {
            public This(Token keyword)
            {
                this.keyword = keyword;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitThisExpr(this);
            }

            public readonly Token keyword;
        }

        public class Unary : Expr
        {
            public Unary(Token operator_, Expr right)
            {
                this.operator_ = operator_;
                this.right = right;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitUnaryExpr(this);
            }

            public readonly Token operator_;
            public readonly Expr right;
        }

        public class Variable : Expr
        {
            public Variable(Token name)
            {
                this.name = name;
            }


            public override R accept<R>(Visitor<R> visitor)
            {
                return visitor.visitVariableExpr(this);
            }

            public readonly Token name;
        }
    }

}
