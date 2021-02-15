using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    class JingleFunc : CallableFunc
    {
        private readonly Stmt.Function declaration;
        private readonly Environment closure;
        private readonly bool isInitializer;

        public JingleFunc(Stmt.Function declaration, Environment closure, bool isInitializer)
        {
            this.isInitializer = isInitializer;
            this.closure = closure;
            this.declaration = declaration;
        }

        public JingleFunc bind(Instance instance)
        {
            Environment environment = new Environment(closure);
            environment.define("this", instance);
            return new JingleFunc(declaration, environment, isInitializer);
        }

        public override string ToString()
        {
            return "<fn " + declaration.name.lexeme + ">";
        }

        public int arity()
        {
            return declaration.params_.Count;
        }

        public object call(Interpreter interpreter, List<object> arguments)
        {
            Environment environment = new Environment(closure);

            for (int i = 0; i < declaration.params_.Count; i++)
            {
                environment.define(declaration.params_[i].lexeme, arguments[i]);
            }

            try
            {
                interpreter.executeBlock(declaration.body, environment);
            }
            catch (Return returnValue)
            {
                if (isInitializer)
                    return closure.getAt(0, "this");

                return returnValue.value;
            }

            if (isInitializer)
                return closure.getAt(0, "this");

            return null;
        }

    }
}