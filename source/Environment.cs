using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    class Environment
    {
        public readonly Environment enclosing;
        private readonly Dictionary<string, object> values = new Dictionary<string, object>();

        public Environment()
        {
            enclosing = null;
        }

        public Environment(Environment enclosing)
        {
            this.enclosing = enclosing;
        }


        public object get(Token name)
        {
            if (values.ContainsKey(name.lexeme))
            {
                return values[name.lexeme];
            }

            if (enclosing != null)
                return enclosing.get(name);

            throw new RuntimeError(name, "Undefined variable '" + name.lexeme + "'.");
        }

        public void assign(Token name, object value)
        {
            if (values.ContainsKey(name.lexeme))
            {
                values[name.lexeme] = value;
                return;
            }

            if (enclosing != null)
            {
                enclosing.assign(name, value);
            }

            throw new RuntimeError(name, "Undefined variable '" + name.lexeme + "'.");
        }

        public void define(string name, object value)
        {
            if (values.ContainsKey(name))
                values[name] = value;
            else
                values.Add(name, value);
        }

        Environment ancestor(int distance)
        {
            Environment environment = this;
            for (int i = 0; i < distance; i++)
            {
                environment = environment.enclosing;
            }

            return environment;
        }

        public object getAt(int distance, string name)
        {
            return ancestor(distance).values[name];
        }

        public void assignAt(int distance, Token name, object value)
        {
            ancestor(distance).values[name.lexeme] = value;
        }

        public override string ToString()
        {
            string result = values.ToString();
            if (enclosing != null)
            {
                result += " -> " + enclosing.ToString();
            }

            return result;
        }

    }
}