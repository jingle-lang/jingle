using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    class AstPrinter : Expr.Visitor<string>
    {
        public string echo(Expr expr)
        {
            return expr.accept(this);
        }

        public string visitBinaryExpr(Expr.Binary expr)
        {
            return parenthesize(expr.operator_.lexeme, expr.left, expr.right);
        }

        public string visitGroupingExpr(Expr.Grouping expr)
        {
            return parenthesize("group", expr.expression);
        }

        public string visitLiteralExpr(Expr.Literal expr)
        {
            if (expr.value == null)
                return "nil";
            return expr.value.ToString();
        }

        public string visitUnaryExpr(Expr.Unary expr)
        {
            return parenthesize(expr.operator_.lexeme, expr.right);
        }

        private string parenthesize(string name, params Expr[] exprs)
        {
            StringBuilder builder = new StringBuilder();

            builder.Append("(").Append(name);
            foreach (Expr expr in exprs)
            {
                builder.Append(" ");
                builder.Append(expr.accept(this));
            }
            builder.Append(")");

            return builder.ToString();
        }

        public string visitAssignExpr(Expr.Assign expr)
        {
            return "";
        }

        public string visitCallExpr(Expr.Call expr)
        {
            return "";
        }

        public string visitGetExpr(Expr.Get expr)
        {
            return "";
        }

        public string visitLogicalExpr(Expr.Logical expr)
        {
            return "";
        }

        public string visitSetExpr(Expr.Set expr)
        {
            return "";
        }

        public string visitSuperExpr(Expr.Super expr)
        {
            return "";
        }

        public string visitThisExpr(Expr.This expr)
        {
            return "";
        }

        public string visitVariableExpr(Expr.Variable expr)
        {
            return "";
        }
    }
}