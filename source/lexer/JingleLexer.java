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
		COMMENT=1, VAR=2, CONST=3, DISPLAY=4, RETURN=5, IF=6, ELSE=7, ELIF=8, 
		FOR=9, TRUE=10, FALSE=11, FUNC=12, CLASS=13, LET=14, ASSIGN=15, EQUALS=16, 
		PLUS=17, MINUS=18, MULTIPLY=19, DIVIDE=20, LESSTHAN=21, GREATERTHAN=22, 
		NOTEQUAL=23, BANG=24, COMMA=25, SEMICOLON=26, LBRACKET=27, RBRACKET=28, 
		LBRACE=29, RBRACE=30, LSQRBRACKET=31, RSQRBRACKET=32, ARROW=33, FLOAT=34, 
		STRING=35, BOOLEAN=36, NULL=37, CHAR=38, INT=39;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DIGIT", "COMMENT", "VAR", "CONST", "DISPLAY", "RETURN", "IF", "ELSE", 
			"ELIF", "FOR", "TRUE", "FALSE", "FUNC", "CLASS", "LET", "ASSIGN", "EQUALS", 
			"PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", "NOTEQUAL", 
			"BANG", "COMMA", "SEMICOLON", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", 
			"LSQRBRACKET", "RSQRBRACKET", "ARROW", "FLOAT", "STRING", "BOOLEAN", 
			"NULL", "CHAR", "INT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'var'", null, "'display'", "'return'", "'if'", "'else'", 
			"'elif'", "'for'", "'true'", "'false'", "'func'", "'class'", "'let'", 
			"':'", "'='", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'!='", "'!'", 
			"','", "';'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'->'", "'float'", 
			"'string'", "'bool'", "'null'", "'char'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMMENT", "VAR", "CONST", "DISPLAY", "RETURN", "IF", "ELSE", "ELIF", 
			"FOR", "TRUE", "FALSE", "FUNC", "CLASS", "LET", "ASSIGN", "EQUALS", "PLUS", 
			"MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", "NOTEQUAL", 
			"BANG", "COMMA", "SEMICOLON", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", 
			"LSQRBRACKET", "RSQRBRACKET", "ARROW", "FLOAT", "STRING", "BOOLEAN", 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2)\u00f7\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\3\3"+
		"\3\3\3\3\3\5\3Z\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\5\5n\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n"+
		"\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3"+
		"\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3"+
		"\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3"+
		"\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3"+
		"%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)"+
		"\6)\u00ef\n)\r)\16)\u00f0\3)\3)\3)\5)\u00f6\n)\2\2*\3\2\5\3\7\4\t\5\13"+
		"\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17\37\20!\21#\22%\23\'"+
		"\24)\25+\26-\27/\30\61\31\63\32\65\33\67\349\35;\36=\37? A!C\"E#G$I%K"+
		"&M\'O(Q)\3\2\3\3\2\62;\2\u00fb\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2"+
		"\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E"+
		"\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2"+
		"\2\2\3S\3\2\2\2\5Y\3\2\2\2\7[\3\2\2\2\tm\3\2\2\2\13o\3\2\2\2\rw\3\2\2"+
		"\2\17~\3\2\2\2\21\u0081\3\2\2\2\23\u0086\3\2\2\2\25\u008b\3\2\2\2\27\u008f"+
		"\3\2\2\2\31\u0094\3\2\2\2\33\u009a\3\2\2\2\35\u009f\3\2\2\2\37\u00a5\3"+
		"\2\2\2!\u00a9\3\2\2\2#\u00ab\3\2\2\2%\u00ad\3\2\2\2\'\u00af\3\2\2\2)\u00b1"+
		"\3\2\2\2+\u00b3\3\2\2\2-\u00b5\3\2\2\2/\u00b7\3\2\2\2\61\u00b9\3\2\2\2"+
		"\63\u00bc\3\2\2\2\65\u00be\3\2\2\2\67\u00c0\3\2\2\29\u00c2\3\2\2\2;\u00c4"+
		"\3\2\2\2=\u00c6\3\2\2\2?\u00c8\3\2\2\2A\u00ca\3\2\2\2C\u00cc\3\2\2\2E"+
		"\u00ce\3\2\2\2G\u00d1\3\2\2\2I\u00d7\3\2\2\2K\u00de\3\2\2\2M\u00e3\3\2"+
		"\2\2O\u00e8\3\2\2\2Q\u00f5\3\2\2\2ST\t\2\2\2T\4\3\2\2\2UZ\7%\2\2VZ\13"+
		"\2\2\2WX\7\61\2\2XZ\7\61\2\2YU\3\2\2\2YV\3\2\2\2YW\3\2\2\2Z\6\3\2\2\2"+
		"[\\\7x\2\2\\]\7c\2\2]^\7t\2\2^\b\3\2\2\2_`\7e\2\2`a\7q\2\2ab\7p\2\2bc"+
		"\7u\2\2cn\7v\2\2dn\13\2\2\2ef\7e\2\2fg\7q\2\2gh\7p\2\2hi\7u\2\2ij\7v\2"+
		"\2jk\7c\2\2kl\7p\2\2ln\7v\2\2m_\3\2\2\2md\3\2\2\2me\3\2\2\2n\n\3\2\2\2"+
		"op\7f\2\2pq\7k\2\2qr\7u\2\2rs\7r\2\2st\7n\2\2tu\7c\2\2uv\7{\2\2v\f\3\2"+
		"\2\2wx\7t\2\2xy\7g\2\2yz\7v\2\2z{\7w\2\2{|\7t\2\2|}\7p\2\2}\16\3\2\2\2"+
		"~\177\7k\2\2\177\u0080\7h\2\2\u0080\20\3\2\2\2\u0081\u0082\7g\2\2\u0082"+
		"\u0083\7n\2\2\u0083\u0084\7u\2\2\u0084\u0085\7g\2\2\u0085\22\3\2\2\2\u0086"+
		"\u0087\7g\2\2\u0087\u0088\7n\2\2\u0088\u0089\7k\2\2\u0089\u008a\7h\2\2"+
		"\u008a\24\3\2\2\2\u008b\u008c\7h\2\2\u008c\u008d\7q\2\2\u008d\u008e\7"+
		"t\2\2\u008e\26\3\2\2\2\u008f\u0090\7v\2\2\u0090\u0091\7t\2\2\u0091\u0092"+
		"\7w\2\2\u0092\u0093\7g\2\2\u0093\30\3\2\2\2\u0094\u0095\7h\2\2\u0095\u0096"+
		"\7c\2\2\u0096\u0097\7n\2\2\u0097\u0098\7u\2\2\u0098\u0099\7g\2\2\u0099"+
		"\32\3\2\2\2\u009a\u009b\7h\2\2\u009b\u009c\7w\2\2\u009c\u009d\7p\2\2\u009d"+
		"\u009e\7e\2\2\u009e\34\3\2\2\2\u009f\u00a0\7e\2\2\u00a0\u00a1\7n\2\2\u00a1"+
		"\u00a2\7c\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4\7u\2\2\u00a4\36\3\2\2\2\u00a5"+
		"\u00a6\7n\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7v\2\2\u00a8 \3\2\2\2\u00a9"+
		"\u00aa\7<\2\2\u00aa\"\3\2\2\2\u00ab\u00ac\7?\2\2\u00ac$\3\2\2\2\u00ad"+
		"\u00ae\7-\2\2\u00ae&\3\2\2\2\u00af\u00b0\7/\2\2\u00b0(\3\2\2\2\u00b1\u00b2"+
		"\7,\2\2\u00b2*\3\2\2\2\u00b3\u00b4\7\61\2\2\u00b4,\3\2\2\2\u00b5\u00b6"+
		"\7>\2\2\u00b6.\3\2\2\2\u00b7\u00b8\7@\2\2\u00b8\60\3\2\2\2\u00b9\u00ba"+
		"\7#\2\2\u00ba\u00bb\7?\2\2\u00bb\62\3\2\2\2\u00bc\u00bd\7#\2\2\u00bd\64"+
		"\3\2\2\2\u00be\u00bf\7.\2\2\u00bf\66\3\2\2\2\u00c0\u00c1\7=\2\2\u00c1"+
		"8\3\2\2\2\u00c2\u00c3\7*\2\2\u00c3:\3\2\2\2\u00c4\u00c5\7+\2\2\u00c5<"+
		"\3\2\2\2\u00c6\u00c7\7}\2\2\u00c7>\3\2\2\2\u00c8\u00c9\7\177\2\2\u00c9"+
		"@\3\2\2\2\u00ca\u00cb\7]\2\2\u00cbB\3\2\2\2\u00cc\u00cd\7_\2\2\u00cdD"+
		"\3\2\2\2\u00ce\u00cf\7/\2\2\u00cf\u00d0\7@\2\2\u00d0F\3\2\2\2\u00d1\u00d2"+
		"\7h\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7c\2\2\u00d5"+
		"\u00d6\7v\2\2\u00d6H\3\2\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9\7v\2\2\u00d9"+
		"\u00da\7t\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7i\2\2"+
		"\u00ddJ\3\2\2\2\u00de\u00df\7d\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7q\2"+
		"\2\u00e1\u00e2\7n\2\2\u00e2L\3\2\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7"+
		"w\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7n\2\2\u00e7N\3\2\2\2\u00e8\u00e9"+
		"\7e\2\2\u00e9\u00ea\7j\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7t\2\2\u00ec"+
		"P\3\2\2\2\u00ed\u00ef\5\3\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2"+
		"\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f6\3\2\2\2\u00f2\u00f3"+
		"\7k\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f6\7v\2\2\u00f5\u00ee\3\2\2\2\u00f5"+
		"\u00f2\3\2\2\2\u00f6R\3\2\2\2\7\2Ym\u00f0\u00f5\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}