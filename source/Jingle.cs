using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Jingle
{
    public class Jingle
    {
        public static string version = "Jingle Lang 2021.2";
        private static readonly Interpreter interpreter = new Interpreter();
        static bool hadError = false;
        static bool hadRuntimeError = false;
        public static void Main(String[] arguments)
        {
            if (arguments.Length > 1)
            {
                Console.WriteLine("Too many arguments: jingle [file]");
                System.Environment.Exit(64);
            } else if (arguments.Length == 1)
            {
                RunFile(arguments[0]);
            } else
            {
                RunPrompt();
            }
        }
        public static void RunFile(string path)
        {
            byte[] bytes = File.ReadAllBytes(Path.GetFullPath(path));
            Execute(System.Text.Encoding.Default.GetString(bytes, 0, bytes.Length));

            if (hadError) System.Environment.Exit(65);
            if (hadRuntimeError) System.Environment.Exit(70);
        }
        public static void RunPrompt()
        {
            Console.WriteLine(version);
            for (;;)
            {
                Console.Write("> ");
                Execute(Console.ReadLine());
                hadError = false;
            }
        }
        public static void Execute(string source)
        {
            Scanner scanner = new Scanner(source);
            List<Token> tokens = scanner.scanTokens();
            Parser parser = new Parser(tokens);
            List<Stmt> statements = parser.parse();

            if (hadError)
                return;

            Resolver resolver = new Resolver(interpreter);
            resolver.resolve(statements);

            if (hadError)
                return;

            interpreter.interpret(statements);

        }
        public static void Error(int line, string message)
        {
            Report(line, "", message);
        }
        private static void Report(int line, string location, string message)
        {
            Console.WriteLine($"[Line {line}] Error {location}: {message}");
            hadError = true;
        }

        public static void Error(Token token, string message)
        {
            if (token.type == TokenType.EOF)
            {
                Report(token.line, " at end", message);
            }
            else
            {
                Report(token.line, " at '" + token.lexeme + "'", message);
            }
        }
        public static void runtimeError(RuntimeError error)
        {
            System.Console.WriteLine(error.Message + "\n[line " + error.token.line + "]");
            hadRuntimeError = true;
        }
    }
}
