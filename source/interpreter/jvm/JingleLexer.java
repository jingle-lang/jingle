// Generated from JingleLexer.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JingleLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ENDSTATEMENT=1, SEMICOLONTERMINATE=2, SPEECHMARKS=3, VAR=4, ARRAY=5, CONST=6, 
		DISPLAY=7, RETURN=8, IF=9, THEN=10, AND=11, OR=12, IN=13, ELSE=14, ELIF=15, 
		WHILE=16, FOR=17, TRUE=18, FALSE=19, FUNC=20, CLASS=21, LET=22, TRAIT=23, 
		DEFINE=24, PROTOCOL=25, ENUM=26, IMPORT=27, FROM=28, PACKAGE=29, AS=30, 
		BREAK=31, ABSTRACT=32, SELECT=33, ASSIGN=34, EQUALS=35, EQEQ=36, NOTEQUAL=37, 
		LTEQUALS=38, GTEQUALS=39, PLUS=40, MINUS=41, MULTIPLY=42, DIVIDE=43, LESSTHAN=44, 
		GREATERTHAN=45, BANG=46, POWER=47, MODULUS=48, VERTICAL=49, ORSYMBOL=50, 
		HASH=51, AMBERSAND=52, ANDSYMBOL=53, COMMA=54, LBRACKET=55, RBRACKET=56, 
		LBRACE=57, RBRACE=58, LSQRBRACKET=59, RSQRBRACKET=60, ARROW=61, COLON=62, 
		DOT=63, ELLIPSIS=64, PLUSPLUS=65, MINUSMINUS=66, FLOAT=67, STRING=68, 
		BOOLEAN=69, NULL=70, CHAR=71, INT=72, COMMENT=73, TERMINATOR=74, IDENTIFIER=75, 
		BINARY_OP=76, INT_LIT=77, FLOAT_LIT=78, STRING_LIT=79, RUNE_LIT=80, LITTLE_U_VALUE=81, 
		BIG_U_VALUE=82;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", "VAR", "ARRAY", 
			"CONST", "DISPLAY", "RETURN", "IF", "THEN", "AND", "OR", "IN", "ELSE", 
			"ELIF", "WHILE", "FOR", "TRUE", "FALSE", "FUNC", "CLASS", "LET", "TRAIT", 
			"DEFINE", "PROTOCOL", "ENUM", "IMPORT", "FROM", "PACKAGE", "AS", "BREAK", 
			"ABSTRACT", "SELECT", "ASSIGN", "EQUALS", "EQEQ", "NOTEQUAL", "LTEQUALS", 
			"GTEQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", 
			"BANG", "POWER", "MODULUS", "VERTICAL", "ORSYMBOL", "HASH", "AMBERSAND", 
			"ANDSYMBOL", "COMMA", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET", 
			"RSQRBRACKET", "ARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS", 
			"FLOAT", "STRING", "BOOLEAN", "NULL", "CHAR", "INT", "SEMICOLON", "NEWLINE", 
			"ID", "DIGIT_CONT", "HEXDIGIT", "BINARY", "WHITESPACE", "UNICODE_WS", 
			"COMMENT", "TERMINATOR", "IDENTIFIER", "BINARY_OP", "REL_OP", "ADD_OP", 
			"MUL_OP", "UNARY_OP", "INT_LIT", "DECIMAL_LIT", "OCTAL_LIT", "HEX_LIT", 
			"FLOAT_LIT", "DECIMALS", "STRING_LIT", "RAW_STRING_LIT", "INTERPRETED_STRING_LIT", 
			"RUNE_LIT", "UNICODE_VALUE", "BYTE_VALUE", "OCTAL_BYTE_VALUE", "HEX_BYTE_VALUE", 
			"LITTLE_U_VALUE", "BIG_U_VALUE", "ESCAPED_CHAR", "EXPONENT", "DECIMAL_DIGIT", 
			"LETTER", "OCTAL_DIGIT", "HEX_DIGIT", "UNICODE_CHAR", "UNICODE_LETTER", 
			"UNICODE_DIGIT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'\"'", "'var'", "'array'", null, "'display'", "'return'", 
			"'if'", "'then'", "'and'", "'or'", "'in'", "'else'", "'elif'", "'while'", 
			"'for'", "'true'", "'false'", null, "'class'", "'let'", "'trait'", "'def'", 
			"'protocol'", "'enum'", "'import'", "'from'", "'package'", "'as'", "'break'", 
			"'abstract'", "'select'", "':='", "'='", "'=='", "'!='", "'<='", "'>='", 
			"'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'!'", "'^'", "'%'", "'|'", 
			"'||'", "'#'", "'&'", "'&&'", "','", "'('", "')'", "'{'", "'}'", "'['", 
			"']'", "'->'", "':'", "'.'", "'...'", "'++'", "'--'", "'float'", "'string'", 
			"'bool'", "'null'", "'char'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", "VAR", "ARRAY", 
			"CONST", "DISPLAY", "RETURN", "IF", "THEN", "AND", "OR", "IN", "ELSE", 
			"ELIF", "WHILE", "FOR", "TRUE", "FALSE", "FUNC", "CLASS", "LET", "TRAIT", 
			"DEFINE", "PROTOCOL", "ENUM", "IMPORT", "FROM", "PACKAGE", "AS", "BREAK", 
			"ABSTRACT", "SELECT", "ASSIGN", "EQUALS", "EQEQ", "NOTEQUAL", "LTEQUALS", 
			"GTEQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", 
			"BANG", "POWER", "MODULUS", "VERTICAL", "ORSYMBOL", "HASH", "AMBERSAND", 
			"ANDSYMBOL", "COMMA", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET", 
			"RSQRBRACKET", "ARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS", 
			"FLOAT", "STRING", "BOOLEAN", "NULL", "CHAR", "INT", "COMMENT", "TERMINATOR", 
			"IDENTIFIER", "BINARY_OP", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "RUNE_LIT", 
			"LITTLE_U_VALUE", "BIG_U_VALUE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public JingleLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "JingleLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2T\u0326\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4"+
		"`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4h\th\4i\ti\4j\tj\4k\t"+
		"k\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4q\tq\4r\tr\3\2\7\2\u00e7\n\2\f\2\16\2"+
		"\u00ea\13\2\3\2\6\2\u00ed\n\2\r\2\16\2\u00ee\5\2\u00f1\n\2\3\3\3\3\7\3"+
		"\u00f5\n\3\f\3\16\3\u00f8\13\3\3\3\6\3\u00fb\n\3\r\3\16\3\u00fc\5\3\u00ff"+
		"\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u011b\n\7\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13"+
		"\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3"+
		"\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3"+
		"\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3"+
		"\25\3\25\5\25\u016d\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27"+
		"\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34"+
		"\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36"+
		"\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!"+
		"\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3"+
		"\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60"+
		"\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66"+
		"\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3@\3@\3"+
		"A\3A\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3"+
		"F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3H\3H\3H\3H\3H\3I\6I\u0229\nI\rI\16I\u022a"+
		"\3I\3I\3I\5I\u0230\nI\3J\3J\3K\3K\3K\5K\u0237\nK\3L\6L\u023a\nL\rL\16"+
		"L\u023b\3M\3M\3N\3N\3O\3O\3P\6P\u0245\nP\rP\16P\u0246\3P\3P\3Q\3Q\3Q\3"+
		"Q\3R\3R\3R\3R\7R\u0253\nR\fR\16R\u0256\13R\3R\3R\3S\6S\u025b\nS\rS\16"+
		"S\u025c\3S\3S\3T\3T\3T\7T\u0264\nT\fT\16T\u0267\13T\3U\3U\3U\3U\3U\3U"+
		"\3U\5U\u0270\nU\3V\3V\3V\3V\3V\3V\3V\5V\u0279\nV\3W\3W\5W\u027d\nW\3X"+
		"\3X\3X\5X\u0282\nX\3Y\3Y\3Y\3Y\3Y\3Y\5Y\u028a\nY\3Z\3Z\3Z\5Z\u028f\nZ"+
		"\3[\3[\7[\u0293\n[\f[\16[\u0296\13[\3\\\3\\\7\\\u029a\n\\\f\\\16\\\u029d"+
		"\13\\\3]\3]\3]\6]\u02a2\n]\r]\16]\u02a3\3^\3^\3^\5^\u02a9\n^\3^\5^\u02ac"+
		"\n^\3^\3^\3^\3^\3^\3^\5^\u02b4\n^\5^\u02b6\n^\3_\6_\u02b9\n_\r_\16_\u02ba"+
		"\3`\3`\5`\u02bf\n`\3a\3a\3a\3a\7a\u02c5\na\fa\16a\u02c8\13a\3a\3a\3b\3"+
		"b\3b\3b\3b\7b\u02d1\nb\fb\16b\u02d4\13b\3b\3b\3c\3c\3c\5c\u02db\nc\3c"+
		"\3c\3d\3d\3d\3d\5d\u02e3\nd\3e\3e\5e\u02e7\ne\3f\3f\3f\3f\3f\3g\3g\3g"+
		"\3g\3g\3h\3h\3h\3h\3h\3h\3h\3h\3i\3i\3i\3i\3i\3i\3i\3i\3i\3i\3i\3i\3j"+
		"\3j\3j\3k\3k\3k\3k\5k\u030e\nk\3k\5k\u0311\nk\3k\3k\3l\3l\3m\3m\5m\u0319"+
		"\nm\3n\3n\3o\3o\3p\3p\3q\5q\u0322\nq\3r\5r\u0325\nr\4\u02c6\u02d2\2s\3"+
		"\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37"+
		"\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37="+
		" ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9"+
		"q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008f"+
		"I\u0091J\u0093\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1"+
		"\2\u00a3K\u00a5L\u00a7M\u00a9N\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3O"+
		"\u00b5\2\u00b7\2\u00b9\2\u00bbP\u00bd\2\u00bfQ\u00c1\2\u00c3\2\u00c5R"+
		"\u00c7\2\u00c9\2\u00cb\2\u00cd\2\u00cfS\u00d1T\u00d3\2\u00d5\2\u00d7\2"+
		"\u00d9\2\u00db\2\u00dd\2\u00df\2\u00e1\2\u00e3\2\3\2\25\4\2\f\f\17\17"+
		"\4\2C\\c|\4\2\62;aa\6\2\62;CHaach\4\2\62\63aa\5\2\13\f\17\17\"\"\f\2\13"+
		"\17\"\"\u0087\u0087\u00a2\u00a2\u1682\u1682\u2002\u200c\u202a\u202b\u2031"+
		"\u2031\u2061\u2061\u3002\u3002\3\2\63;\4\2ZZzz\4\2bb\u0080\u0080\13\2"+
		"$$))^^cdhhppttvvxx\4\2GGgg\4\2--//\3\2\62;\3\2\629\5\2\62;CHch\3\2\f\f"+
		"\u0102\2C\\c|\u00ac\u00ac\u00b7\u00b7\u00bc\u00bc\u00c2\u00d8\u00da\u00f8"+
		"\u00fa\u0221\u0224\u0235\u0252\u02af\u02b2\u02ba\u02bd\u02c3\u02d2\u02d3"+
		"\u02e2\u02e6\u02f0\u02f0\u037c\u037c\u0388\u0388\u038a\u038c\u038e\u038e"+
		"\u0390\u03a3\u03a5\u03d0\u03d2\u03d9\u03dc\u03f5\u0402\u0483\u048e\u04c6"+
		"\u04c9\u04ca\u04cd\u04ce\u04d2\u04f7\u04fa\u04fb\u0533\u0558\u055b\u055b"+
		"\u0563\u0589\u05d2\u05ec\u05f2\u05f4\u0623\u063c\u0642\u064c\u0673\u06d5"+
		"\u06d7\u06d7\u06e7\u06e8\u06fc\u06fe\u0712\u0712\u0714\u072e\u0782\u07a7"+
		"\u0907\u093b\u093f\u093f\u0952\u0952\u095a\u0963\u0987\u098e\u0991\u0992"+
		"\u0995\u09aa\u09ac\u09b2\u09b4\u09b4\u09b8\u09bb\u09de\u09df\u09e1\u09e3"+
		"\u09f2\u09f3\u0a07\u0a0c\u0a11\u0a12\u0a15\u0a2a\u0a2c\u0a32\u0a34\u0a35"+
		"\u0a37\u0a38\u0a3a\u0a3b\u0a5b\u0a5e\u0a60\u0a60\u0a74\u0a76\u0a87\u0a8d"+
		"\u0a8f\u0a8f\u0a91\u0a93\u0a95\u0aaa\u0aac\u0ab2\u0ab4\u0ab5\u0ab7\u0abb"+
		"\u0abf\u0abf\u0ad2\u0ad2\u0ae2\u0ae2\u0b07\u0b0e\u0b11\u0b12\u0b15\u0b2a"+
		"\u0b2c\u0b32\u0b34\u0b35\u0b38\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f\u0b61\u0b63"+
		"\u0b87\u0b8c\u0b90\u0b92\u0b94\u0b97\u0b9b\u0b9c\u0b9e\u0b9e\u0ba0\u0ba1"+
		"\u0ba5\u0ba6\u0baa\u0bac\u0bb0\u0bb7\u0bb9\u0bbb\u0c07\u0c0e\u0c10\u0c12"+
		"\u0c14\u0c2a\u0c2c\u0c35\u0c37\u0c3b\u0c62\u0c63\u0c87\u0c8e\u0c90\u0c92"+
		"\u0c94\u0caa\u0cac\u0cb5\u0cb7\u0cbb\u0ce0\u0ce0\u0ce2\u0ce3\u0d07\u0d0e"+
		"\u0d10\u0d12\u0d14\u0d2a\u0d2c\u0d3b\u0d62\u0d63\u0d87\u0d98\u0d9c\u0db3"+
		"\u0db5\u0dbd\u0dbf\u0dbf\u0dc2\u0dc8\u0e03\u0e32\u0e34\u0e35\u0e42\u0e48"+
		"\u0e83\u0e84\u0e86\u0e86\u0e89\u0e8a\u0e8c\u0e8c\u0e8f\u0e8f\u0e96\u0e99"+
		"\u0e9b\u0ea1\u0ea3\u0ea5\u0ea7\u0ea7\u0ea9\u0ea9\u0eac\u0ead\u0eaf\u0eb2"+
		"\u0eb4\u0eb5\u0ebf\u0ec6\u0ec8\u0ec8\u0ede\u0edf\u0f02\u0f02\u0f42\u0f6c"+
		"\u0f8a\u0f8d\u1002\u1023\u1025\u1029\u102b\u102c\u1052\u1057\u10a2\u10c7"+
		"\u10d2\u10f8\u1102\u115b\u1161\u11a4\u11aa\u11fb\u1202\u1208\u120a\u1248"+
		"\u124a\u124a\u124c\u124f\u1252\u1258\u125a\u125a\u125c\u125f\u1262\u1288"+
		"\u128a\u128a\u128c\u128f\u1292\u12b0\u12b2\u12b2\u12b4\u12b7\u12ba\u12c0"+
		"\u12c2\u12c2\u12c4\u12c7\u12ca\u12d0\u12d2\u12d8\u12da\u12f0\u12f2\u1310"+
		"\u1312\u1312\u1314\u1317\u131a\u1320\u1322\u1348\u134a\u135c\u13a2\u13f6"+
		"\u1403\u1678\u1683\u169c\u16a2\u16ec\u1782\u17b5\u1822\u1879\u1882\u18aa"+
		"\u1e02\u1e9d\u1ea2\u1efb\u1f02\u1f17\u1f1a\u1f1f\u1f22\u1f47\u1f4a\u1f4f"+
		"\u1f52\u1f59\u1f5b\u1f5b\u1f5d\u1f5d\u1f5f\u1f5f\u1f61\u1f7f\u1f82\u1fb6"+
		"\u1fb8\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8\u1fce\u1fd2\u1fd5\u1fd8\u1fdd"+
		"\u1fe2\u1fee\u1ff4\u1ff6\u1ff8\u1ffe\u2081\u2081\u2104\u2104\u2109\u2109"+
		"\u210c\u2115\u2117\u2117\u211b\u211f\u2126\u2126\u2128\u2128\u212a\u212a"+
		"\u212c\u212f\u2131\u2133\u2135\u213b\u2162\u2185\u3007\u3009\u3023\u302b"+
		"\u3033\u3037\u303a\u303c\u3043\u3096\u309f\u30a0\u30a3\u30fc\u30fe\u3100"+
		"\u3107\u312e\u3133\u3190\u31a2\u31b9\u3402\u4db7\u4e02\u9fa7\ua002\ua48e"+
		"\uac02\uac02\ud7a5\ud7a5\uf902\ufa2f\ufb02\ufb08\ufb15\ufb19\ufb1f\ufb1f"+
		"\ufb21\ufb2a\ufb2c\ufb38\ufb3a\ufb3e\ufb40\ufb40\ufb42\ufb43\ufb45\ufb46"+
		"\ufb48\ufbb3\ufbd5\ufd3f\ufd52\ufd91\ufd94\ufdc9\ufdf2\ufdfd\ufe72\ufe74"+
		"\ufe76\ufe76\ufe78\ufefe\uff23\uff3c\uff43\uff5c\uff68\uffc0\uffc4\uffc9"+
		"\uffcc\uffd1\uffd4\uffd9\uffdc\uffde\26\2\62;\u0662\u066b\u06f2\u06fb"+
		"\u0968\u0971\u09e8\u09f1\u0a68\u0a71\u0ae8\u0af1\u0b68\u0b71\u0be9\u0bf1"+
		"\u0c68\u0c71\u0ce8\u0cf1\u0d68\u0d71\u0e52\u0e5b\u0ed2\u0edb\u0f22\u0f2b"+
		"\u1042\u104b\u136b\u1373\u17e2\u17eb\u1812\u181b\uff12\uff1b\2\u0349\2"+
		"\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2"+
		"\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2"+
		"\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2"+
		"\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2"+
		"\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2"+
		"\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2"+
		"\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U"+
		"\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2"+
		"\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2"+
		"\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{"+
		"\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085"+
		"\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2"+
		"\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7"+
		"\3\2\2\2\2\u00a9\3\2\2\2\2\u00b3\3\2\2\2\2\u00bb\3\2\2\2\2\u00bf\3\2\2"+
		"\2\2\u00c5\3\2\2\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2\2\3\u00f0\3\2\2\2\5\u00fe"+
		"\3\2\2\2\7\u0100\3\2\2\2\t\u0102\3\2\2\2\13\u0106\3\2\2\2\r\u011a\3\2"+
		"\2\2\17\u011c\3\2\2\2\21\u0124\3\2\2\2\23\u012b\3\2\2\2\25\u012e\3\2\2"+
		"\2\27\u0133\3\2\2\2\31\u0137\3\2\2\2\33\u013a\3\2\2\2\35\u013d\3\2\2\2"+
		"\37\u0142\3\2\2\2!\u0147\3\2\2\2#\u014d\3\2\2\2%\u0151\3\2\2\2\'\u0156"+
		"\3\2\2\2)\u016c\3\2\2\2+\u016e\3\2\2\2-\u0174\3\2\2\2/\u0178\3\2\2\2\61"+
		"\u017e\3\2\2\2\63\u0182\3\2\2\2\65\u018b\3\2\2\2\67\u0190\3\2\2\29\u0197"+
		"\3\2\2\2;\u019c\3\2\2\2=\u01a4\3\2\2\2?\u01a7\3\2\2\2A\u01ad\3\2\2\2C"+
		"\u01b6\3\2\2\2E\u01bd\3\2\2\2G\u01c0\3\2\2\2I\u01c2\3\2\2\2K\u01c5\3\2"+
		"\2\2M\u01c8\3\2\2\2O\u01cb\3\2\2\2Q\u01ce\3\2\2\2S\u01d0\3\2\2\2U\u01d2"+
		"\3\2\2\2W\u01d4\3\2\2\2Y\u01d6\3\2\2\2[\u01d8\3\2\2\2]\u01da\3\2\2\2_"+
		"\u01dc\3\2\2\2a\u01de\3\2\2\2c\u01e0\3\2\2\2e\u01e2\3\2\2\2g\u01e5\3\2"+
		"\2\2i\u01e7\3\2\2\2k\u01e9\3\2\2\2m\u01ec\3\2\2\2o\u01ee\3\2\2\2q\u01f0"+
		"\3\2\2\2s\u01f2\3\2\2\2u\u01f4\3\2\2\2w\u01f6\3\2\2\2y\u01f8\3\2\2\2{"+
		"\u01fa\3\2\2\2}\u01fd\3\2\2\2\177\u01ff\3\2\2\2\u0081\u0201\3\2\2\2\u0083"+
		"\u0205\3\2\2\2\u0085\u0208\3\2\2\2\u0087\u020b\3\2\2\2\u0089\u0211\3\2"+
		"\2\2\u008b\u0218\3\2\2\2\u008d\u021d\3\2\2\2\u008f\u0222\3\2\2\2\u0091"+
		"\u022f\3\2\2\2\u0093\u0231\3\2\2\2\u0095\u0236\3\2\2\2\u0097\u0239\3\2"+
		"\2\2\u0099\u023d\3\2\2\2\u009b\u023f\3\2\2\2\u009d\u0241\3\2\2\2\u009f"+
		"\u0244\3\2\2\2\u00a1\u024a\3\2\2\2\u00a3\u024e\3\2\2\2\u00a5\u025a\3\2"+
		"\2\2\u00a7\u0260\3\2\2\2\u00a9\u026f\3\2\2\2\u00ab\u0278\3\2\2\2\u00ad"+
		"\u027c\3\2\2\2\u00af\u0281\3\2\2\2\u00b1\u0289\3\2\2\2\u00b3\u028e\3\2"+
		"\2\2\u00b5\u0290\3\2\2\2\u00b7\u0297\3\2\2\2\u00b9\u029e\3\2\2\2\u00bb"+
		"\u02b5\3\2\2\2\u00bd\u02b8\3\2\2\2\u00bf\u02be\3\2\2\2\u00c1\u02c0\3\2"+
		"\2\2\u00c3\u02cb\3\2\2\2\u00c5\u02d7\3\2\2\2\u00c7\u02e2\3\2\2\2\u00c9"+
		"\u02e6\3\2\2\2\u00cb\u02e8\3\2\2\2\u00cd\u02ed\3\2\2\2\u00cf\u02f2\3\2"+
		"\2\2\u00d1\u02fa\3\2\2\2\u00d3\u0306\3\2\2\2\u00d5\u030d\3\2\2\2\u00d7"+
		"\u0314\3\2\2\2\u00d9\u0318\3\2\2\2\u00db\u031a\3\2\2\2\u00dd\u031c\3\2"+
		"\2\2\u00df\u031e\3\2\2\2\u00e1\u0321\3\2\2\2\u00e3\u0324\3\2\2\2\u00e5"+
		"\u00e7\5\u0095K\2\u00e6\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6"+
		"\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00f1\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb"+
		"\u00ed\5\u0095K\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ec"+
		"\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1\3\2\2\2\u00f0\u00e8\3\2\2\2\u00f0"+
		"\u00ec\3\2\2\2\u00f1\4\3\2\2\2\u00f2\u00f6\5\u0093J\2\u00f3\u00f5\5\u0095"+
		"K\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6"+
		"\u00f7\3\2\2\2\u00f7\u00ff\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fb\5\u0095"+
		"K\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc"+
		"\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00f2\3\2\2\2\u00fe\u00fa\3\2"+
		"\2\2\u00ff\6\3\2\2\2\u0100\u0101\7$\2\2\u0101\b\3\2\2\2\u0102\u0103\7"+
		"x\2\2\u0103\u0104\7c\2\2\u0104\u0105\7t\2\2\u0105\n\3\2\2\2\u0106\u0107"+
		"\7c\2\2\u0107\u0108\7t\2\2\u0108\u0109\7t\2\2\u0109\u010a\7c\2\2\u010a"+
		"\u010b\7{\2\2\u010b\f\3\2\2\2\u010c\u010d\7e\2\2\u010d\u010e\7q\2\2\u010e"+
		"\u010f\7p\2\2\u010f\u0110\7u\2\2\u0110\u011b\7v\2\2\u0111\u011b\13\2\2"+
		"\2\u0112\u0113\7e\2\2\u0113\u0114\7q\2\2\u0114\u0115\7p\2\2\u0115\u0116"+
		"\7u\2\2\u0116\u0117\7v\2\2\u0117\u0118\7c\2\2\u0118\u0119\7p\2\2\u0119"+
		"\u011b\7v\2\2\u011a\u010c\3\2\2\2\u011a\u0111\3\2\2\2\u011a\u0112\3\2"+
		"\2\2\u011b\16\3\2\2\2\u011c\u011d\7f\2\2\u011d\u011e\7k\2\2\u011e\u011f"+
		"\7u\2\2\u011f\u0120\7r\2\2\u0120\u0121\7n\2\2\u0121\u0122\7c\2\2\u0122"+
		"\u0123\7{\2\2\u0123\20\3\2\2\2\u0124\u0125\7t\2\2\u0125\u0126\7g\2\2\u0126"+
		"\u0127\7v\2\2\u0127\u0128\7w\2\2\u0128\u0129\7t\2\2\u0129\u012a\7p\2\2"+
		"\u012a\22\3\2\2\2\u012b\u012c\7k\2\2\u012c\u012d\7h\2\2\u012d\24\3\2\2"+
		"\2\u012e\u012f\7v\2\2\u012f\u0130\7j\2\2\u0130\u0131\7g\2\2\u0131\u0132"+
		"\7p\2\2\u0132\26\3\2\2\2\u0133\u0134\7c\2\2\u0134\u0135\7p\2\2\u0135\u0136"+
		"\7f\2\2\u0136\30\3\2\2\2\u0137\u0138\7q\2\2\u0138\u0139\7t\2\2\u0139\32"+
		"\3\2\2\2\u013a\u013b\7k\2\2\u013b\u013c\7p\2\2\u013c\34\3\2\2\2\u013d"+
		"\u013e\7g\2\2\u013e\u013f\7n\2\2\u013f\u0140\7u\2\2\u0140\u0141\7g\2\2"+
		"\u0141\36\3\2\2\2\u0142\u0143\7g\2\2\u0143\u0144\7n\2\2\u0144\u0145\7"+
		"k\2\2\u0145\u0146\7h\2\2\u0146 \3\2\2\2\u0147\u0148\7y\2\2\u0148\u0149"+
		"\7j\2\2\u0149\u014a\7k\2\2\u014a\u014b\7n\2\2\u014b\u014c\7g\2\2\u014c"+
		"\"\3\2\2\2\u014d\u014e\7h\2\2\u014e\u014f\7q\2\2\u014f\u0150\7t\2\2\u0150"+
		"$\3\2\2\2\u0151\u0152\7v\2\2\u0152\u0153\7t\2\2\u0153\u0154\7w\2\2\u0154"+
		"\u0155\7g\2\2\u0155&\3\2\2\2\u0156\u0157\7h\2\2\u0157\u0158\7c\2\2\u0158"+
		"\u0159\7n\2\2\u0159\u015a\7u\2\2\u015a\u015b\7g\2\2\u015b(\3\2\2\2\u015c"+
		"\u015d\7h\2\2\u015d\u015e\7w\2\2\u015e\u015f\7p\2\2\u015f\u0160\7e\2\2"+
		"\u0160\u0161\7v\2\2\u0161\u0162\7k\2\2\u0162\u0163\7q\2\2\u0163\u016d"+
		"\7p\2\2\u0164\u016d\13\2\2\2\u0165\u0166\7h\2\2\u0166\u0167\7w\2\2\u0167"+
		"\u0168\7p\2\2\u0168\u016d\7e\2\2\u0169\u016d\13\2\2\2\u016a\u016b\7h\2"+
		"\2\u016b\u016d\7p\2\2\u016c\u015c\3\2\2\2\u016c\u0164\3\2\2\2\u016c\u0165"+
		"\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016d*\3\2\2\2\u016e"+
		"\u016f\7e\2\2\u016f\u0170\7n\2\2\u0170\u0171\7c\2\2\u0171\u0172\7u\2\2"+
		"\u0172\u0173\7u\2\2\u0173,\3\2\2\2\u0174\u0175\7n\2\2\u0175\u0176\7g\2"+
		"\2\u0176\u0177\7v\2\2\u0177.\3\2\2\2\u0178\u0179\7v\2\2\u0179\u017a\7"+
		"t\2\2\u017a\u017b\7c\2\2\u017b\u017c\7k\2\2\u017c\u017d\7v\2\2\u017d\60"+
		"\3\2\2\2\u017e\u017f\7f\2\2\u017f\u0180\7g\2\2\u0180\u0181\7h\2\2\u0181"+
		"\62\3\2\2\2\u0182\u0183\7r\2\2\u0183\u0184\7t\2\2\u0184\u0185\7q\2\2\u0185"+
		"\u0186\7v\2\2\u0186\u0187\7q\2\2\u0187\u0188\7e\2\2\u0188\u0189\7q\2\2"+
		"\u0189\u018a\7n\2\2\u018a\64\3\2\2\2\u018b\u018c\7g\2\2\u018c\u018d\7"+
		"p\2\2\u018d\u018e\7w\2\2\u018e\u018f\7o\2\2\u018f\66\3\2\2\2\u0190\u0191"+
		"\7k\2\2\u0191\u0192\7o\2\2\u0192\u0193\7r\2\2\u0193\u0194\7q\2\2\u0194"+
		"\u0195\7t\2\2\u0195\u0196\7v\2\2\u01968\3\2\2\2\u0197\u0198\7h\2\2\u0198"+
		"\u0199\7t\2\2\u0199\u019a\7q\2\2\u019a\u019b\7o\2\2\u019b:\3\2\2\2\u019c"+
		"\u019d\7r\2\2\u019d\u019e\7c\2\2\u019e\u019f\7e\2\2\u019f\u01a0\7m\2\2"+
		"\u01a0\u01a1\7c\2\2\u01a1\u01a2\7i\2\2\u01a2\u01a3\7g\2\2\u01a3<\3\2\2"+
		"\2\u01a4\u01a5\7c\2\2\u01a5\u01a6\7u\2\2\u01a6>\3\2\2\2\u01a7\u01a8\7"+
		"d\2\2\u01a8\u01a9\7t\2\2\u01a9\u01aa\7g\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac"+
		"\7m\2\2\u01ac@\3\2\2\2\u01ad\u01ae\7c\2\2\u01ae\u01af\7d\2\2\u01af\u01b0"+
		"\7u\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2\7t\2\2\u01b2\u01b3\7c\2\2\u01b3"+
		"\u01b4\7e\2\2\u01b4\u01b5\7v\2\2\u01b5B\3\2\2\2\u01b6\u01b7\7u\2\2\u01b7"+
		"\u01b8\7g\2\2\u01b8\u01b9\7n\2\2\u01b9\u01ba\7g\2\2\u01ba\u01bb\7e\2\2"+
		"\u01bb\u01bc\7v\2\2\u01bcD\3\2\2\2\u01bd\u01be\7<\2\2\u01be\u01bf\7?\2"+
		"\2\u01bfF\3\2\2\2\u01c0\u01c1\7?\2\2\u01c1H\3\2\2\2\u01c2\u01c3\7?\2\2"+
		"\u01c3\u01c4\7?\2\2\u01c4J\3\2\2\2\u01c5\u01c6\7#\2\2\u01c6\u01c7\7?\2"+
		"\2\u01c7L\3\2\2\2\u01c8\u01c9\7>\2\2\u01c9\u01ca\7?\2\2\u01caN\3\2\2\2"+
		"\u01cb\u01cc\7@\2\2\u01cc\u01cd\7?\2\2\u01cdP\3\2\2\2\u01ce\u01cf\7-\2"+
		"\2\u01cfR\3\2\2\2\u01d0\u01d1\7/\2\2\u01d1T\3\2\2\2\u01d2\u01d3\7,\2\2"+
		"\u01d3V\3\2\2\2\u01d4\u01d5\7\61\2\2\u01d5X\3\2\2\2\u01d6\u01d7\7>\2\2"+
		"\u01d7Z\3\2\2\2\u01d8\u01d9\7@\2\2\u01d9\\\3\2\2\2\u01da\u01db\7#\2\2"+
		"\u01db^\3\2\2\2\u01dc\u01dd\7`\2\2\u01dd`\3\2\2\2\u01de\u01df\7\'\2\2"+
		"\u01dfb\3\2\2\2\u01e0\u01e1\7~\2\2\u01e1d\3\2\2\2\u01e2\u01e3\7~\2\2\u01e3"+
		"\u01e4\7~\2\2\u01e4f\3\2\2\2\u01e5\u01e6\7%\2\2\u01e6h\3\2\2\2\u01e7\u01e8"+
		"\7(\2\2\u01e8j\3\2\2\2\u01e9\u01ea\7(\2\2\u01ea\u01eb\7(\2\2\u01ebl\3"+
		"\2\2\2\u01ec\u01ed\7.\2\2\u01edn\3\2\2\2\u01ee\u01ef\7*\2\2\u01efp\3\2"+
		"\2\2\u01f0\u01f1\7+\2\2\u01f1r\3\2\2\2\u01f2\u01f3\7}\2\2\u01f3t\3\2\2"+
		"\2\u01f4\u01f5\7\177\2\2\u01f5v\3\2\2\2\u01f6\u01f7\7]\2\2\u01f7x\3\2"+
		"\2\2\u01f8\u01f9\7_\2\2\u01f9z\3\2\2\2\u01fa\u01fb\7/\2\2\u01fb\u01fc"+
		"\7@\2\2\u01fc|\3\2\2\2\u01fd\u01fe\7<\2\2\u01fe~\3\2\2\2\u01ff\u0200\7"+
		"\60\2\2\u0200\u0080\3\2\2\2\u0201\u0202\7\60\2\2\u0202\u0203\7\60\2\2"+
		"\u0203\u0204\7\60\2\2\u0204\u0082\3\2\2\2\u0205\u0206\7-\2\2\u0206\u0207"+
		"\7-\2\2\u0207\u0084\3\2\2\2\u0208\u0209\7/\2\2\u0209\u020a\7/\2\2\u020a"+
		"\u0086\3\2\2\2\u020b\u020c\7h\2\2\u020c\u020d\7n\2\2\u020d\u020e\7q\2"+
		"\2\u020e\u020f\7c\2\2\u020f\u0210\7v\2\2\u0210\u0088\3\2\2\2\u0211\u0212"+
		"\7u\2\2\u0212\u0213\7v\2\2\u0213\u0214\7t\2\2\u0214\u0215\7k\2\2\u0215"+
		"\u0216\7p\2\2\u0216\u0217\7i\2\2\u0217\u008a\3\2\2\2\u0218\u0219\7d\2"+
		"\2\u0219\u021a\7q\2\2\u021a\u021b\7q\2\2\u021b\u021c\7n\2\2\u021c\u008c"+
		"\3\2\2\2\u021d\u021e\7p\2\2\u021e\u021f\7w\2\2\u021f\u0220\7n\2\2\u0220"+
		"\u0221\7n\2\2\u0221\u008e\3\2\2\2\u0222\u0223\7e\2\2\u0223\u0224\7j\2"+
		"\2\u0224\u0225\7c\2\2\u0225\u0226\7t\2\2\u0226\u0090\3\2\2\2\u0227\u0229"+
		"\5\u00d7l\2\u0228\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u0228\3\2\2"+
		"\2\u022a\u022b\3\2\2\2\u022b\u0230\3\2\2\2\u022c\u022d\7k\2\2\u022d\u022e"+
		"\7p\2\2\u022e\u0230\7v\2\2\u022f\u0228\3\2\2\2\u022f\u022c\3\2\2\2\u0230"+
		"\u0092\3\2\2\2\u0231\u0232\7=\2\2\u0232\u0094\3\2\2\2\u0233\u0234\7\17"+
		"\2\2\u0234\u0237\7\f\2\2\u0235\u0237\t\2\2\2\u0236\u0233\3\2\2\2\u0236"+
		"\u0235\3\2\2\2\u0237\u0096\3\2\2\2\u0238\u023a\t\3\2\2\u0239\u0238\3\2"+
		"\2\2\u023a\u023b\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c"+
		"\u0098\3\2\2\2\u023d\u023e\t\4\2\2\u023e\u009a\3\2\2\2\u023f\u0240\t\5"+
		"\2\2\u0240\u009c\3\2\2\2\u0241\u0242\t\6\2\2\u0242\u009e\3\2\2\2\u0243"+
		"\u0245\t\7\2\2\u0244\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0244\3\2"+
		"\2\2\u0246\u0247\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u0249\bP\2\2\u0249"+
		"\u00a0\3\2\2\2\u024a\u024b\t\b\2\2\u024b\u024c\3\2\2\2\u024c\u024d\bQ"+
		"\2\2\u024d\u00a2\3\2\2\2\u024e\u024f\7\61\2\2\u024f\u0250\7\61\2\2\u0250"+
		"\u0254\3\2\2\2\u0251\u0253\n\2\2\2\u0252\u0251\3\2\2\2\u0253\u0256\3\2"+
		"\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0257\3\2\2\2\u0256"+
		"\u0254\3\2\2\2\u0257\u0258\bR\3\2\u0258\u00a4\3\2\2\2\u0259\u025b\t\2"+
		"\2\2\u025a\u0259\3\2\2\2\u025b\u025c\3\2\2\2\u025c\u025a\3\2\2\2\u025c"+
		"\u025d\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u025f\bS\2\2\u025f\u00a6\3\2"+
		"\2\2\u0260\u0265\5\u00d9m\2\u0261\u0264\5\u00d9m\2\u0262\u0264\5\u00e3"+
		"r\2\u0263\u0261\3\2\2\2\u0263\u0262\3\2\2\2\u0264\u0267\3\2\2\2\u0265"+
		"\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u00a8\3\2\2\2\u0267\u0265\3\2"+
		"\2\2\u0268\u0270\5\31\r\2\u0269\u0270\5\27\f\2\u026a\u0270\5e\63\2\u026b"+
		"\u0270\5k\66\2\u026c\u0270\5\u00abV\2\u026d\u0270\5\u00adW\2\u026e\u0270"+
		"\5\u00afX\2\u026f\u0268\3\2\2\2\u026f\u0269\3\2\2\2\u026f\u026a\3\2\2"+
		"\2\u026f\u026b\3\2\2\2\u026f\u026c\3\2\2\2\u026f\u026d\3\2\2\2\u026f\u026e"+
		"\3\2\2\2\u0270\u00aa\3\2\2\2\u0271\u0279\5G$\2\u0272\u0279\5I%\2\u0273"+
		"\u0279\5K&\2\u0274\u0279\5Y-\2\u0275\u0279\5M\'\2\u0276\u0279\5[.\2\u0277"+
		"\u0279\5O(\2\u0278\u0271\3\2\2\2\u0278\u0272\3\2\2\2\u0278\u0273\3\2\2"+
		"\2\u0278\u0274\3\2\2\2\u0278\u0275\3\2\2\2\u0278\u0276\3\2\2\2\u0278\u0277"+
		"\3\2\2\2\u0279\u00ac\3\2\2\2\u027a\u027d\5Q)\2\u027b\u027d\5S*\2\u027c"+
		"\u027a\3\2\2\2\u027c\u027b\3\2\2\2\u027d\u00ae\3\2\2\2\u027e\u0282\5U"+
		"+\2\u027f\u0282\5W,\2\u0280\u0282\5a\61\2\u0281\u027e\3\2\2\2\u0281\u027f"+
		"\3\2\2\2\u0281\u0280\3\2\2\2\u0282\u00b0\3\2\2\2\u0283\u028a\5Q)\2\u0284"+
		"\u028a\5S*\2\u0285\u028a\5]/\2\u0286\u028a\5_\60\2\u0287\u028a\5U+\2\u0288"+
		"\u028a\5k\66\2\u0289\u0283\3\2\2\2\u0289\u0284\3\2\2\2\u0289\u0285\3\2"+
		"\2\2\u0289\u0286\3\2\2\2\u0289\u0287\3\2\2\2\u0289\u0288\3\2\2\2\u028a"+
		"\u00b2\3\2\2\2\u028b\u028f\5\u00b5[\2\u028c\u028f\5\u00b7\\\2\u028d\u028f"+
		"\5\u00b9]\2\u028e\u028b\3\2\2\2\u028e\u028c\3\2\2\2\u028e\u028d\3\2\2"+
		"\2\u028f\u00b4\3\2\2\2\u0290\u0294\t\t\2\2\u0291\u0293\5\u00d7l\2\u0292"+
		"\u0291\3\2\2\2\u0293\u0296\3\2\2\2\u0294\u0292\3\2\2\2\u0294\u0295\3\2"+
		"\2\2\u0295\u00b6\3\2\2\2\u0296\u0294\3\2\2\2\u0297\u029b\7\62\2\2\u0298"+
		"\u029a\5\u00dbn\2\u0299\u0298\3\2\2\2\u029a\u029d\3\2\2\2\u029b\u0299"+
		"\3\2\2\2\u029b\u029c\3\2\2\2\u029c\u00b8\3\2\2\2\u029d\u029b\3\2\2\2\u029e"+
		"\u029f\7\62\2\2\u029f\u02a1\t\n\2\2\u02a0\u02a2\5\u00ddo\2\u02a1\u02a0"+
		"\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4"+
		"\u00ba\3\2\2\2\u02a5\u02a6\5\u00bd_\2\u02a6\u02a8\7\60\2\2\u02a7\u02a9"+
		"\5\u00bd_\2\u02a8\u02a7\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02ab\3\2\2"+
		"\2\u02aa\u02ac\5\u00d5k\2\u02ab\u02aa\3\2\2\2\u02ab\u02ac\3\2\2\2\u02ac"+
		"\u02b6\3\2\2\2\u02ad\u02ae\5\u00bd_\2\u02ae\u02af\5\u00d5k\2\u02af\u02b6"+
		"\3\2\2\2\u02b0\u02b1\7\60\2\2\u02b1\u02b3\5\u00bd_\2\u02b2\u02b4\5\u00d5"+
		"k\2\u02b3\u02b2\3\2\2\2\u02b3\u02b4\3\2\2\2\u02b4\u02b6\3\2\2\2\u02b5"+
		"\u02a5\3\2\2\2\u02b5\u02ad\3\2\2\2\u02b5\u02b0\3\2\2\2\u02b6\u00bc\3\2"+
		"\2\2\u02b7\u02b9\5\u00d7l\2\u02b8\u02b7\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba"+
		"\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u00be\3\2\2\2\u02bc\u02bf\5\u00c1"+
		"a\2\u02bd\u02bf\5\u00c3b\2\u02be\u02bc\3\2\2\2\u02be\u02bd\3\2\2\2\u02bf"+
		"\u00c0\3\2\2\2\u02c0\u02c6\7b\2\2\u02c1\u02c5\5\u00dfp\2\u02c2\u02c5\5"+
		"\u0095K\2\u02c3\u02c5\t\13\2\2\u02c4\u02c1\3\2\2\2\u02c4\u02c2\3\2\2\2"+
		"\u02c4\u02c3\3\2\2\2\u02c5\u02c8\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c6\u02c4"+
		"\3\2\2\2\u02c7\u02c9\3\2\2\2\u02c8\u02c6\3\2\2\2\u02c9\u02ca\7b\2\2\u02ca"+
		"\u00c2\3\2\2\2\u02cb\u02d2\7$\2\2\u02cc\u02cd\7^\2\2\u02cd\u02d1\7$\2"+
		"\2\u02ce\u02d1\5\u00c7d\2\u02cf\u02d1\5\u00c9e\2\u02d0\u02cc\3\2\2\2\u02d0"+
		"\u02ce\3\2\2\2\u02d0\u02cf\3\2\2\2\u02d1\u02d4\3\2\2\2\u02d2\u02d3\3\2"+
		"\2\2\u02d2\u02d0\3\2\2\2\u02d3\u02d5\3\2\2\2\u02d4\u02d2\3\2\2\2\u02d5"+
		"\u02d6\7$\2\2\u02d6\u00c4\3\2\2\2\u02d7\u02da\7)\2\2\u02d8\u02db\5\u00c7"+
		"d\2\u02d9\u02db\5\u00c9e\2\u02da\u02d8\3\2\2\2\u02da\u02d9\3\2\2\2\u02db"+
		"\u02dc\3\2\2\2\u02dc\u02dd\7)\2\2\u02dd\u00c6\3\2\2\2\u02de\u02e3\5\u00df"+
		"p\2\u02df\u02e3\5\u00cfh\2\u02e0\u02e3\5\u00d1i\2\u02e1\u02e3\5\u00d3"+
		"j\2\u02e2\u02de\3\2\2\2\u02e2\u02df\3\2\2\2\u02e2\u02e0\3\2\2\2\u02e2"+
		"\u02e1\3\2\2\2\u02e3\u00c8\3\2\2\2\u02e4\u02e7\5\u00cbf\2\u02e5\u02e7"+
		"\5\u00cdg\2\u02e6\u02e4\3\2\2\2\u02e6\u02e5\3\2\2\2\u02e7\u00ca\3\2\2"+
		"\2\u02e8\u02e9\7^\2\2\u02e9\u02ea\5\u00dbn\2\u02ea\u02eb\5\u00dbn\2\u02eb"+
		"\u02ec\5\u00dbn\2\u02ec\u00cc\3\2\2\2\u02ed\u02ee\7^\2\2\u02ee\u02ef\7"+
		"z\2\2\u02ef\u02f0\5\u00ddo\2\u02f0\u02f1\5\u00ddo\2\u02f1\u00ce\3\2\2"+
		"\2\u02f2\u02f3\7^\2\2\u02f3\u02f4\7w\2\2\u02f4\u02f5\3\2\2\2\u02f5\u02f6"+
		"\5\u00ddo\2\u02f6\u02f7\5\u00ddo\2\u02f7\u02f8\5\u00ddo\2\u02f8\u02f9"+
		"\5\u00ddo\2\u02f9\u00d0\3\2\2\2\u02fa\u02fb\7^\2\2\u02fb\u02fc\7W\2\2"+
		"\u02fc\u02fd\3\2\2\2\u02fd\u02fe\5\u00ddo\2\u02fe\u02ff\5\u00ddo\2\u02ff"+
		"\u0300\5\u00ddo\2\u0300\u0301\5\u00ddo\2\u0301\u0302\5\u00ddo\2\u0302"+
		"\u0303\5\u00ddo\2\u0303\u0304\5\u00ddo\2\u0304\u0305\5\u00ddo\2\u0305"+
		"\u00d2\3\2\2\2\u0306\u0307\7^\2\2\u0307\u0308\t\f\2\2\u0308\u00d4\3\2"+
		"\2\2\u0309\u030e\t\r\2\2\u030a\u030b\7g\2\2\u030b\u030c\7z\2\2\u030c\u030e"+
		"\7p\2\2\u030d\u0309\3\2\2\2\u030d\u030a\3\2\2\2\u030e\u0310\3\2\2\2\u030f"+
		"\u0311\t\16\2\2\u0310\u030f\3\2\2\2\u0310\u0311\3\2\2\2\u0311\u0312\3"+
		"\2\2\2\u0312\u0313\5\u00bd_\2\u0313\u00d6\3\2\2\2\u0314\u0315\t\17\2\2"+
		"\u0315\u00d8\3\2\2\2\u0316\u0319\5\u00e1q\2\u0317\u0319\7a\2\2\u0318\u0316"+
		"\3\2\2\2\u0318\u0317\3\2\2\2\u0319\u00da\3\2\2\2\u031a\u031b\t\20\2\2"+
		"\u031b\u00dc\3\2\2\2\u031c\u031d\t\21\2\2\u031d\u00de\3\2\2\2\u031e\u031f"+
		"\n\22\2\2\u031f\u00e0\3\2\2\2\u0320\u0322\t\23\2\2\u0321\u0320\3\2\2\2"+
		"\u0322\u00e2\3\2\2\2\u0323\u0325\t\24\2\2\u0324\u0323\3\2\2\2\u0325\u00e4"+
		"\3\2\2\2/\2\u00e8\u00ee\u00f0\u00f6\u00fc\u00fe\u011a\u016c\u022a\u022f"+
		"\u0236\u023b\u0246\u0254\u025c\u0263\u0265\u026f\u0278\u027c\u0281\u0289"+
		"\u028e\u0294\u029b\u02a3\u02a8\u02ab\u02b3\u02b5\u02ba\u02be\u02c4\u02c6"+
		"\u02d0\u02d2\u02da\u02e2\u02e6\u030d\u0310\u0318\u0321\u0324\4\2\3\2\b"+
		"\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}