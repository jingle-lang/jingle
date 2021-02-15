using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    class Builtins
    {
        public class clockFunction : CallableFunc
        {
            public int arity()
            {
                return 0;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return (double)System.Environment.TickCount / 1000.0;
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class versionFunction : CallableFunc
        {
            public int arity()
            {
                return 0;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return "You are running " + Jingle.version;
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class inputFunction : CallableFunc
        {
            public int arity()
            {
                return 0;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return Console.ReadLine();
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class toStringFunction : CallableFunc
        {
            public int arity()
            {
                return 1;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return arguments[0].ToString();
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class lengthFunction : CallableFunc
        {
            public int arity()
            {
                return 1;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return Convert.ToDouble(arguments[0].ToString().Length);
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class sqrtFunction : CallableFunc
        {
            public int arity()
            {
                return 1;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return Math.Sqrt(Convert.ToDouble(arguments[0]));
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class randomFunction : CallableFunc
        {
            public int arity()
            {
                return 2;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                Random rng = new Random();
                return Convert.ToDouble(rng.Next(Convert.ToInt32(arguments[0]), Convert.ToInt32(arguments[1])));
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class toNumberFunction : CallableFunc
        {
            public int arity()
            {
                return 1;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return Convert.ToDouble(arguments[0]);
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class roundFunction : CallableFunc
        {
            public int arity()
            {
                return 2;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return Math.Round(Convert.ToDouble(arguments[0]), Convert.ToInt32(arguments[1]));
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class toAsciiFunction : CallableFunc
        {
            public int arity()
            {
                return 1;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return (char)arguments[0];
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
        public class fromAsciiFunction : CallableFunc
        {
            public int arity()
            {
                return 1;
            }
            public object call(Interpreter interpreter, List<object> arguments)
            {
                return(int)arguments[0];
            }
            public override string ToString()
            {
                return "<native fn>";
            }
        }
    }
}