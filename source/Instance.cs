using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    class Instance
    {
        private JingleClass jnclass;
        private readonly Dictionary<string, object> fields = new Dictionary<string, object>();

        public Instance(JingleClass jnclass)
        {
            this.jnclass = jnclass;
        }

        public object get(Token name)
        {
            if (fields.ContainsKey(name.lexeme))
            {
                return fields[name.lexeme];
            }

            JingleFunc method = jnclass.findMethod(name.lexeme);
            if (method != null)
                return method.bind(this);

            throw new RuntimeError(name, "Undefined property '" + name.lexeme + "'.");
        }

        public void set(Token name, object value)
        {
            if (fields.ContainsKey(name.lexeme))
                fields[name.lexeme] = value;
            else
                fields.Add(name.lexeme, value);
        }

        public override string ToString()
        {
            return jnclass.name + " instance";
        }
    }
}