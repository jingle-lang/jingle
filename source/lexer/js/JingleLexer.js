// Generated from JingleLexer.g4 by ANTLR 4.7.2
// jshint ignore: start
var antlr4 = require('antlr4/index');



var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0002&\u00df\b\u0001\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004",
    "\u0004\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t",
    "\u0007\u0004\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004",
    "\f\t\f\u0004\r\t\r\u0004\u000e\t\u000e\u0004\u000f\t\u000f\u0004\u0010",
    "\t\u0010\u0004\u0011\t\u0011\u0004\u0012\t\u0012\u0004\u0013\t\u0013",
    "\u0004\u0014\t\u0014\u0004\u0015\t\u0015\u0004\u0016\t\u0016\u0004\u0017",
    "\t\u0017\u0004\u0018\t\u0018\u0004\u0019\t\u0019\u0004\u001a\t\u001a",
    "\u0004\u001b\t\u001b\u0004\u001c\t\u001c\u0004\u001d\t\u001d\u0004\u001e",
    "\t\u001e\u0004\u001f\t\u001f\u0004 \t \u0004!\t!\u0004\"\t\"\u0004#",
    "\t#\u0004$\t$\u0004%\t%\u0004&\t&\u0003\u0002\u0003\u0002\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0005\u0003T\n\u0003\u0003\u0004",
    "\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0005\u0003\u0005\u0003\u0005",
    "\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005",
    "\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005\u0005\u0005",
    "h\n\u0005\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006",
    "\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0007\u0003\u0007\u0003\u0007",
    "\u0003\b\u0003\b\u0003\b\u0003\b\u0003\b\u0003\t\u0003\t\u0003\t\u0003",
    "\t\u0003\n\u0003\n\u0003\n\u0003\n\u0003\n\u0003\u000b\u0003\u000b\u0003",
    "\u000b\u0003\u000b\u0003\u000b\u0003\u000b\u0003\f\u0003\f\u0003\f\u0003",
    "\f\u0003\f\u0003\r\u0003\r\u0003\r\u0003\r\u0003\u000e\u0003\u000e\u0003",
    "\u000f\u0003\u000f\u0003\u0010\u0003\u0010\u0003\u0011\u0003\u0011\u0003",
    "\u0012\u0003\u0012\u0003\u0013\u0003\u0013\u0003\u0014\u0003\u0014\u0003",
    "\u0015\u0003\u0015\u0003\u0016\u0003\u0016\u0003\u0016\u0003\u0017\u0003",
    "\u0017\u0003\u0018\u0003\u0018\u0003\u0019\u0003\u0019\u0003\u001a\u0003",
    "\u001a\u0003\u001b\u0003\u001b\u0003\u001c\u0003\u001c\u0003\u001d\u0003",
    "\u001d\u0003\u001e\u0003\u001e\u0003\u001f\u0003\u001f\u0003 \u0003",
    " \u0003 \u0003!\u0003!\u0003!\u0003!\u0003!\u0003!\u0003\"\u0003\"\u0003",
    "\"\u0003\"\u0003\"\u0003\"\u0003\"\u0003#\u0003#\u0003#\u0003#\u0003",
    "#\u0003$\u0003$\u0003$\u0003$\u0003$\u0003%\u0003%\u0003%\u0003%\u0003",
    "%\u0003&\u0006&\u00d7\n&\r&\u000e&\u00d8\u0003&\u0003&\u0003&\u0005",
    "&\u00de\n&\u0002\u0002\'\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005",
    "\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019",
    "\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014",
    ")\u0015+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e",
    "=\u001f? A!C\"E#G$I%K&\u0003\u0002\u0003\u0003\u00022;\u0002\u00e3\u0002",
    "\u0005\u0003\u0002\u0002\u0002\u0002\u0007\u0003\u0002\u0002\u0002\u0002",
    "\t\u0003\u0002\u0002\u0002\u0002\u000b\u0003\u0002\u0002\u0002\u0002",
    "\r\u0003\u0002\u0002\u0002\u0002\u000f\u0003\u0002\u0002\u0002\u0002",
    "\u0011\u0003\u0002\u0002\u0002\u0002\u0013\u0003\u0002\u0002\u0002\u0002",
    "\u0015\u0003\u0002\u0002\u0002\u0002\u0017\u0003\u0002\u0002\u0002\u0002",
    "\u0019\u0003\u0002\u0002\u0002\u0002\u001b\u0003\u0002\u0002\u0002\u0002",
    "\u001d\u0003\u0002\u0002\u0002\u0002\u001f\u0003\u0002\u0002\u0002\u0002",
    "!\u0003\u0002\u0002\u0002\u0002#\u0003\u0002\u0002\u0002\u0002%\u0003",
    "\u0002\u0002\u0002\u0002\'\u0003\u0002\u0002\u0002\u0002)\u0003\u0002",
    "\u0002\u0002\u0002+\u0003\u0002\u0002\u0002\u0002-\u0003\u0002\u0002",
    "\u0002\u0002/\u0003\u0002\u0002\u0002\u00021\u0003\u0002\u0002\u0002",
    "\u00023\u0003\u0002\u0002\u0002\u00025\u0003\u0002\u0002\u0002\u0002",
    "7\u0003\u0002\u0002\u0002\u00029\u0003\u0002\u0002\u0002\u0002;\u0003",
    "\u0002\u0002\u0002\u0002=\u0003\u0002\u0002\u0002\u0002?\u0003\u0002",
    "\u0002\u0002\u0002A\u0003\u0002\u0002\u0002\u0002C\u0003\u0002\u0002",
    "\u0002\u0002E\u0003\u0002\u0002\u0002\u0002G\u0003\u0002\u0002\u0002",
    "\u0002I\u0003\u0002\u0002\u0002\u0002K\u0003\u0002\u0002\u0002\u0003",
    "M\u0003\u0002\u0002\u0002\u0005S\u0003\u0002\u0002\u0002\u0007U\u0003",
    "\u0002\u0002\u0002\tg\u0003\u0002\u0002\u0002\u000bi\u0003\u0002\u0002",
    "\u0002\rq\u0003\u0002\u0002\u0002\u000ft\u0003\u0002\u0002\u0002\u0011",
    "y\u0003\u0002\u0002\u0002\u0013}\u0003\u0002\u0002\u0002\u0015\u0082",
    "\u0003\u0002\u0002\u0002\u0017\u0088\u0003\u0002\u0002\u0002\u0019\u008d",
    "\u0003\u0002\u0002\u0002\u001b\u0091\u0003\u0002\u0002\u0002\u001d\u0093",
    "\u0003\u0002\u0002\u0002\u001f\u0095\u0003\u0002\u0002\u0002!\u0097",
    "\u0003\u0002\u0002\u0002#\u0099\u0003\u0002\u0002\u0002%\u009b\u0003",
    "\u0002\u0002\u0002\'\u009d\u0003\u0002\u0002\u0002)\u009f\u0003\u0002",
    "\u0002\u0002+\u00a1\u0003\u0002\u0002\u0002-\u00a4\u0003\u0002\u0002",
    "\u0002/\u00a6\u0003\u0002\u0002\u00021\u00a8\u0003\u0002\u0002\u0002",
    "3\u00aa\u0003\u0002\u0002\u00025\u00ac\u0003\u0002\u0002\u00027\u00ae",
    "\u0003\u0002\u0002\u00029\u00b0\u0003\u0002\u0002\u0002;\u00b2\u0003",
    "\u0002\u0002\u0002=\u00b4\u0003\u0002\u0002\u0002?\u00b6\u0003\u0002",
    "\u0002\u0002A\u00b9\u0003\u0002\u0002\u0002C\u00bf\u0003\u0002\u0002",
    "\u0002E\u00c6\u0003\u0002\u0002\u0002G\u00cb\u0003\u0002\u0002\u0002",
    "I\u00d0\u0003\u0002\u0002\u0002K\u00dd\u0003\u0002\u0002\u0002MN\t\u0002",
    "\u0002\u0002N\u0004\u0003\u0002\u0002\u0002OT\u0007%\u0002\u0002PT\u000b",
    "\u0002\u0002\u0002QR\u00071\u0002\u0002RT\u00071\u0002\u0002SO\u0003",
    "\u0002\u0002\u0002SP\u0003\u0002\u0002\u0002SQ\u0003\u0002\u0002\u0002",
    "T\u0006\u0003\u0002\u0002\u0002UV\u0007x\u0002\u0002VW\u0007c\u0002",
    "\u0002WX\u0007t\u0002\u0002X\b\u0003\u0002\u0002\u0002YZ\u0007e\u0002",
    "\u0002Z[\u0007q\u0002\u0002[\\\u0007p\u0002\u0002\\]\u0007u\u0002\u0002",
    "]h\u0007v\u0002\u0002^h\u000b\u0002\u0002\u0002_`\u0007e\u0002\u0002",
    "`a\u0007q\u0002\u0002ab\u0007p\u0002\u0002bc\u0007u\u0002\u0002cd\u0007",
    "v\u0002\u0002de\u0007c\u0002\u0002ef\u0007p\u0002\u0002fh\u0007v\u0002",
    "\u0002gY\u0003\u0002\u0002\u0002g^\u0003\u0002\u0002\u0002g_\u0003\u0002",
    "\u0002\u0002h\n\u0003\u0002\u0002\u0002ij\u0007f\u0002\u0002jk\u0007",
    "k\u0002\u0002kl\u0007u\u0002\u0002lm\u0007r\u0002\u0002mn\u0007n\u0002",
    "\u0002no\u0007c\u0002\u0002op\u0007{\u0002\u0002p\f\u0003\u0002\u0002",
    "\u0002qr\u0007k\u0002\u0002rs\u0007h\u0002\u0002s\u000e\u0003\u0002",
    "\u0002\u0002tu\u0007g\u0002\u0002uv\u0007n\u0002\u0002vw\u0007u\u0002",
    "\u0002wx\u0007g\u0002\u0002x\u0010\u0003\u0002\u0002\u0002yz\u0007h",
    "\u0002\u0002z{\u0007q\u0002\u0002{|\u0007t\u0002\u0002|\u0012\u0003",
    "\u0002\u0002\u0002}~\u0007v\u0002\u0002~\u007f\u0007t\u0002\u0002\u007f",
    "\u0080\u0007w\u0002\u0002\u0080\u0081\u0007g\u0002\u0002\u0081\u0014",
    "\u0003\u0002\u0002\u0002\u0082\u0083\u0007h\u0002\u0002\u0083\u0084",
    "\u0007c\u0002\u0002\u0084\u0085\u0007n\u0002\u0002\u0085\u0086\u0007",
    "u\u0002\u0002\u0086\u0087\u0007g\u0002\u0002\u0087\u0016\u0003\u0002",
    "\u0002\u0002\u0088\u0089\u0007h\u0002\u0002\u0089\u008a\u0007w\u0002",
    "\u0002\u008a\u008b\u0007p\u0002\u0002\u008b\u008c\u0007e\u0002\u0002",
    "\u008c\u0018\u0003\u0002\u0002\u0002\u008d\u008e\u0007n\u0002\u0002",
    "\u008e\u008f\u0007g\u0002\u0002\u008f\u0090\u0007v\u0002\u0002\u0090",
    "\u001a\u0003\u0002\u0002\u0002\u0091\u0092\u0007<\u0002\u0002\u0092",
    "\u001c\u0003\u0002\u0002\u0002\u0093\u0094\u0007?\u0002\u0002\u0094",
    "\u001e\u0003\u0002\u0002\u0002\u0095\u0096\u0007-\u0002\u0002\u0096",
    " \u0003\u0002\u0002\u0002\u0097\u0098\u0007/\u0002\u0002\u0098\"\u0003",
    "\u0002\u0002\u0002\u0099\u009a\u0007,\u0002\u0002\u009a$\u0003\u0002",
    "\u0002\u0002\u009b\u009c\u00071\u0002\u0002\u009c&\u0003\u0002\u0002",
    "\u0002\u009d\u009e\u0007>\u0002\u0002\u009e(\u0003\u0002\u0002\u0002",
    "\u009f\u00a0\u0007@\u0002\u0002\u00a0*\u0003\u0002\u0002\u0002\u00a1",
    "\u00a2\u0007#\u0002\u0002\u00a2\u00a3\u0007?\u0002\u0002\u00a3,\u0003",
    "\u0002\u0002\u0002\u00a4\u00a5\u0007#\u0002\u0002\u00a5.\u0003\u0002",
    "\u0002\u0002\u00a6\u00a7\u0007.\u0002\u0002\u00a70\u0003\u0002\u0002",
    "\u0002\u00a8\u00a9\u0007=\u0002\u0002\u00a92\u0003\u0002\u0002\u0002",
    "\u00aa\u00ab\u0007*\u0002\u0002\u00ab4\u0003\u0002\u0002\u0002\u00ac",
    "\u00ad\u0007+\u0002\u0002\u00ad6\u0003\u0002\u0002\u0002\u00ae\u00af",
    "\u0007}\u0002\u0002\u00af8\u0003\u0002\u0002\u0002\u00b0\u00b1\u0007",
    "\u007f\u0002\u0002\u00b1:\u0003\u0002\u0002\u0002\u00b2\u00b3\u0007",
    "]\u0002\u0002\u00b3<\u0003\u0002\u0002\u0002\u00b4\u00b5\u0007_\u0002",
    "\u0002\u00b5>\u0003\u0002\u0002\u0002\u00b6\u00b7\u0007/\u0002\u0002",
    "\u00b7\u00b8\u0007@\u0002\u0002\u00b8@\u0003\u0002\u0002\u0002\u00b9",
    "\u00ba\u0007h\u0002\u0002\u00ba\u00bb\u0007n\u0002\u0002\u00bb\u00bc",
    "\u0007q\u0002\u0002\u00bc\u00bd\u0007c\u0002\u0002\u00bd\u00be\u0007",
    "v\u0002\u0002\u00beB\u0003\u0002\u0002\u0002\u00bf\u00c0\u0007u\u0002",
    "\u0002\u00c0\u00c1\u0007v\u0002\u0002\u00c1\u00c2\u0007t\u0002\u0002",
    "\u00c2\u00c3\u0007k\u0002\u0002\u00c3\u00c4\u0007p\u0002\u0002\u00c4",
    "\u00c5\u0007i\u0002\u0002\u00c5D\u0003\u0002\u0002\u0002\u00c6\u00c7",
    "\u0007d\u0002\u0002\u00c7\u00c8\u0007q\u0002\u0002\u00c8\u00c9\u0007",
    "q\u0002\u0002\u00c9\u00ca\u0007n\u0002\u0002\u00caF\u0003\u0002\u0002",
    "\u0002\u00cb\u00cc\u0007p\u0002\u0002\u00cc\u00cd\u0007w\u0002\u0002",
    "\u00cd\u00ce\u0007n\u0002\u0002\u00ce\u00cf\u0007n\u0002\u0002\u00cf",
    "H\u0003\u0002\u0002\u0002\u00d0\u00d1\u0007e\u0002\u0002\u00d1\u00d2",
    "\u0007j\u0002\u0002\u00d2\u00d3\u0007c\u0002\u0002\u00d3\u00d4\u0007",
    "t\u0002\u0002\u00d4J\u0003\u0002\u0002\u0002\u00d5\u00d7\u0005\u0003",
    "\u0002\u0002\u00d6\u00d5\u0003\u0002\u0002\u0002\u00d7\u00d8\u0003\u0002",
    "\u0002\u0002\u00d8\u00d6\u0003\u0002\u0002\u0002\u00d8\u00d9\u0003\u0002",
    "\u0002\u0002\u00d9\u00de\u0003\u0002\u0002\u0002\u00da\u00db\u0007k",
    "\u0002\u0002\u00db\u00dc\u0007p\u0002\u0002\u00dc\u00de\u0007v\u0002",
    "\u0002\u00dd\u00d6\u0003\u0002\u0002\u0002\u00dd\u00da\u0003\u0002\u0002",
    "\u0002\u00deL\u0003\u0002\u0002\u0002\u0007\u0002Sg\u00d8\u00dd\u0002"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

function JingleLexer(input) {
	antlr4.Lexer.call(this, input);
    this._interp = new antlr4.atn.LexerATNSimulator(this, atn, decisionsToDFA, new antlr4.PredictionContextCache());
    return this;
}

JingleLexer.prototype = Object.create(antlr4.Lexer.prototype);
JingleLexer.prototype.constructor = JingleLexer;

Object.defineProperty(JingleLexer.prototype, "atn", {
        get : function() {
                return atn;
        }
});

JingleLexer.EOF = antlr4.Token.EOF;
JingleLexer.COMMENT = 1;
JingleLexer.VAR = 2;
JingleLexer.CONST = 3;
JingleLexer.DISPLAY = 4;
JingleLexer.IF = 5;
JingleLexer.ELSE = 6;
JingleLexer.FOR = 7;
JingleLexer.TRUE = 8;
JingleLexer.FALSE = 9;
JingleLexer.FUNC = 10;
JingleLexer.LET = 11;
JingleLexer.ASSIGN = 12;
JingleLexer.EQUALS = 13;
JingleLexer.PLUS = 14;
JingleLexer.MINUS = 15;
JingleLexer.MULTIPLY = 16;
JingleLexer.DIVIDE = 17;
JingleLexer.LESSTHAN = 18;
JingleLexer.GREATERTHAN = 19;
JingleLexer.NOTEQUAL = 20;
JingleLexer.BANG = 21;
JingleLexer.COMMA = 22;
JingleLexer.SEMICOLON = 23;
JingleLexer.LBRACKET = 24;
JingleLexer.RBRACKET = 25;
JingleLexer.LBRACE = 26;
JingleLexer.RBRACE = 27;
JingleLexer.LSQRBRACKET = 28;
JingleLexer.RSQRBRACKET = 29;
JingleLexer.ARROW = 30;
JingleLexer.FLOAT = 31;
JingleLexer.STRING = 32;
JingleLexer.BOOLEAN = 33;
JingleLexer.NULL = 34;
JingleLexer.CHAR = 35;
JingleLexer.INT = 36;

JingleLexer.prototype.channelNames = [ "DEFAULT_TOKEN_CHANNEL", "HIDDEN" ];

JingleLexer.prototype.modeNames = [ "DEFAULT_MODE" ];

JingleLexer.prototype.literalNames = [ null, null, "'var'", null, "'display'", 
                                       "'if'", "'else'", "'for'", "'true'", 
                                       "'false'", "'func'", "'let'", "':'", 
                                       "'='", "'+'", "'-'", "'*'", "'/'", 
                                       "'<'", "'>'", "'!='", "'!'", "','", 
                                       "';'", "'('", "')'", "'{'", "'}'", 
                                       "'['", "']'", "'->'", "'float'", 
                                       "'string'", "'bool'", "'null'", "'char'" ];

JingleLexer.prototype.symbolicNames = [ null, "COMMENT", "VAR", "CONST", 
                                        "DISPLAY", "IF", "ELSE", "FOR", 
                                        "TRUE", "FALSE", "FUNC", "LET", 
                                        "ASSIGN", "EQUALS", "PLUS", "MINUS", 
                                        "MULTIPLY", "DIVIDE", "LESSTHAN", 
                                        "GREATERTHAN", "NOTEQUAL", "BANG", 
                                        "COMMA", "SEMICOLON", "LBRACKET", 
                                        "RBRACKET", "LBRACE", "RBRACE", 
                                        "LSQRBRACKET", "RSQRBRACKET", "ARROW", 
                                        "FLOAT", "STRING", "BOOLEAN", "NULL", 
                                        "CHAR", "INT" ];

JingleLexer.prototype.ruleNames = [ "DIGIT", "COMMENT", "VAR", "CONST", 
                                    "DISPLAY", "IF", "ELSE", "FOR", "TRUE", 
                                    "FALSE", "FUNC", "LET", "ASSIGN", "EQUALS", 
                                    "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                                    "LESSTHAN", "GREATERTHAN", "NOTEQUAL", 
                                    "BANG", "COMMA", "SEMICOLON", "LBRACKET", 
                                    "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET", 
                                    "RSQRBRACKET", "ARROW", "FLOAT", "STRING", 
                                    "BOOLEAN", "NULL", "CHAR", "INT" ];

JingleLexer.prototype.grammarFileName = "JingleLexer.g4";



exports.JingleLexer = JingleLexer;

