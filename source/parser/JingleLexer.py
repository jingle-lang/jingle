# Generated from JingleLexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
import typing
import sys

from antlr4.Token import CommonToken
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2q")
        buf.write("\u042f\b\1\b\1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6")
        buf.write("\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f")
        buf.write("\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22")
        buf.write("\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write("\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write("\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write("$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write("\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write("9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4")
        buf.write("B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4")
        buf.write("K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4")
        buf.write("T\tT\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\")
        buf.write("\4]\t]\4^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\t")
        buf.write("e\4f\tf\4g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\t")
        buf.write("n\4o\to\4p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\t")
        buf.write("w\4x\tx\4y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177")
        buf.write("\4\u0080\t\u0080\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083")
        buf.write("\t\u0083\4\u0084\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086")
        buf.write("\4\u0087\t\u0087\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a")
        buf.write("\t\u008a\4\u008b\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d")
        buf.write("\3\2\7\2\u011f\n\2\f\2\16\2\u0122\13\2\3\2\6\2\u0125\n")
        buf.write("\2\r\2\16\2\u0126\5\2\u0129\n\2\3\3\3\3\7\3\u012d\n\3")
        buf.write("\f\3\16\3\u0130\13\3\3\3\6\3\u0133\n\3\r\3\16\3\u0134")
        buf.write("\5\3\u0137\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6\u0148\n\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u015c\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0167")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u0197\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$")
        buf.write("\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\3A\5A\u0274\nA\3B\3B\3B\3B\3B\3B\3B\3B\5B\u027e\nB\3")
        buf.write("C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u0289\nC\3D\3D\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\5D\u0296\nD\3E\3E\3F\3F\3G\3G\3H\3H\3")
        buf.write("I\3I\3J\3J\3K\3K\3L\3L\3L\3M\3M\3N\3N\3O\3O\3O\3O\3P\3")
        buf.write("P\3P\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3S\3S\3S\3S\3S\3S\3S\3")
        buf.write("T\3T\3T\3T\3T\3U\3U\3U\3U\3U\3V\3V\3V\3V\3V\3W\3W\3W\7")
        buf.write("W\u02d6\nW\fW\16W\u02d9\13W\5W\u02db\nW\3X\3X\3X\7X\u02e0")
        buf.write("\nX\fX\16X\u02e3\13X\3X\3X\6X\u02e7\nX\rX\16X\u02e8\5")
        buf.write("X\u02eb\nX\3Y\3Y\3Z\3Z\3Z\5Z\u02f2\nZ\3[\7[\u02f5\n[\f")
        buf.write("[\16[\u02f8\13[\3[\3[\7[\u02fc\n[\f[\16[\u02ff\13[\3\\")
        buf.write("\3\\\3]\3]\3^\3^\3_\3_\3_\3_\3`\6`\u030c\n`\r`\16`\u030d")
        buf.write("\3`\3`\3a\3a\3a\3a\7a\u0316\na\fa\16a\u0319\13a\3a\5a")
        buf.write("\u031c\na\3a\3a\3a\3a\3a\7a\u0323\na\fa\16a\u0326\13a")
        buf.write("\3a\3a\5a\u032a\na\3a\3a\3b\6b\u032f\nb\rb\16b\u0330\3")
        buf.write("b\3b\3c\3c\3c\3c\3d\3d\3e\3e\3e\3f\3f\3f\3g\3g\3g\3h\3")
        buf.write("h\3h\3i\3i\3i\3i\3j\3j\3j\3j\3j\3k\6k\u0351\nk\rk\16k")
        buf.write("\u0352\3l\3l\3l\3l\3m\3m\3m\3m\3n\7n\u035e\nn\fn\16n\u0361")
        buf.write("\13n\3n\3n\7n\u0365\nn\fn\16n\u0368\13n\3o\3o\3o\7o\u036d")
        buf.write("\no\fo\16o\u0370\13o\3p\3p\3p\3p\3p\3p\3p\5p\u0379\np")
        buf.write("\3q\3q\3q\3q\3q\3q\3q\5q\u0382\nq\3r\3r\5r\u0386\nr\3")
        buf.write("s\3s\3s\5s\u038b\ns\3t\3t\3t\3t\3t\3t\5t\u0393\nt\3u\3")
        buf.write("u\3u\5u\u0398\nu\3v\3v\7v\u039c\nv\fv\16v\u039f\13v\3")
        buf.write("w\3w\7w\u03a3\nw\fw\16w\u03a6\13w\3x\3x\3x\6x\u03ab\n")
        buf.write("x\rx\16x\u03ac\3y\3y\3y\5y\u03b2\ny\3y\5y\u03b5\ny\3y")
        buf.write("\3y\3y\3y\3y\3y\5y\u03bd\ny\5y\u03bf\ny\3z\6z\u03c2\n")
        buf.write("z\rz\16z\u03c3\3{\3{\5{\u03c8\n{\3|\3|\3|\3|\7|\u03ce")
        buf.write("\n|\f|\16|\u03d1\13|\3|\3|\3}\3}\3}\3}\3}\7}\u03da\n}")
        buf.write("\f}\16}\u03dd\13}\3}\3}\3~\3~\3~\5~\u03e4\n~\3~\3~\3\177")
        buf.write("\3\177\3\177\3\177\5\177\u03ec\n\177\3\u0080\3\u0080\5")
        buf.write("\u0080\u03f0\n\u0080\3\u0081\3\u0081\3\u0081\3\u0081\3")
        buf.write("\u0081\3\u0082\3\u0082\3\u0082\3\u0082\3\u0082\3\u0083")
        buf.write("\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083\3\u0083")
        buf.write("\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write("\3\u0084\3\u0084\3\u0084\3\u0084\3\u0084\3\u0085\3\u0085")
        buf.write("\3\u0085\3\u0086\3\u0086\3\u0086\3\u0086\5\u0086\u0417")
        buf.write("\n\u0086\3\u0086\5\u0086\u041a\n\u0086\3\u0086\3\u0086")
        buf.write("\3\u0087\3\u0087\3\u0088\3\u0088\5\u0088\u0422\n\u0088")
        buf.write("\3\u0089\3\u0089\3\u008a\3\u008a\3\u008b\3\u008b\3\u008c")
        buf.write("\5\u008c\u042b\n\u008c\3\u008d\5\u008d\u042e\n\u008d\5")
        buf.write("\u0324\u03cf\u03db\2\u008e\5\5\7\6\t\7\13\b\r\t\17\n\21")
        buf.write("\13\23\f\25\r\27\16\31\17\33\20\35\21\37\22!\23#\24%\25")
        buf.write("\'\26)\27+\30-\31/\32\61\33\63\34\65\35\67\369\37; =!")
        buf.write("?\"A#C$E%G&I\'K(M)O*Q+S,U-W.Y/[\60]\61_\62a\63c\64e\65")
        buf.write("g\66i\67k8m9o:q;s<u=w>y?{@}A\177B\u0081C\u0083D\u0085")
        buf.write("E\u0087F\u0089G\u008bH\u008dI\u008fJ\u0091K\u0093L\u0095")
        buf.write("M\u0097N\u0099O\u009bP\u009dQ\u009fR\u00a1S\u00a3T\u00a5")
        buf.write("U\u00a7V\u00a9W\u00abX\u00adY\u00afZ\u00b1[\u00b3\2\u00b5")
        buf.write("\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf\2\u00c1\\\u00c3")
        buf.write("]\u00c5^\u00c7_\u00c9`\u00cba\u00cdb\u00cfc\u00d1d\u00d3")
        buf.write("e\u00d5f\u00d7g\u00d9\2\u00dbh\u00ddi\u00dfj\u00e1k\u00e3")
        buf.write("\2\u00e5\2\u00e7\2\u00e9\2\u00ebl\u00ed\2\u00ef\2\u00f1")
        buf.write("\2\u00f3m\u00f5\2\u00f7n\u00f9\2\u00fb\2\u00fdo\u00ff")
        buf.write("\2\u0101\2\u0103\2\u0105\2\u0107p\u0109q\u010b\2\u010d")
        buf.write("\2\u010f\2\u0111\2\u0113\2\u0115\2\u0117\2\u0119\2\u011b")
        buf.write("\2\5\2\3\4\30\3\2\63;\3\2\62;\4\2\f\f\17\17\3\2aa\3\2")
        buf.write("c|\6\2\62;C\\aac|\4\2\62;aa\6\2\62;CHaach\4\2\62\63aa")
        buf.write("\f\2\13\17\"\"\u0087\u0087\u00a2\u00a2\u1682\u1682\u2002")
        buf.write("\u200c\u202a\u202b\u2031\u2031\u2061\u2061\u3002\u3002")
        buf.write("\5\2\13\f\17\17\"\"\6\2\13\f\17\17$%^^\4\2ZZzz\4\2bb\u0080")
        buf.write("\u0080\13\2$$))^^cdhhppttvvxx\4\2GGgg\4\2--//\3\2\629")
        buf.write("\5\2\62;CHch\3\2\f\f\u0102\2C\\c|\u00ac\u00ac\u00b7\u00b7")
        buf.write("\u00bc\u00bc\u00c2\u00d8\u00da\u00f8\u00fa\u0221\u0224")
        buf.write("\u0235\u0252\u02af\u02b2\u02ba\u02bd\u02c3\u02d2\u02d3")
        buf.write("\u02e2\u02e6\u02f0\u02f0\u037c\u037c\u0388\u0388\u038a")
        buf.write("\u038c\u038e\u038e\u0390\u03a3\u03a5\u03d0\u03d2\u03d9")
        buf.write("\u03dc\u03f5\u0402\u0483\u048e\u04c6\u04c9\u04ca\u04cd")
        buf.write("\u04ce\u04d2\u04f7\u04fa\u04fb\u0533\u0558\u055b\u055b")
        buf.write("\u0563\u0589\u05d2\u05ec\u05f2\u05f4\u0623\u063c\u0642")
        buf.write("\u064c\u0673\u06d5\u06d7\u06d7\u06e7\u06e8\u06fc\u06fe")
        buf.write("\u0712\u0712\u0714\u072e\u0782\u07a7\u0907\u093b\u093f")
        buf.write("\u093f\u0952\u0952\u095a\u0963\u0987\u098e\u0991\u0992")
        buf.write("\u0995\u09aa\u09ac\u09b2\u09b4\u09b4\u09b8\u09bb\u09de")
        buf.write("\u09df\u09e1\u09e3\u09f2\u09f3\u0a07\u0a0c\u0a11\u0a12")
        buf.write("\u0a15\u0a2a\u0a2c\u0a32\u0a34\u0a35\u0a37\u0a38\u0a3a")
        buf.write("\u0a3b\u0a5b\u0a5e\u0a60\u0a60\u0a74\u0a76\u0a87\u0a8d")
        buf.write("\u0a8f\u0a8f\u0a91\u0a93\u0a95\u0aaa\u0aac\u0ab2\u0ab4")
        buf.write("\u0ab5\u0ab7\u0abb\u0abf\u0abf\u0ad2\u0ad2\u0ae2\u0ae2")
        buf.write("\u0b07\u0b0e\u0b11\u0b12\u0b15\u0b2a\u0b2c\u0b32\u0b34")
        buf.write("\u0b35\u0b38\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f\u0b61\u0b63")
        buf.write("\u0b87\u0b8c\u0b90\u0b92\u0b94\u0b97\u0b9b\u0b9c\u0b9e")
        buf.write("\u0b9e\u0ba0\u0ba1\u0ba5\u0ba6\u0baa\u0bac\u0bb0\u0bb7")
        buf.write("\u0bb9\u0bbb\u0c07\u0c0e\u0c10\u0c12\u0c14\u0c2a\u0c2c")
        buf.write("\u0c35\u0c37\u0c3b\u0c62\u0c63\u0c87\u0c8e\u0c90\u0c92")
        buf.write("\u0c94\u0caa\u0cac\u0cb5\u0cb7\u0cbb\u0ce0\u0ce0\u0ce2")
        buf.write("\u0ce3\u0d07\u0d0e\u0d10\u0d12\u0d14\u0d2a\u0d2c\u0d3b")
        buf.write("\u0d62\u0d63\u0d87\u0d98\u0d9c\u0db3\u0db5\u0dbd\u0dbf")
        buf.write("\u0dbf\u0dc2\u0dc8\u0e03\u0e32\u0e34\u0e35\u0e42\u0e48")
        buf.write("\u0e83\u0e84\u0e86\u0e86\u0e89\u0e8a\u0e8c\u0e8c\u0e8f")
        buf.write("\u0e8f\u0e96\u0e99\u0e9b\u0ea1\u0ea3\u0ea5\u0ea7\u0ea7")
        buf.write("\u0ea9\u0ea9\u0eac\u0ead\u0eaf\u0eb2\u0eb4\u0eb5\u0ebf")
        buf.write("\u0ec6\u0ec8\u0ec8\u0ede\u0edf\u0f02\u0f02\u0f42\u0f6c")
        buf.write("\u0f8a\u0f8d\u1002\u1023\u1025\u1029\u102b\u102c\u1052")
        buf.write("\u1057\u10a2\u10c7\u10d2\u10f8\u1102\u115b\u1161\u11a4")
        buf.write("\u11aa\u11fb\u1202\u1208\u120a\u1248\u124a\u124a\u124c")
        buf.write("\u124f\u1252\u1258\u125a\u125a\u125c\u125f\u1262\u1288")
        buf.write("\u128a\u128a\u128c\u128f\u1292\u12b0\u12b2\u12b2\u12b4")
        buf.write("\u12b7\u12ba\u12c0\u12c2\u12c2\u12c4\u12c7\u12ca\u12d0")
        buf.write("\u12d2\u12d8\u12da\u12f0\u12f2\u1310\u1312\u1312\u1314")
        buf.write("\u1317\u131a\u1320\u1322\u1348\u134a\u135c\u13a2\u13f6")
        buf.write("\u1403\u1678\u1683\u169c\u16a2\u16ec\u1782\u17b5\u1822")
        buf.write("\u1879\u1882\u18aa\u1e02\u1e9d\u1ea2\u1efb\u1f02\u1f17")
        buf.write("\u1f1a\u1f1f\u1f22\u1f47\u1f4a\u1f4f\u1f52\u1f59\u1f5b")
        buf.write("\u1f5b\u1f5d\u1f5d\u1f5f\u1f5f\u1f61\u1f7f\u1f82\u1fb6")
        buf.write("\u1fb8\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8\u1fce\u1fd2")
        buf.write("\u1fd5\u1fd8\u1fdd\u1fe2\u1fee\u1ff4\u1ff6\u1ff8\u1ffe")
        buf.write("\u2081\u2081\u2104\u2104\u2109\u2109\u210c\u2115\u2117")
        buf.write("\u2117\u211b\u211f\u2126\u2126\u2128\u2128\u212a\u212a")
        buf.write("\u212c\u212f\u2131\u2133\u2135\u213b\u2162\u2185\u3007")
        buf.write("\u3009\u3023\u302b\u3033\u3037\u303a\u303c\u3043\u3096")
        buf.write("\u309f\u30a0\u30a3\u30fc\u30fe\u3100\u3107\u312e\u3133")
        buf.write("\u3190\u31a2\u31b9\u3402\u4db7\u4e02\u9fa7\ua002\ua48e")
        buf.write("\uac02\uac02\ud7a5\ud7a5\uf902\ufa2f\ufb02\ufb08\ufb15")
        buf.write("\ufb19\ufb1f\ufb1f\ufb21\ufb2a\ufb2c\ufb38\ufb3a\ufb3e")
        buf.write("\ufb40\ufb40\ufb42\ufb43\ufb45\ufb46\ufb48\ufbb3\ufbd5")
        buf.write("\ufd3f\ufd52\ufd91\ufd94\ufdc9\ufdf2\ufdfd\ufe72\ufe74")
        buf.write("\ufe76\ufe76\ufe78\ufefe\uff23\uff3c\uff43\uff5c\uff68")
        buf.write("\uffc0\uffc4\uffc9\uffcc\uffd1\uffd4\uffd9\uffdc\uffde")
        buf.write("\26\2\62;\u0662\u066b\u06f2\u06fb\u0968\u0971\u09e8\u09f1")
        buf.write("\u0a68\u0a71\u0ae8\u0af1\u0b68\u0b71\u0be9\u0bf1\u0c68")
        buf.write("\u0c71\u0ce8\u0cf1\u0d68\u0d71\u0e52\u0e5b\u0ed2\u0edb")
        buf.write("\u0f22\u0f2b\u1042\u104b\u136b\u1373\u17e2\u17eb\u1812")
        buf.write("\u181b\uff12\uff1b\2\u0463\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7")
        buf.write("\3\2\2\2\2\u00c9\3\2\2\2\3\u00cb\3\2\2\2\3\u00cd\3\2\2")
        buf.write("\2\3\u00cf\3\2\2\2\3\u00d1\3\2\2\2\3\u00d3\3\2\2\2\3\u00d5")
        buf.write("\3\2\2\2\3\u00d7\3\2\2\2\3\u00d9\3\2\2\2\4\u00db\3\2\2")
        buf.write("\2\4\u00dd\3\2\2\2\4\u00df\3\2\2\2\4\u00e1\3\2\2\2\4\u00eb")
        buf.write("\3\2\2\2\4\u00f3\3\2\2\2\4\u00f7\3\2\2\2\4\u00fd\3\2\2")
        buf.write("\2\4\u0107\3\2\2\2\4\u0109\3\2\2\2\5\u0128\3\2\2\2\7\u0136")
        buf.write("\3\2\2\2\t\u0138\3\2\2\2\13\u013a\3\2\2\2\r\u0147\3\2")
        buf.write("\2\2\17\u015b\3\2\2\2\21\u0166\3\2\2\2\23\u0168\3\2\2")
        buf.write("\2\25\u016d\3\2\2\2\27\u0174\3\2\2\2\31\u0177\3\2\2\2")
        buf.write("\33\u017c\3\2\2\2\35\u0180\3\2\2\2\37\u0183\3\2\2\2!\u0186")
        buf.write("\3\2\2\2#\u0196\3\2\2\2%\u0198\3\2\2\2\'\u019e\3\2\2\2")
        buf.write(")\u01a2\3\2\2\2+\u01a7\3\2\2\2-\u01ad\3\2\2\2/\u01b0\3")
        buf.write("\2\2\2\61\u01b6\3\2\2\2\63\u01ba\3\2\2\2\65\u01bf\3\2")
        buf.write("\2\2\67\u01c5\3\2\2\29\u01c9\3\2\2\2;\u01d2\3\2\2\2=\u01d7")
        buf.write("\3\2\2\2?\u01de\3\2\2\2A\u01e3\3\2\2\2C\u01eb\3\2\2\2")
        buf.write("E\u01ee\3\2\2\2G\u01f4\3\2\2\2I\u01fd\3\2\2\2K\u0204\3")
        buf.write("\2\2\2M\u020a\3\2\2\2O\u020f\3\2\2\2Q\u0213\3\2\2\2S\u021c")
        buf.write("\3\2\2\2U\u0223\3\2\2\2W\u022b\3\2\2\2Y\u0233\3\2\2\2")
        buf.write("[\u023a\3\2\2\2]\u023d\3\2\2\2_\u023f\3\2\2\2a\u0242\3")
        buf.write("\2\2\2c\u0245\3\2\2\2e\u0248\3\2\2\2g\u024b\3\2\2\2i\u024d")
        buf.write("\3\2\2\2k\u024f\3\2\2\2m\u0251\3\2\2\2o\u0253\3\2\2\2")
        buf.write("q\u0255\3\2\2\2s\u0257\3\2\2\2u\u0259\3\2\2\2w\u025b\3")
        buf.write("\2\2\2y\u025d\3\2\2\2{\u025f\3\2\2\2}\u0262\3\2\2\2\177")
        buf.write("\u0264\3\2\2\2\u0081\u0266\3\2\2\2\u0083\u0273\3\2\2\2")
        buf.write("\u0085\u027d\3\2\2\2\u0087\u0288\3\2\2\2\u0089\u0295\3")
        buf.write("\2\2\2\u008b\u0297\3\2\2\2\u008d\u0299\3\2\2\2\u008f\u029b")
        buf.write("\3\2\2\2\u0091\u029d\3\2\2\2\u0093\u029f\3\2\2\2\u0095")
        buf.write("\u02a1\3\2\2\2\u0097\u02a3\3\2\2\2\u0099\u02a5\3\2\2\2")
        buf.write("\u009b\u02a8\3\2\2\2\u009d\u02aa\3\2\2\2\u009f\u02ac\3")
        buf.write("\2\2\2\u00a1\u02b0\3\2\2\2\u00a3\u02b3\3\2\2\2\u00a5\u02b6")
        buf.write("\3\2\2\2\u00a7\u02bc\3\2\2\2\u00a9\u02c3\3\2\2\2\u00ab")
        buf.write("\u02c8\3\2\2\2\u00ad\u02cd\3\2\2\2\u00af\u02da\3\2\2\2")
        buf.write("\u00b1\u02ea\3\2\2\2\u00b3\u02ec\3\2\2\2\u00b5\u02f1\3")
        buf.write("\2\2\2\u00b7\u02f6\3\2\2\2\u00b9\u0300\3\2\2\2\u00bb\u0302")
        buf.write("\3\2\2\2\u00bd\u0304\3\2\2\2\u00bf\u0306\3\2\2\2\u00c1")
        buf.write("\u030b\3\2\2\2\u00c3\u0329\3\2\2\2\u00c5\u032e\3\2\2\2")
        buf.write("\u00c7\u0334\3\2\2\2\u00c9\u0338\3\2\2\2\u00cb\u033a\3")
        buf.write("\2\2\2\u00cd\u033d\3\2\2\2\u00cf\u0340\3\2\2\2\u00d1\u0343")
        buf.write("\3\2\2\2\u00d3\u0346\3\2\2\2\u00d5\u034a\3\2\2\2\u00d7")
        buf.write("\u0350\3\2\2\2\u00d9\u0354\3\2\2\2\u00db\u0358\3\2\2\2")
        buf.write("\u00dd\u035f\3\2\2\2\u00df\u0369\3\2\2\2\u00e1\u0378\3")
        buf.write("\2\2\2\u00e3\u0381\3\2\2\2\u00e5\u0385\3\2\2\2\u00e7\u038a")
        buf.write("\3\2\2\2\u00e9\u0392\3\2\2\2\u00eb\u0397\3\2\2\2\u00ed")
        buf.write("\u0399\3\2\2\2\u00ef\u03a0\3\2\2\2\u00f1\u03a7\3\2\2\2")
        buf.write("\u00f3\u03be\3\2\2\2\u00f5\u03c1\3\2\2\2\u00f7\u03c7\3")
        buf.write("\2\2\2\u00f9\u03c9\3\2\2\2\u00fb\u03d4\3\2\2\2\u00fd\u03e0")
        buf.write("\3\2\2\2\u00ff\u03eb\3\2\2\2\u0101\u03ef\3\2\2\2\u0103")
        buf.write("\u03f1\3\2\2\2\u0105\u03f6\3\2\2\2\u0107\u03fb\3\2\2\2")
        buf.write("\u0109\u0403\3\2\2\2\u010b\u040f\3\2\2\2\u010d\u0416\3")
        buf.write("\2\2\2\u010f\u041d\3\2\2\2\u0111\u0421\3\2\2\2\u0113\u0423")
        buf.write("\3\2\2\2\u0115\u0425\3\2\2\2\u0117\u0427\3\2\2\2\u0119")
        buf.write("\u042a\3\2\2\2\u011b\u042d\3\2\2\2\u011d\u011f\5\u00b5")
        buf.write("Z\2\u011e\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0129\3\2\2\2\u0122")
        buf.write("\u0120\3\2\2\2\u0123\u0125\5\u00b5Z\2\u0124\u0123\3\2")
        buf.write("\2\2\u0125\u0126\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127")
        buf.write("\3\2\2\2\u0127\u0129\3\2\2\2\u0128\u0120\3\2\2\2\u0128")
        buf.write("\u0124\3\2\2\2\u0129\6\3\2\2\2\u012a\u012e\5\u00b3Y\2")
        buf.write("\u012b\u012d\5\u00b5Z\2\u012c\u012b\3\2\2\2\u012d\u0130")
        buf.write("\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("\u0137\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0133\5\u00b5")
        buf.write("Z\2\u0132\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0132")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137\3\2\2\2\u0136")
        buf.write("\u012a\3\2\2\2\u0136\u0132\3\2\2\2\u0137\b\3\2\2\2\u0138")
        buf.write("\u0139\7$\2\2\u0139\n\3\2\2\2\u013a\u013b\7x\2\2\u013b")
        buf.write("\u013c\7c\2\2\u013c\u013d\7t\2\2\u013d\f\3\2\2\2\u013e")
        buf.write("\u013f\7c\2\2\u013f\u0140\7t\2\2\u0140\u0141\7t\2\2\u0141")
        buf.write("\u0142\7c\2\2\u0142\u0148\7{\2\2\u0143\u0148\13\2\2\2")
        buf.write("\u0144\u0145\7c\2\2\u0145\u0146\7t\2\2\u0146\u0148\7t")
        buf.write("\2\2\u0147\u013e\3\2\2\2\u0147\u0143\3\2\2\2\u0147\u0144")
        buf.write("\3\2\2\2\u0148\16\3\2\2\2\u0149\u014a\7e\2\2\u014a\u014b")
        buf.write("\7q\2\2\u014b\u015c\7p\2\2\u014c\u015c\13\2\2\2\u014d")
        buf.write("\u014e\7e\2\2\u014e\u014f\7q\2\2\u014f\u0150\7p\2\2\u0150")
        buf.write("\u0151\7u\2\2\u0151\u015c\7v\2\2\u0152\u015c\13\2\2\2")
        buf.write("\u0153\u0154\7e\2\2\u0154\u0155\7q\2\2\u0155\u0156\7p")
        buf.write("\2\2\u0156\u0157\7u\2\2\u0157\u0158\7v\2\2\u0158\u0159")
        buf.write("\7c\2\2\u0159\u015a\7p\2\2\u015a\u015c\7v\2\2\u015b\u0149")
        buf.write("\3\2\2\2\u015b\u014c\3\2\2\2\u015b\u014d\3\2\2\2\u015b")
        buf.write("\u0152\3\2\2\2\u015b\u0153\3\2\2\2\u015c\20\3\2\2\2\u015d")
        buf.write("\u015e\7n\2\2\u015e\u015f\7q\2\2\u015f\u0167\7e\2\2\u0160")
        buf.write("\u0167\13\2\2\2\u0161\u0162\7n\2\2\u0162\u0163\7q\2\2")
        buf.write("\u0163\u0164\7e\2\2\u0164\u0165\7c\2\2\u0165\u0167\7n")
        buf.write("\2\2\u0166\u015d\3\2\2\2\u0166\u0160\3\2\2\2\u0166\u0161")
        buf.write("\3\2\2\2\u0167\22\3\2\2\2\u0168\u0169\7g\2\2\u0169\u016a")
        buf.write("\7e\2\2\u016a\u016b\7j\2\2\u016b\u016c\7q\2\2\u016c\24")
        buf.write("\3\2\2\2\u016d\u016e\7t\2\2\u016e\u016f\7g\2\2\u016f\u0170")
        buf.write("\7v\2\2\u0170\u0171\7w\2\2\u0171\u0172\7t\2\2\u0172\u0173")
        buf.write("\7p\2\2\u0173\26\3\2\2\2\u0174\u0175\7k\2\2\u0175\u0176")
        buf.write("\7h\2\2\u0176\30\3\2\2\2\u0177\u0178\7v\2\2\u0178\u0179")
        buf.write("\7j\2\2\u0179\u017a\7g\2\2\u017a\u017b\7p\2\2\u017b\32")
        buf.write("\3\2\2\2\u017c\u017d\7c\2\2\u017d\u017e\7p\2\2\u017e\u017f")
        buf.write("\7f\2\2\u017f\34\3\2\2\2\u0180\u0181\7q\2\2\u0181\u0182")
        buf.write("\7t\2\2\u0182\36\3\2\2\2\u0183\u0184\7k\2\2\u0184\u0185")
        buf.write("\7p\2\2\u0185 \3\2\2\2\u0186\u0187\7g\2\2\u0187\u0188")
        buf.write("\7n\2\2\u0188\u0189\7u\2\2\u0189\u018a\7g\2\2\u018a\"")
        buf.write("\3\2\2\2\u018b\u018c\7g\2\2\u018c\u018d\7n\2\2\u018d\u018e")
        buf.write("\7u\2\2\u018e\u018f\7g\2\2\u018f\u0190\7k\2\2\u0190\u0197")
        buf.write("\7h\2\2\u0191\u0197\13\2\2\2\u0192\u0193\7g\2\2\u0193")
        buf.write("\u0194\7n\2\2\u0194\u0195\7k\2\2\u0195\u0197\7h\2\2\u0196")
        buf.write("\u018b\3\2\2\2\u0196\u0191\3\2\2\2\u0196\u0192\3\2\2\2")
        buf.write("\u0197$\3\2\2\2\u0198\u0199\7y\2\2\u0199\u019a\7j\2\2")
        buf.write("\u019a\u019b\7k\2\2\u019b\u019c\7n\2\2\u019c\u019d\7g")
        buf.write("\2\2\u019d&\3\2\2\2\u019e\u019f\7h\2\2\u019f\u01a0\7q")
        buf.write("\2\2\u01a0\u01a1\7t\2\2\u01a1(\3\2\2\2\u01a2\u01a3\7v")
        buf.write("\2\2\u01a3\u01a4\7t\2\2\u01a4\u01a5\7w\2\2\u01a5\u01a6")
        buf.write("\7g\2\2\u01a6*\3\2\2\2\u01a7\u01a8\7h\2\2\u01a8\u01a9")
        buf.write("\7c\2\2\u01a9\u01aa\7n\2\2\u01aa\u01ab\7u\2\2\u01ab\u01ac")
        buf.write("\7g\2\2\u01ac,\3\2\2\2\u01ad\u01ae\7h\2\2\u01ae\u01af")
        buf.write("\7p\2\2\u01af.\3\2\2\2\u01b0\u01b1\7e\2\2\u01b1\u01b2")
        buf.write("\7n\2\2\u01b2\u01b3\7c\2\2\u01b3\u01b4\7u\2\2\u01b4\u01b5")
        buf.write("\7u\2\2\u01b5\60\3\2\2\2\u01b6\u01b7\7n\2\2\u01b7\u01b8")
        buf.write("\7g\2\2\u01b8\u01b9\7v\2\2\u01b9\62\3\2\2\2\u01ba\u01bb")
        buf.write("\7d\2\2\u01bb\u01bc\7k\2\2\u01bc\u01bd\7p\2\2\u01bd\u01be")
        buf.write("\7f\2\2\u01be\64\3\2\2\2\u01bf\u01c0\7v\2\2\u01c0\u01c1")
        buf.write("\7t\2\2\u01c1\u01c2\7c\2\2\u01c2\u01c3\7k\2\2\u01c3\u01c4")
        buf.write("\7v\2\2\u01c4\66\3\2\2\2\u01c5\u01c6\7f\2\2\u01c6\u01c7")
        buf.write("\7g\2\2\u01c7\u01c8\7h\2\2\u01c88\3\2\2\2\u01c9\u01ca")
        buf.write("\7r\2\2\u01ca\u01cb\7t\2\2\u01cb\u01cc\7q\2\2\u01cc\u01cd")
        buf.write("\7v\2\2\u01cd\u01ce\7q\2\2\u01ce\u01cf\7e\2\2\u01cf\u01d0")
        buf.write("\7q\2\2\u01d0\u01d1\7n\2\2\u01d1:\3\2\2\2\u01d2\u01d3")
        buf.write("\7g\2\2\u01d3\u01d4\7p\2\2\u01d4\u01d5\7w\2\2\u01d5\u01d6")
        buf.write("\7o\2\2\u01d6<\3\2\2\2\u01d7\u01d8\7k\2\2\u01d8\u01d9")
        buf.write("\7o\2\2\u01d9\u01da\7r\2\2\u01da\u01db\7q\2\2\u01db\u01dc")
        buf.write("\7t\2\2\u01dc\u01dd\7v\2\2\u01dd>\3\2\2\2\u01de\u01df")
        buf.write("\7h\2\2\u01df\u01e0\7t\2\2\u01e0\u01e1\7q\2\2\u01e1\u01e2")
        buf.write("\7o\2\2\u01e2@\3\2\2\2\u01e3\u01e4\7r\2\2\u01e4\u01e5")
        buf.write("\7c\2\2\u01e5\u01e6\7e\2\2\u01e6\u01e7\7m\2\2\u01e7\u01e8")
        buf.write("\7c\2\2\u01e8\u01e9\7i\2\2\u01e9\u01ea\7g\2\2\u01eaB\3")
        buf.write("\2\2\2\u01eb\u01ec\7c\2\2\u01ec\u01ed\7u\2\2\u01edD\3")
        buf.write("\2\2\2\u01ee\u01ef\7d\2\2\u01ef\u01f0\7t\2\2\u01f0\u01f1")
        buf.write("\7g\2\2\u01f1\u01f2\7c\2\2\u01f2\u01f3\7m\2\2\u01f3F\3")
        buf.write("\2\2\2\u01f4\u01f5\7c\2\2\u01f5\u01f6\7d\2\2\u01f6\u01f7")
        buf.write("\7u\2\2\u01f7\u01f8\7v\2\2\u01f8\u01f9\7t\2\2\u01f9\u01fa")
        buf.write("\7c\2\2\u01fa\u01fb\7e\2\2\u01fb\u01fc\7v\2\2\u01fcH\3")
        buf.write("\2\2\2\u01fd\u01fe\7u\2\2\u01fe\u01ff\7g\2\2\u01ff\u0200")
        buf.write("\7n\2\2\u0200\u0201\7g\2\2\u0201\u0202\7e\2\2\u0202\u0203")
        buf.write("\7v\2\2\u0203J\3\2\2\2\u0204\u0205\7k\2\2\u0205\u0206")
        buf.write("\7p\2\2\u0206\u0207\7r\2\2\u0207\u0208\7w\2\2\u0208\u0209")
        buf.write("\7v\2\2\u0209L\3\2\2\2\u020a\u020b\7g\2\2\u020b\u020c")
        buf.write("\7c\2\2\u020c\u020d\7e\2\2\u020d\u020e\7j\2\2\u020eN\3")
        buf.write("\2\2\2\u020f\u0210\7p\2\2\u0210\u0211\7g\2\2\u0211\u0212")
        buf.write("\7y\2\2\u0212P\3\2\2\2\u0213\u0214\7e\2\2\u0214\u0215")
        buf.write("\7q\2\2\u0215\u0216\7p\2\2\u0216\u0217\7v\2\2\u0217\u0218")
        buf.write("\7k\2\2\u0218\u0219\7p\2\2\u0219\u021a\7w\2\2\u021a\u021b")
        buf.write("\7g\2\2\u021bR\3\2\2\2\u021c\u021d\7g\2\2\u021d\u021e")
        buf.write("\7z\2\2\u021e\u021f\7r\2\2\u021f\u0220\7q\2\2\u0220\u0221")
        buf.write("\7t\2\2\u0221\u0222\7v\2\2\u0222T\3\2\2\2\u0223\u0224")
        buf.write("\7k\2\2\u0224\u0225\7p\2\2\u0225\u0226\7e\2\2\u0226\u0227")
        buf.write("\7n\2\2\u0227\u0228\7w\2\2\u0228\u0229\7f\2\2\u0229\u022a")
        buf.write("\7g\2\2\u022aV\3\2\2\2\u022b\u022c\7t\2\2\u022c\u022d")
        buf.write("\7g\2\2\u022d\u022e\7s\2\2\u022e\u022f\7w\2\2\u022f\u0230")
        buf.write("\7k\2\2\u0230\u0231\7t\2\2\u0231\u0232\7g\2\2\u0232X\3")
        buf.write("\2\2\2\u0233\u0234\7u\2\2\u0234\u0235\7w\2\2\u0235\u0236")
        buf.write("\7o\2\2\u0236\u0237\7o\2\2\u0237\u0238\7q\2\2\u0238\u0239")
        buf.write("\7p\2\2\u0239Z\3\2\2\2\u023a\u023b\7<\2\2\u023b\u023c")
        buf.write("\7?\2\2\u023c\\\3\2\2\2\u023d\u023e\7?\2\2\u023e^\3\2")
        buf.write("\2\2\u023f\u0240\7?\2\2\u0240\u0241\7?\2\2\u0241`\3\2")
        buf.write("\2\2\u0242\u0243\7#\2\2\u0243\u0244\7?\2\2\u0244b\3\2")
        buf.write("\2\2\u0245\u0246\7>\2\2\u0246\u0247\7?\2\2\u0247d\3\2")
        buf.write("\2\2\u0248\u0249\7@\2\2\u0249\u024a\7?\2\2\u024af\3\2")
        buf.write("\2\2\u024b\u024c\7-\2\2\u024ch\3\2\2\2\u024d\u024e\7/")
        buf.write("\2\2\u024ej\3\2\2\2\u024f\u0250\7,\2\2\u0250l\3\2\2\2")
        buf.write("\u0251\u0252\7\61\2\2\u0252n\3\2\2\2\u0253\u0254\7>\2")
        buf.write("\2\u0254p\3\2\2\2\u0255\u0256\7@\2\2\u0256r\3\2\2\2\u0257")
        buf.write("\u0258\7#\2\2\u0258t\3\2\2\2\u0259\u025a\7`\2\2\u025a")
        buf.write("v\3\2\2\2\u025b\u025c\7\'\2\2\u025cx\3\2\2\2\u025d\u025e")
        buf.write("\7~\2\2\u025ez\3\2\2\2\u025f\u0260\7~\2\2\u0260\u0261")
        buf.write("\7~\2\2\u0261|\3\2\2\2\u0262\u0263\7%\2\2\u0263~\3\2\2")
        buf.write("\2\u0264\u0265\7(\2\2\u0265\u0080\3\2\2\2\u0266\u0267")
        buf.write("\7(\2\2\u0267\u0268\7(\2\2\u0268\u0082\3\2\2\2\u0269\u026a")
        buf.write("\7k\2\2\u026a\u026b\7p\2\2\u026b\u0274\7v\2\2\u026c\u026d")
        buf.write("\7k\2\2\u026d\u026e\7p\2\2\u026e\u026f\7v\2\2\u026f\u0270")
        buf.write("\7g\2\2\u0270\u0271\7i\2\2\u0271\u0272\7g\2\2\u0272\u0274")
        buf.write("\7t\2\2\u0273\u0269\3\2\2\2\u0273\u026c\3\2\2\2\u0274")
        buf.write("\u0084\3\2\2\2\u0275\u0276\7h\2\2\u0276\u0277\7n\2\2\u0277")
        buf.write("\u027e\7v\2\2\u0278\u0279\7h\2\2\u0279\u027a\7n\2\2\u027a")
        buf.write("\u027b\7q\2\2\u027b\u027c\7c\2\2\u027c\u027e\7v\2\2\u027d")
        buf.write("\u0275\3\2\2\2\u027d\u0278\3\2\2\2\u027e\u0086\3\2\2\2")
        buf.write("\u027f\u0280\7u\2\2\u0280\u0281\7v\2\2\u0281\u0289\7t")
        buf.write("\2\2\u0282\u0283\7u\2\2\u0283\u0284\7v\2\2\u0284\u0285")
        buf.write("\7t\2\2\u0285\u0286\7k\2\2\u0286\u0287\7p\2\2\u0287\u0289")
        buf.write("\7i\2\2\u0288\u027f\3\2\2\2\u0288\u0282\3\2\2\2\u0289")
        buf.write("\u0088\3\2\2\2\u028a\u028b\7d\2\2\u028b\u028c\7q\2\2\u028c")
        buf.write("\u028d\7q\2\2\u028d\u0296\7n\2\2\u028e\u028f\7d\2\2\u028f")
        buf.write("\u0290\7q\2\2\u0290\u0291\7q\2\2\u0291\u0292\7n\2\2\u0292")
        buf.write("\u0293\7g\2\2\u0293\u0294\7c\2\2\u0294\u0296\7p\2\2\u0295")
        buf.write("\u028a\3\2\2\2\u0295\u028e\3\2\2\2\u0296\u008a\3\2\2\2")
        buf.write("\u0297\u0298\7.\2\2\u0298\u008c\3\2\2\2\u0299\u029a\7")
        buf.write("*\2\2\u029a\u008e\3\2\2\2\u029b\u029c\7+\2\2\u029c\u0090")
        buf.write("\3\2\2\2\u029d\u029e\7}\2\2\u029e\u0092\3\2\2\2\u029f")
        buf.write("\u02a0\7\177\2\2\u02a0\u0094\3\2\2\2\u02a1\u02a2\7]\2")
        buf.write("\2\u02a2\u0096\3\2\2\2\u02a3\u02a4\7_\2\2\u02a4\u0098")
        buf.write("\3\2\2\2\u02a5\u02a6\7/\2\2\u02a6\u02a7\7@\2\2\u02a7\u009a")
        buf.write("\3\2\2\2\u02a8\u02a9\7<\2\2\u02a9\u009c\3\2\2\2\u02aa")
        buf.write("\u02ab\7\60\2\2\u02ab\u009e\3\2\2\2\u02ac\u02ad\7\60\2")
        buf.write("\2\u02ad\u02ae\7\60\2\2\u02ae\u02af\7\60\2\2\u02af\u00a0")
        buf.write("\3\2\2\2\u02b0\u02b1\7-\2\2\u02b1\u02b2\7-\2\2\u02b2\u00a2")
        buf.write("\3\2\2\2\u02b3\u02b4\7/\2\2\u02b4\u02b5\7/\2\2\u02b5\u00a4")
        buf.write("\3\2\2\2\u02b6\u02b7\7h\2\2\u02b7\u02b8\7n\2\2\u02b8\u02b9")
        buf.write("\7q\2\2\u02b9\u02ba\7c\2\2\u02ba\u02bb\7v\2\2\u02bb\u00a6")
        buf.write("\3\2\2\2\u02bc\u02bd\7u\2\2\u02bd\u02be\7v\2\2\u02be\u02bf")
        buf.write("\7t\2\2\u02bf\u02c0\7k\2\2\u02c0\u02c1\7p\2\2\u02c1\u02c2")
        buf.write("\7i\2\2\u02c2\u00a8\3\2\2\2\u02c3\u02c4\7d\2\2\u02c4\u02c5")
        buf.write("\7q\2\2\u02c5\u02c6\7q\2\2\u02c6\u02c7\7n\2\2\u02c7\u00aa")
        buf.write("\3\2\2\2\u02c8\u02c9\7p\2\2\u02c9\u02ca\7w\2\2\u02ca\u02cb")
        buf.write("\7n\2\2\u02cb\u02cc\7n\2\2\u02cc\u00ac\3\2\2\2\u02cd\u02ce")
        buf.write("\7e\2\2\u02ce\u02cf\7j\2\2\u02cf\u02d0\7c\2\2\u02d0\u02d1")
        buf.write("\7t\2\2\u02d1\u00ae\3\2\2\2\u02d2\u02db\7\62\2\2\u02d3")
        buf.write("\u02d7\t\2\2\2\u02d4\u02d6\t\3\2\2\u02d5\u02d4\3\2\2\2")
        buf.write("\u02d6\u02d9\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d7\u02d8\3")
        buf.write("\2\2\2\u02d8\u02db\3\2\2\2\u02d9\u02d7\3\2\2\2\u02da\u02d2")
        buf.write("\3\2\2\2\u02da\u02d3\3\2\2\2\u02db\u00b0\3\2\2\2\u02dc")
        buf.write("\u02eb\7\62\2\2\u02dd\u02e1\t\2\2\2\u02de\u02e0\t\3\2")
        buf.write("\2\u02df\u02de\3\2\2\2\u02e0\u02e3\3\2\2\2\u02e1\u02df")
        buf.write("\3\2\2\2\u02e1\u02e2\3\2\2\2\u02e2\u02e4\3\2\2\2\u02e3")
        buf.write("\u02e1\3\2\2\2\u02e4\u02e6\7\60\2\2\u02e5\u02e7\t\3\2")
        buf.write("\2\u02e6\u02e5\3\2\2\2\u02e7\u02e8\3\2\2\2\u02e8\u02e6")
        buf.write("\3\2\2\2\u02e8\u02e9\3\2\2\2\u02e9\u02eb\3\2\2\2\u02ea")
        buf.write("\u02dc\3\2\2\2\u02ea\u02dd\3\2\2\2\u02eb\u00b2\3\2\2\2")
        buf.write("\u02ec\u02ed\7=\2\2\u02ed\u00b4\3\2\2\2\u02ee\u02ef\7")
        buf.write("\17\2\2\u02ef\u02f2\7\f\2\2\u02f0\u02f2\t\4\2\2\u02f1")
        buf.write("\u02ee\3\2\2\2\u02f1\u02f0\3\2\2\2\u02f2\u00b6\3\2\2\2")
        buf.write("\u02f3\u02f5\t\5\2\2\u02f4\u02f3\3\2\2\2\u02f5\u02f8\3")
        buf.write("\2\2\2\u02f6\u02f4\3\2\2\2\u02f6\u02f7\3\2\2\2\u02f7\u02f9")
        buf.write("\3\2\2\2\u02f8\u02f6\3\2\2\2\u02f9\u02fd\t\6\2\2\u02fa")
        buf.write("\u02fc\t\7\2\2\u02fb\u02fa\3\2\2\2\u02fc\u02ff\3\2\2\2")
        buf.write("\u02fd\u02fb\3\2\2\2\u02fd\u02fe\3\2\2\2\u02fe\u00b8\3")
        buf.write("\2\2\2\u02ff\u02fd\3\2\2\2\u0300\u0301\t\b\2\2\u0301\u00ba")
        buf.write("\3\2\2\2\u0302\u0303\t\t\2\2\u0303\u00bc\3\2\2\2\u0304")
        buf.write("\u0305\t\n\2\2\u0305\u00be\3\2\2\2\u0306\u0307\t\13\2")
        buf.write("\2\u0307\u0308\3\2\2\2\u0308\u0309\b_\2\2\u0309\u00c0")
        buf.write("\3\2\2\2\u030a\u030c\t\f\2\2\u030b\u030a\3\2\2\2\u030c")
        buf.write("\u030d\3\2\2\2\u030d\u030b\3\2\2\2\u030d\u030e\3\2\2\2")
        buf.write("\u030e\u030f\3\2\2\2\u030f\u0310\b`\3\2\u0310\u00c2\3")
        buf.write("\2\2\2\u0311\u0312\7\61\2\2\u0312\u0313\7\61\2\2\u0313")
        buf.write("\u0317\3\2\2\2\u0314\u0316\n\4\2\2\u0315\u0314\3\2\2\2")
        buf.write("\u0316\u0319\3\2\2\2\u0317\u0315\3\2\2\2\u0317\u0318\3")
        buf.write("\2\2\2\u0318\u031b\3\2\2\2\u0319\u0317\3\2\2\2\u031a\u031c")
        buf.write("\7\17\2\2\u031b\u031a\3\2\2\2\u031b\u031c\3\2\2\2\u031c")
        buf.write("\u031d\3\2\2\2\u031d\u032a\7\f\2\2\u031e\u031f\7\61\2")
        buf.write("\2\u031f\u0320\7,\2\2\u0320\u0324\3\2\2\2\u0321\u0323")
        buf.write("\13\2\2\2\u0322\u0321\3\2\2\2\u0323\u0326\3\2\2\2\u0324")
        buf.write("\u0325\3\2\2\2\u0324\u0322\3\2\2\2\u0325\u0327\3\2\2\2")
        buf.write("\u0326\u0324\3\2\2\2\u0327\u0328\7,\2\2\u0328\u032a\7")
        buf.write("\61\2\2\u0329\u0311\3\2\2\2\u0329\u031e\3\2\2\2\u032a")
        buf.write("\u032b\3\2\2\2\u032b\u032c\ba\2\2\u032c\u00c4\3\2\2\2")
        buf.write("\u032d\u032f\t\4\2\2\u032e\u032d\3\2\2\2\u032f\u0330\3")
        buf.write("\2\2\2\u0330\u032e\3\2\2\2\u0330\u0331\3\2\2\2\u0331\u0332")
        buf.write("\3\2\2\2\u0332\u0333\bb\2\2\u0333\u00c6\3\2\2\2\u0334")
        buf.write("\u0335\7$\2\2\u0335\u0336\3\2\2\2\u0336\u0337\bc\4\2\u0337")
        buf.write("\u00c8\3\2\2\2\u0338\u0339\13\2\2\2\u0339\u00ca\3\2\2")
        buf.write("\2\u033a\u033b\7^\2\2\u033b\u033c\7$\2\2\u033c\u00cc\3")
        buf.write("\2\2\2\u033d\u033e\7^\2\2\u033e\u033f\7^\2\2\u033f\u00ce")
        buf.write("\3\2\2\2\u0340\u0341\7^\2\2\u0341\u0342\7p\2\2\u0342\u00d0")
        buf.write("\3\2\2\2\u0343\u0344\7^\2\2\u0344\u0345\7%\2\2\u0345\u00d2")
        buf.write("\3\2\2\2\u0346\u0347\7$\2\2\u0347\u0348\3\2\2\2\u0348")
        buf.write("\u0349\bi\5\2\u0349\u00d4\3\2\2\2\u034a\u034b\7%\2\2\u034b")
        buf.write("\u034c\7}\2\2\u034c\u034d\3\2\2\2\u034d\u034e\bj\6\2\u034e")
        buf.write("\u00d6\3\2\2\2\u034f\u0351\n\r\2\2\u0350\u034f\3\2\2\2")
        buf.write("\u0351\u0352\3\2\2\2\u0352\u0350\3\2\2\2\u0352\u0353\3")
        buf.write("\2\2\2\u0353\u00d8\3\2\2\2\u0354\u0355\13\2\2\2\u0355")
        buf.write("\u0356\3\2\2\2\u0356\u0357\bl\7\2\u0357\u00da\3\2\2\2")
        buf.write("\u0358\u0359\7\177\2\2\u0359\u035a\3\2\2\2\u035a\u035b")
        buf.write("\bm\5\2\u035b\u00dc\3\2\2\2\u035c\u035e\t\5\2\2\u035d")
        buf.write("\u035c\3\2\2\2\u035e\u0361\3\2\2\2\u035f\u035d\3\2\2\2")
        buf.write("\u035f\u0360\3\2\2\2\u0360\u0362\3\2\2\2\u0361\u035f\3")
        buf.write("\2\2\2\u0362\u0366\t\6\2\2\u0363\u0365\t\7\2\2\u0364\u0363")
        buf.write("\3\2\2\2\u0365\u0368\3\2\2\2\u0366\u0364\3\2\2\2\u0366")
        buf.write("\u0367\3\2\2\2\u0367\u00de\3\2\2\2\u0368\u0366\3\2\2\2")
        buf.write("\u0369\u036e\5\u0111\u0088\2\u036a\u036d\5\u0111\u0088")
        buf.write("\2\u036b\u036d\5\u011b\u008d\2\u036c\u036a\3\2\2\2\u036c")
        buf.write("\u036b\3\2\2\2\u036d\u0370\3\2\2\2\u036e\u036c\3\2\2\2")
        buf.write("\u036e\u036f\3\2\2\2\u036f\u00e0\3\2\2\2\u0370\u036e\3")
        buf.write("\2\2\2\u0371\u0379\5\35\16\2\u0372\u0379\5\33\r\2\u0373")
        buf.write("\u0379\5{=\2\u0374\u0379\5\u0081@\2\u0375\u0379\5\u00e3")
        buf.write("q\2\u0376\u0379\5\u00e5r\2\u0377\u0379\5\u00e7s\2\u0378")
        buf.write("\u0371\3\2\2\2\u0378\u0372\3\2\2\2\u0378\u0373\3\2\2\2")
        buf.write("\u0378\u0374\3\2\2\2\u0378\u0375\3\2\2\2\u0378\u0376\3")
        buf.write("\2\2\2\u0378\u0377\3\2\2\2\u0379\u00e2\3\2\2\2\u037a\u0382")
        buf.write("\5].\2\u037b\u0382\5_/\2\u037c\u0382\5a\60\2\u037d\u0382")
        buf.write("\5o\67\2\u037e\u0382\5c\61\2\u037f\u0382\5q8\2\u0380\u0382")
        buf.write("\5e\62\2\u0381\u037a\3\2\2\2\u0381\u037b\3\2\2\2\u0381")
        buf.write("\u037c\3\2\2\2\u0381\u037d\3\2\2\2\u0381\u037e\3\2\2\2")
        buf.write("\u0381\u037f\3\2\2\2\u0381\u0380\3\2\2\2\u0382\u00e4\3")
        buf.write("\2\2\2\u0383\u0386\5g\63\2\u0384\u0386\5i\64\2\u0385\u0383")
        buf.write("\3\2\2\2\u0385\u0384\3\2\2\2\u0386\u00e6\3\2\2\2\u0387")
        buf.write("\u038b\5k\65\2\u0388\u038b\5m\66\2\u0389\u038b\5w;\2\u038a")
        buf.write("\u0387\3\2\2\2\u038a\u0388\3\2\2\2\u038a\u0389\3\2\2\2")
        buf.write("\u038b\u00e8\3\2\2\2\u038c\u0393\5g\63\2\u038d\u0393\5")
        buf.write("i\64\2\u038e\u0393\5s9\2\u038f\u0393\5u:\2\u0390\u0393")
        buf.write("\5k\65\2\u0391\u0393\5\u0081@\2\u0392\u038c\3\2\2\2\u0392")
        buf.write("\u038d\3\2\2\2\u0392\u038e\3\2\2\2\u0392\u038f\3\2\2\2")
        buf.write("\u0392\u0390\3\2\2\2\u0392\u0391\3\2\2\2\u0393\u00ea\3")
        buf.write("\2\2\2\u0394\u0398\5\u00edv\2\u0395\u0398\5\u00efw\2\u0396")
        buf.write("\u0398\5\u00f1x\2\u0397\u0394\3\2\2\2\u0397\u0395\3\2")
        buf.write("\2\2\u0397\u0396\3\2\2\2\u0398\u00ec\3\2\2\2\u0399\u039d")
        buf.write("\t\2\2\2\u039a\u039c\5\u010f\u0087\2\u039b\u039a\3\2\2")
        buf.write("\2\u039c\u039f\3\2\2\2\u039d\u039b\3\2\2\2\u039d\u039e")
        buf.write("\3\2\2\2\u039e\u00ee\3\2\2\2\u039f\u039d\3\2\2\2\u03a0")
        buf.write("\u03a4\7\62\2\2\u03a1\u03a3\5\u0113\u0089\2\u03a2\u03a1")
        buf.write("\3\2\2\2\u03a3\u03a6\3\2\2\2\u03a4\u03a2\3\2\2\2\u03a4")
        buf.write("\u03a5\3\2\2\2\u03a5\u00f0\3\2\2\2\u03a6\u03a4\3\2\2\2")
        buf.write("\u03a7\u03a8\7\62\2\2\u03a8\u03aa\t\16\2\2\u03a9\u03ab")
        buf.write("\5\u0115\u008a\2\u03aa\u03a9\3\2\2\2\u03ab\u03ac\3\2\2")
        buf.write("\2\u03ac\u03aa\3\2\2\2\u03ac\u03ad\3\2\2\2\u03ad\u00f2")
        buf.write("\3\2\2\2\u03ae\u03af\5\u00f5z\2\u03af\u03b1\7\60\2\2\u03b0")
        buf.write("\u03b2\5\u00f5z\2\u03b1\u03b0\3\2\2\2\u03b1\u03b2\3\2")
        buf.write("\2\2\u03b2\u03b4\3\2\2\2\u03b3\u03b5\5\u010d\u0086\2\u03b4")
        buf.write("\u03b3\3\2\2\2\u03b4\u03b5\3\2\2\2\u03b5\u03bf\3\2\2\2")
        buf.write("\u03b6\u03b7\5\u00f5z\2\u03b7\u03b8\5\u010d\u0086\2\u03b8")
        buf.write("\u03bf\3\2\2\2\u03b9\u03ba\7\60\2\2\u03ba\u03bc\5\u00f5")
        buf.write("z\2\u03bb\u03bd\5\u010d\u0086\2\u03bc\u03bb\3\2\2\2\u03bc")
        buf.write("\u03bd\3\2\2\2\u03bd\u03bf\3\2\2\2\u03be\u03ae\3\2\2\2")
        buf.write("\u03be\u03b6\3\2\2\2\u03be\u03b9\3\2\2\2\u03bf\u00f4\3")
        buf.write("\2\2\2\u03c0\u03c2\5\u010f\u0087\2\u03c1\u03c0\3\2\2\2")
        buf.write("\u03c2\u03c3\3\2\2\2\u03c3\u03c1\3\2\2\2\u03c3\u03c4\3")
        buf.write("\2\2\2\u03c4\u00f6\3\2\2\2\u03c5\u03c8\5\u00f9|\2\u03c6")
        buf.write("\u03c8\5\u00fb}\2\u03c7\u03c5\3\2\2\2\u03c7\u03c6\3\2")
        buf.write("\2\2\u03c8\u00f8\3\2\2\2\u03c9\u03cf\7b\2\2\u03ca\u03ce")
        buf.write("\5\u0117\u008b\2\u03cb\u03ce\5\u00b5Z\2\u03cc\u03ce\t")
        buf.write("\17\2\2\u03cd\u03ca\3\2\2\2\u03cd\u03cb\3\2\2\2\u03cd")
        buf.write("\u03cc\3\2\2\2\u03ce\u03d1\3\2\2\2\u03cf\u03d0\3\2\2\2")
        buf.write("\u03cf\u03cd\3\2\2\2\u03d0\u03d2\3\2\2\2\u03d1\u03cf\3")
        buf.write("\2\2\2\u03d2\u03d3\7b\2\2\u03d3\u00fa\3\2\2\2\u03d4\u03db")
        buf.write("\7$\2\2\u03d5\u03d6\7^\2\2\u03d6\u03da\7$\2\2\u03d7\u03da")
        buf.write("\5\u00ff\177\2\u03d8\u03da\5\u0101\u0080\2\u03d9\u03d5")
        buf.write("\3\2\2\2\u03d9\u03d7\3\2\2\2\u03d9\u03d8\3\2\2\2\u03da")
        buf.write("\u03dd\3\2\2\2\u03db\u03dc\3\2\2\2\u03db\u03d9\3\2\2\2")
        buf.write("\u03dc\u03de\3\2\2\2\u03dd\u03db\3\2\2\2\u03de\u03df\7")
        buf.write("$\2\2\u03df\u00fc\3\2\2\2\u03e0\u03e3\7)\2\2\u03e1\u03e4")
        buf.write("\5\u00ff\177\2\u03e2\u03e4\5\u0101\u0080\2\u03e3\u03e1")
        buf.write("\3\2\2\2\u03e3\u03e2\3\2\2\2\u03e4\u03e5\3\2\2\2\u03e5")
        buf.write("\u03e6\7)\2\2\u03e6\u00fe\3\2\2\2\u03e7\u03ec\5\u0117")
        buf.write("\u008b\2\u03e8\u03ec\5\u0107\u0083\2\u03e9\u03ec\5\u0109")
        buf.write("\u0084\2\u03ea\u03ec\5\u010b\u0085\2\u03eb\u03e7\3\2\2")
        buf.write("\2\u03eb\u03e8\3\2\2\2\u03eb\u03e9\3\2\2\2\u03eb\u03ea")
        buf.write("\3\2\2\2\u03ec\u0100\3\2\2\2\u03ed\u03f0\5\u0103\u0081")
        buf.write("\2\u03ee\u03f0\5\u0105\u0082\2\u03ef\u03ed\3\2\2\2\u03ef")
        buf.write("\u03ee\3\2\2\2\u03f0\u0102\3\2\2\2\u03f1\u03f2\7^\2\2")
        buf.write("\u03f2\u03f3\5\u0113\u0089\2\u03f3\u03f4\5\u0113\u0089")
        buf.write("\2\u03f4\u03f5\5\u0113\u0089\2\u03f5\u0104\3\2\2\2\u03f6")
        buf.write("\u03f7\7^\2\2\u03f7\u03f8\7z\2\2\u03f8\u03f9\5\u0115\u008a")
        buf.write("\2\u03f9\u03fa\5\u0115\u008a\2\u03fa\u0106\3\2\2\2\u03fb")
        buf.write("\u03fc\7^\2\2\u03fc\u03fd\7w\2\2\u03fd\u03fe\3\2\2\2\u03fe")
        buf.write("\u03ff\5\u0115\u008a\2\u03ff\u0400\5\u0115\u008a\2\u0400")
        buf.write("\u0401\5\u0115\u008a\2\u0401\u0402\5\u0115\u008a\2\u0402")
        buf.write("\u0108\3\2\2\2\u0403\u0404\7^\2\2\u0404\u0405\7W\2\2\u0405")
        buf.write("\u0406\3\2\2\2\u0406\u0407\5\u0115\u008a\2\u0407\u0408")
        buf.write("\5\u0115\u008a\2\u0408\u0409\5\u0115\u008a\2\u0409\u040a")
        buf.write("\5\u0115\u008a\2\u040a\u040b\5\u0115\u008a\2\u040b\u040c")
        buf.write("\5\u0115\u008a\2\u040c\u040d\5\u0115\u008a\2\u040d\u040e")
        buf.write("\5\u0115\u008a\2\u040e\u010a\3\2\2\2\u040f\u0410\7^\2")
        buf.write("\2\u0410\u0411\t\20\2\2\u0411\u010c\3\2\2\2\u0412\u0417")
        buf.write("\t\21\2\2\u0413\u0414\7g\2\2\u0414\u0415\7z\2\2\u0415")
        buf.write("\u0417\7p\2\2\u0416\u0412\3\2\2\2\u0416\u0413\3\2\2\2")
        buf.write("\u0417\u0419\3\2\2\2\u0418\u041a\t\22\2\2\u0419\u0418")
        buf.write("\3\2\2\2\u0419\u041a\3\2\2\2\u041a\u041b\3\2\2\2\u041b")
        buf.write("\u041c\5\u00f5z\2\u041c\u010e\3\2\2\2\u041d\u041e\t\3")
        buf.write("\2\2\u041e\u0110\3\2\2\2\u041f\u0422\5\u0119\u008c\2\u0420")
        buf.write("\u0422\7a\2\2\u0421\u041f\3\2\2\2\u0421\u0420\3\2\2\2")
        buf.write("\u0422\u0112\3\2\2\2\u0423\u0424\t\23\2\2\u0424\u0114")
        buf.write("\3\2\2\2\u0425\u0426\t\24\2\2\u0426\u0116\3\2\2\2\u0427")
        buf.write("\u0428\n\25\2\2\u0428\u0118\3\2\2\2\u0429\u042b\t\26\2")
        buf.write("\2\u042a\u0429\3\2\2\2\u042b\u011a\3\2\2\2\u042c\u042e")
        buf.write("\t\27\2\2\u042d\u042c\3\2\2\2\u042e\u011c\3\2\2\2A\2\3")
        buf.write("\4\u0120\u0126\u0128\u012e\u0134\u0136\u0147\u015b\u0166")
        buf.write("\u0196\u0273\u027d\u0288\u0295\u02d7\u02da\u02e1\u02e8")
        buf.write("\u02ea\u02f1\u02f6\u02fd\u030d\u0317\u031b\u0324\u0329")
        buf.write("\u0330\u0352\u035f\u0366\u036c\u036e\u0378\u0381\u0385")
        buf.write("\u038a\u0392\u0397\u039d\u03a4\u03ac\u03b1\u03b4\u03bc")
        buf.write("\u03be\u03c3\u03c7\u03cd\u03cf\u03d9\u03db\u03e3\u03eb")
        buf.write("\u03ef\u0416\u0419\u0421\u042a\u042d\b\2\3\2\2\4\2\7\3")
        buf.write("\2\6\2\2\7\4\2\t`\2")
        return buf.getvalue()


class JingleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CONSUME = 2

    MODE_IN_STRING = 1
    MODE_IN_INTERPOLATION = 2

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
    ENUM = 30
    IMPORT = 31
    FROM = 32
    PACKAGE = 33
    AS = 34
    BREAK = 35
    ABSTRACT = 36
    SELECT = 37
    INPUT = 38
    EACH = 39
    NEW = 40
    CONTINUE = 41
    EXPORT = 42
    INCLUDE = 43
    REQUIRE = 44
    SUMMON = 45
    WALRUS = 46
    EQUALS = 47
    EQEQ = 48
    NOTEQUAL = 49
    LTEQUALS = 50
    GTEQUALS = 51
    PLUS = 52
    MINUS = 53
    MULTIPLY = 54
    DIVIDE = 55
    LESSTHAN = 56
    GREATERTHAN = 57
    BANG = 58
    POWER = 59
    MODULUS = 60
    VERTICAL = 61
    ORSYMBOL = 62
    HASH = 63
    AMBERSAND = 64
    ANDSYMBOL = 65
    TYPE_INT = 66
    TYPE_DECIMAL = 67
    TYPE_STRING = 68
    TYPE_BOOLEAN = 69
    COMMA = 70
    LBRACKET = 71
    RBRACKET = 72
    LBRACE = 73
    RBRACE = 74
    LSQRBRACKET = 75
    RSQRBRACKET = 76
    ARROW = 77
    COLON = 78
    DOT = 79
    ELLIPSIS = 80
    PLUSPLUS = 81
    MINUSMINUS = 82
    FLOAT = 83
    STRING = 84
    BOOLEAN = 85
    NULL = 86
    CHAR = 87
    INT_LITERAL = 88
    FLOAT_LITERAL = 89
    WHITESPACE = 90
    COMMENT = 91
    TERMINATOR = 92
    STRING_OPEN = 93
    UNMATCHED = 94
    SCAPE_STRING_DELIMITER = 95
    ESCAPE_SLASH = 96
    ESCAPE_NEWLINE = 97
    ESCAPE_SHARP = 98
    STRING_CLOSE = 99
    INTERPOLATION_OPEN = 100
    STRING_CONTENT = 101
    INTERPOLATION_CLOSE = 102
    NOUNICODEID = 103
    IDENTIFIER = 104
    BINARY_OP = 105
    INT_LIT = 106
    FLOAT_LIT = 107
    STRING_LIT = 108
    RUNE_LIT = 109
    LITTLE_U_VALUE = 110
    BIG_U_VALUE = 111

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"CONSUME" ]

    modeNames = [ "DEFAULT_MODE", "MODE_IN_STRING", "MODE_IN_INTERPOLATION" ]

    literalNames = [ "<INVALID>",
            "'var'", "'echo'", "'return'", "'if'", "'then'", "'and'", "'or'",
            "'in'", "'else'", "'while'", "'for'", "'true'", "'false'", "'fn'",
            "'class'", "'let'", "'bind'", "'trait'", "'def'", "'protocol'",
            "'enum'", "'import'", "'from'", "'package'", "'as'", "'break'",
            "'abstract'", "'select'", "'input'", "'each'", "'new'", "'continue'",
            "'export'", "'include'", "'require'", "'summon'", "':='", "'='",
            "'=='", "'!='", "'<='", "'>='", "'+'", "'-'", "'*'", "'/'",
            "'<'", "'>'", "'!'", "'^'", "'%'", "'|'", "'||'", "'#'", "'&'",
            "'&&'", "','", "'('", "')'", "'{'", "'['", "']'", "'->'", "':'",
            "'.'", "'...'", "'++'", "'--'", "'float'", "'string'", "'bool'",
            "'null'", "'char'", "'\\\"'", "'\\\\'", "'\\n'", "'\\#'", "'#{'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS",
            "VAR", "ARRAY", "CONST", "LOCAL", "ECHO", "RETURN", "IF", "THEN",
            "AND", "OR", "IN", "ELSE", "ELSEIF", "WHILE", "FOR", "TRUE",
            "FALSE", "FUNCTION", "CLASS", "LET", "BIND", "TRAIT", "DEFINE",
            "PROTOCOL", "ENUM", "IMPORT", "FROM", "PACKAGE", "AS", "BREAK",
            "ABSTRACT", "SELECT", "INPUT", "EACH", "NEW", "CONTINUE", "EXPORT",
            "INCLUDE", "REQUIRE", "SUMMON", "WALRUS", "EQUALS", "EQEQ",
            "NOTEQUAL", "LTEQUALS", "GTEQUALS", "PLUS", "MINUS", "MULTIPLY",
            "DIVIDE", "LESSTHAN", "GREATERTHAN", "BANG", "POWER", "MODULUS",
            "VERTICAL", "ORSYMBOL", "HASH", "AMBERSAND", "ANDSYMBOL", "TYPE_INT",
            "TYPE_DECIMAL", "TYPE_STRING", "TYPE_BOOLEAN", "COMMA", "LBRACKET",
            "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET",
            "ARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS",
            "FLOAT", "STRING", "BOOLEAN", "NULL", "CHAR", "INT_LITERAL",
            "FLOAT_LITERAL", "WHITESPACE", "COMMENT", "TERMINATOR", "STRING_OPEN",
            "UNMATCHED", "SCAPE_STRING_DELIMITER", "ESCAPE_SLASH", "ESCAPE_NEWLINE",
            "ESCAPE_SHARP", "STRING_CLOSE", "INTERPOLATION_OPEN", "STRING_CONTENT",
            "INTERPOLATION_CLOSE", "NOUNICODEID", "IDENTIFIER", "BINARY_OP",
            "INT_LIT", "FLOAT_LIT", "STRING_LIT", "RUNE_LIT", "LITTLE_U_VALUE",
            "BIG_U_VALUE" ]

    ruleNames = [ "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", "VAR",
                  "ARRAY", "CONST", "LOCAL", "ECHO", "RETURN", "IF", "THEN",
                  "AND", "OR", "IN", "ELSE", "ELSEIF", "WHILE", "FOR", "TRUE",
                  "FALSE", "FUNCTION", "CLASS", "LET", "BIND", "TRAIT",
                  "DEFINE", "PROTOCOL", "ENUM", "IMPORT", "FROM", "PACKAGE",
                  "AS", "BREAK", "ABSTRACT", "SELECT", "INPUT", "EACH",
                  "NEW", "CONTINUE", "EXPORT", "INCLUDE", "REQUIRE", "SUMMON",
                  "WALRUS", "EQUALS", "EQEQ", "NOTEQUAL", "LTEQUALS", "GTEQUALS",
                  "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN",
                  "BANG", "POWER", "MODULUS", "VERTICAL", "ORSYMBOL", "HASH",
                  "AMBERSAND", "ANDSYMBOL", "TYPE_INT", "TYPE_DECIMAL",
                  "TYPE_STRING", "TYPE_BOOLEAN", "COMMA", "LBRACKET", "RBRACKET",
                  "LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET", "ARROW",
                  "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS",
                  "FLOAT", "STRING", "BOOLEAN", "NULL", "CHAR", "INT_LITERAL",
                  "FLOAT_LITERAL", "SEMICOLON", "NEWLINE", "ID", "DIGIT_CONT",
                  "HEXDIGIT", "BINARY", "UNICODE_WS", "WHITESPACE", "COMMENT",
                  "TERMINATOR", "STRING_OPEN", "UNMATCHED", "SCAPE_STRING_DELIMITER",
                  "ESCAPE_SLASH", "ESCAPE_NEWLINE", "ESCAPE_SHARP", "STRING_CLOSE",
                  "INTERPOLATION_OPEN", "STRING_CONTENT", "STR_UNMATCHED",
                  "INTERPOLATION_CLOSE", "NOUNICODEID", "IDENTIFIER", "BINARY_OP",
                  "REL_OP", "ADD_OP", "MUL_OP", "UNARY_OP", "INT_LIT", "DECIMAL_LIT"
                  "OCTAL_LIT", "HEX_LIT", "FLOAT_LIT", "DECIMALS", "STRING_LIT",
                  "RAW_STRING_LIT", "INTERPRETED_STRING_LIT", "RUNE_LIT",
                  "UNICODE_VALUE", "BYTE_VALUE", "OCTAL_BYTE_VALUE", "HEX_BYTE_VALUE",
                  "LITTLE_U_VALUE", "BIG_U_VALUE", "ESCAPED_CHAR", "EXPONENT",
                  "DECIMAL_DIGIT", "LETTER", "OCTAL_DIGIT", "HEX_DIGIT",
                  "UNICODE_CHAR", "UNICODE_LETTER", "UNICODE_DIGIT" ]

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


