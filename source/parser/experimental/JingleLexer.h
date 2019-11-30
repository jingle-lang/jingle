
// Generated from JingleLexer.g4 by ANTLR 4.7.2

#pragma once


#include "../cpp/antlr4-runtime/antlr4-runtime.h"


namespace Jingle {


class  JingleLexer : public antlr4::Lexer {
public:
  enum {
    INDENT = 1, DEDENT = 2, ENDSTATEMENT = 3, SEMICOLONTERMINATE = 4, SPEECHMARKS = 5, 
    VAR = 6, ARRAY = 7, CONST = 8, LOCAL = 9, ECHO = 10, RETURN = 11, IF = 12, 
    THEN = 13, AND = 14, OR = 15, IN = 16, ELSE = 17, ELSEIF = 18, WHILE = 19, 
    FOR = 20, TRUE = 21, FALSE = 22, FUNCTION = 23, CLASS = 24, LET = 25, 
    BIND = 26, TRAIT = 27, DEFINE = 28, PROTOCOL = 29, ENUM = 30, IMPORT = 31, 
    FROM = 32, PACKAGE = 33, AS = 34, BREAK = 35, ABSTRACT = 36, SELECT = 37, 
    INPUT = 38, EACH = 39, NEW = 40, CONTINUE = 41, EXPORT = 42, INCLUDE = 43, 
    REQUIRE = 44, SUMMON = 45, WALRUS = 46, EQUALS = 47, EQEQ = 48, NOTEQUAL = 49, 
    LTEQUALS = 50, GTEQUALS = 51, PLUS = 52, MINUS = 53, MULTIPLY = 54, 
    DIVIDE = 55, LESSTHAN = 56, GREATERTHAN = 57, BANG = 58, POWER = 59, 
    MODULUS = 60, VERTICAL = 61, ORSYMBOL = 62, HASH = 63, AMBERSAND = 64, 
    ANDSYMBOL = 65, TYPE_INT = 66, TYPE_DECIMAL = 67, TYPE_STRING = 68, 
    TYPE_BOOLEAN = 69, COMMA = 70, LBRACKET = 71, RBRACKET = 72, LBRACE = 73, 
    RBRACE = 74, LSQRBRACKET = 75, RSQRBRACKET = 76, ARROW = 77, COLON = 78, 
    DOT = 79, ELLIPSIS = 80, PLUSPLUS = 81, MINUSMINUS = 82, FLOAT = 83, 
    STRING = 84, BOOLEAN = 85, NULL = 86, CHAR = 87, INT_LITERAL = 88, FLOAT_LITERAL = 89, 
    WHITESPACE = 90, COMMENT = 91, TERMINATOR = 92, STRING_OPEN = 93, UNMATCHED = 94, 
    SCAPE_STRING_DELIMITER = 95, ESCAPE_SLASH = 96, ESCAPE_NEWLINE = 97, 
    ESCAPE_SHARP = 98, STRING_CLOSE = 99, INTERPOLATION_OPEN = 100, STRING_CONTENT = 101, 
    INTERPOLATION_CLOSE = 102, NOUNICODEID = 103, IDENTIFIER = 104, BINARY_OP = 105, 
    INT_LIT = 106, FLOAT_LIT = 107, STRING_LIT = 108, RUNE_LIT = 109, LITTLE_U_VALUE = 110, 
    BIG_U_VALUE = 111
  };

  enum {
    CONSUME = 2
  };

  enum {
    MODE_IN_STRING = 1, MODE_IN_INTERPOLATION = 2
  };

  JingleLexer(antlr4::CharStream *input);
  ~JingleLexer();

  virtual std::string getGrammarFileName() const override;
  virtual const std::vector<std::string>& getRuleNames() const override;

  virtual const std::vector<std::string>& getChannelNames() const override;
  virtual const std::vector<std::string>& getModeNames() const override;
  virtual const std::vector<std::string>& getTokenNames() const override; // deprecated, use vocabulary instead
  virtual antlr4::dfa::Vocabulary& getVocabulary() const override;

  virtual const std::vector<uint16_t> getSerializedATN() const override;
  virtual const antlr4::atn::ATN& getATN() const override;

private:
  static std::vector<antlr4::dfa::DFA> _decisionToDFA;
  static antlr4::atn::PredictionContextCache _sharedContextCache;
  static std::vector<std::string> _ruleNames;
  static std::vector<std::string> _tokenNames;
  static std::vector<std::string> _channelNames;
  static std::vector<std::string> _modeNames;

  static std::vector<std::string> _literalNames;
  static std::vector<std::string> _symbolicNames;
  static antlr4::dfa::Vocabulary _vocabulary;
  static antlr4::atn::ATN _atn;
  static std::vector<uint16_t> _serializedATN;


  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

  struct Initializer {
    Initializer();
  };
  static Initializer _init;
};

}  // namespace Jingle
