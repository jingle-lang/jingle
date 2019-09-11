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
		ENDSTATEMENT=1, COMMENT=2, SPEECHMARKS=3, VAR=4, ARRAY=5, CONST=6, DISPLAY=7, 
		RETURN=8, IF=9, IN=10, ELSE=11, ELIF=12, WHILE=13, FOR=14, TRUE=15, FALSE=16, 
		FUNC=17, CLASS=18, LET=19, TRAIT=20, DEFINE=21, PROTOCOL=22, ENUM=23, 
		IMPORT=24, FROM=25, PACKAGE=26, AS=27, ASSIGN=28, EQUALS=29, PLUS=30, 
		MINUS=31, MULTIPLY=32, DIVIDE=33, LESSTHAN=34, GREATERTHAN=35, NOTEQUAL=36, 
		BANG=37, OR=38, EQEQ=39, HASH=40, AMBERSAND=41, COMMA=42, LBRACKET=43, 
		RBRACKET=44, LBRACE=45, RBRACE=46, LSQRBRACKET=47, RSQRBRACKET=48, ARROW=49, 
		FLOAT=50, STRING=51, BOOLEAN=52, NULL=53, CHAR=54, INT=55;
	public static final int
		COMMENTS=2;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN", "COMMENTS"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SEMICOLON", "NEWLINE", "ID", "DIGIT", "DIGIT_CONT", "HEXDIGIT", "BINARY", 
			"WHITESPACE", "UNICODE_WS", "ENDSTATEMENT", "COMMENT", "SPEECHMARKS", 
			"VAR", "ARRAY", "CONST", "DISPLAY", "RETURN", "IF", "IN", "ELSE", "ELIF", 
			"WHILE", "FOR", "TRUE", "FALSE", "FUNC", "CLASS", "LET", "TRAIT", "DEFINE", 
			"PROTOCOL", "ENUM", "IMPORT", "FROM", "PACKAGE", "AS", "ASSIGN", "EQUALS", 
			"PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", "NOTEQUAL", 
			"BANG", "OR", "EQEQ", "HASH", "AMBERSAND", "COMMA", "LBRACKET", "RBRACKET", 
			"LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET", "ARROW", "FLOAT", "STRING", 
			"BOOLEAN", "NULL", "CHAR", "INT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'##'", "'\"'", "'var'", "'array'", null, "'display'", "'return'", 
			"'if'", "'in'", "'else'", "'elif'", "'while'", "'for'", "'true'", "'false'", 
			null, "'class'", "'let'", "'trait'", "'def'", "'protocol'", "'enum'", 
			"'import'", "'from'", "'package'", "'as'", "':='", "'='", "'+'", "'-'", 
			"'*'", "'/'", "'<'", "'>'", "'!='", "'!'", "'|'", "'=='", "'#'", "'&'", 
			"','", "'('", "')'", "'{'", "'}'", "'['", "']'", "'->'", "'float'", "'string'", 
			"'bool'", "'null'", "'char'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ENDSTATEMENT", "COMMENT", "SPEECHMARKS", "VAR", "ARRAY", "CONST", 
			"DISPLAY", "RETURN", "IF", "IN", "ELSE", "ELIF", "WHILE", "FOR", "TRUE", 
			"FALSE", "FUNC", "CLASS", "LET", "TRAIT", "DEFINE", "PROTOCOL", "ENUM", 
			"IMPORT", "FROM", "PACKAGE", "AS", "ASSIGN", "EQUALS", "PLUS", "MINUS", 
			"MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", "NOTEQUAL", "BANG", 
			"OR", "EQEQ", "HASH", "AMBERSAND", "COMMA", "LBRACKET", "RBRACKET", "LBRACE", 
			"RBRACE", "LSQRBRACKET", "RSQRBRACKET", "ARROW", "FLOAT", "STRING", "BOOLEAN", 
			"NULL", "CHAR", "INT"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29\u01a6\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\3\3\3\3\3\5\3\u0089\n\3\3\4\6\4\u008c"+
		"\n\4\r\4\16\4\u008d\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t\u0099\n\t"+
		"\r\t\16\t\u009a\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\7\13\u00a5\n\13\f\13"+
		"\16\13\u00a8\13\13\3\13\6\13\u00ab\n\13\r\13\16\13\u00ac\5\13\u00af\n"+
		"\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\5\20\u00d0\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25"+
		"\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\3\33\5\33\u0116\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35"+
		"\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 "+
		"\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3"+
		"#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)"+
		"\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62"+
		"\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3"+
		":\3:\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3"+
		"?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3A\6A\u019e\nA\rA\16A\u019f\3A\3A\3A\5A\u01a5"+
		"\nA\2\2B\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\3\27\4\31\5\33\6\35"+
		"\7\37\b!\t#\n%\13\'\f)\r+\16-\17/\20\61\21\63\22\65\23\67\249\25;\26="+
		"\27?\30A\31C\32E\33G\34I\35K\36M\37O Q!S\"U#W$Y%[&]\'_(a)c*e+g,i-k.m/"+
		"o\60q\61s\62u\63w\64y\65{\66}\67\1778\u00819\3\2\n\4\2\f\f\17\17\4\2C"+
		"\\c|\3\2\62;\4\2\62;aa\6\2\62;CHaach\4\2\62\63aa\5\2\13\f\17\17\"\"\f"+
		"\2\13\17\"\"\u0087\u0087\u00a2\u00a2\u1682\u1682\u2002\u200c\u202a\u202b"+
		"\u2031\u2031\u2061\u2061\u3002\u3002\2\u01aa\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3"+
		"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2"+
		"\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2"+
		"U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3"+
		"\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2"+
		"\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2"+
		"{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u0088"+
		"\3\2\2\2\7\u008b\3\2\2\2\t\u008f\3\2\2\2\13\u0091\3\2\2\2\r\u0093\3\2"+
		"\2\2\17\u0095\3\2\2\2\21\u0098\3\2\2\2\23\u009e\3\2\2\2\25\u00ae\3\2\2"+
		"\2\27\u00b0\3\2\2\2\31\u00b5\3\2\2\2\33\u00b7\3\2\2\2\35\u00bb\3\2\2\2"+
		"\37\u00cf\3\2\2\2!\u00d1\3\2\2\2#\u00d9\3\2\2\2%\u00e0\3\2\2\2\'\u00e3"+
		"\3\2\2\2)\u00e6\3\2\2\2+\u00eb\3\2\2\2-\u00f0\3\2\2\2/\u00f6\3\2\2\2\61"+
		"\u00fa\3\2\2\2\63\u00ff\3\2\2\2\65\u0115\3\2\2\2\67\u0117\3\2\2\29\u011d"+
		"\3\2\2\2;\u0121\3\2\2\2=\u0127\3\2\2\2?\u012b\3\2\2\2A\u0134\3\2\2\2C"+
		"\u0139\3\2\2\2E\u0140\3\2\2\2G\u0145\3\2\2\2I\u014d\3\2\2\2K\u0150\3\2"+
		"\2\2M\u0153\3\2\2\2O\u0155\3\2\2\2Q\u0157\3\2\2\2S\u0159\3\2\2\2U\u015b"+
		"\3\2\2\2W\u015d\3\2\2\2Y\u015f\3\2\2\2[\u0161\3\2\2\2]\u0164\3\2\2\2_"+
		"\u0166\3\2\2\2a\u0168\3\2\2\2c\u016b\3\2\2\2e\u016d\3\2\2\2g\u016f\3\2"+
		"\2\2i\u0171\3\2\2\2k\u0173\3\2\2\2m\u0175\3\2\2\2o\u0177\3\2\2\2q\u0179"+
		"\3\2\2\2s\u017b\3\2\2\2u\u017d\3\2\2\2w\u0180\3\2\2\2y\u0186\3\2\2\2{"+
		"\u018d\3\2\2\2}\u0192\3\2\2\2\177\u0197\3\2\2\2\u0081\u01a4\3\2\2\2\u0083"+
		"\u0084\7=\2\2\u0084\4\3\2\2\2\u0085\u0086\7\17\2\2\u0086\u0089\7\f\2\2"+
		"\u0087\u0089\t\2\2\2\u0088\u0085\3\2\2\2\u0088\u0087\3\2\2\2\u0089\6\3"+
		"\2\2\2\u008a\u008c\t\3\2\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d"+
		"\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\b\3\2\2\2\u008f\u0090\t\4\2\2"+
		"\u0090\n\3\2\2\2\u0091\u0092\t\5\2\2\u0092\f\3\2\2\2\u0093\u0094\t\6\2"+
		"\2\u0094\16\3\2\2\2\u0095\u0096\t\7\2\2\u0096\20\3\2\2\2\u0097\u0099\t"+
		"\b\2\2\u0098\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a"+
		"\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\b\t\2\2\u009d\22\3\2\2"+
		"\2\u009e\u009f\t\t\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\b\n\2\2\u00a1\24"+
		"\3\2\2\2\u00a2\u00a6\5\3\2\2\u00a3\u00a5\5\5\3\2\u00a4\u00a3\3\2\2\2\u00a5"+
		"\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00af\3\2"+
		"\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ab\5\5\3\2\u00aa\u00a9\3\2\2\2\u00ab"+
		"\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2"+
		"\2\2\u00ae\u00a2\3\2\2\2\u00ae\u00aa\3\2\2\2\u00af\26\3\2\2\2\u00b0\u00b1"+
		"\7%\2\2\u00b1\u00b2\7%\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\b\f\3\2\u00b4"+
		"\30\3\2\2\2\u00b5\u00b6\7$\2\2\u00b6\32\3\2\2\2\u00b7\u00b8\7x\2\2\u00b8"+
		"\u00b9\7c\2\2\u00b9\u00ba\7t\2\2\u00ba\34\3\2\2\2\u00bb\u00bc\7c\2\2\u00bc"+
		"\u00bd\7t\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0\7{\2\2"+
		"\u00c0\36\3\2\2\2\u00c1\u00c2\7e\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7"+
		"p\2\2\u00c4\u00c5\7u\2\2\u00c5\u00d0\7v\2\2\u00c6\u00d0\13\2\2\2\u00c7"+
		"\u00c8\7e\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7u\2\2"+
		"\u00cb\u00cc\7v\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7p\2\2\u00ce\u00d0"+
		"\7v\2\2\u00cf\u00c1\3\2\2\2\u00cf\u00c6\3\2\2\2\u00cf\u00c7\3\2\2\2\u00d0"+
		" \3\2\2\2\u00d1\u00d2\7f\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7u\2\2\u00d4"+
		"\u00d5\7r\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7{\2\2"+
		"\u00d8\"\3\2\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7v"+
		"\2\2\u00dc\u00dd\7w\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7p\2\2\u00df$\3"+
		"\2\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7h\2\2\u00e2&\3\2\2\2\u00e3\u00e4"+
		"\7k\2\2\u00e4\u00e5\7p\2\2\u00e5(\3\2\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8"+
		"\7n\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea\7g\2\2\u00ea*\3\2\2\2\u00eb\u00ec"+
		"\7g\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7h\2\2\u00ef"+
		",\3\2\2\2\u00f0\u00f1\7y\2\2\u00f1\u00f2\7j\2\2\u00f2\u00f3\7k\2\2\u00f3"+
		"\u00f4\7n\2\2\u00f4\u00f5\7g\2\2\u00f5.\3\2\2\2\u00f6\u00f7\7h\2\2\u00f7"+
		"\u00f8\7q\2\2\u00f8\u00f9\7t\2\2\u00f9\60\3\2\2\2\u00fa\u00fb\7v\2\2\u00fb"+
		"\u00fc\7t\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7g\2\2\u00fe\62\3\2\2\2\u00ff"+
		"\u0100\7h\2\2\u0100\u0101\7c\2\2\u0101\u0102\7n\2\2\u0102\u0103\7u\2\2"+
		"\u0103\u0104\7g\2\2\u0104\64\3\2\2\2\u0105\u0106\7h\2\2\u0106\u0107\7"+
		"w\2\2\u0107\u0108\7p\2\2\u0108\u0109\7e\2\2\u0109\u010a\7v\2\2\u010a\u010b"+
		"\7k\2\2\u010b\u010c\7q\2\2\u010c\u0116\7p\2\2\u010d\u0116\13\2\2\2\u010e"+
		"\u010f\7h\2\2\u010f\u0110\7w\2\2\u0110\u0111\7p\2\2\u0111\u0116\7e\2\2"+
		"\u0112\u0116\13\2\2\2\u0113\u0114\7h\2\2\u0114\u0116\7p\2\2\u0115\u0105"+
		"\3\2\2\2\u0115\u010d\3\2\2\2\u0115\u010e\3\2\2\2\u0115\u0112\3\2\2\2\u0115"+
		"\u0113\3\2\2\2\u0116\66\3\2\2\2\u0117\u0118\7e\2\2\u0118\u0119\7n\2\2"+
		"\u0119\u011a\7c\2\2\u011a\u011b\7u\2\2\u011b\u011c\7u\2\2\u011c8\3\2\2"+
		"\2\u011d\u011e\7n\2\2\u011e\u011f\7g\2\2\u011f\u0120\7v\2\2\u0120:\3\2"+
		"\2\2\u0121\u0122\7v\2\2\u0122\u0123\7t\2\2\u0123\u0124\7c\2\2\u0124\u0125"+
		"\7k\2\2\u0125\u0126\7v\2\2\u0126<\3\2\2\2\u0127\u0128\7f\2\2\u0128\u0129"+
		"\7g\2\2\u0129\u012a\7h\2\2\u012a>\3\2\2\2\u012b\u012c\7r\2\2\u012c\u012d"+
		"\7t\2\2\u012d\u012e\7q\2\2\u012e\u012f\7v\2\2\u012f\u0130\7q\2\2\u0130"+
		"\u0131\7e\2\2\u0131\u0132\7q\2\2\u0132\u0133\7n\2\2\u0133@\3\2\2\2\u0134"+
		"\u0135\7g\2\2\u0135\u0136\7p\2\2\u0136\u0137\7w\2\2\u0137\u0138\7o\2\2"+
		"\u0138B\3\2\2\2\u0139\u013a\7k\2\2\u013a\u013b\7o\2\2\u013b\u013c\7r\2"+
		"\2\u013c\u013d\7q\2\2\u013d\u013e\7t\2\2\u013e\u013f\7v\2\2\u013fD\3\2"+
		"\2\2\u0140\u0141\7h\2\2\u0141\u0142\7t\2\2\u0142\u0143\7q\2\2\u0143\u0144"+
		"\7o\2\2\u0144F\3\2\2\2\u0145\u0146\7r\2\2\u0146\u0147\7c\2\2\u0147\u0148"+
		"\7e\2\2\u0148\u0149\7m\2\2\u0149\u014a\7c\2\2\u014a\u014b\7i\2\2\u014b"+
		"\u014c\7g\2\2\u014cH\3\2\2\2\u014d\u014e\7c\2\2\u014e\u014f\7u\2\2\u014f"+
		"J\3\2\2\2\u0150\u0151\7<\2\2\u0151\u0152\7?\2\2\u0152L\3\2\2\2\u0153\u0154"+
		"\7?\2\2\u0154N\3\2\2\2\u0155\u0156\7-\2\2\u0156P\3\2\2\2\u0157\u0158\7"+
		"/\2\2\u0158R\3\2\2\2\u0159\u015a\7,\2\2\u015aT\3\2\2\2\u015b\u015c\7\61"+
		"\2\2\u015cV\3\2\2\2\u015d\u015e\7>\2\2\u015eX\3\2\2\2\u015f\u0160\7@\2"+
		"\2\u0160Z\3\2\2\2\u0161\u0162\7#\2\2\u0162\u0163\7?\2\2\u0163\\\3\2\2"+
		"\2\u0164\u0165\7#\2\2\u0165^\3\2\2\2\u0166\u0167\7~\2\2\u0167`\3\2\2\2"+
		"\u0168\u0169\7?\2\2\u0169\u016a\7?\2\2\u016ab\3\2\2\2\u016b\u016c\7%\2"+
		"\2\u016cd\3\2\2\2\u016d\u016e\7(\2\2\u016ef\3\2\2\2\u016f\u0170\7.\2\2"+
		"\u0170h\3\2\2\2\u0171\u0172\7*\2\2\u0172j\3\2\2\2\u0173\u0174\7+\2\2\u0174"+
		"l\3\2\2\2\u0175\u0176\7}\2\2\u0176n\3\2\2\2\u0177\u0178\7\177\2\2\u0178"+
		"p\3\2\2\2\u0179\u017a\7]\2\2\u017ar\3\2\2\2\u017b\u017c\7_\2\2\u017ct"+
		"\3\2\2\2\u017d\u017e\7/\2\2\u017e\u017f\7@\2\2\u017fv\3\2\2\2\u0180\u0181"+
		"\7h\2\2\u0181\u0182\7n\2\2\u0182\u0183\7q\2\2\u0183\u0184\7c\2\2\u0184"+
		"\u0185\7v\2\2\u0185x\3\2\2\2\u0186\u0187\7u\2\2\u0187\u0188\7v\2\2\u0188"+
		"\u0189\7t\2\2\u0189\u018a\7k\2\2\u018a\u018b\7p\2\2\u018b\u018c\7i\2\2"+
		"\u018cz\3\2\2\2\u018d\u018e\7d\2\2\u018e\u018f\7q\2\2\u018f\u0190\7q\2"+
		"\2\u0190\u0191\7n\2\2\u0191|\3\2\2\2\u0192\u0193\7p\2\2\u0193\u0194\7"+
		"w\2\2\u0194\u0195\7n\2\2\u0195\u0196\7n\2\2\u0196~\3\2\2\2\u0197\u0198"+
		"\7e\2\2\u0198\u0199\7j\2\2\u0199\u019a\7c\2\2\u019a\u019b\7t\2\2\u019b"+
		"\u0080\3\2\2\2\u019c\u019e\5\t\5\2\u019d\u019c\3\2\2\2\u019e\u019f\3\2"+
		"\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a5\3\2\2\2\u01a1"+
		"\u01a2\7k\2\2\u01a2\u01a3\7p\2\2\u01a3\u01a5\7v\2\2\u01a4\u019d\3\2\2"+
		"\2\u01a4\u01a1\3\2\2\2\u01a5\u0082\3\2\2\2\r\2\u0088\u008d\u009a\u00a6"+
		"\u00ac\u00ae\u00cf\u0115\u019f\u01a4\4\b\2\2\2\4\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}