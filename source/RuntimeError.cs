namespace Jingle
{
    public class RuntimeError : System.SystemException
    {
        public readonly Token token;
        public RuntimeError(Token token, string message) : base(message)
        {
            this.token = token;
        }
    }
}
