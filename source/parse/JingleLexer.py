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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2`")
        buf.write("\u03b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\4}\t}\3\2\7\2\u00fd\n\2\f\2\16")
        buf.write("\2\u0100\13\2\3\2\6\2\u0103\n\2\r\2\16\2\u0104\5\2\u0107")
        buf.write("\n\2\3\3\3\3\7\3\u010b\n\3\f\3\16\3\u010e\13\3\3\3\6\3")
        buf.write("\u0111\n\3\r\3\16\3\u0112\5\3\u0115\n\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\5:\u01e7\n:\3;\3;\3;\3;\3;\3;\3;\3;\5;\u01f1\n;\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u01fc\n<\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\5=\u0209\n=\3>\3>\3?\3?\3?\3@\3@\3@\3")
        buf.write("A\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3F\3")
        buf.write("G\3G\3H\3H\3I\3I\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3L\7L\u0236")
        buf.write("\nL\fL\16L\u0239\13L\5L\u023b\nL\3M\3M\3M\7M\u0240\nM")
        buf.write("\fM\16M\u0243\13M\3M\3M\6M\u0247\nM\rM\16M\u0248\5M\u024b")
        buf.write("\nM\3N\3N\3O\7O\u0250\nO\fO\16O\u0253\13O\3O\3O\7O\u0257")
        buf.write("\nO\fO\16O\u025a\13O\3P\3P\3Q\3Q\3R\3R\3S\3S\3S\3S\3T")
        buf.write("\6T\u0267\nT\rT\16T\u0268\3U\3U\7U\u026d\nU\fU\16U\u0270")
        buf.write("\13U\3V\3V\3V\3V\7V\u0276\nV\fV\16V\u0279\13V\3V\5V\u027c")
        buf.write("\nV\3V\3V\3V\3V\3V\7V\u0283\nV\fV\16V\u0286\13V\3V\3V")
        buf.write("\5V\u028a\nV\3W\3W\5W\u028e\nW\3X\3X\3X\5X\u0293\nX\3")
        buf.write("Y\3Y\3Y\3Y\5Y\u0299\nY\3Z\3Z\3Z\3Z\3Z\5Z\u02a0\nZ\3Z\3")
        buf.write("Z\5Z\u02a4\nZ\3[\3[\3[\3[\3[\5[\u02ab\n[\3[\3[\5[\u02af")
        buf.write("\n[\3\\\3\\\7\\\u02b3\n\\\f\\\16\\\u02b6\13\\\3\\\6\\")
        buf.write("\u02b9\n\\\r\\\16\\\u02ba\5\\\u02bd\n\\\3]\3]\3]\6]\u02c2")
        buf.write("\n]\r]\16]\u02c3\3^\3^\3^\6^\u02c9\n^\r^\16^\u02ca\3_")
        buf.write("\3_\3_\6_\u02d0\n_\r_\16_\u02d1\3`\3`\5`\u02d6\n`\3a\3")
        buf.write("a\5a\u02da\na\3a\3a\3b\3b\3b\5b\u02e1\nb\3b\3b\3c\3c\3")
        buf.write("d\3d\3d\7d\u02ea\nd\fd\16d\u02ed\13d\3d\3d\3d\3d\7d\u02f3")
        buf.write("\nd\fd\16d\u02f6\13d\3d\5d\u02f9\nd\3e\3e\3e\3e\3e\7e")
        buf.write("\u0300\ne\fe\16e\u0303\13e\3e\3e\3e\3e\3e\3e\3e\3e\7e")
        buf.write("\u030d\ne\fe\16e\u0310\13e\3e\3e\3e\5e\u0315\ne\3f\3f")
        buf.write("\5f\u0319\nf\3g\3g\3h\3h\3h\3h\5h\u0321\nh\3i\3i\3j\3")
        buf.write("j\3k\3k\3l\3l\3m\3m\3n\5n\u032e\nn\3n\3n\3n\3n\5n\u0334")
        buf.write("\nn\3o\3o\5o\u0338\no\3o\3o\3p\6p\u033d\np\rp\16p\u033e")
        buf.write("\3q\3q\6q\u0343\nq\rq\16q\u0344\3r\3r\5r\u0349\nr\3r\6")
        buf.write("r\u034c\nr\rr\16r\u034d\3s\3s\3s\7s\u0353\ns\fs\16s\u0356")
        buf.write("\13s\3s\3s\3s\3s\7s\u035c\ns\fs\16s\u035f\13s\3s\5s\u0362")
        buf.write("\ns\3t\3t\3t\3t\3t\7t\u0369\nt\ft\16t\u036c\13t\3t\3t")
        buf.write("\3t\3t\3t\3t\3t\3t\7t\u0376\nt\ft\16t\u0379\13t\3t\3t")
        buf.write("\3t\5t\u037e\nt\3u\3u\5u\u0382\nu\3v\5v\u0385\nv\3w\5")
        buf.write("w\u0388\nw\3x\5x\u038b\nx\3y\3y\3y\3z\3z\5z\u0392\nz\3")
        buf.write("z\5z\u0395\nz\3z\3z\5z\u0399\nz\3{\5{\u039c\n{\3|\3|\5")
        buf.write("|\u03a0\n|\3}\3}\3}\5}\u03a5\n}\3}\3}\5}\u03a9\n}\3}\5")
        buf.write("}\u03ac\n}\5}\u03ae\n}\3}\3}\7\u0284\u0301\u030e\u036a")
        buf.write("\u0377\2~\3\5\5\6\7\7\t\b\13\t\r\n\17\13\21\f\23\r\25")
        buf.write("\16\27\17\31\20\33\21\35\22\37\23!\24#\25%\26\'\27)\30")
        buf.write("+\31-\32/\33\61\34\63\35\65\36\67\379 ;!=\"?#A$C%E&G\'")
        buf.write("I(K)M*O+Q,S-U.W/Y\60[\61]\62_\63a\64c\65e\66g\67i8k9m")
        buf.write(":o;q<s=u>w?y@{A}B\177C\u0081D\u0083E\u0085F\u0087G\u0089")
        buf.write("H\u008bI\u008dJ\u008fK\u0091L\u0093M\u0095N\u0097O\u0099")
        buf.write("P\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9Q\u00abR\u00adS\u00afT\u00b1U\u00b3V\u00b5W\u00b7")
        buf.write("X\u00b9Y\u00bbZ\u00bd[\u00bf\\\u00c1]\u00c3^\u00c5_\u00c7")
        buf.write("\2\u00c9\2\u00cb\2\u00cd\2\u00cf\2\u00d1\2\u00d3\2\u00d5")
        buf.write("\2\u00d7\2\u00d9\2\u00db\2\u00dd\2\u00df\2\u00e1\2\u00e3")
        buf.write("\2\u00e5\2\u00e7\2\u00e9\2\u00eb\2\u00ed\2\u00ef\2\u00f1")
        buf.write("\2\u00f3\2\u00f5\2\u00f7\2\u00f9`\3\2\"\3\2\63;\3\2\62")
        buf.write(";\3\2aa\3\2c|\6\2\62;C\\aac|\4\2\62;aa\6\2\62;CHaach\4")
        buf.write("\2\62\63aa\f\2\13\17\"\"\u0087\u0087\u00a2\u00a2\u1682")
        buf.write("\u1682\u2002\u200c\u202a\u202b\u2031\u2031\u2061\u2061")
        buf.write("\u3002\u3002\4\2\13\13\"\"\4\2\f\f\17\17\b\2HHTTWWhht")
        buf.write("tww\4\2HHhh\4\2TTtt\4\2DDdd\4\2QQqq\4\2ZZzz\4\2LLll\6")
        buf.write("\2\f\f\16\17))^^\6\2\f\f\16\17$$^^\3\2^^\3\2\629\5\2\62")
        buf.write(";CHch\3\2\62\63\4\2GGgg\4\2--//\7\2\2\13\r\16\20(*]_\u0081")
        buf.write("\7\2\2\13\r\16\20#%]_\u0081\4\2\2]_\u0081\3\2\2\u0081")
        buf.write("\u0129\2C\\aac|\u00ac\u00ac\u00b7\u00b7\u00bc\u00bc\u00c2")
        buf.write("\u00d8\u00da\u00f8\u00fa\u0243\u0252\u02c3\u02c8\u02d3")
        buf.write("\u02e2\u02e6\u02f0\u02f0\u037c\u037c\u0388\u0388\u038a")
        buf.write("\u038c\u038e\u038e\u0390\u03a3\u03a5\u03d0\u03d2\u03f7")
        buf.write("\u03f9\u0483\u048c\u04d0\u04d2\u04fb\u0502\u0511\u0533")
        buf.write("\u0558\u055b\u055b\u0563\u0589\u05d2\u05ec\u05f2\u05f4")
        buf.write("\u0623\u063c\u0642\u064c\u0670\u0671\u0673\u06d5\u06d7")
        buf.write("\u06d7\u06e7\u06e8\u06f0\u06f1\u06fc\u06fe\u0701\u0701")
        buf.write("\u0712\u0712\u0714\u0731\u074f\u076f\u0782\u07a7\u07b3")
        buf.write("\u07b3\u0906\u093b\u093f\u093f\u0952\u0952\u095a\u0963")
        buf.write("\u097f\u097f\u0987\u098e\u0991\u0992\u0995\u09aa\u09ac")
        buf.write("\u09b2\u09b4\u09b4\u09b8\u09bb\u09bf\u09bf\u09d0\u09d0")
        buf.write("\u09de\u09df\u09e1\u09e3\u09f2\u09f3\u0a07\u0a0c\u0a11")
        buf.write("\u0a12\u0a15\u0a2a\u0a2c\u0a32\u0a34\u0a35\u0a37\u0a38")
        buf.write("\u0a3a\u0a3b\u0a5b\u0a5e\u0a60\u0a60\u0a74\u0a76\u0a87")
        buf.write("\u0a8f\u0a91\u0a93\u0a95\u0aaa\u0aac\u0ab2\u0ab4\u0ab5")
        buf.write("\u0ab7\u0abb\u0abf\u0abf\u0ad2\u0ad2\u0ae2\u0ae3\u0b07")
        buf.write("\u0b0e\u0b11\u0b12\u0b15\u0b2a\u0b2c\u0b32\u0b34\u0b35")
        buf.write("\u0b37\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f\u0b61\u0b63\u0b73")
        buf.write("\u0b73\u0b85\u0b85\u0b87\u0b8c\u0b90\u0b92\u0b94\u0b97")
        buf.write("\u0b9b\u0b9c\u0b9e\u0b9e\u0ba0\u0ba1\u0ba5\u0ba6\u0baa")
        buf.write("\u0bac\u0bb0\u0bbb\u0c07\u0c0e\u0c10\u0c12\u0c14\u0c2a")
        buf.write("\u0c2c\u0c35\u0c37\u0c3b\u0c62\u0c63\u0c87\u0c8e\u0c90")
        buf.write("\u0c92\u0c94\u0caa\u0cac\u0cb5\u0cb7\u0cbb\u0cbf\u0cbf")
        buf.write("\u0ce0\u0ce0\u0ce2\u0ce3\u0d07\u0d0e\u0d10\u0d12\u0d14")
        buf.write("\u0d2a\u0d2c\u0d3b\u0d62\u0d63\u0d87\u0d98\u0d9c\u0db3")
        buf.write("\u0db5\u0dbd\u0dbf\u0dbf\u0dc2\u0dc8\u0e03\u0e32\u0e34")
        buf.write("\u0e35\u0e42\u0e48\u0e83\u0e84\u0e86\u0e86\u0e89\u0e8a")
        buf.write("\u0e8c\u0e8c\u0e8f\u0e8f\u0e96\u0e99\u0e9b\u0ea1\u0ea3")
        buf.write("\u0ea5\u0ea7\u0ea7\u0ea9\u0ea9\u0eac\u0ead\u0eaf\u0eb2")
        buf.write("\u0eb4\u0eb5\u0ebf\u0ebf\u0ec2\u0ec6\u0ec8\u0ec8\u0ede")
        buf.write("\u0edf\u0f02\u0f02\u0f42\u0f49\u0f4b\u0f6c\u0f8a\u0f8d")
        buf.write("\u1002\u1023\u1025\u1029\u102b\u102c\u1052\u1057\u10a2")
        buf.write("\u10c7\u10d2\u10fc\u10fe\u10fe\u1102\u115b\u1161\u11a4")
        buf.write("\u11aa\u11fb\u1202\u124a\u124c\u124f\u1252\u1258\u125a")
        buf.write("\u125a\u125c\u125f\u1262\u128a\u128c\u128f\u1292\u12b2")
        buf.write("\u12b4\u12b7\u12ba\u12c0\u12c2\u12c2\u12c4\u12c7\u12ca")
        buf.write("\u12d8\u12da\u1312\u1314\u1317\u131a\u135c\u1382\u1391")
        buf.write("\u13a2\u13f6\u1403\u166e\u1671\u1678\u1683\u169c\u16a2")
        buf.write("\u16ec\u16f0\u16f2\u1702\u170e\u1710\u1713\u1722\u1733")
        buf.write("\u1742\u1753\u1762\u176e\u1770\u1772\u1782\u17b5\u17d9")
        buf.write("\u17d9\u17de\u17de\u1822\u1879\u1882\u18aa\u1902\u191e")
        buf.write("\u1952\u196f\u1972\u1976\u1982\u19ab\u19c3\u19c9\u1a02")
        buf.write("\u1a18\u1d02\u1dc1\u1e02\u1e9d\u1ea2\u1efb\u1f02\u1f17")
        buf.write("\u1f1a\u1f1f\u1f22\u1f47\u1f4a\u1f4f\u1f52\u1f59\u1f5b")
        buf.write("\u1f5b\u1f5d\u1f5d\u1f5f\u1f5f\u1f61\u1f7f\u1f82\u1fb6")
        buf.write("\u1fb8\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8\u1fce\u1fd2")
        buf.write("\u1fd5\u1fd8\u1fdd\u1fe2\u1fee\u1ff4\u1ff6\u1ff8\u1ffe")
        buf.write("\u2073\u2073\u2081\u2081\u2092\u2096\u2104\u2104\u2109")
        buf.write("\u2109\u210c\u2115\u2117\u2117\u211a\u211f\u2126\u2126")
        buf.write("\u2128\u2128\u212a\u212a\u212c\u2133\u2135\u213b\u213e")
        buf.write("\u2141\u2147\u214b\u2162\u2185\u2c02\u2c30\u2c32\u2c60")
        buf.write("\u2c82\u2ce6\u2d02\u2d27\u2d32\u2d67\u2d71\u2d71\u2d82")
        buf.write("\u2d98\u2da2\u2da8\u2daa\u2db0\u2db2\u2db8\u2dba\u2dc0")
        buf.write("\u2dc2\u2dc8\u2dca\u2dd0\u2dd2\u2dd8\u2dda\u2de0\u3007")
        buf.write("\u3009\u3023\u302b\u3033\u3037\u303a\u303e\u3043\u3098")
        buf.write("\u309d\u30a1\u30a3\u30fc\u30fe\u3101\u3107\u312e\u3133")
        buf.write("\u3190\u31a2\u31b9\u31f2\u3201\u3402\u4db7\u4e02\u9fbd")
        buf.write("\ua002\ua48e\ua802\ua803\ua805\ua807\ua809\ua80c\ua80e")
        buf.write("\ua824\uac02\ud7a5\uf902\ufa2f\ufa32\ufa6c\ufa72\ufadb")
        buf.write("\ufb02\ufb08\ufb15\ufb19\ufb1f\ufb1f\ufb21\ufb2a\ufb2c")
        buf.write("\ufb38\ufb3a\ufb3e\ufb40\ufb40\ufb42\ufb43\ufb45\ufb46")
        buf.write("\ufb48\ufbb3\ufbd5\ufd3f\ufd52\ufd91\ufd94\ufdc9\ufdf2")
        buf.write("\ufdfd\ufe72\ufe76\ufe78\ufefe\uff23\uff3c\uff43\uff5c")
        buf.write("\uff68\uffc0\uffc4\uffc9\uffcc\uffd1\uffd4\uffd9\uffdc")
        buf.write("\uffde\u0096\2\62;\u0302\u0371\u0485\u0488\u0593\u05bb")
        buf.write("\u05bd\u05bf\u05c1\u05c1\u05c3\u05c4\u05c6\u05c7\u05c9")
        buf.write("\u05c9\u0612\u0617\u064d\u0660\u0662\u066b\u0672\u0672")
        buf.write("\u06d8\u06de\u06e1\u06e6\u06e9\u06ea\u06ec\u06ef\u06f2")
        buf.write("\u06fb\u0713\u0713\u0732\u074c\u07a8\u07b2\u0903\u0905")
        buf.write("\u093e\u093e\u0940\u094f\u0953\u0956\u0964\u0965\u0968")
        buf.write("\u0971\u0983\u0985\u09be\u09be\u09c0\u09c6\u09c9\u09ca")
        buf.write("\u09cd\u09cf\u09d9\u09d9\u09e4\u09e5\u09e8\u09f1\u0a03")
        buf.write("\u0a05\u0a3e\u0a3e\u0a40\u0a44\u0a49\u0a4a\u0a4d\u0a4f")
        buf.write("\u0a68\u0a73\u0a83\u0a85\u0abe\u0abe\u0ac0\u0ac7\u0ac9")
        buf.write("\u0acb\u0acd\u0acf\u0ae4\u0ae5\u0ae8\u0af1\u0b03\u0b05")
        buf.write("\u0b3e\u0b3e\u0b40\u0b45\u0b49\u0b4a\u0b4d\u0b4f\u0b58")
        buf.write("\u0b59\u0b68\u0b71\u0b84\u0b84\u0bc0\u0bc4\u0bc8\u0bca")
        buf.write("\u0bcc\u0bcf\u0bd9\u0bd9\u0be8\u0bf1\u0c03\u0c05\u0c40")
        buf.write("\u0c46\u0c48\u0c4a\u0c4c\u0c4f\u0c57\u0c58\u0c68\u0c71")
        buf.write("\u0c84\u0c85\u0cbe\u0cbe\u0cc0\u0cc6\u0cc8\u0cca\u0ccc")
        buf.write("\u0ccf\u0cd7\u0cd8\u0ce8\u0cf1\u0d04\u0d05\u0d40\u0d45")
        buf.write("\u0d48\u0d4a\u0d4c\u0d4f\u0d59\u0d59\u0d68\u0d71\u0d84")
        buf.write("\u0d85\u0dcc\u0dcc\u0dd1\u0dd6\u0dd8\u0dd8\u0dda\u0de1")
        buf.write("\u0df4\u0df5\u0e33\u0e33\u0e36\u0e3c\u0e49\u0e50\u0e52")
        buf.write("\u0e5b\u0eb3\u0eb3\u0eb6\u0ebb\u0ebd\u0ebe\u0eca\u0ecf")
        buf.write("\u0ed2\u0edb\u0f1a\u0f1b\u0f22\u0f2b\u0f37\u0f37\u0f39")
        buf.write("\u0f39\u0f3b\u0f3b\u0f40\u0f41\u0f73\u0f86\u0f88\u0f89")
        buf.write("\u0f92\u0f99\u0f9b\u0fbe\u0fc8\u0fc8\u102e\u1034\u1038")
        buf.write("\u103b\u1042\u104b\u1058\u105b\u1361\u1361\u136b\u1373")
        buf.write("\u1714\u1716\u1734\u1736\u1754\u1755\u1774\u1775\u17b8")
        buf.write("\u17d5\u17df\u17df\u17e2\u17eb\u180d\u180f\u1812\u181b")
        buf.write("\u18ab\u18ab\u1922\u192d\u1932\u193d\u1948\u1951\u19b2")
        buf.write("\u19c2\u19ca\u19cb\u19d2\u19db\u1a19\u1a1d\u1dc2\u1dc5")
        buf.write("\u2041\u2042\u2056\u2056\u20d2\u20de\u20e3\u20e3\u20e7")
        buf.write("\u20ed\u302c\u3031\u309b\u309c\ua804\ua804\ua808\ua808")
        buf.write("\ua80d\ua80d\ua825\ua829\ufb20\ufb20\ufe02\ufe11\ufe22")
        buf.write("\ufe25\ufe35\ufe36\ufe4f\ufe51\uff12\uff1b\uff41\uff41")
        buf.write("\2\u03e0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9")
        buf.write("\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2")
        buf.write("\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00f9")
        buf.write("\3\2\2\2\3\u0106\3\2\2\2\5\u0114\3\2\2\2\7\u0116\3\2\2")
        buf.write("\2\t\u0118\3\2\2\2\13\u011c\3\2\2\2\r\u0122\3\2\2\2\17")
        buf.write("\u0126\3\2\2\2\21\u012b\3\2\2\2\23\u0132\3\2\2\2\25\u0135")
        buf.write("\3\2\2\2\27\u013a\3\2\2\2\31\u013e\3\2\2\2\33\u0141\3")
        buf.write("\2\2\2\35\u0144\3\2\2\2\37\u0149\3\2\2\2!\u014e\3\2\2")
        buf.write("\2#\u0154\3\2\2\2%\u0158\3\2\2\2\'\u015c\3\2\2\2)\u0161")
        buf.write("\3\2\2\2+\u0167\3\2\2\2-\u016a\3\2\2\2/\u0170\3\2\2\2")
        buf.write("\61\u0174\3\2\2\2\63\u017a\3\2\2\2\65\u017e\3\2\2\2\67")
        buf.write("\u0185\3\2\2\29\u018a\3\2\2\2;\u018d\3\2\2\2=\u0193\3")
        buf.write("\2\2\2?\u0197\3\2\2\2A\u019f\3\2\2\2C\u01a2\3\2\2\2E\u01a4")
        buf.write("\3\2\2\2G\u01a7\3\2\2\2I\u01aa\3\2\2\2K\u01ad\3\2\2\2")
        buf.write("M\u01b0\3\2\2\2O\u01b2\3\2\2\2Q\u01b4\3\2\2\2S\u01b6\3")
        buf.write("\2\2\2U\u01b8\3\2\2\2W\u01ba\3\2\2\2Y\u01bc\3\2\2\2[\u01bf")
        buf.write("\3\2\2\2]\u01c2\3\2\2\2_\u01c4\3\2\2\2a\u01c6\3\2\2\2")
        buf.write("c\u01c8\3\2\2\2e\u01ca\3\2\2\2g\u01cd\3\2\2\2i\u01cf\3")
        buf.write("\2\2\2k\u01d1\3\2\2\2m\u01d4\3\2\2\2o\u01d6\3\2\2\2q\u01d9")
        buf.write("\3\2\2\2s\u01e6\3\2\2\2u\u01f0\3\2\2\2w\u01fb\3\2\2\2")
        buf.write("y\u0208\3\2\2\2{\u020a\3\2\2\2}\u020c\3\2\2\2\177\u020f")
        buf.write("\3\2\2\2\u0081\u0212\3\2\2\2\u0083\u0215\3\2\2\2\u0085")
        buf.write("\u0218\3\2\2\2\u0087\u021b\3\2\2\2\u0089\u021e\3\2\2\2")
        buf.write("\u008b\u0221\3\2\2\2\u008d\u0224\3\2\2\2\u008f\u0226\3")
        buf.write("\2\2\2\u0091\u0228\3\2\2\2\u0093\u022c\3\2\2\2\u0095\u022f")
        buf.write("\3\2\2\2\u0097\u023a\3\2\2\2\u0099\u024a\3\2\2\2\u009b")
        buf.write("\u024c\3\2\2\2\u009d\u0251\3\2\2\2\u009f\u025b\3\2\2\2")
        buf.write("\u00a1\u025d\3\2\2\2\u00a3\u025f\3\2\2\2\u00a5\u0261\3")
        buf.write("\2\2\2\u00a7\u0266\3\2\2\2\u00a9\u026a\3\2\2\2\u00ab\u0289")
        buf.write("\3\2\2\2\u00ad\u028d\3\2\2\2\u00af\u0292\3\2\2\2\u00b1")
        buf.write("\u0298\3\2\2\2\u00b3\u029f\3\2\2\2\u00b5\u02aa\3\2\2\2")
        buf.write("\u00b7\u02bc\3\2\2\2\u00b9\u02be\3\2\2\2\u00bb\u02c5\3")
        buf.write("\2\2\2\u00bd\u02cc\3\2\2\2\u00bf\u02d5\3\2\2\2\u00c1\u02d9")
        buf.write("\3\2\2\2\u00c3\u02e0\3\2\2\2\u00c5\u02e4\3\2\2\2\u00c7")
        buf.write("\u02f8\3\2\2\2\u00c9\u0314\3\2\2\2\u00cb\u0318\3\2\2\2")
        buf.write("\u00cd\u031a\3\2\2\2\u00cf\u0320\3\2\2\2\u00d1\u0322\3")
        buf.write("\2\2\2\u00d3\u0324\3\2\2\2\u00d5\u0326\3\2\2\2\u00d7\u0328")
        buf.write("\3\2\2\2\u00d9\u032a\3\2\2\2\u00db\u0333\3\2\2\2\u00dd")
        buf.write("\u0337\3\2\2\2\u00df\u033c\3\2\2\2\u00e1\u0340\3\2\2\2")
        buf.write("\u00e3\u0346\3\2\2\2\u00e5\u0361\3\2\2\2\u00e7\u037d\3")
        buf.write("\2\2\2\u00e9\u0381\3\2\2\2\u00eb\u0384\3\2\2\2\u00ed\u0387")
        buf.write("\3\2\2\2\u00ef\u038a\3\2\2\2\u00f1\u038c\3\2\2\2\u00f3")
        buf.write("\u038f\3\2\2\2\u00f5\u039b\3\2\2\2\u00f7\u039f\3\2\2\2")
        buf.write("\u00f9\u03ad\3\2\2\2\u00fb\u00fd\5\u00f9}\2\u00fc\u00fb")
        buf.write("\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\u0107\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0101\u0103\5\u00f9}\2\u0102\u0101\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105")
        buf.write("\u0107\3\2\2\2\u0106\u00fe\3\2\2\2\u0106\u0102\3\2\2\2")
        buf.write("\u0107\4\3\2\2\2\u0108\u010c\5\u009bN\2\u0109\u010b\5")
        buf.write("\u00f9}\2\u010a\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u0115\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010f\u0111\5\u00f9}\2\u0110\u010f")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0108\3\2\2\2")
        buf.write("\u0114\u0110\3\2\2\2\u0115\6\3\2\2\2\u0116\u0117\7$\2")
        buf.write("\2\u0117\b\3\2\2\2\u0118\u0119\7x\2\2\u0119\u011a\7c\2")
        buf.write("\2\u011a\u011b\7t\2\2\u011b\n\3\2\2\2\u011c\u011d\7e\2")
        buf.write("\2\u011d\u011e\7q\2\2\u011e\u011f\7p\2\2\u011f\u0120\7")
        buf.write("u\2\2\u0120\u0121\7v\2\2\u0121\f\3\2\2\2\u0122\u0123\7")
        buf.write("n\2\2\u0123\u0124\7q\2\2\u0124\u0125\7e\2\2\u0125\16\3")
        buf.write("\2\2\2\u0126\u0127\7g\2\2\u0127\u0128\7e\2\2\u0128\u0129")
        buf.write("\7j\2\2\u0129\u012a\7q\2\2\u012a\20\3\2\2\2\u012b\u012c")
        buf.write("\7t\2\2\u012c\u012d\7g\2\2\u012d\u012e\7v\2\2\u012e\u012f")
        buf.write("\7w\2\2\u012f\u0130\7t\2\2\u0130\u0131\7p\2\2\u0131\22")
        buf.write("\3\2\2\2\u0132\u0133\7k\2\2\u0133\u0134\7h\2\2\u0134\24")
        buf.write("\3\2\2\2\u0135\u0136\7v\2\2\u0136\u0137\7j\2\2\u0137\u0138")
        buf.write("\7g\2\2\u0138\u0139\7p\2\2\u0139\26\3\2\2\2\u013a\u013b")
        buf.write("\7c\2\2\u013b\u013c\7p\2\2\u013c\u013d\7f\2\2\u013d\30")
        buf.write("\3\2\2\2\u013e\u013f\7q\2\2\u013f\u0140\7t\2\2\u0140\32")
        buf.write("\3\2\2\2\u0141\u0142\7k\2\2\u0142\u0143\7p\2\2\u0143\34")
        buf.write("\3\2\2\2\u0144\u0145\7g\2\2\u0145\u0146\7n\2\2\u0146\u0147")
        buf.write("\7u\2\2\u0147\u0148\7g\2\2\u0148\36\3\2\2\2\u0149\u014a")
        buf.write("\7g\2\2\u014a\u014b\7n\2\2\u014b\u014c\7k\2\2\u014c\u014d")
        buf.write("\7h\2\2\u014d \3\2\2\2\u014e\u014f\7y\2\2\u014f\u0150")
        buf.write("\7j\2\2\u0150\u0151\7k\2\2\u0151\u0152\7n\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153\"\3\2\2\2\u0154\u0155\7h\2\2\u0155\u0156")
        buf.write("\7q\2\2\u0156\u0157\7t\2\2\u0157$\3\2\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159\u015a\7p\2\2\u015a\u015b\7f\2\2\u015b&\3")
        buf.write("\2\2\2\u015c\u015d\7v\2\2\u015d\u015e\7t\2\2\u015e\u015f")
        buf.write("\7w\2\2\u015f\u0160\7g\2\2\u0160(\3\2\2\2\u0161\u0162")
        buf.write("\7h\2\2\u0162\u0163\7c\2\2\u0163\u0164\7n\2\2\u0164\u0165")
        buf.write("\7u\2\2\u0165\u0166\7g\2\2\u0166*\3\2\2\2\u0167\u0168")
        buf.write("\7h\2\2\u0168\u0169\7p\2\2\u0169,\3\2\2\2\u016a\u016b")
        buf.write("\7e\2\2\u016b\u016c\7n\2\2\u016c\u016d\7c\2\2\u016d\u016e")
        buf.write("\7u\2\2\u016e\u016f\7u\2\2\u016f.\3\2\2\2\u0170\u0171")
        buf.write("\7n\2\2\u0171\u0172\7g\2\2\u0172\u0173\7v\2\2\u0173\60")
        buf.write("\3\2\2\2\u0174\u0175\7v\2\2\u0175\u0176\7t\2\2\u0176\u0177")
        buf.write("\7c\2\2\u0177\u0178\7k\2\2\u0178\u0179\7v\2\2\u0179\62")
        buf.write("\3\2\2\2\u017a\u017b\7f\2\2\u017b\u017c\7g\2\2\u017c\u017d")
        buf.write("\7h\2\2\u017d\64\3\2\2\2\u017e\u017f\7k\2\2\u017f\u0180")
        buf.write("\7o\2\2\u0180\u0181\7r\2\2\u0181\u0182\7q\2\2\u0182\u0183")
        buf.write("\7t\2\2\u0183\u0184\7v\2\2\u0184\66\3\2\2\2\u0185\u0186")
        buf.write("\7h\2\2\u0186\u0187\7t\2\2\u0187\u0188\7q\2\2\u0188\u0189")
        buf.write("\7o\2\2\u01898\3\2\2\2\u018a\u018b\7c\2\2\u018b\u018c")
        buf.write("\7u\2\2\u018c:\3\2\2\2\u018d\u018e\7d\2\2\u018e\u018f")
        buf.write("\7t\2\2\u018f\u0190\7g\2\2\u0190\u0191\7c\2\2\u0191\u0192")
        buf.write("\7m\2\2\u0192<\3\2\2\2\u0193\u0194\7p\2\2\u0194\u0195")
        buf.write("\7g\2\2\u0195\u0196\7y\2\2\u0196>\3\2\2\2\u0197\u0198")
        buf.write("\7t\2\2\u0198\u0199\7g\2\2\u0199\u019a\7s\2\2\u019a\u019b")
        buf.write("\7w\2\2\u019b\u019c\7k\2\2\u019c\u019d\7t\2\2\u019d\u019e")
        buf.write("\7g\2\2\u019e@\3\2\2\2\u019f\u01a0\7<\2\2\u01a0\u01a1")
        buf.write("\7?\2\2\u01a1B\3\2\2\2\u01a2\u01a3\7?\2\2\u01a3D\3\2\2")
        buf.write("\2\u01a4\u01a5\7?\2\2\u01a5\u01a6\7?\2\2\u01a6F\3\2\2")
        buf.write("\2\u01a7\u01a8\7#\2\2\u01a8\u01a9\7?\2\2\u01a9H\3\2\2")
        buf.write("\2\u01aa\u01ab\7>\2\2\u01ab\u01ac\7?\2\2\u01acJ\3\2\2")
        buf.write("\2\u01ad\u01ae\7@\2\2\u01ae\u01af\7?\2\2\u01afL\3\2\2")
        buf.write("\2\u01b0\u01b1\7-\2\2\u01b1N\3\2\2\2\u01b2\u01b3\7/\2")
        buf.write("\2\u01b3P\3\2\2\2\u01b4\u01b5\7,\2\2\u01b5R\3\2\2\2\u01b6")
        buf.write("\u01b7\7\61\2\2\u01b7T\3\2\2\2\u01b8\u01b9\7>\2\2\u01b9")
        buf.write("V\3\2\2\2\u01ba\u01bb\7@\2\2\u01bbX\3\2\2\2\u01bc\u01bd")
        buf.write("\7>\2\2\u01bd\u01be\7?\2\2\u01beZ\3\2\2\2\u01bf\u01c0")
        buf.write("\7@\2\2\u01c0\u01c1\7?\2\2\u01c1\\\3\2\2\2\u01c2\u01c3")
        buf.write("\7#\2\2\u01c3^\3\2\2\2\u01c4\u01c5\7`\2\2\u01c5`\3\2\2")
        buf.write("\2\u01c6\u01c7\7\'\2\2\u01c7b\3\2\2\2\u01c8\u01c9\7~\2")
        buf.write("\2\u01c9d\3\2\2\2\u01ca\u01cb\7~\2\2\u01cb\u01cc\7~\2")
        buf.write("\2\u01ccf\3\2\2\2\u01cd\u01ce\7%\2\2\u01ceh\3\2\2\2\u01cf")
        buf.write("\u01d0\7(\2\2\u01d0j\3\2\2\2\u01d1\u01d2\7(\2\2\u01d2")
        buf.write("\u01d3\7(\2\2\u01d3l\3\2\2\2\u01d4\u01d5\7B\2\2\u01d5")
        buf.write("n\3\2\2\2\u01d6\u01d7\7B\2\2\u01d7\u01d8\7B\2\2\u01d8")
        buf.write("p\3\2\2\2\u01d9\u01da\7~\2\2\u01da\u01db\7@\2\2\u01db")
        buf.write("r\3\2\2\2\u01dc\u01dd\7k\2\2\u01dd\u01de\7p\2\2\u01de")
        buf.write("\u01e7\7v\2\2\u01df\u01e0\7k\2\2\u01e0\u01e1\7p\2\2\u01e1")
        buf.write("\u01e2\7v\2\2\u01e2\u01e3\7g\2\2\u01e3\u01e4\7i\2\2\u01e4")
        buf.write("\u01e5\7g\2\2\u01e5\u01e7\7t\2\2\u01e6\u01dc\3\2\2\2\u01e6")
        buf.write("\u01df\3\2\2\2\u01e7t\3\2\2\2\u01e8\u01e9\7h\2\2\u01e9")
        buf.write("\u01ea\7n\2\2\u01ea\u01f1\7v\2\2\u01eb\u01ec\7h\2\2\u01ec")
        buf.write("\u01ed\7n\2\2\u01ed\u01ee\7q\2\2\u01ee\u01ef\7c\2\2\u01ef")
        buf.write("\u01f1\7v\2\2\u01f0\u01e8\3\2\2\2\u01f0\u01eb\3\2\2\2")
        buf.write("\u01f1v\3\2\2\2\u01f2\u01f3\7u\2\2\u01f3\u01f4\7v\2\2")
        buf.write("\u01f4\u01fc\7t\2\2\u01f5\u01f6\7u\2\2\u01f6\u01f7\7v")
        buf.write("\2\2\u01f7\u01f8\7t\2\2\u01f8\u01f9\7k\2\2\u01f9\u01fa")
        buf.write("\7p\2\2\u01fa\u01fc\7i\2\2\u01fb\u01f2\3\2\2\2\u01fb\u01f5")
        buf.write("\3\2\2\2\u01fcx\3\2\2\2\u01fd\u01fe\7d\2\2\u01fe\u01ff")
        buf.write("\7q\2\2\u01ff\u0200\7q\2\2\u0200\u0209\7n\2\2\u0201\u0202")
        buf.write("\7d\2\2\u0202\u0203\7q\2\2\u0203\u0204\7q\2\2\u0204\u0205")
        buf.write("\7n\2\2\u0205\u0206\7g\2\2\u0206\u0207\7c\2\2\u0207\u0209")
        buf.write("\7p\2\2\u0208\u01fd\3\2\2\2\u0208\u0201\3\2\2\2\u0209")
        buf.write("z\3\2\2\2\u020a\u020b\7.\2\2\u020b|\3\2\2\2\u020c\u020d")
        buf.write("\7*\2\2\u020d\u020e\b?\2\2\u020e~\3\2\2\2\u020f\u0210")
        buf.write("\7+\2\2\u0210\u0211\b@\3\2\u0211\u0080\3\2\2\2\u0212\u0213")
        buf.write("\7}\2\2\u0213\u0214\bA\4\2\u0214\u0082\3\2\2\2\u0215\u0216")
        buf.write("\7\177\2\2\u0216\u0217\bB\5\2\u0217\u0084\3\2\2\2\u0218")
        buf.write("\u0219\7]\2\2\u0219\u021a\bC\6\2\u021a\u0086\3\2\2\2\u021b")
        buf.write("\u021c\7_\2\2\u021c\u021d\bD\7\2\u021d\u0088\3\2\2\2\u021e")
        buf.write("\u021f\7/\2\2\u021f\u0220\7@\2\2\u0220\u008a\3\2\2\2\u0221")
        buf.write("\u0222\7>\2\2\u0222\u0223\7/\2\2\u0223\u008c\3\2\2\2\u0224")
        buf.write("\u0225\7<\2\2\u0225\u008e\3\2\2\2\u0226\u0227\7\60\2\2")
        buf.write("\u0227\u0090\3\2\2\2\u0228\u0229\7\60\2\2\u0229\u022a")
        buf.write("\7\60\2\2\u022a\u022b\7\60\2\2\u022b\u0092\3\2\2\2\u022c")
        buf.write("\u022d\7-\2\2\u022d\u022e\7-\2\2\u022e\u0094\3\2\2\2\u022f")
        buf.write("\u0230\7/\2\2\u0230\u0231\7/\2\2\u0231\u0096\3\2\2\2\u0232")
        buf.write("\u023b\7\62\2\2\u0233\u0237\t\2\2\2\u0234\u0236\t\3\2")
        buf.write("\2\u0235\u0234\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u023b\3\2\2\2\u0239")
        buf.write("\u0237\3\2\2\2\u023a\u0232\3\2\2\2\u023a\u0233\3\2\2\2")
        buf.write("\u023b\u0098\3\2\2\2\u023c\u024b\7\62\2\2\u023d\u0241")
        buf.write("\t\2\2\2\u023e\u0240\t\3\2\2\u023f\u023e\3\2\2\2\u0240")
        buf.write("\u0243\3\2\2\2\u0241\u023f\3\2\2\2\u0241\u0242\3\2\2\2")
        buf.write("\u0242\u0244\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0246\7")
        buf.write("\60\2\2\u0245\u0247\t\3\2\2\u0246\u0245\3\2\2\2\u0247")
        buf.write("\u0248\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2")
        buf.write("\u0249\u024b\3\2\2\2\u024a\u023c\3\2\2\2\u024a\u023d\3")
        buf.write("\2\2\2\u024b\u009a\3\2\2\2\u024c\u024d\7=\2\2\u024d\u009c")
        buf.write("\3\2\2\2\u024e\u0250\t\4\2\2\u024f\u024e\3\2\2\2\u0250")
        buf.write("\u0253\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2")
        buf.write("\u0252\u0254\3\2\2\2\u0253\u0251\3\2\2\2\u0254\u0258\t")
        buf.write("\5\2\2\u0255\u0257\t\6\2\2\u0256\u0255\3\2\2\2\u0257\u025a")
        buf.write("\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259")
        buf.write("\u009e\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025c\t\7\2\2")
        buf.write("\u025c\u00a0\3\2\2\2\u025d\u025e\t\b\2\2\u025e\u00a2\3")
        buf.write("\2\2\2\u025f\u0260\t\t\2\2\u0260\u00a4\3\2\2\2\u0261\u0262")
        buf.write("\t\n\2\2\u0262\u0263\3\2\2\2\u0263\u0264\bS\b\2\u0264")
        buf.write("\u00a6\3\2\2\2\u0265\u0267\t\13\2\2\u0266\u0265\3\2\2")
        buf.write("\2\u0267\u0268\3\2\2\2\u0268\u0266\3\2\2\2\u0268\u0269")
        buf.write("\3\2\2\2\u0269\u00a8\3\2\2\2\u026a\u026e\5\u00f5{\2\u026b")
        buf.write("\u026d\5\u00f7|\2\u026c\u026b\3\2\2\2\u026d\u0270\3\2")
        buf.write("\2\2\u026e\u026c\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u00aa")
        buf.write("\3\2\2\2\u0270\u026e\3\2\2\2\u0271\u0272\7\61\2\2\u0272")
        buf.write("\u0273\7\61\2\2\u0273\u0277\3\2\2\2\u0274\u0276\n\f\2")
        buf.write("\2\u0275\u0274\3\2\2\2\u0276\u0279\3\2\2\2\u0277\u0275")
        buf.write("\3\2\2\2\u0277\u0278\3\2\2\2\u0278\u027b\3\2\2\2\u0279")
        buf.write("\u0277\3\2\2\2\u027a\u027c\7\17\2\2\u027b\u027a\3\2\2")
        buf.write("\2\u027b\u027c\3\2\2\2\u027c\u027d\3\2\2\2\u027d\u028a")
        buf.write("\7\f\2\2\u027e\u027f\7\61\2\2\u027f\u0280\7,\2\2\u0280")
        buf.write("\u0284\3\2\2\2\u0281\u0283\13\2\2\2\u0282\u0281\3\2\2")
        buf.write("\2\u0283\u0286\3\2\2\2\u0284\u0285\3\2\2\2\u0284\u0282")
        buf.write("\3\2\2\2\u0285\u0287\3\2\2\2\u0286\u0284\3\2\2\2\u0287")
        buf.write("\u0288\7,\2\2\u0288\u028a\7\61\2\2\u0289\u0271\3\2\2\2")
        buf.write("\u0289\u027e\3\2\2\2\u028a\u00ac\3\2\2\2\u028b\u028e\5")
        buf.write("\u00b3Z\2\u028c\u028e\5\u00b5[\2\u028d\u028b\3\2\2\2\u028d")
        buf.write("\u028c\3\2\2\2\u028e\u00ae\3\2\2\2\u028f\u0293\5\u00b1")
        buf.write("Y\2\u0290\u0293\5\u00bf`\2\u0291\u0293\5\u00c1a\2\u0292")
        buf.write("\u028f\3\2\2\2\u0292\u0290\3\2\2\2\u0292\u0291\3\2\2\2")
        buf.write("\u0293\u00b0\3\2\2\2\u0294\u0299\5\u00b7\\\2\u0295\u0299")
        buf.write("\5\u00b9]\2\u0296\u0299\5\u00bb^\2\u0297\u0299\5\u00bd")
        buf.write("_\2\u0298\u0294\3\2\2\2\u0298\u0295\3\2\2\2\u0298\u0296")
        buf.write("\3\2\2\2\u0298\u0297\3\2\2\2\u0299\u00b2\3\2\2\2\u029a")
        buf.write("\u02a0\t\r\2\2\u029b\u029c\t\16\2\2\u029c\u02a0\t\17\2")
        buf.write("\2\u029d\u029e\t\17\2\2\u029e\u02a0\t\16\2\2\u029f\u029a")
        buf.write("\3\2\2\2\u029f\u029b\3\2\2\2\u029f\u029d\3\2\2\2\u029f")
        buf.write("\u02a0\3\2\2\2\u02a0\u02a3\3\2\2\2\u02a1\u02a4\5\u00c7")
        buf.write("d\2\u02a2\u02a4\5\u00c9e\2\u02a3\u02a1\3\2\2\2\u02a3\u02a2")
        buf.write("\3\2\2\2\u02a4\u00b4\3\2\2\2\u02a5\u02ab\t\20\2\2\u02a6")
        buf.write("\u02a7\t\20\2\2\u02a7\u02ab\t\17\2\2\u02a8\u02a9\t\17")
        buf.write("\2\2\u02a9\u02ab\t\20\2\2\u02aa\u02a5\3\2\2\2\u02aa\u02a6")
        buf.write("\3\2\2\2\u02aa\u02a8\3\2\2\2\u02ab\u02ae\3\2\2\2\u02ac")
        buf.write("\u02af\5\u00e5s\2\u02ad\u02af\5\u00e7t\2\u02ae\u02ac\3")
        buf.write("\2\2\2\u02ae\u02ad\3\2\2\2\u02af\u00b6\3\2\2\2\u02b0\u02b4")
        buf.write("\5\u00d1i\2\u02b1\u02b3\5\u00d3j\2\u02b2\u02b1\3\2\2\2")
        buf.write("\u02b3\u02b6\3\2\2\2\u02b4\u02b2\3\2\2\2\u02b4\u02b5\3")
        buf.write("\2\2\2\u02b5\u02bd\3\2\2\2\u02b6\u02b4\3\2\2\2\u02b7\u02b9")
        buf.write("\7\62\2\2\u02b8\u02b7\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba")
        buf.write("\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02bd\3\2\2\2")
        buf.write("\u02bc\u02b0\3\2\2\2\u02bc\u02b8\3\2\2\2\u02bd\u00b8\3")
        buf.write("\2\2\2\u02be\u02bf\7\62\2\2\u02bf\u02c1\t\21\2\2\u02c0")
        buf.write("\u02c2\5\u00d5k\2\u02c1\u02c0\3\2\2\2\u02c2\u02c3\3\2")
        buf.write("\2\2\u02c3\u02c1\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4\u00ba")
        buf.write("\3\2\2\2\u02c5\u02c6\7\62\2\2\u02c6\u02c8\t\22\2\2\u02c7")
        buf.write("\u02c9\5\u00d7l\2\u02c8\u02c7\3\2\2\2\u02c9\u02ca\3\2")
        buf.write("\2\2\u02ca\u02c8\3\2\2\2\u02ca\u02cb\3\2\2\2\u02cb\u00bc")
        buf.write("\3\2\2\2\u02cc\u02cd\7\62\2\2\u02cd\u02cf\t\20\2\2\u02ce")
        buf.write("\u02d0\5\u00d9m\2\u02cf\u02ce\3\2\2\2\u02d0\u02d1\3\2")
        buf.write("\2\2\u02d1\u02cf\3\2\2\2\u02d1\u02d2\3\2\2\2\u02d2\u00be")
        buf.write("\3\2\2\2\u02d3\u02d6\5\u00dbn\2\u02d4\u02d6\5\u00ddo\2")
        buf.write("\u02d5\u02d3\3\2\2\2\u02d5\u02d4\3\2\2\2\u02d6\u00c0\3")
        buf.write("\2\2\2\u02d7\u02da\5\u00bf`\2\u02d8\u02da\5\u00dfp\2\u02d9")
        buf.write("\u02d7\3\2\2\2\u02d9\u02d8\3\2\2\2\u02da\u02db\3\2\2\2")
        buf.write("\u02db\u02dc\t\23\2\2\u02dc\u00c2\3\2\2\2\u02dd\u02e1")
        buf.write("\5\u00a7T\2\u02de\u02e1\5\u00abV\2\u02df\u02e1\5\u00f3")
        buf.write("z\2\u02e0\u02dd\3\2\2\2\u02e0\u02de\3\2\2\2\u02e0\u02df")
        buf.write("\3\2\2\2\u02e1\u02e2\3\2\2\2\u02e2\u02e3\bb\t\2\u02e3")
        buf.write("\u00c4\3\2\2\2\u02e4\u02e5\13\2\2\2\u02e5\u00c6\3\2\2")
        buf.write("\2\u02e6\u02eb\7)\2\2\u02e7\u02ea\5\u00cfh\2\u02e8\u02ea")
        buf.write("\n\24\2\2\u02e9\u02e7\3\2\2\2\u02e9\u02e8\3\2\2\2\u02ea")
        buf.write("\u02ed\3\2\2\2\u02eb\u02e9\3\2\2\2\u02eb\u02ec\3\2\2\2")
        buf.write("\u02ec\u02ee\3\2\2\2\u02ed\u02eb\3\2\2\2\u02ee\u02f9\7")
        buf.write(")\2\2\u02ef\u02f4\7$\2\2\u02f0\u02f3\5\u00cfh\2\u02f1")
        buf.write("\u02f3\n\25\2\2\u02f2\u02f0\3\2\2\2\u02f2\u02f1\3\2\2")
        buf.write("\2\u02f3\u02f6\3\2\2\2\u02f4\u02f2\3\2\2\2\u02f4\u02f5")
        buf.write("\3\2\2\2\u02f5\u02f7\3\2\2\2\u02f6\u02f4\3\2\2\2\u02f7")
        buf.write("\u02f9\7$\2\2\u02f8\u02e6\3\2\2\2\u02f8\u02ef\3\2\2\2")
        buf.write("\u02f9\u00c8\3\2\2\2\u02fa\u02fb\7)\2\2\u02fb\u02fc\7")
        buf.write(")\2\2\u02fc\u02fd\7)\2\2\u02fd\u0301\3\2\2\2\u02fe\u0300")
        buf.write("\5\u00cbf\2\u02ff\u02fe\3\2\2\2\u0300\u0303\3\2\2\2\u0301")
        buf.write("\u0302\3\2\2\2\u0301\u02ff\3\2\2\2\u0302\u0304\3\2\2\2")
        buf.write("\u0303\u0301\3\2\2\2\u0304\u0305\7)\2\2\u0305\u0306\7")
        buf.write(")\2\2\u0306\u0315\7)\2\2\u0307\u0308\7$\2\2\u0308\u0309")
        buf.write("\7$\2\2\u0309\u030a\7$\2\2\u030a\u030e\3\2\2\2\u030b\u030d")
        buf.write("\5\u00cbf\2\u030c\u030b\3\2\2\2\u030d\u0310\3\2\2\2\u030e")
        buf.write("\u030f\3\2\2\2\u030e\u030c\3\2\2\2\u030f\u0311\3\2\2\2")
        buf.write("\u0310\u030e\3\2\2\2\u0311\u0312\7$\2\2\u0312\u0313\7")
        buf.write("$\2\2\u0313\u0315\7$\2\2\u0314\u02fa\3\2\2\2\u0314\u0307")
        buf.write("\3\2\2\2\u0315\u00ca\3\2\2\2\u0316\u0319\5\u00cdg\2\u0317")
        buf.write("\u0319\5\u00cfh\2\u0318\u0316\3\2\2\2\u0318\u0317\3\2")
        buf.write("\2\2\u0319\u00cc\3\2\2\2\u031a\u031b\n\26\2\2\u031b\u00ce")
        buf.write("\3\2\2\2\u031c\u031d\7^\2\2\u031d\u0321\13\2\2\2\u031e")
        buf.write("\u031f\7^\2\2\u031f\u0321\5\u00f9}\2\u0320\u031c\3\2\2")
        buf.write("\2\u0320\u031e\3\2\2\2\u0321\u00d0\3\2\2\2\u0322\u0323")
        buf.write("\t\2\2\2\u0323\u00d2\3\2\2\2\u0324\u0325\t\3\2\2\u0325")
        buf.write("\u00d4\3\2\2\2\u0326\u0327\t\27\2\2\u0327\u00d6\3\2\2")
        buf.write("\2\u0328\u0329\t\30\2\2\u0329\u00d8\3\2\2\2\u032a\u032b")
        buf.write("\t\31\2\2\u032b\u00da\3\2\2\2\u032c\u032e\5\u00dfp\2\u032d")
        buf.write("\u032c\3\2\2\2\u032d\u032e\3\2\2\2\u032e\u032f\3\2\2\2")
        buf.write("\u032f\u0334\5\u00e1q\2\u0330\u0331\5\u00dfp\2\u0331\u0332")
        buf.write("\7\60\2\2\u0332\u0334\3\2\2\2\u0333\u032d\3\2\2\2\u0333")
        buf.write("\u0330\3\2\2\2\u0334\u00dc\3\2\2\2\u0335\u0338\5\u00df")
        buf.write("p\2\u0336\u0338\5\u00dbn\2\u0337\u0335\3\2\2\2\u0337\u0336")
        buf.write("\3\2\2\2\u0338\u0339\3\2\2\2\u0339\u033a\5\u00e3r\2\u033a")
        buf.write("\u00de\3\2\2\2\u033b\u033d\5\u00d3j\2\u033c\u033b\3\2")
        buf.write("\2\2\u033d\u033e\3\2\2\2\u033e\u033c\3\2\2\2\u033e\u033f")
        buf.write("\3\2\2\2\u033f\u00e0\3\2\2\2\u0340\u0342\7\60\2\2\u0341")
        buf.write("\u0343\5\u00d3j\2\u0342\u0341\3\2\2\2\u0343\u0344\3\2")
        buf.write("\2\2\u0344\u0342\3\2\2\2\u0344\u0345\3\2\2\2\u0345\u00e2")
        buf.write("\3\2\2\2\u0346\u0348\t\32\2\2\u0347\u0349\t\33\2\2\u0348")
        buf.write("\u0347\3\2\2\2\u0348\u0349\3\2\2\2\u0349\u034b\3\2\2\2")
        buf.write("\u034a\u034c\5\u00d3j\2\u034b\u034a\3\2\2\2\u034c\u034d")
        buf.write("\3\2\2\2\u034d\u034b\3\2\2\2\u034d\u034e\3\2\2\2\u034e")
        buf.write("\u00e4\3\2\2\2\u034f\u0354\7)\2\2\u0350\u0353\5\u00eb")
        buf.write("v\2\u0351\u0353\5\u00f1y\2\u0352\u0350\3\2\2\2\u0352\u0351")
        buf.write("\3\2\2\2\u0353\u0356\3\2\2\2\u0354\u0352\3\2\2\2\u0354")
        buf.write("\u0355\3\2\2\2\u0355\u0357\3\2\2\2\u0356\u0354\3\2\2\2")
        buf.write("\u0357\u0362\7)\2\2\u0358\u035d\7$\2\2\u0359\u035c\5\u00ed")
        buf.write("w\2\u035a\u035c\5\u00f1y\2\u035b\u0359\3\2\2\2\u035b\u035a")
        buf.write("\3\2\2\2\u035c\u035f\3\2\2\2\u035d\u035b\3\2\2\2\u035d")
        buf.write("\u035e\3\2\2\2\u035e\u0360\3\2\2\2\u035f\u035d\3\2\2\2")
        buf.write("\u0360\u0362\7$\2\2\u0361\u034f\3\2\2\2\u0361\u0358\3")
        buf.write("\2\2\2\u0362\u00e6\3\2\2\2\u0363\u0364\7)\2\2\u0364\u0365")
        buf.write("\7)\2\2\u0365\u0366\7)\2\2\u0366\u036a\3\2\2\2\u0367\u0369")
        buf.write("\5\u00e9u\2\u0368\u0367\3\2\2\2\u0369\u036c\3\2\2\2\u036a")
        buf.write("\u036b\3\2\2\2\u036a\u0368\3\2\2\2\u036b\u036d\3\2\2\2")
        buf.write("\u036c\u036a\3\2\2\2\u036d\u036e\7)\2\2\u036e\u036f\7")
        buf.write(")\2\2\u036f\u037e\7)\2\2\u0370\u0371\7$\2\2\u0371\u0372")
        buf.write("\7$\2\2\u0372\u0373\7$\2\2\u0373\u0377\3\2\2\2\u0374\u0376")
        buf.write("\5\u00e9u\2\u0375\u0374\3\2\2\2\u0376\u0379\3\2\2\2\u0377")
        buf.write("\u0378\3\2\2\2\u0377\u0375\3\2\2\2\u0378\u037a\3\2\2\2")
        buf.write("\u0379\u0377\3\2\2\2\u037a\u037b\7$\2\2\u037b\u037c\7")
        buf.write("$\2\2\u037c\u037e\7$\2\2\u037d\u0363\3\2\2\2\u037d\u0370")
        buf.write("\3\2\2\2\u037e\u00e8\3\2\2\2\u037f\u0382\5\u00efx\2\u0380")
        buf.write("\u0382\5\u00f1y\2\u0381\u037f\3\2\2\2\u0381\u0380\3\2")
        buf.write("\2\2\u0382\u00ea\3\2\2\2\u0383\u0385\t\34\2\2\u0384\u0383")
        buf.write("\3\2\2\2\u0385\u00ec\3\2\2\2\u0386\u0388\t\35\2\2\u0387")
        buf.write("\u0386\3\2\2\2\u0388\u00ee\3\2\2\2\u0389\u038b\t\36\2")
        buf.write("\2\u038a\u0389\3\2\2\2\u038b\u00f0\3\2\2\2\u038c\u038d")
        buf.write("\7^\2\2\u038d\u038e\t\37\2\2\u038e\u00f2\3\2\2\2\u038f")
        buf.write("\u0391\7^\2\2\u0390\u0392\5\u00a7T\2\u0391\u0390\3\2\2")
        buf.write("\2\u0391\u0392\3\2\2\2\u0392\u0398\3\2\2\2\u0393\u0395")
        buf.write("\7\17\2\2\u0394\u0393\3\2\2\2\u0394\u0395\3\2\2\2\u0395")
        buf.write("\u0396\3\2\2\2\u0396\u0399\7\f\2\2\u0397\u0399\4\16\17")
        buf.write("\2\u0398\u0394\3\2\2\2\u0398\u0397\3\2\2\2\u0399\u00f4")
        buf.write("\3\2\2\2\u039a\u039c\t \2\2\u039b\u039a\3\2\2\2\u039c")
        buf.write("\u00f6\3\2\2\2\u039d\u03a0\5\u00f5{\2\u039e\u03a0\t!\2")
        buf.write("\2\u039f\u039d\3\2\2\2\u039f\u039e\3\2\2\2\u03a0\u00f8")
        buf.write("\3\2\2\2\u03a1\u03a2\6}\2\2\u03a2\u03ae\5\u00a7T\2\u03a3")
        buf.write("\u03a5\7\17\2\2\u03a4\u03a3\3\2\2\2\u03a4\u03a5\3\2\2")
        buf.write("\2\u03a5\u03a6\3\2\2\2\u03a6\u03a9\7\f\2\2\u03a7\u03a9")
        buf.write("\4\16\17\2\u03a8\u03a4\3\2\2\2\u03a8\u03a7\3\2\2\2\u03a9")
        buf.write("\u03ab\3\2\2\2\u03aa\u03ac\5\u00a7T\2\u03ab\u03aa\3\2")
        buf.write("\2\2\u03ab\u03ac\3\2\2\2\u03ac\u03ae\3\2\2\2\u03ad\u03a1")
        buf.write("\3\2\2\2\u03ad\u03a8\3\2\2\2\u03ae\u03af\3\2\2\2\u03af")
        buf.write("\u03b0\b}\n\2\u03b0\u00fa\3\2\2\2P\2\u00fe\u0104\u0106")
        buf.write("\u010c\u0112\u0114\u01e6\u01f0\u01fb\u0208\u0237\u023a")
        buf.write("\u0241\u0248\u024a\u0251\u0258\u0268\u026e\u0277\u027b")
        buf.write("\u0284\u0289\u028d\u0292\u0298\u029f\u02a3\u02aa\u02ae")
        buf.write("\u02b4\u02ba\u02bc\u02c3\u02ca\u02d1\u02d5\u02d9\u02e0")
        buf.write("\u02e9\u02eb\u02f2\u02f4\u02f8\u0301\u030e\u0314\u0318")
        buf.write("\u0320\u032d\u0333\u0337\u033e\u0344\u0348\u034d\u0352")
        buf.write("\u0354\u035b\u035d\u0361\u036a\u0377\u037d\u0381\u0384")
        buf.write("\u0387\u038a\u0391\u0394\u0398\u039b\u039f\u03a4\u03a8")
        buf.write("\u03ab\u03ad\13\3?\2\3@\3\3A\4\3B\5\3C\6\3D\7\2\3\2\b")
        buf.write("\2\2\3}\b")
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
    CONST = 7
    LOCAL = 8
    ECHO = 9
    RETURN = 10
    IF = 11
    THEN = 12
    AND = 13
    OR = 14
    IN = 15
    ELSE = 16
    ELSEIF = 17
    WHILE = 18
    FOR = 19
    END = 20
    TRUE = 21
    FALSE = 22
    FUNCTION = 23
    CLASS = 24
    LET = 25
    TRAIT = 26
    DEFINE = 27
    IMPORT = 28
    FROM = 29
    AS = 30
    BREAK = 31
    NEW = 32
    REQUIRE = 33
    WALRUS = 34
    EQUALS = 35
    EQEQ = 36
    NOTEQUAL = 37
    LTEQUALS = 38
    GTEQUALS = 39
    PLUS = 40
    MINUS = 41
    MULTIPLY = 42
    DIVIDE = 43
    LESSTHAN = 44
    GREATERTHAN = 45
    LESSTHANEQUAL = 46
    MORETHANEQUAL = 47
    BANG = 48
    POWER = 49
    MODULUS = 50
    VERTICAL = 51
    ORSYMBOL = 52
    HASH = 53
    AMBERSAND = 54
    ANDSYMBOL = 55
    ATSYMBOL = 56
    ATTSYMBOL = 57
    PIPE = 58
    TYPE_INT = 59
    TYPE_DECIMAL = 60
    TYPE_STRING = 61
    TYPE_BOOLEAN = 62
    COMMA = 63
    LBRACKET = 64
    RBRACKET = 65
    LBRACE = 66
    RBRACE = 67
    LSQRBRACKET = 68
    RSQRBRACKET = 69
    ARROW = 70
    BACKARROW = 71
    COLON = 72
    DOT = 73
    ELLIPSIS = 74
    PLUSPLUS = 75
    MINUSMINUS = 76
    INT_LITERAL = 77
    FLOAT_LITERAL = 78
    IDENTIFIER = 79
    COMMENT = 80
    STRING = 81
    NUMBER = 82
    INTEGER = 83
    STRING_LITERAL = 84
    BYTES_LITERAL = 85
    DECIMAL_INTEGER = 86
    OCT_INTEGER = 87
    HEX_INTEGER = 88
    BIN_INTEGER = 89
    FLOAT_NUMBER = 90
    IMAG_NUMBER = 91
    SKIP_ = 92
    UNKNOWN_CHAR = 93
    NEWLINE = 94

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"CONSUME" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"'", "'var'", "'const'", "'loc'", "'echo'", "'return'", "'if'", 
            "'then'", "'and'", "'or'", "'in'", "'else'", "'elif'", "'while'", 
            "'for'", "'end'", "'true'", "'false'", "'fn'", "'class'", "'let'", 
            "'trait'", "'def'", "'import'", "'from'", "'as'", "'break'", 
            "'new'", "'require'", "':='", "'='", "'=='", "'!='", "'+'", 
            "'-'", "'*'", "'/'", "'<'", "'>'", "'!'", "'^'", "'%'", "'|'", 
            "'||'", "'#'", "'&'", "'&&'", "'@'", "'@@'", "'|>'", "','", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "'->'", "'<-'", "':'", 
            "'.'", "'...'", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", 
            "VAR", "CONST", "LOCAL", "ECHO", "RETURN", "IF", "THEN", "AND", 
            "OR", "IN", "ELSE", "ELSEIF", "WHILE", "FOR", "END", "TRUE", 
            "FALSE", "FUNCTION", "CLASS", "LET", "TRAIT", "DEFINE", "IMPORT", 
            "FROM", "AS", "BREAK", "NEW", "REQUIRE", "WALRUS", "EQUALS", 
            "EQEQ", "NOTEQUAL", "LTEQUALS", "GTEQUALS", "PLUS", "MINUS", 
            "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", "LESSTHANEQUAL", 
            "MORETHANEQUAL", "BANG", "POWER", "MODULUS", "VERTICAL", "ORSYMBOL", 
            "HASH", "AMBERSAND", "ANDSYMBOL", "ATSYMBOL", "ATTSYMBOL", "PIPE", 
            "TYPE_INT", "TYPE_DECIMAL", "TYPE_STRING", "TYPE_BOOLEAN", "COMMA", 
            "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET", 
            "ARROW", "BACKARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", 
            "MINUSMINUS", "INT_LITERAL", "FLOAT_LITERAL", "IDENTIFIER", 
            "COMMENT", "STRING", "NUMBER", "INTEGER", "STRING_LITERAL", 
            "BYTES_LITERAL", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
            "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER", "SKIP_", "UNKNOWN_CHAR", 
            "NEWLINE" ]

    ruleNames = [ "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", "VAR", 
                  "CONST", "LOCAL", "ECHO", "RETURN", "IF", "THEN", "AND", 
                  "OR", "IN", "ELSE", "ELSEIF", "WHILE", "FOR", "END", "TRUE", 
                  "FALSE", "FUNCTION", "CLASS", "LET", "TRAIT", "DEFINE", 
                  "IMPORT", "FROM", "AS", "BREAK", "NEW", "REQUIRE", "WALRUS", 
                  "EQUALS", "EQEQ", "NOTEQUAL", "LTEQUALS", "GTEQUALS", 
                  "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", 
                  "LESSTHANEQUAL", "MORETHANEQUAL", "BANG", "POWER", "MODULUS", 
                  "VERTICAL", "ORSYMBOL", "HASH", "AMBERSAND", "ANDSYMBOL", 
                  "ATSYMBOL", "ATTSYMBOL", "PIPE", "TYPE_INT", "TYPE_DECIMAL", 
                  "TYPE_STRING", "TYPE_BOOLEAN", "COMMA", "LBRACKET", "RBRACKET", 
                  "LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET", "ARROW", 
                  "BACKARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS", 
                  "INT_LITERAL", "FLOAT_LITERAL", "SEMICOLON", "ID", "DIGIT_CONT", 
                  "HEXDIGIT", "BINARY", "UNICODE_WS", "SPACES", "IDENTIFIER", 
                  "COMMENT", "STRING", "NUMBER", "INTEGER", "STRING_LITERAL", 
                  "BYTES_LITERAL", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
                  "BIN_INTEGER", "FLOAT_NUMBER", "IMAG_NUMBER", "SKIP_", 
                  "UNKNOWN_CHAR", "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM", 
                  "LONG_STRING_CHAR", "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", 
                  "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", 
                  "EXPONENT_FLOAT", "INT_PART", "FRACTION", "EXPONENT", 
                  "SHORT_BYTES", "LONG_BYTES", "LONG_BYTES_ITEM", "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", 
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
            actions[61] = self.LBRACKET_action 
            actions[62] = self.RBRACKET_action 
            actions[63] = self.LBRACE_action 
            actions[64] = self.RBRACE_action 
            actions[65] = self.LSQRBRACKET_action 
            actions[66] = self.RSQRBRACKET_action 
            actions[123] = self.NEWLINE_action 
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
            preds[123] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


