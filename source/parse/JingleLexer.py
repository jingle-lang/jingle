# Generated from JingleLexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
import re
import importlib
# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2p")
        buf.write("\u0438\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080")
        buf.write("\t\u0080\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083")
        buf.write("\4\u0084\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087")
        buf.write("\t\u0087\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a")
        buf.write("\4\u008b\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\3\2\7")
        buf.write("\2\u011d\n\2\f\2\16\2\u0120\13\2\3\2\6\2\u0123\n\2\r\2")
        buf.write("\16\2\u0124\5\2\u0127\n\2\3\3\3\3\7\3\u012b\n\3\f\3\16")
        buf.write("\3\u012e\13\3\3\3\6\3\u0131\n\3\r\3\16\3\u0132\5\3\u0135")
        buf.write("\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\39\39\39\3:\3")
        buf.write(":\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3A\3B\3")
        buf.write("B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u0252")
        buf.write("\nE\3F\3F\3F\3F\3F\3F\3F\3F\5F\u025c\nF\3G\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3G\5G\u0267\nG\3H\3H\3H\3H\3H\3H\3H\3H\3H\3")
        buf.write("H\3H\5H\u0274\nH\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3L\3M\3")
        buf.write("M\3M\3N\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3R\3S\3S\3")
        buf.write("T\3T\3T\3T\3U\3U\3U\3V\3V\3V\3W\3W\3W\3W\3W\3W\3X\3X\3")
        buf.write("X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3[\3[\3[\3")
        buf.write("[\3[\3\\\3\\\3\\\7\\\u02bd\n\\\f\\\16\\\u02c0\13\\\5\\")
        buf.write("\u02c2\n\\\3]\3]\3]\7]\u02c7\n]\f]\16]\u02ca\13]\3]\3")
        buf.write("]\6]\u02ce\n]\r]\16]\u02cf\5]\u02d2\n]\3^\3^\3_\7_\u02d7")
        buf.write("\n_\f_\16_\u02da\13_\3_\3_\7_\u02de\n_\f_\16_\u02e1\13")
        buf.write("_\3`\3`\3a\3a\3b\3b\3c\3c\3c\3c\3d\6d\u02ee\nd\rd\16d")
        buf.write("\u02ef\3e\3e\7e\u02f4\ne\fe\16e\u02f7\13e\3f\3f\3f\3f")
        buf.write("\7f\u02fd\nf\ff\16f\u0300\13f\3f\5f\u0303\nf\3f\3f\3f")
        buf.write("\3f\3f\7f\u030a\nf\ff\16f\u030d\13f\3f\3f\5f\u0311\nf")
        buf.write("\3g\3g\5g\u0315\ng\3h\3h\3h\5h\u031a\nh\3i\3i\3i\3i\5")
        buf.write("i\u0320\ni\3j\3j\3j\3j\3j\5j\u0327\nj\3j\3j\5j\u032b\n")
        buf.write("j\3k\3k\3k\3k\3k\5k\u0332\nk\3k\3k\5k\u0336\nk\3l\3l\7")
        buf.write("l\u033a\nl\fl\16l\u033d\13l\3l\6l\u0340\nl\rl\16l\u0341")
        buf.write("\5l\u0344\nl\3m\3m\3m\6m\u0349\nm\rm\16m\u034a\3n\3n\3")
        buf.write("n\6n\u0350\nn\rn\16n\u0351\3o\3o\3o\6o\u0357\no\ro\16")
        buf.write("o\u0358\3p\3p\5p\u035d\np\3q\3q\5q\u0361\nq\3q\3q\3r\3")
        buf.write("r\3r\5r\u0368\nr\3r\3r\3s\3s\3t\3t\3t\7t\u0371\nt\ft\16")
        buf.write("t\u0374\13t\3t\3t\3t\3t\7t\u037a\nt\ft\16t\u037d\13t\3")
        buf.write("t\5t\u0380\nt\3u\3u\3u\3u\3u\7u\u0387\nu\fu\16u\u038a")
        buf.write("\13u\3u\3u\3u\3u\3u\3u\3u\3u\7u\u0394\nu\fu\16u\u0397")
        buf.write("\13u\3u\3u\3u\5u\u039c\nu\3v\3v\5v\u03a0\nv\3w\3w\3x\3")
        buf.write("x\3x\3x\5x\u03a8\nx\3y\3y\3z\3z\3{\3{\3|\3|\3}\3}\3~\5")
        buf.write("~\u03b5\n~\3~\3~\3~\3~\5~\u03bb\n~\3\177\3\177\5\177\u03bf")
        buf.write("\n\177\3\177\3\177\3\u0080\6\u0080\u03c4\n\u0080\r\u0080")
        buf.write("\16\u0080\u03c5\3\u0081\3\u0081\6\u0081\u03ca\n\u0081")
        buf.write("\r\u0081\16\u0081\u03cb\3\u0082\3\u0082\5\u0082\u03d0")
        buf.write("\n\u0082\3\u0082\6\u0082\u03d3\n\u0082\r\u0082\16\u0082")
        buf.write("\u03d4\3\u0083\3\u0083\3\u0083\7\u0083\u03da\n\u0083\f")
        buf.write("\u0083\16\u0083\u03dd\13\u0083\3\u0083\3\u0083\3\u0083")
        buf.write("\3\u0083\7\u0083\u03e3\n\u0083\f\u0083\16\u0083\u03e6")
        buf.write("\13\u0083\3\u0083\5\u0083\u03e9\n\u0083\3\u0084\3\u0084")
        buf.write("\3\u0084\3\u0084\3\u0084\7\u0084\u03f0\n\u0084\f\u0084")
        buf.write("\16\u0084\u03f3\13\u0084\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write("\3\u0084\3\u0084\3\u0084\3\u0084\7\u0084\u03fd\n\u0084")
        buf.write("\f\u0084\16\u0084\u0400\13\u0084\3\u0084\3\u0084\3\u0084")
        buf.write("\5\u0084\u0405\n\u0084\3\u0085\3\u0085\5\u0085\u0409\n")
        buf.write("\u0085\3\u0086\5\u0086\u040c\n\u0086\3\u0087\5\u0087\u040f")
        buf.write("\n\u0087\3\u0088\5\u0088\u0412\n\u0088\3\u0089\3\u0089")
        buf.write("\3\u0089\3\u008a\3\u008a\5\u008a\u0419\n\u008a\3\u008a")
        buf.write("\5\u008a\u041c\n\u008a\3\u008a\3\u008a\5\u008a\u0420\n")
        buf.write("\u008a\3\u008b\5\u008b\u0423\n\u008b\3\u008c\3\u008c\5")
        buf.write("\u008c\u0427\n\u008c\3\u008d\3\u008d\3\u008d\5\u008d\u042c")
        buf.write("\n\u008d\3\u008d\3\u008d\5\u008d\u0430\n\u008d\3\u008d")
        buf.write("\5\u008d\u0433\n\u008d\5\u008d\u0435\n\u008d\3\u008d\3")
        buf.write("\u008d\7\u030b\u0388\u0395\u03f1\u03fe\2\u008e\3\5\5\6")
        buf.write("\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25\16\27\17\31\20\33")
        buf.write("\21\35\22\37\23!\24#\25%\26\'\27)\30+\31-\32/\33\61\34")
        buf.write("\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.W/Y")
        buf.write("\60[\61]\62_\63a\64c\65e\66g\67i8k9m:o;q<s=u>w?y@{A}B")
        buf.write("\177C\u0081D\u0083E\u0085F\u0087G\u0089H\u008bI\u008d")
        buf.write("J\u008fK\u0091L\u0093M\u0095N\u0097O\u0099P\u009bQ\u009d")
        buf.write("R\u009fS\u00a1T\u00a3U\u00a5V\u00a7W\u00a9X\u00abY\u00ad")
        buf.write("Z\u00af[\u00b1\\\u00b3]\u00b5^\u00b7_\u00b9`\u00bb\2\u00bd")
        buf.write("\2\u00bf\2\u00c1\2\u00c3\2\u00c5\2\u00c7\2\u00c9a\u00cb")
        buf.write("b\u00cdc\u00cfd\u00d1e\u00d3f\u00d5g\u00d7h\u00d9i\u00db")
        buf.write("j\u00ddk\u00dfl\u00e1m\u00e3n\u00e5o\u00e7\2\u00e9\2\u00eb")
        buf.write("\2\u00ed\2\u00ef\2\u00f1\2\u00f3\2\u00f5\2\u00f7\2\u00f9")
        buf.write("\2\u00fb\2\u00fd\2\u00ff\2\u0101\2\u0103\2\u0105\2\u0107")
        buf.write("\2\u0109\2\u010b\2\u010d\2\u010f\2\u0111\2\u0113\2\u0115")
        buf.write("\2\u0117\2\u0119p\3\2\"\3\2\63;\3\2\62;\3\2aa\3\2c|\6")
        buf.write("\2\62;C\\aac|\4\2\62;aa\6\2\62;CHaach\4\2\62\63aa\f\2")
        buf.write("\13\17\"\"\u0087\u0087\u00a2\u00a2\u1682\u1682\u2002\u200c")
        buf.write("\u202a\u202b\u2031\u2031\u2061\u2061\u3002\u3002\4\2\13")
        buf.write("\13\"\"\4\2\f\f\17\17\b\2HHTTWWhhttww\4\2HHhh\4\2TTtt")
        buf.write("\4\2DDdd\4\2QQqq\4\2ZZzz\4\2LLll\6\2\f\f\16\17))^^\6\2")
        buf.write("\f\f\16\17$$^^\3\2^^\3\2\629\5\2\62;CHch\3\2\62\63\4\2")
        buf.write("GGgg\4\2--//\7\2\2\13\r\16\20(*]_\u0081\7\2\2\13\r\16")
        buf.write("\20#%]_\u0081\4\2\2]_\u0081\3\2\2\u0081\u0129\2C\\aac")
        buf.write("|\u00ac\u00ac\u00b7\u00b7\u00bc\u00bc\u00c2\u00d8\u00da")
        buf.write("\u00f8\u00fa\u0243\u0252\u02c3\u02c8\u02d3\u02e2\u02e6")
        buf.write("\u02f0\u02f0\u037c\u037c\u0388\u0388\u038a\u038c\u038e")
        buf.write("\u038e\u0390\u03a3\u03a5\u03d0\u03d2\u03f7\u03f9\u0483")
        buf.write("\u048c\u04d0\u04d2\u04fb\u0502\u0511\u0533\u0558\u055b")
        buf.write("\u055b\u0563\u0589\u05d2\u05ec\u05f2\u05f4\u0623\u063c")
        buf.write("\u0642\u064c\u0670\u0671\u0673\u06d5\u06d7\u06d7\u06e7")
        buf.write("\u06e8\u06f0\u06f1\u06fc\u06fe\u0701\u0701\u0712\u0712")
        buf.write("\u0714\u0731\u074f\u076f\u0782\u07a7\u07b3\u07b3\u0906")
        buf.write("\u093b\u093f\u093f\u0952\u0952\u095a\u0963\u097f\u097f")
        buf.write("\u0987\u098e\u0991\u0992\u0995\u09aa\u09ac\u09b2\u09b4")
        buf.write("\u09b4\u09b8\u09bb\u09bf\u09bf\u09d0\u09d0\u09de\u09df")
        buf.write("\u09e1\u09e3\u09f2\u09f3\u0a07\u0a0c\u0a11\u0a12\u0a15")
        buf.write("\u0a2a\u0a2c\u0a32\u0a34\u0a35\u0a37\u0a38\u0a3a\u0a3b")
        buf.write("\u0a5b\u0a5e\u0a60\u0a60\u0a74\u0a76\u0a87\u0a8f\u0a91")
        buf.write("\u0a93\u0a95\u0aaa\u0aac\u0ab2\u0ab4\u0ab5\u0ab7\u0abb")
        buf.write("\u0abf\u0abf\u0ad2\u0ad2\u0ae2\u0ae3\u0b07\u0b0e\u0b11")
        buf.write("\u0b12\u0b15\u0b2a\u0b2c\u0b32\u0b34\u0b35\u0b37\u0b3b")
        buf.write("\u0b3f\u0b3f\u0b5e\u0b5f\u0b61\u0b63\u0b73\u0b73\u0b85")
        buf.write("\u0b85\u0b87\u0b8c\u0b90\u0b92\u0b94\u0b97\u0b9b\u0b9c")
        buf.write("\u0b9e\u0b9e\u0ba0\u0ba1\u0ba5\u0ba6\u0baa\u0bac\u0bb0")
        buf.write("\u0bbb\u0c07\u0c0e\u0c10\u0c12\u0c14\u0c2a\u0c2c\u0c35")
        buf.write("\u0c37\u0c3b\u0c62\u0c63\u0c87\u0c8e\u0c90\u0c92\u0c94")
        buf.write("\u0caa\u0cac\u0cb5\u0cb7\u0cbb\u0cbf\u0cbf\u0ce0\u0ce0")
        buf.write("\u0ce2\u0ce3\u0d07\u0d0e\u0d10\u0d12\u0d14\u0d2a\u0d2c")
        buf.write("\u0d3b\u0d62\u0d63\u0d87\u0d98\u0d9c\u0db3\u0db5\u0dbd")
        buf.write("\u0dbf\u0dbf\u0dc2\u0dc8\u0e03\u0e32\u0e34\u0e35\u0e42")
        buf.write("\u0e48\u0e83\u0e84\u0e86\u0e86\u0e89\u0e8a\u0e8c\u0e8c")
        buf.write("\u0e8f\u0e8f\u0e96\u0e99\u0e9b\u0ea1\u0ea3\u0ea5\u0ea7")
        buf.write("\u0ea7\u0ea9\u0ea9\u0eac\u0ead\u0eaf\u0eb2\u0eb4\u0eb5")
        buf.write("\u0ebf\u0ebf\u0ec2\u0ec6\u0ec8\u0ec8\u0ede\u0edf\u0f02")
        buf.write("\u0f02\u0f42\u0f49\u0f4b\u0f6c\u0f8a\u0f8d\u1002\u1023")
        buf.write("\u1025\u1029\u102b\u102c\u1052\u1057\u10a2\u10c7\u10d2")
        buf.write("\u10fc\u10fe\u10fe\u1102\u115b\u1161\u11a4\u11aa\u11fb")
        buf.write("\u1202\u124a\u124c\u124f\u1252\u1258\u125a\u125a\u125c")
        buf.write("\u125f\u1262\u128a\u128c\u128f\u1292\u12b2\u12b4\u12b7")
        buf.write("\u12ba\u12c0\u12c2\u12c2\u12c4\u12c7\u12ca\u12d8\u12da")
        buf.write("\u1312\u1314\u1317\u131a\u135c\u1382\u1391\u13a2\u13f6")
        buf.write("\u1403\u166e\u1671\u1678\u1683\u169c\u16a2\u16ec\u16f0")
        buf.write("\u16f2\u1702\u170e\u1710\u1713\u1722\u1733\u1742\u1753")
        buf.write("\u1762\u176e\u1770\u1772\u1782\u17b5\u17d9\u17d9\u17de")
        buf.write("\u17de\u1822\u1879\u1882\u18aa\u1902\u191e\u1952\u196f")
        buf.write("\u1972\u1976\u1982\u19ab\u19c3\u19c9\u1a02\u1a18\u1d02")
        buf.write("\u1dc1\u1e02\u1e9d\u1ea2\u1efb\u1f02\u1f17\u1f1a\u1f1f")
        buf.write("\u1f22\u1f47\u1f4a\u1f4f\u1f52\u1f59\u1f5b\u1f5b\u1f5d")
        buf.write("\u1f5d\u1f5f\u1f5f\u1f61\u1f7f\u1f82\u1fb6\u1fb8\u1fbe")
        buf.write("\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8\u1fce\u1fd2\u1fd5\u1fd8")
        buf.write("\u1fdd\u1fe2\u1fee\u1ff4\u1ff6\u1ff8\u1ffe\u2073\u2073")
        buf.write("\u2081\u2081\u2092\u2096\u2104\u2104\u2109\u2109\u210c")
        buf.write("\u2115\u2117\u2117\u211a\u211f\u2126\u2126\u2128\u2128")
        buf.write("\u212a\u212a\u212c\u2133\u2135\u213b\u213e\u2141\u2147")
        buf.write("\u214b\u2162\u2185\u2c02\u2c30\u2c32\u2c60\u2c82\u2ce6")
        buf.write("\u2d02\u2d27\u2d32\u2d67\u2d71\u2d71\u2d82\u2d98\u2da2")
        buf.write("\u2da8\u2daa\u2db0\u2db2\u2db8\u2dba\u2dc0\u2dc2\u2dc8")
        buf.write("\u2dca\u2dd0\u2dd2\u2dd8\u2dda\u2de0\u3007\u3009\u3023")
        buf.write("\u302b\u3033\u3037\u303a\u303e\u3043\u3098\u309d\u30a1")
        buf.write("\u30a3\u30fc\u30fe\u3101\u3107\u312e\u3133\u3190\u31a2")
        buf.write("\u31b9\u31f2\u3201\u3402\u4db7\u4e02\u9fbd\ua002\ua48e")
        buf.write("\ua802\ua803\ua805\ua807\ua809\ua80c\ua80e\ua824\uac02")
        buf.write("\ud7a5\uf902\ufa2f\ufa32\ufa6c\ufa72\ufadb\ufb02\ufb08")
        buf.write("\ufb15\ufb19\ufb1f\ufb1f\ufb21\ufb2a\ufb2c\ufb38\ufb3a")
        buf.write("\ufb3e\ufb40\ufb40\ufb42\ufb43\ufb45\ufb46\ufb48\ufbb3")
        buf.write("\ufbd5\ufd3f\ufd52\ufd91\ufd94\ufdc9\ufdf2\ufdfd\ufe72")
        buf.write("\ufe76\ufe78\ufefe\uff23\uff3c\uff43\uff5c\uff68\uffc0")
        buf.write("\uffc4\uffc9\uffcc\uffd1\uffd4\uffd9\uffdc\uffde\u0096")
        buf.write("\2\62;\u0302\u0371\u0485\u0488\u0593\u05bb\u05bd\u05bf")
        buf.write("\u05c1\u05c1\u05c3\u05c4\u05c6\u05c7\u05c9\u05c9\u0612")
        buf.write("\u0617\u064d\u0660\u0662\u066b\u0672\u0672\u06d8\u06de")
        buf.write("\u06e1\u06e6\u06e9\u06ea\u06ec\u06ef\u06f2\u06fb\u0713")
        buf.write("\u0713\u0732\u074c\u07a8\u07b2\u0903\u0905\u093e\u093e")
        buf.write("\u0940\u094f\u0953\u0956\u0964\u0965\u0968\u0971\u0983")
        buf.write("\u0985\u09be\u09be\u09c0\u09c6\u09c9\u09ca\u09cd\u09cf")
        buf.write("\u09d9\u09d9\u09e4\u09e5\u09e8\u09f1\u0a03\u0a05\u0a3e")
        buf.write("\u0a3e\u0a40\u0a44\u0a49\u0a4a\u0a4d\u0a4f\u0a68\u0a73")
        buf.write("\u0a83\u0a85\u0abe\u0abe\u0ac0\u0ac7\u0ac9\u0acb\u0acd")
        buf.write("\u0acf\u0ae4\u0ae5\u0ae8\u0af1\u0b03\u0b05\u0b3e\u0b3e")
        buf.write("\u0b40\u0b45\u0b49\u0b4a\u0b4d\u0b4f\u0b58\u0b59\u0b68")
        buf.write("\u0b71\u0b84\u0b84\u0bc0\u0bc4\u0bc8\u0bca\u0bcc\u0bcf")
        buf.write("\u0bd9\u0bd9\u0be8\u0bf1\u0c03\u0c05\u0c40\u0c46\u0c48")
        buf.write("\u0c4a\u0c4c\u0c4f\u0c57\u0c58\u0c68\u0c71\u0c84\u0c85")
        buf.write("\u0cbe\u0cbe\u0cc0\u0cc6\u0cc8\u0cca\u0ccc\u0ccf\u0cd7")
        buf.write("\u0cd8\u0ce8\u0cf1\u0d04\u0d05\u0d40\u0d45\u0d48\u0d4a")
        buf.write("\u0d4c\u0d4f\u0d59\u0d59\u0d68\u0d71\u0d84\u0d85\u0dcc")
        buf.write("\u0dcc\u0dd1\u0dd6\u0dd8\u0dd8\u0dda\u0de1\u0df4\u0df5")
        buf.write("\u0e33\u0e33\u0e36\u0e3c\u0e49\u0e50\u0e52\u0e5b\u0eb3")
        buf.write("\u0eb3\u0eb6\u0ebb\u0ebd\u0ebe\u0eca\u0ecf\u0ed2\u0edb")
        buf.write("\u0f1a\u0f1b\u0f22\u0f2b\u0f37\u0f37\u0f39\u0f39\u0f3b")
        buf.write("\u0f3b\u0f40\u0f41\u0f73\u0f86\u0f88\u0f89\u0f92\u0f99")
        buf.write("\u0f9b\u0fbe\u0fc8\u0fc8\u102e\u1034\u1038\u103b\u1042")
        buf.write("\u104b\u1058\u105b\u1361\u1361\u136b\u1373\u1714\u1716")
        buf.write("\u1734\u1736\u1754\u1755\u1774\u1775\u17b8\u17d5\u17df")
        buf.write("\u17df\u17e2\u17eb\u180d\u180f\u1812\u181b\u18ab\u18ab")
        buf.write("\u1922\u192d\u1932\u193d\u1948\u1951\u19b2\u19c2\u19ca")
        buf.write("\u19cb\u19d2\u19db\u1a19\u1a1d\u1dc2\u1dc5\u2041\u2042")
        buf.write("\u2056\u2056\u20d2\u20de\u20e3\u20e3\u20e7\u20ed\u302c")
        buf.write("\u3031\u309b\u309c\ua804\ua804\ua808\ua808\ua80d\ua80d")
        buf.write("\ua825\ua829\ufb20\ufb20\ufe02\ufe11\ufe22\ufe25\ufe35")
        buf.write("\ufe36\ufe4f\ufe51\uff12\uff1b\uff41\uff41\2\u0467\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00c9")
        buf.write("\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2")
        buf.write("\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2\2\2\u00d7")
        buf.write("\3\2\2\2\2\u00d9\3\2\2\2\2\u00db\3\2\2\2\2\u00dd\3\2\2")
        buf.write("\2\2\u00df\3\2\2\2\2\u00e1\3\2\2\2\2\u00e3\3\2\2\2\2\u00e5")
        buf.write("\3\2\2\2\2\u0119\3\2\2\2\3\u0126\3\2\2\2\5\u0134\3\2\2")
        buf.write("\2\7\u0136\3\2\2\2\t\u0138\3\2\2\2\13\u013c\3\2\2\2\r")
        buf.write("\u0140\3\2\2\2\17\u0144\3\2\2\2\21\u0148\3\2\2\2\23\u014d")
        buf.write("\3\2\2\2\25\u0154\3\2\2\2\27\u0157\3\2\2\2\31\u015c\3")
        buf.write("\2\2\2\33\u0160\3\2\2\2\35\u0163\3\2\2\2\37\u0166\3\2")
        buf.write("\2\2!\u016b\3\2\2\2#\u0170\3\2\2\2%\u0176\3\2\2\2\'\u017a")
        buf.write("\3\2\2\2)\u017f\3\2\2\2+\u0185\3\2\2\2-\u0188\3\2\2\2")
        buf.write("/\u018e\3\2\2\2\61\u0192\3\2\2\2\63\u0197\3\2\2\2\65\u019d")
        buf.write("\3\2\2\2\67\u01a1\3\2\2\29\u01a7\3\2\2\2;\u01ae\3\2\2")
        buf.write("\2=\u01b3\3\2\2\2?\u01bb\3\2\2\2A\u01be\3\2\2\2C\u01c4")
        buf.write("\3\2\2\2E\u01cd\3\2\2\2G\u01d4\3\2\2\2I\u01da\3\2\2\2")
        buf.write("K\u01df\3\2\2\2M\u01e3\3\2\2\2O\u01ec\3\2\2\2Q\u01f3\3")
        buf.write("\2\2\2S\u01fb\3\2\2\2U\u0203\3\2\2\2W\u020a\3\2\2\2Y\u020d")
        buf.write("\3\2\2\2[\u020f\3\2\2\2]\u0212\3\2\2\2_\u0215\3\2\2\2")
        buf.write("a\u0218\3\2\2\2c\u021b\3\2\2\2e\u021d\3\2\2\2g\u021f\3")
        buf.write("\2\2\2i\u0221\3\2\2\2k\u0223\3\2\2\2m\u0225\3\2\2\2o\u0227")
        buf.write("\3\2\2\2q\u022a\3\2\2\2s\u022d\3\2\2\2u\u022f\3\2\2\2")
        buf.write("w\u0231\3\2\2\2y\u0233\3\2\2\2{\u0235\3\2\2\2}\u0238\3")
        buf.write("\2\2\2\177\u023a\3\2\2\2\u0081\u023c\3\2\2\2\u0083\u023f")
        buf.write("\3\2\2\2\u0085\u0241\3\2\2\2\u0087\u0244\3\2\2\2\u0089")
        buf.write("\u0251\3\2\2\2\u008b\u025b\3\2\2\2\u008d\u0266\3\2\2\2")
        buf.write("\u008f\u0273\3\2\2\2\u0091\u0275\3\2\2\2\u0093\u0277\3")
        buf.write("\2\2\2\u0095\u027a\3\2\2\2\u0097\u027d\3\2\2\2\u0099\u0280")
        buf.write("\3\2\2\2\u009b\u0283\3\2\2\2\u009d\u0286\3\2\2\2\u009f")
        buf.write("\u0289\3\2\2\2\u00a1\u028c\3\2\2\2\u00a3\u028f\3\2\2\2")
        buf.write("\u00a5\u0291\3\2\2\2\u00a7\u0293\3\2\2\2\u00a9\u0297\3")
        buf.write("\2\2\2\u00ab\u029a\3\2\2\2\u00ad\u029d\3\2\2\2\u00af\u02a3")
        buf.write("\3\2\2\2\u00b1\u02aa\3\2\2\2\u00b3\u02af\3\2\2\2\u00b5")
        buf.write("\u02b4\3\2\2\2\u00b7\u02c1\3\2\2\2\u00b9\u02d1\3\2\2\2")
        buf.write("\u00bb\u02d3\3\2\2\2\u00bd\u02d8\3\2\2\2\u00bf\u02e2\3")
        buf.write("\2\2\2\u00c1\u02e4\3\2\2\2\u00c3\u02e6\3\2\2\2\u00c5\u02e8")
        buf.write("\3\2\2\2\u00c7\u02ed\3\2\2\2\u00c9\u02f1\3\2\2\2\u00cb")
        buf.write("\u0310\3\2\2\2\u00cd\u0314\3\2\2\2\u00cf\u0319\3\2\2\2")
        buf.write("\u00d1\u031f\3\2\2\2\u00d3\u0326\3\2\2\2\u00d5\u0331\3")
        buf.write("\2\2\2\u00d7\u0343\3\2\2\2\u00d9\u0345\3\2\2\2\u00db\u034c")
        buf.write("\3\2\2\2\u00dd\u0353\3\2\2\2\u00df\u035c\3\2\2\2\u00e1")
        buf.write("\u0360\3\2\2\2\u00e3\u0367\3\2\2\2\u00e5\u036b\3\2\2\2")
        buf.write("\u00e7\u037f\3\2\2\2\u00e9\u039b\3\2\2\2\u00eb\u039f\3")
        buf.write("\2\2\2\u00ed\u03a1\3\2\2\2\u00ef\u03a7\3\2\2\2\u00f1\u03a9")
        buf.write("\3\2\2\2\u00f3\u03ab\3\2\2\2\u00f5\u03ad\3\2\2\2\u00f7")
        buf.write("\u03af\3\2\2\2\u00f9\u03b1\3\2\2\2\u00fb\u03ba\3\2\2\2")
        buf.write("\u00fd\u03be\3\2\2\2\u00ff\u03c3\3\2\2\2\u0101\u03c7\3")
        buf.write("\2\2\2\u0103\u03cd\3\2\2\2\u0105\u03e8\3\2\2\2\u0107\u0404")
        buf.write("\3\2\2\2\u0109\u0408\3\2\2\2\u010b\u040b\3\2\2\2\u010d")
        buf.write("\u040e\3\2\2\2\u010f\u0411\3\2\2\2\u0111\u0413\3\2\2\2")
        buf.write("\u0113\u0416\3\2\2\2\u0115\u0422\3\2\2\2\u0117\u0426\3")
        buf.write("\2\2\2\u0119\u0434\3\2\2\2\u011b\u011d\5\u0119\u008d\2")
        buf.write("\u011c\u011b\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3")
        buf.write("\2\2\2\u011e\u011f\3\2\2\2\u011f\u0127\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0121\u0123\5\u0119\u008d\2\u0122\u0121\3\2\2")
        buf.write("\2\u0123\u0124\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125")
        buf.write("\3\2\2\2\u0125\u0127\3\2\2\2\u0126\u011e\3\2\2\2\u0126")
        buf.write("\u0122\3\2\2\2\u0127\4\3\2\2\2\u0128\u012c\5\u00bb^\2")
        buf.write("\u0129\u012b\5\u0119\u008d\2\u012a\u0129\3\2\2\2\u012b")
        buf.write("\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2")
        buf.write("\u012d\u0135\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0131\5")
        buf.write("\u0119\u008d\2\u0130\u012f\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\3")
        buf.write("\2\2\2\u0134\u0128\3\2\2\2\u0134\u0130\3\2\2\2\u0135\6")
        buf.write("\3\2\2\2\u0136\u0137\7$\2\2\u0137\b\3\2\2\2\u0138\u0139")
        buf.write("\7x\2\2\u0139\u013a\7c\2\2\u013a\u013b\7t\2\2\u013b\n")
        buf.write("\3\2\2\2\u013c\u013d\7c\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7t\2\2\u013f\f\3\2\2\2\u0140\u0141\7e\2\2\u0141\u0142")
        buf.write("\7q\2\2\u0142\u0143\7p\2\2\u0143\16\3\2\2\2\u0144\u0145")
        buf.write("\7n\2\2\u0145\u0146\7q\2\2\u0146\u0147\7e\2\2\u0147\20")
        buf.write("\3\2\2\2\u0148\u0149\7g\2\2\u0149\u014a\7e\2\2\u014a\u014b")
        buf.write("\7j\2\2\u014b\u014c\7q\2\2\u014c\22\3\2\2\2\u014d\u014e")
        buf.write("\7t\2\2\u014e\u014f\7g\2\2\u014f\u0150\7v\2\2\u0150\u0151")
        buf.write("\7w\2\2\u0151\u0152\7t\2\2\u0152\u0153\7p\2\2\u0153\24")
        buf.write("\3\2\2\2\u0154\u0155\7k\2\2\u0155\u0156\7h\2\2\u0156\26")
        buf.write("\3\2\2\2\u0157\u0158\7v\2\2\u0158\u0159\7j\2\2\u0159\u015a")
        buf.write("\7g\2\2\u015a\u015b\7p\2\2\u015b\30\3\2\2\2\u015c\u015d")
        buf.write("\7c\2\2\u015d\u015e\7p\2\2\u015e\u015f\7f\2\2\u015f\32")
        buf.write("\3\2\2\2\u0160\u0161\7q\2\2\u0161\u0162\7t\2\2\u0162\34")
        buf.write("\3\2\2\2\u0163\u0164\7k\2\2\u0164\u0165\7p\2\2\u0165\36")
        buf.write("\3\2\2\2\u0166\u0167\7g\2\2\u0167\u0168\7n\2\2\u0168\u0169")
        buf.write("\7u\2\2\u0169\u016a\7g\2\2\u016a \3\2\2\2\u016b\u016c")
        buf.write("\7g\2\2\u016c\u016d\7n\2\2\u016d\u016e\7k\2\2\u016e\u016f")
        buf.write("\7h\2\2\u016f\"\3\2\2\2\u0170\u0171\7y\2\2\u0171\u0172")
        buf.write("\7j\2\2\u0172\u0173\7k\2\2\u0173\u0174\7n\2\2\u0174\u0175")
        buf.write("\7g\2\2\u0175$\3\2\2\2\u0176\u0177\7h\2\2\u0177\u0178")
        buf.write("\7q\2\2\u0178\u0179\7t\2\2\u0179&\3\2\2\2\u017a\u017b")
        buf.write("\7v\2\2\u017b\u017c\7t\2\2\u017c\u017d\7w\2\2\u017d\u017e")
        buf.write("\7g\2\2\u017e(\3\2\2\2\u017f\u0180\7h\2\2\u0180\u0181")
        buf.write("\7c\2\2\u0181\u0182\7n\2\2\u0182\u0183\7u\2\2\u0183\u0184")
        buf.write("\7g\2\2\u0184*\3\2\2\2\u0185\u0186\7h\2\2\u0186\u0187")
        buf.write("\7p\2\2\u0187,\3\2\2\2\u0188\u0189\7e\2\2\u0189\u018a")
        buf.write("\7n\2\2\u018a\u018b\7c\2\2\u018b\u018c\7u\2\2\u018c\u018d")
        buf.write("\7u\2\2\u018d.\3\2\2\2\u018e\u018f\7n\2\2\u018f\u0190")
        buf.write("\7g\2\2\u0190\u0191\7v\2\2\u0191\60\3\2\2\2\u0192\u0193")
        buf.write("\7d\2\2\u0193\u0194\7k\2\2\u0194\u0195\7p\2\2\u0195\u0196")
        buf.write("\7f\2\2\u0196\62\3\2\2\2\u0197\u0198\7v\2\2\u0198\u0199")
        buf.write("\7t\2\2\u0199\u019a\7c\2\2\u019a\u019b\7k\2\2\u019b\u019c")
        buf.write("\7v\2\2\u019c\64\3\2\2\2\u019d\u019e\7f\2\2\u019e\u019f")
        buf.write("\7g\2\2\u019f\u01a0\7h\2\2\u01a0\66\3\2\2\2\u01a1\u01a2")
        buf.write("\7r\2\2\u01a2\u01a3\7t\2\2\u01a3\u01a4\7q\2\2\u01a4\u01a5")
        buf.write("\7v\2\2\u01a5\u01a6\7q\2\2\u01a68\3\2\2\2\u01a7\u01a8")
        buf.write("\7k\2\2\u01a8\u01a9\7o\2\2\u01a9\u01aa\7r\2\2\u01aa\u01ab")
        buf.write("\7q\2\2\u01ab\u01ac\7t\2\2\u01ac\u01ad\7v\2\2\u01ad:\3")
        buf.write("\2\2\2\u01ae\u01af\7h\2\2\u01af\u01b0\7t\2\2\u01b0\u01b1")
        buf.write("\7q\2\2\u01b1\u01b2\7o\2\2\u01b2<\3\2\2\2\u01b3\u01b4")
        buf.write("\7r\2\2\u01b4\u01b5\7c\2\2\u01b5\u01b6\7e\2\2\u01b6\u01b7")
        buf.write("\7m\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9\7i\2\2\u01b9\u01ba")
        buf.write("\7g\2\2\u01ba>\3\2\2\2\u01bb\u01bc\7c\2\2\u01bc\u01bd")
        buf.write("\7u\2\2\u01bd@\3\2\2\2\u01be\u01bf\7d\2\2\u01bf\u01c0")
        buf.write("\7t\2\2\u01c0\u01c1\7g\2\2\u01c1\u01c2\7c\2\2\u01c2\u01c3")
        buf.write("\7m\2\2\u01c3B\3\2\2\2\u01c4\u01c5\7c\2\2\u01c5\u01c6")
        buf.write("\7d\2\2\u01c6\u01c7\7u\2\2\u01c7\u01c8\7v\2\2\u01c8\u01c9")
        buf.write("\7t\2\2\u01c9\u01ca\7c\2\2\u01ca\u01cb\7e\2\2\u01cb\u01cc")
        buf.write("\7v\2\2\u01ccD\3\2\2\2\u01cd\u01ce\7u\2\2\u01ce\u01cf")
        buf.write("\7g\2\2\u01cf\u01d0\7n\2\2\u01d0\u01d1\7g\2\2\u01d1\u01d2")
        buf.write("\7e\2\2\u01d2\u01d3\7v\2\2\u01d3F\3\2\2\2\u01d4\u01d5")
        buf.write("\7k\2\2\u01d5\u01d6\7p\2\2\u01d6\u01d7\7r\2\2\u01d7\u01d8")
        buf.write("\7w\2\2\u01d8\u01d9\7v\2\2\u01d9H\3\2\2\2\u01da\u01db")
        buf.write("\7g\2\2\u01db\u01dc\7c\2\2\u01dc\u01dd\7e\2\2\u01dd\u01de")
        buf.write("\7j\2\2\u01deJ\3\2\2\2\u01df\u01e0\7p\2\2\u01e0\u01e1")
        buf.write("\7g\2\2\u01e1\u01e2\7y\2\2\u01e2L\3\2\2\2\u01e3\u01e4")
        buf.write("\7e\2\2\u01e4\u01e5\7q\2\2\u01e5\u01e6\7p\2\2\u01e6\u01e7")
        buf.write("\7v\2\2\u01e7\u01e8\7k\2\2\u01e8\u01e9\7p\2\2\u01e9\u01ea")
        buf.write("\7w\2\2\u01ea\u01eb\7g\2\2\u01ebN\3\2\2\2\u01ec\u01ed")
        buf.write("\7g\2\2\u01ed\u01ee\7z\2\2\u01ee\u01ef\7r\2\2\u01ef\u01f0")
        buf.write("\7q\2\2\u01f0\u01f1\7t\2\2\u01f1\u01f2\7v\2\2\u01f2P\3")
        buf.write("\2\2\2\u01f3\u01f4\7k\2\2\u01f4\u01f5\7p\2\2\u01f5\u01f6")
        buf.write("\7e\2\2\u01f6\u01f7\7n\2\2\u01f7\u01f8\7w\2\2\u01f8\u01f9")
        buf.write("\7f\2\2\u01f9\u01fa\7g\2\2\u01faR\3\2\2\2\u01fb\u01fc")
        buf.write("\7t\2\2\u01fc\u01fd\7g\2\2\u01fd\u01fe\7s\2\2\u01fe\u01ff")
        buf.write("\7w\2\2\u01ff\u0200\7k\2\2\u0200\u0201\7t\2\2\u0201\u0202")
        buf.write("\7g\2\2\u0202T\3\2\2\2\u0203\u0204\7u\2\2\u0204\u0205")
        buf.write("\7w\2\2\u0205\u0206\7o\2\2\u0206\u0207\7o\2\2\u0207\u0208")
        buf.write("\7q\2\2\u0208\u0209\7p\2\2\u0209V\3\2\2\2\u020a\u020b")
        buf.write("\7<\2\2\u020b\u020c\7?\2\2\u020cX\3\2\2\2\u020d\u020e")
        buf.write("\7?\2\2\u020eZ\3\2\2\2\u020f\u0210\7?\2\2\u0210\u0211")
        buf.write("\7?\2\2\u0211\\\3\2\2\2\u0212\u0213\7#\2\2\u0213\u0214")
        buf.write("\7?\2\2\u0214^\3\2\2\2\u0215\u0216\7>\2\2\u0216\u0217")
        buf.write("\7?\2\2\u0217`\3\2\2\2\u0218\u0219\7@\2\2\u0219\u021a")
        buf.write("\7?\2\2\u021ab\3\2\2\2\u021b\u021c\7-\2\2\u021cd\3\2\2")
        buf.write("\2\u021d\u021e\7/\2\2\u021ef\3\2\2\2\u021f\u0220\7,\2")
        buf.write("\2\u0220h\3\2\2\2\u0221\u0222\7\61\2\2\u0222j\3\2\2\2")
        buf.write("\u0223\u0224\7>\2\2\u0224l\3\2\2\2\u0225\u0226\7@\2\2")
        buf.write("\u0226n\3\2\2\2\u0227\u0228\7>\2\2\u0228\u0229\7?\2\2")
        buf.write("\u0229p\3\2\2\2\u022a\u022b\7@\2\2\u022b\u022c\7?\2\2")
        buf.write("\u022cr\3\2\2\2\u022d\u022e\7#\2\2\u022et\3\2\2\2\u022f")
        buf.write("\u0230\7`\2\2\u0230v\3\2\2\2\u0231\u0232\7\'\2\2\u0232")
        buf.write("x\3\2\2\2\u0233\u0234\7~\2\2\u0234z\3\2\2\2\u0235\u0236")
        buf.write("\7~\2\2\u0236\u0237\7~\2\2\u0237|\3\2\2\2\u0238\u0239")
        buf.write("\7%\2\2\u0239~\3\2\2\2\u023a\u023b\7(\2\2\u023b\u0080")
        buf.write("\3\2\2\2\u023c\u023d\7(\2\2\u023d\u023e\7(\2\2\u023e\u0082")
        buf.write("\3\2\2\2\u023f\u0240\7B\2\2\u0240\u0084\3\2\2\2\u0241")
        buf.write("\u0242\7B\2\2\u0242\u0243\7B\2\2\u0243\u0086\3\2\2\2\u0244")
        buf.write("\u0245\7~\2\2\u0245\u0246\7@\2\2\u0246\u0088\3\2\2\2\u0247")
        buf.write("\u0248\7k\2\2\u0248\u0249\7p\2\2\u0249\u0252\7v\2\2\u024a")
        buf.write("\u024b\7k\2\2\u024b\u024c\7p\2\2\u024c\u024d\7v\2\2\u024d")
        buf.write("\u024e\7g\2\2\u024e\u024f\7i\2\2\u024f\u0250\7g\2\2\u0250")
        buf.write("\u0252\7t\2\2\u0251\u0247\3\2\2\2\u0251\u024a\3\2\2\2")
        buf.write("\u0252\u008a\3\2\2\2\u0253\u0254\7h\2\2\u0254\u0255\7")
        buf.write("n\2\2\u0255\u025c\7v\2\2\u0256\u0257\7h\2\2\u0257\u0258")
        buf.write("\7n\2\2\u0258\u0259\7q\2\2\u0259\u025a\7c\2\2\u025a\u025c")
        buf.write("\7v\2\2\u025b\u0253\3\2\2\2\u025b\u0256\3\2\2\2\u025c")
        buf.write("\u008c\3\2\2\2\u025d\u025e\7u\2\2\u025e\u025f\7v\2\2\u025f")
        buf.write("\u0267\7t\2\2\u0260\u0261\7u\2\2\u0261\u0262\7v\2\2\u0262")
        buf.write("\u0263\7t\2\2\u0263\u0264\7k\2\2\u0264\u0265\7p\2\2\u0265")
        buf.write("\u0267\7i\2\2\u0266\u025d\3\2\2\2\u0266\u0260\3\2\2\2")
        buf.write("\u0267\u008e\3\2\2\2\u0268\u0269\7d\2\2\u0269\u026a\7")
        buf.write("q\2\2\u026a\u026b\7q\2\2\u026b\u0274\7n\2\2\u026c\u026d")
        buf.write("\7d\2\2\u026d\u026e\7q\2\2\u026e\u026f\7q\2\2\u026f\u0270")
        buf.write("\7n\2\2\u0270\u0271\7g\2\2\u0271\u0272\7c\2\2\u0272\u0274")
        buf.write("\7p\2\2\u0273\u0268\3\2\2\2\u0273\u026c\3\2\2\2\u0274")
        buf.write("\u0090\3\2\2\2\u0275\u0276\7.\2\2\u0276\u0092\3\2\2\2")
        buf.write("\u0277\u0278\7*\2\2\u0278\u0279\bJ\2\2\u0279\u0094\3\2")
        buf.write("\2\2\u027a\u027b\7+\2\2\u027b\u027c\bK\3\2\u027c\u0096")
        buf.write("\3\2\2\2\u027d\u027e\7}\2\2\u027e\u027f\bL\4\2\u027f\u0098")
        buf.write("\3\2\2\2\u0280\u0281\7\177\2\2\u0281\u0282\bM\5\2\u0282")
        buf.write("\u009a\3\2\2\2\u0283\u0284\7]\2\2\u0284\u0285\bN\6\2\u0285")
        buf.write("\u009c\3\2\2\2\u0286\u0287\7_\2\2\u0287\u0288\bO\7\2\u0288")
        buf.write("\u009e\3\2\2\2\u0289\u028a\7/\2\2\u028a\u028b\7@\2\2\u028b")
        buf.write("\u00a0\3\2\2\2\u028c\u028d\7>\2\2\u028d\u028e\7/\2\2\u028e")
        buf.write("\u00a2\3\2\2\2\u028f\u0290\7<\2\2\u0290\u00a4\3\2\2\2")
        buf.write("\u0291\u0292\7\60\2\2\u0292\u00a6\3\2\2\2\u0293\u0294")
        buf.write("\7\60\2\2\u0294\u0295\7\60\2\2\u0295\u0296\7\60\2\2\u0296")
        buf.write("\u00a8\3\2\2\2\u0297\u0298\7-\2\2\u0298\u0299\7-\2\2\u0299")
        buf.write("\u00aa\3\2\2\2\u029a\u029b\7/\2\2\u029b\u029c\7/\2\2\u029c")
        buf.write("\u00ac\3\2\2\2\u029d\u029e\7h\2\2\u029e\u029f\7n\2\2\u029f")
        buf.write("\u02a0\7q\2\2\u02a0\u02a1\7c\2\2\u02a1\u02a2\7v\2\2\u02a2")
        buf.write("\u00ae\3\2\2\2\u02a3\u02a4\7u\2\2\u02a4\u02a5\7v\2\2\u02a5")
        buf.write("\u02a6\7t\2\2\u02a6\u02a7\7k\2\2\u02a7\u02a8\7p\2\2\u02a8")
        buf.write("\u02a9\7i\2\2\u02a9\u00b0\3\2\2\2\u02aa\u02ab\7d\2\2\u02ab")
        buf.write("\u02ac\7q\2\2\u02ac\u02ad\7q\2\2\u02ad\u02ae\7n\2\2\u02ae")
        buf.write("\u00b2\3\2\2\2\u02af\u02b0\7p\2\2\u02b0\u02b1\7w\2\2\u02b1")
        buf.write("\u02b2\7n\2\2\u02b2\u02b3\7n\2\2\u02b3\u00b4\3\2\2\2\u02b4")
        buf.write("\u02b5\7e\2\2\u02b5\u02b6\7j\2\2\u02b6\u02b7\7c\2\2\u02b7")
        buf.write("\u02b8\7t\2\2\u02b8\u00b6\3\2\2\2\u02b9\u02c2\7\62\2\2")
        buf.write("\u02ba\u02be\t\2\2\2\u02bb\u02bd\t\3\2\2\u02bc\u02bb\3")
        buf.write("\2\2\2\u02bd\u02c0\3\2\2\2\u02be\u02bc\3\2\2\2\u02be\u02bf")
        buf.write("\3\2\2\2\u02bf\u02c2\3\2\2\2\u02c0\u02be\3\2\2\2\u02c1")
        buf.write("\u02b9\3\2\2\2\u02c1\u02ba\3\2\2\2\u02c2\u00b8\3\2\2\2")
        buf.write("\u02c3\u02d2\7\62\2\2\u02c4\u02c8\t\2\2\2\u02c5\u02c7")
        buf.write("\t\3\2\2\u02c6\u02c5\3\2\2\2\u02c7\u02ca\3\2\2\2\u02c8")
        buf.write("\u02c6\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u02cb\3\2\2\2")
        buf.write("\u02ca\u02c8\3\2\2\2\u02cb\u02cd\7\60\2\2\u02cc\u02ce")
        buf.write("\t\3\2\2\u02cd\u02cc\3\2\2\2\u02ce\u02cf\3\2\2\2\u02cf")
        buf.write("\u02cd\3\2\2\2\u02cf\u02d0\3\2\2\2\u02d0\u02d2\3\2\2\2")
        buf.write("\u02d1\u02c3\3\2\2\2\u02d1\u02c4\3\2\2\2\u02d2\u00ba\3")
        buf.write("\2\2\2\u02d3\u02d4\7=\2\2\u02d4\u00bc\3\2\2\2\u02d5\u02d7")
        buf.write("\t\4\2\2\u02d6\u02d5\3\2\2\2\u02d7\u02da\3\2\2\2\u02d8")
        buf.write("\u02d6\3\2\2\2\u02d8\u02d9\3\2\2\2\u02d9\u02db\3\2\2\2")
        buf.write("\u02da\u02d8\3\2\2\2\u02db\u02df\t\5\2\2\u02dc\u02de\t")
        buf.write("\6\2\2\u02dd\u02dc\3\2\2\2\u02de\u02e1\3\2\2\2\u02df\u02dd")
        buf.write("\3\2\2\2\u02df\u02e0\3\2\2\2\u02e0\u00be\3\2\2\2\u02e1")
        buf.write("\u02df\3\2\2\2\u02e2\u02e3\t\7\2\2\u02e3\u00c0\3\2\2\2")
        buf.write("\u02e4\u02e5\t\b\2\2\u02e5\u00c2\3\2\2\2\u02e6\u02e7\t")
        buf.write("\t\2\2\u02e7\u00c4\3\2\2\2\u02e8\u02e9\t\n\2\2\u02e9\u02ea")
        buf.write("\3\2\2\2\u02ea\u02eb\bc\b\2\u02eb\u00c6\3\2\2\2\u02ec")
        buf.write("\u02ee\t\13\2\2\u02ed\u02ec\3\2\2\2\u02ee\u02ef\3\2\2")
        buf.write("\2\u02ef\u02ed\3\2\2\2\u02ef\u02f0\3\2\2\2\u02f0\u00c8")
        buf.write("\3\2\2\2\u02f1\u02f5\5\u0115\u008b\2\u02f2\u02f4\5\u0117")
        buf.write("\u008c\2\u02f3\u02f2\3\2\2\2\u02f4\u02f7\3\2\2\2\u02f5")
        buf.write("\u02f3\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u00ca\3\2\2\2")
        buf.write("\u02f7\u02f5\3\2\2\2\u02f8\u02f9\7\61\2\2\u02f9\u02fa")
        buf.write("\7\61\2\2\u02fa\u02fe\3\2\2\2\u02fb\u02fd\n\f\2\2\u02fc")
        buf.write("\u02fb\3\2\2\2\u02fd\u0300\3\2\2\2\u02fe\u02fc\3\2\2\2")
        buf.write("\u02fe\u02ff\3\2\2\2\u02ff\u0302\3\2\2\2\u0300\u02fe\3")
        buf.write("\2\2\2\u0301\u0303\7\17\2\2\u0302\u0301\3\2\2\2\u0302")
        buf.write("\u0303\3\2\2\2\u0303\u0304\3\2\2\2\u0304\u0311\7\f\2\2")
        buf.write("\u0305\u0306\7\61\2\2\u0306\u0307\7,\2\2\u0307\u030b\3")
        buf.write("\2\2\2\u0308\u030a\13\2\2\2\u0309\u0308\3\2\2\2\u030a")
        buf.write("\u030d\3\2\2\2\u030b\u030c\3\2\2\2\u030b\u0309\3\2\2\2")
        buf.write("\u030c\u030e\3\2\2\2\u030d\u030b\3\2\2\2\u030e\u030f\7")
        buf.write(",\2\2\u030f\u0311\7\61\2\2\u0310\u02f8\3\2\2\2\u0310\u0305")
        buf.write("\3\2\2\2\u0311\u00cc\3\2\2\2\u0312\u0315\5\u00d3j\2\u0313")
        buf.write("\u0315\5\u00d5k\2\u0314\u0312\3\2\2\2\u0314\u0313\3\2")
        buf.write("\2\2\u0315\u00ce\3\2\2\2\u0316\u031a\5\u00d1i\2\u0317")
        buf.write("\u031a\5\u00dfp\2\u0318\u031a\5\u00e1q\2\u0319\u0316\3")
        buf.write("\2\2\2\u0319\u0317\3\2\2\2\u0319\u0318\3\2\2\2\u031a\u00d0")
        buf.write("\3\2\2\2\u031b\u0320\5\u00d7l\2\u031c\u0320\5\u00d9m\2")
        buf.write("\u031d\u0320\5\u00dbn\2\u031e\u0320\5\u00ddo\2\u031f\u031b")
        buf.write("\3\2\2\2\u031f\u031c\3\2\2\2\u031f\u031d\3\2\2\2\u031f")
        buf.write("\u031e\3\2\2\2\u0320\u00d2\3\2\2\2\u0321\u0327\t\r\2\2")
        buf.write("\u0322\u0323\t\16\2\2\u0323\u0327\t\17\2\2\u0324\u0325")
        buf.write("\t\17\2\2\u0325\u0327\t\16\2\2\u0326\u0321\3\2\2\2\u0326")
        buf.write("\u0322\3\2\2\2\u0326\u0324\3\2\2\2\u0326\u0327\3\2\2\2")
        buf.write("\u0327\u032a\3\2\2\2\u0328\u032b\5\u00e7t\2\u0329\u032b")
        buf.write("\5\u00e9u\2\u032a\u0328\3\2\2\2\u032a\u0329\3\2\2\2\u032b")
        buf.write("\u00d4\3\2\2\2\u032c\u0332\t\20\2\2\u032d\u032e\t\20\2")
        buf.write("\2\u032e\u0332\t\17\2\2\u032f\u0330\t\17\2\2\u0330\u0332")
        buf.write("\t\20\2\2\u0331\u032c\3\2\2\2\u0331\u032d\3\2\2\2\u0331")
        buf.write("\u032f\3\2\2\2\u0332\u0335\3\2\2\2\u0333\u0336\5\u0105")
        buf.write("\u0083\2\u0334\u0336\5\u0107\u0084\2\u0335\u0333\3\2\2")
        buf.write("\2\u0335\u0334\3\2\2\2\u0336\u00d6\3\2\2\2\u0337\u033b")
        buf.write("\5\u00f1y\2\u0338\u033a\5\u00f3z\2\u0339\u0338\3\2\2\2")
        buf.write("\u033a\u033d\3\2\2\2\u033b\u0339\3\2\2\2\u033b\u033c\3")
        buf.write("\2\2\2\u033c\u0344\3\2\2\2\u033d\u033b\3\2\2\2\u033e\u0340")
        buf.write("\7\62\2\2\u033f\u033e\3\2\2\2\u0340\u0341\3\2\2\2\u0341")
        buf.write("\u033f\3\2\2\2\u0341\u0342\3\2\2\2\u0342\u0344\3\2\2\2")
        buf.write("\u0343\u0337\3\2\2\2\u0343\u033f\3\2\2\2\u0344\u00d8\3")
        buf.write("\2\2\2\u0345\u0346\7\62\2\2\u0346\u0348\t\21\2\2\u0347")
        buf.write("\u0349\5\u00f5{\2\u0348\u0347\3\2\2\2\u0349\u034a\3\2")
        buf.write("\2\2\u034a\u0348\3\2\2\2\u034a\u034b\3\2\2\2\u034b\u00da")
        buf.write("\3\2\2\2\u034c\u034d\7\62\2\2\u034d\u034f\t\22\2\2\u034e")
        buf.write("\u0350\5\u00f7|\2\u034f\u034e\3\2\2\2\u0350\u0351\3\2")
        buf.write("\2\2\u0351\u034f\3\2\2\2\u0351\u0352\3\2\2\2\u0352\u00dc")
        buf.write("\3\2\2\2\u0353\u0354\7\62\2\2\u0354\u0356\t\20\2\2\u0355")
        buf.write("\u0357\5\u00f9}\2\u0356\u0355\3\2\2\2\u0357\u0358\3\2")
        buf.write("\2\2\u0358\u0356\3\2\2\2\u0358\u0359\3\2\2\2\u0359\u00de")
        buf.write("\3\2\2\2\u035a\u035d\5\u00fb~\2\u035b\u035d\5\u00fd\177")
        buf.write("\2\u035c\u035a\3\2\2\2\u035c\u035b\3\2\2\2\u035d\u00e0")
        buf.write("\3\2\2\2\u035e\u0361\5\u00dfp\2\u035f\u0361\5\u00ff\u0080")
        buf.write("\2\u0360\u035e\3\2\2\2\u0360\u035f\3\2\2\2\u0361\u0362")
        buf.write("\3\2\2\2\u0362\u0363\t\23\2\2\u0363\u00e2\3\2\2\2\u0364")
        buf.write("\u0368\5\u00c7d\2\u0365\u0368\5\u00cbf\2\u0366\u0368\5")
        buf.write("\u0113\u008a\2\u0367\u0364\3\2\2\2\u0367\u0365\3\2\2\2")
        buf.write("\u0367\u0366\3\2\2\2\u0368\u0369\3\2\2\2\u0369\u036a\b")
        buf.write("r\t\2\u036a\u00e4\3\2\2\2\u036b\u036c\13\2\2\2\u036c\u00e6")
        buf.write("\3\2\2\2\u036d\u0372\7)\2\2\u036e\u0371\5\u00efx\2\u036f")
        buf.write("\u0371\n\24\2\2\u0370\u036e\3\2\2\2\u0370\u036f\3\2\2")
        buf.write("\2\u0371\u0374\3\2\2\2\u0372\u0370\3\2\2\2\u0372\u0373")
        buf.write("\3\2\2\2\u0373\u0375\3\2\2\2\u0374\u0372\3\2\2\2\u0375")
        buf.write("\u0380\7)\2\2\u0376\u037b\7$\2\2\u0377\u037a\5\u00efx")
        buf.write("\2\u0378\u037a\n\25\2\2\u0379\u0377\3\2\2\2\u0379\u0378")
        buf.write("\3\2\2\2\u037a\u037d\3\2\2\2\u037b\u0379\3\2\2\2\u037b")
        buf.write("\u037c\3\2\2\2\u037c\u037e\3\2\2\2\u037d\u037b\3\2\2\2")
        buf.write("\u037e\u0380\7$\2\2\u037f\u036d\3\2\2\2\u037f\u0376\3")
        buf.write("\2\2\2\u0380\u00e8\3\2\2\2\u0381\u0382\7)\2\2\u0382\u0383")
        buf.write("\7)\2\2\u0383\u0384\7)\2\2\u0384\u0388\3\2\2\2\u0385\u0387")
        buf.write("\5\u00ebv\2\u0386\u0385\3\2\2\2\u0387\u038a\3\2\2\2\u0388")
        buf.write("\u0389\3\2\2\2\u0388\u0386\3\2\2\2\u0389\u038b\3\2\2\2")
        buf.write("\u038a\u0388\3\2\2\2\u038b\u038c\7)\2\2\u038c\u038d\7")
        buf.write(")\2\2\u038d\u039c\7)\2\2\u038e\u038f\7$\2\2\u038f\u0390")
        buf.write("\7$\2\2\u0390\u0391\7$\2\2\u0391\u0395\3\2\2\2\u0392\u0394")
        buf.write("\5\u00ebv\2\u0393\u0392\3\2\2\2\u0394\u0397\3\2\2\2\u0395")
        buf.write("\u0396\3\2\2\2\u0395\u0393\3\2\2\2\u0396\u0398\3\2\2\2")
        buf.write("\u0397\u0395\3\2\2\2\u0398\u0399\7$\2\2\u0399\u039a\7")
        buf.write("$\2\2\u039a\u039c\7$\2\2\u039b\u0381\3\2\2\2\u039b\u038e")
        buf.write("\3\2\2\2\u039c\u00ea\3\2\2\2\u039d\u03a0\5\u00edw\2\u039e")
        buf.write("\u03a0\5\u00efx\2\u039f\u039d\3\2\2\2\u039f\u039e\3\2")
        buf.write("\2\2\u03a0\u00ec\3\2\2\2\u03a1\u03a2\n\26\2\2\u03a2\u00ee")
        buf.write("\3\2\2\2\u03a3\u03a4\7^\2\2\u03a4\u03a8\13\2\2\2\u03a5")
        buf.write("\u03a6\7^\2\2\u03a6\u03a8\5\u0119\u008d\2\u03a7\u03a3")
        buf.write("\3\2\2\2\u03a7\u03a5\3\2\2\2\u03a8\u00f0\3\2\2\2\u03a9")
        buf.write("\u03aa\t\2\2\2\u03aa\u00f2\3\2\2\2\u03ab\u03ac\t\3\2\2")
        buf.write("\u03ac\u00f4\3\2\2\2\u03ad\u03ae\t\27\2\2\u03ae\u00f6")
        buf.write("\3\2\2\2\u03af\u03b0\t\30\2\2\u03b0\u00f8\3\2\2\2\u03b1")
        buf.write("\u03b2\t\31\2\2\u03b2\u00fa\3\2\2\2\u03b3\u03b5\5\u00ff")
        buf.write("\u0080\2\u03b4\u03b3\3\2\2\2\u03b4\u03b5\3\2\2\2\u03b5")
        buf.write("\u03b6\3\2\2\2\u03b6\u03bb\5\u0101\u0081\2\u03b7\u03b8")
        buf.write("\5\u00ff\u0080\2\u03b8\u03b9\7\60\2\2\u03b9\u03bb\3\2")
        buf.write("\2\2\u03ba\u03b4\3\2\2\2\u03ba\u03b7\3\2\2\2\u03bb\u00fc")
        buf.write("\3\2\2\2\u03bc\u03bf\5\u00ff\u0080\2\u03bd\u03bf\5\u00fb")
        buf.write("~\2\u03be\u03bc\3\2\2\2\u03be\u03bd\3\2\2\2\u03bf\u03c0")
        buf.write("\3\2\2\2\u03c0\u03c1\5\u0103\u0082\2\u03c1\u00fe\3\2\2")
        buf.write("\2\u03c2\u03c4\5\u00f3z\2\u03c3\u03c2\3\2\2\2\u03c4\u03c5")
        buf.write("\3\2\2\2\u03c5\u03c3\3\2\2\2\u03c5\u03c6\3\2\2\2\u03c6")
        buf.write("\u0100\3\2\2\2\u03c7\u03c9\7\60\2\2\u03c8\u03ca\5\u00f3")
        buf.write("z\2\u03c9\u03c8\3\2\2\2\u03ca\u03cb\3\2\2\2\u03cb\u03c9")
        buf.write("\3\2\2\2\u03cb\u03cc\3\2\2\2\u03cc\u0102\3\2\2\2\u03cd")
        buf.write("\u03cf\t\32\2\2\u03ce\u03d0\t\33\2\2\u03cf\u03ce\3\2\2")
        buf.write("\2\u03cf\u03d0\3\2\2\2\u03d0\u03d2\3\2\2\2\u03d1\u03d3")
        buf.write("\5\u00f3z\2\u03d2\u03d1\3\2\2\2\u03d3\u03d4\3\2\2\2\u03d4")
        buf.write("\u03d2\3\2\2\2\u03d4\u03d5\3\2\2\2\u03d5\u0104\3\2\2\2")
        buf.write("\u03d6\u03db\7)\2\2\u03d7\u03da\5\u010b\u0086\2\u03d8")
        buf.write("\u03da\5\u0111\u0089\2\u03d9\u03d7\3\2\2\2\u03d9\u03d8")
        buf.write("\3\2\2\2\u03da\u03dd\3\2\2\2\u03db\u03d9\3\2\2\2\u03db")
        buf.write("\u03dc\3\2\2\2\u03dc\u03de\3\2\2\2\u03dd\u03db\3\2\2\2")
        buf.write("\u03de\u03e9\7)\2\2\u03df\u03e4\7$\2\2\u03e0\u03e3\5\u010d")
        buf.write("\u0087\2\u03e1\u03e3\5\u0111\u0089\2\u03e2\u03e0\3\2\2")
        buf.write("\2\u03e2\u03e1\3\2\2\2\u03e3\u03e6\3\2\2\2\u03e4\u03e2")
        buf.write("\3\2\2\2\u03e4\u03e5\3\2\2\2\u03e5\u03e7\3\2\2\2\u03e6")
        buf.write("\u03e4\3\2\2\2\u03e7\u03e9\7$\2\2\u03e8\u03d6\3\2\2\2")
        buf.write("\u03e8\u03df\3\2\2\2\u03e9\u0106\3\2\2\2\u03ea\u03eb\7")
        buf.write(")\2\2\u03eb\u03ec\7)\2\2\u03ec\u03ed\7)\2\2\u03ed\u03f1")
        buf.write("\3\2\2\2\u03ee\u03f0\5\u0109\u0085\2\u03ef\u03ee\3\2\2")
        buf.write("\2\u03f0\u03f3\3\2\2\2\u03f1\u03f2\3\2\2\2\u03f1\u03ef")
        buf.write("\3\2\2\2\u03f2\u03f4\3\2\2\2\u03f3\u03f1\3\2\2\2\u03f4")
        buf.write("\u03f5\7)\2\2\u03f5\u03f6\7)\2\2\u03f6\u0405\7)\2\2\u03f7")
        buf.write("\u03f8\7$\2\2\u03f8\u03f9\7$\2\2\u03f9\u03fa\7$\2\2\u03fa")
        buf.write("\u03fe\3\2\2\2\u03fb\u03fd\5\u0109\u0085\2\u03fc\u03fb")
        buf.write("\3\2\2\2\u03fd\u0400\3\2\2\2\u03fe\u03ff\3\2\2\2\u03fe")
        buf.write("\u03fc\3\2\2\2\u03ff\u0401\3\2\2\2\u0400\u03fe\3\2\2\2")
        buf.write("\u0401\u0402\7$\2\2\u0402\u0403\7$\2\2\u0403\u0405\7$")
        buf.write("\2\2\u0404\u03ea\3\2\2\2\u0404\u03f7\3\2\2\2\u0405\u0108")
        buf.write("\3\2\2\2\u0406\u0409\5\u010f\u0088\2\u0407\u0409\5\u0111")
        buf.write("\u0089\2\u0408\u0406\3\2\2\2\u0408\u0407\3\2\2\2\u0409")
        buf.write("\u010a\3\2\2\2\u040a\u040c\t\34\2\2\u040b\u040a\3\2\2")
        buf.write("\2\u040c\u010c\3\2\2\2\u040d\u040f\t\35\2\2\u040e\u040d")
        buf.write("\3\2\2\2\u040f\u010e\3\2\2\2\u0410\u0412\t\36\2\2\u0411")
        buf.write("\u0410\3\2\2\2\u0412\u0110\3\2\2\2\u0413\u0414\7^\2\2")
        buf.write("\u0414\u0415\t\37\2\2\u0415\u0112\3\2\2\2\u0416\u0418")
        buf.write("\7^\2\2\u0417\u0419\5\u00c7d\2\u0418\u0417\3\2\2\2\u0418")
        buf.write("\u0419\3\2\2\2\u0419\u041f\3\2\2\2\u041a\u041c\7\17\2")
        buf.write("\2\u041b\u041a\3\2\2\2\u041b\u041c\3\2\2\2\u041c\u041d")
        buf.write("\3\2\2\2\u041d\u0420\7\f\2\2\u041e\u0420\4\16\17\2\u041f")
        buf.write("\u041b\3\2\2\2\u041f\u041e\3\2\2\2\u0420\u0114\3\2\2\2")
        buf.write("\u0421\u0423\t \2\2\u0422\u0421\3\2\2\2\u0423\u0116\3")
        buf.write("\2\2\2\u0424\u0427\5\u0115\u008b\2\u0425\u0427\t!\2\2")
        buf.write("\u0426\u0424\3\2\2\2\u0426\u0425\3\2\2\2\u0427\u0118\3")
        buf.write("\2\2\2\u0428\u0429\6\u008d\2\2\u0429\u0435\5\u00c7d\2")
        buf.write("\u042a\u042c\7\17\2\2\u042b\u042a\3\2\2\2\u042b\u042c")
        buf.write("\3\2\2\2\u042c\u042d\3\2\2\2\u042d\u0430\7\f\2\2\u042e")
        buf.write("\u0430\4\16\17\2\u042f\u042b\3\2\2\2\u042f\u042e\3\2\2")
        buf.write("\2\u0430\u0432\3\2\2\2\u0431\u0433\5\u00c7d\2\u0432\u0431")
        buf.write("\3\2\2\2\u0432\u0433\3\2\2\2\u0433\u0435\3\2\2\2\u0434")
        buf.write("\u0428\3\2\2\2\u0434\u042f\3\2\2\2\u0435\u0436\3\2\2\2")
        buf.write("\u0436\u0437\b\u008d\n\2\u0437\u011a\3\2\2\2P\2\u011e")
        buf.write("\u0124\u0126\u012c\u0132\u0134\u0251\u025b\u0266\u0273")
        buf.write("\u02be\u02c1\u02c8\u02cf\u02d1\u02d8\u02df\u02ef\u02f5")
        buf.write("\u02fe\u0302\u030b\u0310\u0314\u0319\u031f\u0326\u032a")
        buf.write("\u0331\u0335\u033b\u0341\u0343\u034a\u0351\u0358\u035c")
        buf.write("\u0360\u0367\u0370\u0372\u0379\u037b\u037f\u0388\u0395")
        buf.write("\u039b\u039f\u03a7\u03b4\u03ba\u03be\u03c5\u03cb\u03cf")
        buf.write("\u03d4\u03d9\u03db\u03e2\u03e4\u03e8\u03f1\u03fe\u0404")
        buf.write("\u0408\u040b\u040e\u0411\u0418\u041b\u041f\u0422\u0426")
        buf.write("\u042b\u042f\u0432\u0434\13\3J\2\3K\3\3L\4\3M\5\3N\6\3")
        buf.write("O\7\2\3\2\b\2\2\3\u008d\b")
        return buf.getvalue()


class JingleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CONSUME = 2

    INDENT = 1
    DEDENT = 2
    ENDSTATEMENT = 3
    SEMICOLONTERMINATE = 4
    SPEECHMARKS = 5
    VAR = 6
    ARRAY = 7
    CONST = 8
    LOCAL = 9
    ECHO = 10
    RETURN = 11
    IF = 12
    THEN = 13
    AND = 14
    OR = 15
    IN = 16
    ELSE = 17
    ELSEIF = 18
    WHILE = 19
    FOR = 20
    TRUE = 21
    FALSE = 22
    FUNCTION = 23
    CLASS = 24
    LET = 25
    BIND = 26
    TRAIT = 27
    DEFINE = 28
    PROTOCOL = 29
    IMPORT = 30
    FROM = 31
    PACKAGE = 32
    AS = 33
    BREAK = 34
    ABSTRACT = 35
    SELECT = 36
    INPUT = 37
    EACH = 38
    NEW = 39
    CONTINUE = 40
    EXPORT = 41
    INCLUDE = 42
    REQUIRE = 43
    SUMMON = 44
    WALRUS = 45
    EQUALS = 46
    EQEQ = 47
    NOTEQUAL = 48
    LTEQUALS = 49
    GTEQUALS = 50
    PLUS = 51
    MINUS = 52
    MULTIPLY = 53
    DIVIDE = 54
    LESSTHAN = 55
    GREATERTHAN = 56
    LESSTHANEQUAL = 57
    MORETHANEQUAL = 58
    BANG = 59
    POWER = 60
    MODULUS = 61
    VERTICAL = 62
    ORSYMBOL = 63
    HASH = 64
    AMBERSAND = 65
    ANDSYMBOL = 66
    ATSYMBOL = 67
    ATTSYMBOL = 68
    PIPE = 69
    TYPE_INT = 70
    TYPE_DECIMAL = 71
    TYPE_STRING = 72
    TYPE_BOOLEAN = 73
    COMMA = 74
    LBRACKET = 75
    RBRACKET = 76
    LBRACE = 77
    RBRACE = 78
    LSQRBRACKET = 79
    RSQRBRACKET = 80
    ARROW = 81
    BACKARROW = 82
    COLON = 83
    DOT = 84
    ELLIPSIS = 85
    PLUSPLUS = 86
    MINUSMINUS = 87
    FLOAT_IDENTIFIER = 88
    STRING_IDENTIFIER = 89
    BOOLEAN_IDENTIFIER = 90
    NULL_IDENTIFIER = 91
    CHAR_IDENTIFIER = 92
    INT_LITERAL = 93
    FLOAT_LITERAL = 94
    IDENTIFIER = 95
    COMMENT = 96
    STRING = 97
    NUMBER = 98
    INTEGER = 99
    STRING_LITERAL = 100
    BYTES_LITERAL = 101
    DECIMAL_INTEGER = 102
    OCT_INTEGER = 103
    HEX_INTEGER = 104
    BIN_INTEGER = 105
    FLOAT_NUMBER = 106
    IMAG_NUMBER = 107
    SKIP_ = 108
    UNKNOWN_CHAR = 109
    NEWLINE = 110

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"CONSUME" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"'", "'var'", "'arr'", "'con'", "'loc'", "'echo'", "'return'", 
            "'if'", "'then'", "'and'", "'or'", "'in'", "'else'", "'elif'", 
            "'while'", "'for'", "'true'", "'false'", "'fn'", "'class'", 
            "'let'", "'bind'", "'trait'", "'def'", "'proto'", "'import'", 
            "'from'", "'package'", "'as'", "'break'", "'abstract'", "'select'", 
            "'input'", "'each'", "'new'", "'continue'", "'export'", "'include'", 
            "'require'", "'summon'", "':='", "'='", "'=='", "'!='", "'+'", 
            "'-'", "'*'", "'/'", "'<'", "'>'", "'!'", "'^'", "'%'", "'|'", 
            "'||'", "'#'", "'&'", "'&&'", "'@'", "'@@'", "'|>'", "','", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "'->'", "'<-'", "':'", 
            "'.'", "'...'", "'++'", "'--'", "'float'", "'string'", "'bool'", 
            "'null'", "'char'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", 
            "VAR", "ARRAY", "CONST", "LOCAL", "ECHO", "RETURN", "IF", "THEN", 
            "AND", "OR", "IN", "ELSE", "ELSEIF", "WHILE", "FOR", "TRUE", 
            "FALSE", "FUNCTION", "CLASS", "LET", "BIND", "TRAIT", "DEFINE", 
            "PROTOCOL", "IMPORT", "FROM", "PACKAGE", "AS", "BREAK", "ABSTRACT", 
            "SELECT", "INPUT", "EACH", "NEW", "CONTINUE", "EXPORT", "INCLUDE", 
            "REQUIRE", "SUMMON", "WALRUS", "EQUALS", "EQEQ", "NOTEQUAL", 
            "LTEQUALS", "GTEQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
            "LESSTHAN", "GREATERTHAN", "LESSTHANEQUAL", "MORETHANEQUAL", 
            "BANG", "POWER", "MODULUS", "VERTICAL", "ORSYMBOL", "HASH", 
            "AMBERSAND", "ANDSYMBOL", "ATSYMBOL", "ATTSYMBOL", "PIPE", "TYPE_INT", 
            "TYPE_DECIMAL", "TYPE_STRING", "TYPE_BOOLEAN", "COMMA", "LBRACKET", 
            "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET", 
            "ARROW", "BACKARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", 
            "MINUSMINUS", "FLOAT_IDENTIFIER", "STRING_IDENTIFIER", "BOOLEAN_IDENTIFIER", 
            "NULL_IDENTIFIER", "CHAR_IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", 
            "IDENTIFIER", "COMMENT", "STRING", "NUMBER", "INTEGER", "STRING_LITERAL", 
            "BYTES_LITERAL", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
            "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER", "SKIP_", "UNKNOWN_CHAR", 
            "NEWLINE" ]

    ruleNames = [ "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", "VAR", 
                  "ARRAY", "CONST", "LOCAL", "ECHO", "RETURN", "IF", "THEN", 
                  "AND", "OR", "IN", "ELSE", "ELSEIF", "WHILE", "FOR", "TRUE", 
                  "FALSE", "FUNCTION", "CLASS", "LET", "BIND", "TRAIT", 
                  "DEFINE", "PROTOCOL", "IMPORT", "FROM", "PACKAGE", "AS", 
                  "BREAK", "ABSTRACT", "SELECT", "INPUT", "EACH", "NEW", 
                  "CONTINUE", "EXPORT", "INCLUDE", "REQUIRE", "SUMMON", 
                  "WALRUS", "EQUALS", "EQEQ", "NOTEQUAL", "LTEQUALS", "GTEQUALS", 
                  "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", 
                  "LESSTHANEQUAL", "MORETHANEQUAL", "BANG", "POWER", "MODULUS", 
                  "VERTICAL", "ORSYMBOL", "HASH", "AMBERSAND", "ANDSYMBOL", 
                  "ATSYMBOL", "ATTSYMBOL", "PIPE", "TYPE_INT", "TYPE_DECIMAL", 
                  "TYPE_STRING", "TYPE_BOOLEAN", "COMMA", "LBRACKET", "RBRACKET", 
                  "LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET", "ARROW", 
                  "BACKARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS", 
                  "FLOAT_IDENTIFIER", "STRING_IDENTIFIER", "BOOLEAN_IDENTIFIER", 
                  "NULL_IDENTIFIER", "CHAR_IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", 
                  "SEMICOLON", "ID", "DIGIT_CONT", "HEXDIGIT", "BINARY", 
                  "UNICODE_WS", "SPACES", "IDENTIFIER", "COMMENT", "STRING", 
                  "NUMBER", "INTEGER", "STRING_LITERAL", "BYTES_LITERAL", 
                  "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
                  "FLOAT_NUMBER", "IMAG_NUMBER", "SKIP_", "UNKNOWN_CHAR", 
                  "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM", "LONG_STRING_CHAR", 
                  "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", 
                  "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", "EXPONENT_FLOAT", 
                  "INT_PART", "FRACTION", "EXPONENT", "SHORT_BYTES", "LONG_BYTES", 
                  "LONG_BYTES_ITEM", "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", 
                  "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", "LONG_BYTES_CHAR", 
                  "BYTES_ESCAPE_SEQ", "LINE_JOINING", "ID_START", "ID_CONTINUE", 
                  "NEWLINE" ]

    grammarFileName = "JingleLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens
    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents
    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened
    @opened.setter
    def opened(self, value):
        self._opened = value
    @property
    def lastToken(self):
        try:
            return self._lastToken
        except AttributeError:
            self._lastToken = None
            return self._lastToken
    @lastToken.setter
    def lastToken(self, value):
        self._lastToken = value
    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.lastToken = None
    def emitToken(self, t):
        super().emitToken(t)
        self.tokens.append(t)
    def nextToken(self):
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)
            self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()
            self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next
        return next if not self.tokens else self.tokens.pop(0)
    def createDedent(self):
        dedent = self.commonToken(LanguageParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent
    def commonToken(self, type, text, indent=0):
        stop = self.getCharIndex()-1-indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)
    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count
    def atStartOfInput(self):
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[72] = self.LBRACKET_action 
            actions[73] = self.RBRACKET_action 
            actions[74] = self.LBRACE_action 
            actions[75] = self.RBRACE_action 
            actions[76] = self.LSQRBRACKET_action 
            actions[77] = self.RSQRBRACKET_action 
            actions[139] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LBRACKET_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.opened += 1
     

    def RBRACKET_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.opened -= 1
     

    def LBRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.opened += 1
     

    def RBRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.opened -= 1
     

    def LSQRBRACKET_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.opened += 1
     

    def RSQRBRACKET_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.opened -= 1
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            tempt = Lexer.text.fget(self)
            newLine = re.sub("[^\r\n\f]+", "", tempt)
            spaces = re.sub("[\r\n\f]+", "", tempt)
            la_char = ""
            try:
                la = self._input.LA(1)
                la_char = chr(la)       # Python does not compare char to ints directly
            except ValueError:          # End of file
                pass
            # Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
            # satisfy the final newline needed by the single_put rule used by the REPL.
            try:
                nextnext_la = self._input.LA(2)
                nextnext_la_char = chr(nextnext_la)
            except ValueError:
                nextnext_eof = True
            else:
                nextnext_eof = False
            if self.opened > 0 or nextnexteof is False and (la_char == '\r' or la_char == '\n' or la_char == '\f' or la_char == '#'):
                self.skip()
            else:
                indent = self.getIndentationCount(spaces)
                previous = self.indents[-1] if self.indents else 0
                self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.createDedent())
                        self.indents.pop()
                
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[139] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


