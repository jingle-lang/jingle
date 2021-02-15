using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    interface CallableFunc
    {
        int arity();
        object call(Interpreter interpreter, List<object> arguments);
    }
}
