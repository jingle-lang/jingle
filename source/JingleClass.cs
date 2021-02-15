using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    class JingleClass : CallableFunc {
        public readonly string name;
        public readonly JingleClass superclass;
        private readonly Dictionary<string, JingleFunc> methods;

        public JingleClass(string name, JingleClass superclass, Dictionary<string, JingleFunc> methods)
        {
            this.superclass = superclass;
            this.name = name;            
            this.methods = methods;
        }

        public JingleFunc findMethod(string name)
        {
            if (methods.ContainsKey(name))
            {
                return methods[name];
            }

            if(superclass != null)
            {
                return superclass.findMethod(name);
            }

            return null;
        }

        public override string ToString()
        {
            return name;
        }

        public object call(Interpreter interpreter, List<object> arguments)
        {
            Instance instance = new Instance(this);
            JingleFunc initializer = findMethod("init");
            if (initializer != null)
            {
                initializer.bind(instance).call(interpreter, arguments);
            }

            return instance;
        }

        public int arity()
        {
            JingleFunc initializer = findMethod("init");
            if (initializer == null)
                return 0;

            return initializer.arity();
        }
    }
}
