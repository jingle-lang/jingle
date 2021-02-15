namespace Jingle
{
    class Return : System.Exception
    {
        public readonly object value;

        public Return(object value) : base()
        {
            this.value = value;
        }
    }
}
