// Code generated from JingleLexer.g4 by ANTLR 4.7.2. DO NOT EDIT.

package parser

import (
	"fmt"
	"unicode"

	"github.com/antlr/antlr4/runtime/Go/antlr"
)

// Suppress unused import error
var _ = fmt.Printf
var _ = unicode.IsLetter

var serializedLexerAtn = []uint16{
	3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 2, 93, 740,
	8, 1, 8, 1, 8, 1, 4, 2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 4, 5, 9, 5, 4, 6,
	9, 6, 4, 7, 9, 7, 4, 8, 9, 8, 4, 9, 9, 9, 4, 10, 9, 10, 4, 11, 9, 11, 4,
	12, 9, 12, 4, 13, 9, 13, 4, 14, 9, 14, 4, 15, 9, 15, 4, 16, 9, 16, 4, 17,
	9, 17, 4, 18, 9, 18, 4, 19, 9, 19, 4, 20, 9, 20, 4, 21, 9, 21, 4, 22, 9,
	22, 4, 23, 9, 23, 4, 24, 9, 24, 4, 25, 9, 25, 4, 26, 9, 26, 4, 27, 9, 27,
	4, 28, 9, 28, 4, 29, 9, 29, 4, 30, 9, 30, 4, 31, 9, 31, 4, 32, 9, 32, 4,
	33, 9, 33, 4, 34, 9, 34, 4, 35, 9, 35, 4, 36, 9, 36, 4, 37, 9, 37, 4, 38,
	9, 38, 4, 39, 9, 39, 4, 40, 9, 40, 4, 41, 9, 41, 4, 42, 9, 42, 4, 43, 9,
	43, 4, 44, 9, 44, 4, 45, 9, 45, 4, 46, 9, 46, 4, 47, 9, 47, 4, 48, 9, 48,
	4, 49, 9, 49, 4, 50, 9, 50, 4, 51, 9, 51, 4, 52, 9, 52, 4, 53, 9, 53, 4,
	54, 9, 54, 4, 55, 9, 55, 4, 56, 9, 56, 4, 57, 9, 57, 4, 58, 9, 58, 4, 59,
	9, 59, 4, 60, 9, 60, 4, 61, 9, 61, 4, 62, 9, 62, 4, 63, 9, 63, 4, 64, 9,
	64, 4, 65, 9, 65, 4, 66, 9, 66, 4, 67, 9, 67, 4, 68, 9, 68, 4, 69, 9, 69,
	4, 70, 9, 70, 4, 71, 9, 71, 4, 72, 9, 72, 4, 73, 9, 73, 4, 74, 9, 74, 4,
	75, 9, 75, 4, 76, 9, 76, 4, 77, 9, 77, 4, 78, 9, 78, 4, 79, 9, 79, 4, 80,
	9, 80, 4, 81, 9, 81, 4, 82, 9, 82, 4, 83, 9, 83, 4, 84, 9, 84, 4, 85, 9,
	85, 4, 86, 9, 86, 4, 87, 9, 87, 4, 88, 9, 88, 4, 89, 9, 89, 4, 90, 9, 90,
	4, 91, 9, 91, 4, 92, 9, 92, 4, 93, 9, 93, 4, 94, 9, 94, 4, 95, 9, 95, 4,
	96, 9, 96, 4, 97, 9, 97, 4, 98, 9, 98, 4, 99, 9, 99, 4, 100, 9, 100, 4,
	101, 9, 101, 3, 2, 7, 2, 207, 10, 2, 12, 2, 14, 2, 210, 11, 2, 3, 2, 6,
	2, 213, 10, 2, 13, 2, 14, 2, 214, 5, 2, 217, 10, 2, 3, 3, 3, 3, 7, 3, 221,
	10, 3, 12, 3, 14, 3, 224, 11, 3, 3, 3, 6, 3, 227, 10, 3, 13, 3, 14, 3,
	228, 5, 3, 231, 10, 3, 3, 4, 3, 4, 3, 5, 3, 5, 3, 5, 3, 5, 3, 6, 3, 6,
	3, 6, 3, 6, 3, 6, 3, 6, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7,
	3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 3, 7, 5, 7, 263,
	10, 7, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 5, 8, 274,
	10, 8, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 10, 3, 10, 3,
	10, 3, 10, 3, 10, 3, 10, 3, 10, 3, 11, 3, 11, 3, 11, 3, 12, 3, 12, 3, 12,
	3, 12, 3, 12, 3, 13, 3, 13, 3, 13, 3, 13, 3, 14, 3, 14, 3, 14, 3, 15, 3,
	15, 3, 15, 3, 16, 3, 16, 3, 16, 3, 16, 3, 16, 3, 17, 3, 17, 3, 17, 3, 17,
	3, 17, 3, 17, 3, 17, 3, 17, 3, 17, 3, 17, 3, 17, 5, 17, 325, 10, 17, 3,
	18, 3, 18, 3, 18, 3, 18, 3, 18, 3, 18, 3, 19, 3, 19, 3, 19, 3, 19, 3, 20,
	3, 20, 3, 20, 3, 20, 3, 20, 3, 21, 3, 21, 3, 21, 3, 21, 3, 21, 3, 21, 3,
	22, 3, 22, 3, 22, 3, 22, 3, 22, 3, 22, 3, 22, 3, 22, 3, 22, 3, 22, 3, 22,
	3, 22, 3, 22, 3, 22, 3, 22, 3, 22, 5, 22, 364, 10, 22, 3, 23, 3, 23, 3,
	23, 3, 23, 3, 23, 3, 23, 3, 24, 3, 24, 3, 24, 3, 24, 3, 25, 3, 25, 3, 25,
	3, 25, 3, 25, 3, 25, 3, 26, 3, 26, 3, 26, 3, 26, 3, 27, 3, 27, 3, 27, 3,
	27, 3, 27, 3, 27, 3, 27, 3, 27, 3, 27, 3, 28, 3, 28, 3, 28, 3, 28, 3, 28,
	3, 29, 3, 29, 3, 29, 3, 29, 3, 29, 3, 29, 3, 29, 3, 30, 3, 30, 3, 30, 3,
	30, 3, 30, 3, 31, 3, 31, 3, 31, 3, 31, 3, 31, 3, 31, 3, 31, 3, 31, 3, 32,
	3, 32, 3, 32, 3, 33, 3, 33, 3, 33, 3, 33, 3, 33, 3, 33, 3, 34, 3, 34, 3,
	34, 3, 34, 3, 34, 3, 34, 3, 34, 3, 34, 3, 34, 3, 35, 3, 35, 3, 35, 3, 35,
	3, 35, 3, 35, 3, 35, 3, 36, 3, 36, 3, 36, 3, 36, 3, 36, 3, 36, 3, 37, 3,
	37, 3, 37, 3, 38, 3, 38, 3, 39, 3, 39, 3, 39, 3, 40, 3, 40, 3, 40, 3, 41,
	3, 41, 3, 41, 3, 42, 3, 42, 3, 42, 3, 43, 3, 43, 3, 44, 3, 44, 3, 45, 3,
	45, 3, 46, 3, 46, 3, 47, 3, 47, 3, 48, 3, 48, 3, 49, 3, 49, 3, 50, 3, 50,
	3, 51, 3, 51, 3, 52, 3, 52, 3, 53, 3, 53, 3, 53, 3, 54, 3, 54, 3, 55, 3,
	55, 3, 56, 3, 56, 3, 56, 3, 57, 3, 57, 3, 57, 3, 57, 3, 57, 3, 57, 3, 57,
	3, 57, 3, 57, 3, 57, 5, 57, 508, 10, 57, 3, 58, 3, 58, 3, 58, 3, 58, 3,
	58, 3, 58, 3, 58, 3, 58, 5, 58, 518, 10, 58, 3, 59, 3, 59, 3, 59, 3, 59,
	3, 59, 3, 59, 3, 59, 3, 59, 3, 59, 5, 59, 529, 10, 59, 3, 60, 3, 60, 3,
	60, 3, 60, 3, 60, 3, 60, 3, 60, 3, 60, 3, 60, 3, 60, 3, 60, 5, 60, 542,
	10, 60, 3, 61, 3, 61, 3, 62, 3, 62, 3, 63, 3, 63, 3, 64, 3, 64, 3, 65,
	3, 65, 3, 66, 3, 66, 3, 67, 3, 67, 3, 68, 3, 68, 3, 68, 3, 69, 3, 69, 3,
	70, 3, 70, 3, 71, 3, 71, 3, 71, 3, 71, 3, 72, 3, 72, 3, 72, 3, 73, 3, 73,
	3, 73, 3, 74, 3, 74, 3, 74, 3, 74, 3, 74, 3, 74, 3, 75, 3, 75, 3, 75, 3,
	75, 3, 75, 3, 75, 3, 75, 3, 76, 3, 76, 3, 76, 3, 76, 3, 76, 3, 77, 3, 77,
	3, 77, 3, 77, 3, 77, 3, 78, 3, 78, 3, 78, 3, 78, 3, 78, 3, 79, 3, 79, 3,
	79, 7, 79, 606, 10, 79, 12, 79, 14, 79, 609, 11, 79, 5, 79, 611, 10, 79,
	3, 80, 3, 80, 3, 80, 7, 80, 616, 10, 80, 12, 80, 14, 80, 619, 11, 80, 3,
	80, 3, 80, 6, 80, 623, 10, 80, 13, 80, 14, 80, 624, 5, 80, 627, 10, 80,
	3, 81, 3, 81, 3, 82, 3, 82, 3, 82, 5, 82, 634, 10, 82, 3, 83, 7, 83, 637,
	10, 83, 12, 83, 14, 83, 640, 11, 83, 3, 83, 3, 83, 7, 83, 644, 10, 83,
	12, 83, 14, 83, 647, 11, 83, 3, 84, 3, 84, 3, 85, 3, 85, 3, 86, 3, 86,
	3, 87, 6, 87, 656, 10, 87, 13, 87, 14, 87, 657, 3, 87, 3, 87, 3, 88, 3,
	88, 3, 88, 3, 88, 3, 89, 3, 89, 3, 89, 3, 89, 7, 89, 670, 10, 89, 12, 89,
	14, 89, 673, 11, 89, 3, 89, 5, 89, 676, 10, 89, 3, 89, 3, 89, 3, 89, 3,
	89, 3, 89, 7, 89, 683, 10, 89, 12, 89, 14, 89, 686, 11, 89, 3, 89, 3, 89,
	5, 89, 690, 10, 89, 3, 89, 3, 89, 3, 90, 6, 90, 695, 10, 90, 13, 90, 14,
	90, 696, 3, 90, 3, 90, 3, 91, 3, 91, 3, 91, 3, 91, 3, 92, 3, 92, 3, 93,
	3, 93, 3, 93, 3, 94, 3, 94, 3, 94, 3, 95, 3, 95, 3, 95, 3, 96, 3, 96, 3,
	96, 3, 97, 3, 97, 3, 97, 3, 97, 3, 98, 3, 98, 3, 98, 3, 98, 3, 98, 3, 99,
	6, 99, 729, 10, 99, 13, 99, 14, 99, 730, 3, 100, 3, 100, 3, 100, 3, 100,
	3, 101, 3, 101, 3, 101, 3, 101, 3, 684, 2, 102, 5, 3, 7, 4, 9, 5, 11, 6,
	13, 7, 15, 8, 17, 9, 19, 10, 21, 11, 23, 12, 25, 13, 27, 14, 29, 15, 31,
	16, 33, 17, 35, 18, 37, 19, 39, 20, 41, 21, 43, 22, 45, 23, 47, 24, 49,
	25, 51, 26, 53, 27, 55, 28, 57, 29, 59, 30, 61, 31, 63, 32, 65, 33, 67,
	34, 69, 35, 71, 36, 73, 37, 75, 38, 77, 39, 79, 40, 81, 41, 83, 42, 85,
	43, 87, 44, 89, 45, 91, 46, 93, 47, 95, 48, 97, 49, 99, 50, 101, 51, 103,
	52, 105, 53, 107, 54, 109, 55, 111, 56, 113, 57, 115, 58, 117, 59, 119,
	60, 121, 61, 123, 62, 125, 63, 127, 64, 129, 65, 131, 66, 133, 67, 135,
	68, 137, 69, 139, 70, 141, 71, 143, 72, 145, 73, 147, 74, 149, 75, 151,
	76, 153, 77, 155, 78, 157, 79, 159, 80, 161, 81, 163, 2, 165, 2, 167, 2,
	169, 2, 171, 2, 173, 2, 175, 2, 177, 2, 179, 82, 181, 83, 183, 84, 185,
	85, 187, 86, 189, 87, 191, 88, 193, 89, 195, 90, 197, 91, 199, 92, 201,
	2, 203, 93, 5, 2, 3, 4, 14, 3, 2, 51, 59, 3, 2, 50, 59, 4, 2, 12, 12, 15,
	15, 3, 2, 97, 97, 3, 2, 99, 124, 6, 2, 50, 59, 67, 92, 97, 97, 99, 124,
	4, 2, 50, 59, 97, 97, 6, 2, 50, 59, 67, 72, 97, 97, 99, 104, 4, 2, 50,
	51, 97, 97, 5, 2, 11, 12, 15, 15, 34, 34, 12, 2, 11, 15, 34, 34, 135, 135,
	162, 162, 5762, 5762, 8194, 8204, 8234, 8235, 8241, 8241, 8289, 8289, 12290,
	12290, 6, 2, 11, 12, 15, 15, 36, 37, 94, 94, 2, 766, 2, 5, 3, 2, 2, 2,
	2, 7, 3, 2, 2, 2, 2, 9, 3, 2, 2, 2, 2, 11, 3, 2, 2, 2, 2, 13, 3, 2, 2,
	2, 2, 15, 3, 2, 2, 2, 2, 17, 3, 2, 2, 2, 2, 19, 3, 2, 2, 2, 2, 21, 3, 2,
	2, 2, 2, 23, 3, 2, 2, 2, 2, 25, 3, 2, 2, 2, 2, 27, 3, 2, 2, 2, 2, 29, 3,
	2, 2, 2, 2, 31, 3, 2, 2, 2, 2, 33, 3, 2, 2, 2, 2, 35, 3, 2, 2, 2, 2, 37,
	3, 2, 2, 2, 2, 39, 3, 2, 2, 2, 2, 41, 3, 2, 2, 2, 2, 43, 3, 2, 2, 2, 2,
	45, 3, 2, 2, 2, 2, 47, 3, 2, 2, 2, 2, 49, 3, 2, 2, 2, 2, 51, 3, 2, 2, 2,
	2, 53, 3, 2, 2, 2, 2, 55, 3, 2, 2, 2, 2, 57, 3, 2, 2, 2, 2, 59, 3, 2, 2,
	2, 2, 61, 3, 2, 2, 2, 2, 63, 3, 2, 2, 2, 2, 65, 3, 2, 2, 2, 2, 67, 3, 2,
	2, 2, 2, 69, 3, 2, 2, 2, 2, 71, 3, 2, 2, 2, 2, 73, 3, 2, 2, 2, 2, 75, 3,
	2, 2, 2, 2, 77, 3, 2, 2, 2, 2, 79, 3, 2, 2, 2, 2, 81, 3, 2, 2, 2, 2, 83,
	3, 2, 2, 2, 2, 85, 3, 2, 2, 2, 2, 87, 3, 2, 2, 2, 2, 89, 3, 2, 2, 2, 2,
	91, 3, 2, 2, 2, 2, 93, 3, 2, 2, 2, 2, 95, 3, 2, 2, 2, 2, 97, 3, 2, 2, 2,
	2, 99, 3, 2, 2, 2, 2, 101, 3, 2, 2, 2, 2, 103, 3, 2, 2, 2, 2, 105, 3, 2,
	2, 2, 2, 107, 3, 2, 2, 2, 2, 109, 3, 2, 2, 2, 2, 111, 3, 2, 2, 2, 2, 113,
	3, 2, 2, 2, 2, 115, 3, 2, 2, 2, 2, 117, 3, 2, 2, 2, 2, 119, 3, 2, 2, 2,
	2, 121, 3, 2, 2, 2, 2, 123, 3, 2, 2, 2, 2, 125, 3, 2, 2, 2, 2, 127, 3,
	2, 2, 2, 2, 129, 3, 2, 2, 2, 2, 131, 3, 2, 2, 2, 2, 133, 3, 2, 2, 2, 2,
	135, 3, 2, 2, 2, 2, 137, 3, 2, 2, 2, 2, 139, 3, 2, 2, 2, 2, 141, 3, 2,
	2, 2, 2, 143, 3, 2, 2, 2, 2, 145, 3, 2, 2, 2, 2, 147, 3, 2, 2, 2, 2, 149,
	3, 2, 2, 2, 2, 151, 3, 2, 2, 2, 2, 153, 3, 2, 2, 2, 2, 155, 3, 2, 2, 2,
	2, 157, 3, 2, 2, 2, 2, 159, 3, 2, 2, 2, 2, 161, 3, 2, 2, 2, 2, 179, 3,
	2, 2, 2, 2, 181, 3, 2, 2, 2, 2, 183, 3, 2, 2, 2, 2, 185, 3, 2, 2, 2, 3,
	187, 3, 2, 2, 2, 3, 189, 3, 2, 2, 2, 3, 191, 3, 2, 2, 2, 3, 193, 3, 2,
	2, 2, 3, 195, 3, 2, 2, 2, 3, 197, 3, 2, 2, 2, 3, 199, 3, 2, 2, 2, 3, 201,
	3, 2, 2, 2, 4, 203, 3, 2, 2, 2, 5, 216, 3, 2, 2, 2, 7, 230, 3, 2, 2, 2,
	9, 232, 3, 2, 2, 2, 11, 234, 3, 2, 2, 2, 13, 238, 3, 2, 2, 2, 15, 262,
	3, 2, 2, 2, 17, 273, 3, 2, 2, 2, 19, 275, 3, 2, 2, 2, 21, 283, 3, 2, 2,
	2, 23, 290, 3, 2, 2, 2, 25, 293, 3, 2, 2, 2, 27, 298, 3, 2, 2, 2, 29, 302,
	3, 2, 2, 2, 31, 305, 3, 2, 2, 2, 33, 308, 3, 2, 2, 2, 35, 324, 3, 2, 2,
	2, 37, 326, 3, 2, 2, 2, 39, 332, 3, 2, 2, 2, 41, 336, 3, 2, 2, 2, 43, 341,
	3, 2, 2, 2, 45, 363, 3, 2, 2, 2, 47, 365, 3, 2, 2, 2, 49, 371, 3, 2, 2,
	2, 51, 375, 3, 2, 2, 2, 53, 381, 3, 2, 2, 2, 55, 385, 3, 2, 2, 2, 57, 394,
	3, 2, 2, 2, 59, 399, 3, 2, 2, 2, 61, 406, 3, 2, 2, 2, 63, 411, 3, 2, 2,
	2, 65, 419, 3, 2, 2, 2, 67, 422, 3, 2, 2, 2, 69, 428, 3, 2, 2, 2, 71, 437,
	3, 2, 2, 2, 73, 444, 3, 2, 2, 2, 75, 450, 3, 2, 2, 2, 77, 453, 3, 2, 2,
	2, 79, 455, 3, 2, 2, 2, 81, 458, 3, 2, 2, 2, 83, 461, 3, 2, 2, 2, 85, 464,
	3, 2, 2, 2, 87, 467, 3, 2, 2, 2, 89, 469, 3, 2, 2, 2, 91, 471, 3, 2, 2,
	2, 93, 473, 3, 2, 2, 2, 95, 475, 3, 2, 2, 2, 97, 477, 3, 2, 2, 2, 99, 479,
	3, 2, 2, 2, 101, 481, 3, 2, 2, 2, 103, 483, 3, 2, 2, 2, 105, 485, 3, 2,
	2, 2, 107, 487, 3, 2, 2, 2, 109, 490, 3, 2, 2, 2, 111, 492, 3, 2, 2, 2,
	113, 494, 3, 2, 2, 2, 115, 507, 3, 2, 2, 2, 117, 517, 3, 2, 2, 2, 119,
	528, 3, 2, 2, 2, 121, 541, 3, 2, 2, 2, 123, 543, 3, 2, 2, 2, 125, 545,
	3, 2, 2, 2, 127, 547, 3, 2, 2, 2, 129, 549, 3, 2, 2, 2, 131, 551, 3, 2,
	2, 2, 133, 553, 3, 2, 2, 2, 135, 555, 3, 2, 2, 2, 137, 557, 3, 2, 2, 2,
	139, 560, 3, 2, 2, 2, 141, 562, 3, 2, 2, 2, 143, 564, 3, 2, 2, 2, 145,
	568, 3, 2, 2, 2, 147, 571, 3, 2, 2, 2, 149, 574, 3, 2, 2, 2, 151, 580,
	3, 2, 2, 2, 153, 587, 3, 2, 2, 2, 155, 592, 3, 2, 2, 2, 157, 597, 3, 2,
	2, 2, 159, 610, 3, 2, 2, 2, 161, 626, 3, 2, 2, 2, 163, 628, 3, 2, 2, 2,
	165, 633, 3, 2, 2, 2, 167, 638, 3, 2, 2, 2, 169, 648, 3, 2, 2, 2, 171,
	650, 3, 2, 2, 2, 173, 652, 3, 2, 2, 2, 175, 655, 3, 2, 2, 2, 177, 661,
	3, 2, 2, 2, 179, 689, 3, 2, 2, 2, 181, 694, 3, 2, 2, 2, 183, 700, 3, 2,
	2, 2, 185, 704, 3, 2, 2, 2, 187, 706, 3, 2, 2, 2, 189, 709, 3, 2, 2, 2,
	191, 712, 3, 2, 2, 2, 193, 715, 3, 2, 2, 2, 195, 718, 3, 2, 2, 2, 197,
	722, 3, 2, 2, 2, 199, 728, 3, 2, 2, 2, 201, 732, 3, 2, 2, 2, 203, 736,
	3, 2, 2, 2, 205, 207, 5, 165, 82, 2, 206, 205, 3, 2, 2, 2, 207, 210, 3,
	2, 2, 2, 208, 206, 3, 2, 2, 2, 208, 209, 3, 2, 2, 2, 209, 217, 3, 2, 2,
	2, 210, 208, 3, 2, 2, 2, 211, 213, 5, 165, 82, 2, 212, 211, 3, 2, 2, 2,
	213, 214, 3, 2, 2, 2, 214, 212, 3, 2, 2, 2, 214, 215, 3, 2, 2, 2, 215,
	217, 3, 2, 2, 2, 216, 208, 3, 2, 2, 2, 216, 212, 3, 2, 2, 2, 217, 6, 3,
	2, 2, 2, 218, 222, 5, 163, 81, 2, 219, 221, 5, 165, 82, 2, 220, 219, 3,
	2, 2, 2, 221, 224, 3, 2, 2, 2, 222, 220, 3, 2, 2, 2, 222, 223, 3, 2, 2,
	2, 223, 231, 3, 2, 2, 2, 224, 222, 3, 2, 2, 2, 225, 227, 5, 165, 82, 2,
	226, 225, 3, 2, 2, 2, 227, 228, 3, 2, 2, 2, 228, 226, 3, 2, 2, 2, 228,
	229, 3, 2, 2, 2, 229, 231, 3, 2, 2, 2, 230, 218, 3, 2, 2, 2, 230, 226,
	3, 2, 2, 2, 231, 8, 3, 2, 2, 2, 232, 233, 7, 36, 2, 2, 233, 10, 3, 2, 2,
	2, 234, 235, 7, 120, 2, 2, 235, 236, 7, 99, 2, 2, 236, 237, 7, 116, 2,
	2, 237, 12, 3, 2, 2, 2, 238, 239, 7, 99, 2, 2, 239, 240, 7, 116, 2, 2,
	240, 241, 7, 116, 2, 2, 241, 242, 7, 99, 2, 2, 242, 243, 7, 123, 2, 2,
	243, 14, 3, 2, 2, 2, 244, 245, 7, 101, 2, 2, 245, 246, 7, 113, 2, 2, 246,
	263, 7, 112, 2, 2, 247, 263, 11, 2, 2, 2, 248, 249, 7, 101, 2, 2, 249,
	250, 7, 113, 2, 2, 250, 251, 7, 112, 2, 2, 251, 252, 7, 117, 2, 2, 252,
	263, 7, 118, 2, 2, 253, 263, 11, 2, 2, 2, 254, 255, 7, 101, 2, 2, 255,
	256, 7, 113, 2, 2, 256, 257, 7, 112, 2, 2, 257, 258, 7, 117, 2, 2, 258,
	259, 7, 118, 2, 2, 259, 260, 7, 99, 2, 2, 260, 261, 7, 112, 2, 2, 261,
	263, 7, 118, 2, 2, 262, 244, 3, 2, 2, 2, 262, 247, 3, 2, 2, 2, 262, 248,
	3, 2, 2, 2, 262, 253, 3, 2, 2, 2, 262, 254, 3, 2, 2, 2, 263, 16, 3, 2,
	2, 2, 264, 265, 7, 110, 2, 2, 265, 266, 7, 113, 2, 2, 266, 274, 7, 101,
	2, 2, 267, 274, 11, 2, 2, 2, 268, 269, 7, 110, 2, 2, 269, 270, 7, 113,
	2, 2, 270, 271, 7, 101, 2, 2, 271, 272, 7, 99, 2, 2, 272, 274, 7, 110,
	2, 2, 273, 264, 3, 2, 2, 2, 273, 267, 3, 2, 2, 2, 273, 268, 3, 2, 2, 2,
	274, 18, 3, 2, 2, 2, 275, 276, 7, 102, 2, 2, 276, 277, 7, 107, 2, 2, 277,
	278, 7, 117, 2, 2, 278, 279, 7, 114, 2, 2, 279, 280, 7, 110, 2, 2, 280,
	281, 7, 99, 2, 2, 281, 282, 7, 123, 2, 2, 282, 20, 3, 2, 2, 2, 283, 284,
	7, 116, 2, 2, 284, 285, 7, 103, 2, 2, 285, 286, 7, 118, 2, 2, 286, 287,
	7, 119, 2, 2, 287, 288, 7, 116, 2, 2, 288, 289, 7, 112, 2, 2, 289, 22,
	3, 2, 2, 2, 290, 291, 7, 107, 2, 2, 291, 292, 7, 104, 2, 2, 292, 24, 3,
	2, 2, 2, 293, 294, 7, 118, 2, 2, 294, 295, 7, 106, 2, 2, 295, 296, 7, 103,
	2, 2, 296, 297, 7, 112, 2, 2, 297, 26, 3, 2, 2, 2, 298, 299, 7, 99, 2,
	2, 299, 300, 7, 112, 2, 2, 300, 301, 7, 102, 2, 2, 301, 28, 3, 2, 2, 2,
	302, 303, 7, 113, 2, 2, 303, 304, 7, 116, 2, 2, 304, 30, 3, 2, 2, 2, 305,
	306, 7, 107, 2, 2, 306, 307, 7, 112, 2, 2, 307, 32, 3, 2, 2, 2, 308, 309,
	7, 103, 2, 2, 309, 310, 7, 110, 2, 2, 310, 311, 7, 117, 2, 2, 311, 312,
	7, 103, 2, 2, 312, 34, 3, 2, 2, 2, 313, 314, 7, 103, 2, 2, 314, 315, 7,
	110, 2, 2, 315, 316, 7, 117, 2, 2, 316, 317, 7, 103, 2, 2, 317, 318, 7,
	107, 2, 2, 318, 325, 7, 104, 2, 2, 319, 325, 11, 2, 2, 2, 320, 321, 7,
	103, 2, 2, 321, 322, 7, 110, 2, 2, 322, 323, 7, 107, 2, 2, 323, 325, 7,
	104, 2, 2, 324, 313, 3, 2, 2, 2, 324, 319, 3, 2, 2, 2, 324, 320, 3, 2,
	2, 2, 325, 36, 3, 2, 2, 2, 326, 327, 7, 121, 2, 2, 327, 328, 7, 106, 2,
	2, 328, 329, 7, 107, 2, 2, 329, 330, 7, 110, 2, 2, 330, 331, 7, 103, 2,
	2, 331, 38, 3, 2, 2, 2, 332, 333, 7, 104, 2, 2, 333, 334, 7, 113, 2, 2,
	334, 335, 7, 116, 2, 2, 335, 40, 3, 2, 2, 2, 336, 337, 7, 118, 2, 2, 337,
	338, 7, 116, 2, 2, 338, 339, 7, 119, 2, 2, 339, 340, 7, 103, 2, 2, 340,
	42, 3, 2, 2, 2, 341, 342, 7, 104, 2, 2, 342, 343, 7, 99, 2, 2, 343, 344,
	7, 110, 2, 2, 344, 345, 7, 117, 2, 2, 345, 346, 7, 103, 2, 2, 346, 44,
	3, 2, 2, 2, 347, 348, 7, 104, 2, 2, 348, 349, 7, 119, 2, 2, 349, 350, 7,
	112, 2, 2, 350, 351, 7, 101, 2, 2, 351, 352, 7, 118, 2, 2, 352, 353, 7,
	107, 2, 2, 353, 354, 7, 113, 2, 2, 354, 364, 7, 112, 2, 2, 355, 364, 11,
	2, 2, 2, 356, 357, 7, 104, 2, 2, 357, 358, 7, 119, 2, 2, 358, 359, 7, 112,
	2, 2, 359, 364, 7, 101, 2, 2, 360, 364, 11, 2, 2, 2, 361, 362, 7, 104,
	2, 2, 362, 364, 7, 112, 2, 2, 363, 347, 3, 2, 2, 2, 363, 355, 3, 2, 2,
	2, 363, 356, 3, 2, 2, 2, 363, 360, 3, 2, 2, 2, 363, 361, 3, 2, 2, 2, 364,
	46, 3, 2, 2, 2, 365, 366, 7, 101, 2, 2, 366, 367, 7, 110, 2, 2, 367, 368,
	7, 99, 2, 2, 368, 369, 7, 117, 2, 2, 369, 370, 7, 117, 2, 2, 370, 48, 3,
	2, 2, 2, 371, 372, 7, 110, 2, 2, 372, 373, 7, 103, 2, 2, 373, 374, 7, 118,
	2, 2, 374, 50, 3, 2, 2, 2, 375, 376, 7, 118, 2, 2, 376, 377, 7, 116, 2,
	2, 377, 378, 7, 99, 2, 2, 378, 379, 7, 107, 2, 2, 379, 380, 7, 118, 2,
	2, 380, 52, 3, 2, 2, 2, 381, 382, 7, 102, 2, 2, 382, 383, 7, 103, 2, 2,
	383, 384, 7, 104, 2, 2, 384, 54, 3, 2, 2, 2, 385, 386, 7, 114, 2, 2, 386,
	387, 7, 116, 2, 2, 387, 388, 7, 113, 2, 2, 388, 389, 7, 118, 2, 2, 389,
	390, 7, 113, 2, 2, 390, 391, 7, 101, 2, 2, 391, 392, 7, 113, 2, 2, 392,
	393, 7, 110, 2, 2, 393, 56, 3, 2, 2, 2, 394, 395, 7, 103, 2, 2, 395, 396,
	7, 112, 2, 2, 396, 397, 7, 119, 2, 2, 397, 398, 7, 111, 2, 2, 398, 58,
	3, 2, 2, 2, 399, 400, 7, 107, 2, 2, 400, 401, 7, 111, 2, 2, 401, 402, 7,
	114, 2, 2, 402, 403, 7, 113, 2, 2, 403, 404, 7, 116, 2, 2, 404, 405, 7,
	118, 2, 2, 405, 60, 3, 2, 2, 2, 406, 407, 7, 104, 2, 2, 407, 408, 7, 116,
	2, 2, 408, 409, 7, 113, 2, 2, 409, 410, 7, 111, 2, 2, 410, 62, 3, 2, 2,
	2, 411, 412, 7, 114, 2, 2, 412, 413, 7, 99, 2, 2, 413, 414, 7, 101, 2,
	2, 414, 415, 7, 109, 2, 2, 415, 416, 7, 99, 2, 2, 416, 417, 7, 105, 2,
	2, 417, 418, 7, 103, 2, 2, 418, 64, 3, 2, 2, 2, 419, 420, 7, 99, 2, 2,
	420, 421, 7, 117, 2, 2, 421, 66, 3, 2, 2, 2, 422, 423, 7, 100, 2, 2, 423,
	424, 7, 116, 2, 2, 424, 425, 7, 103, 2, 2, 425, 426, 7, 99, 2, 2, 426,
	427, 7, 109, 2, 2, 427, 68, 3, 2, 2, 2, 428, 429, 7, 99, 2, 2, 429, 430,
	7, 100, 2, 2, 430, 431, 7, 117, 2, 2, 431, 432, 7, 118, 2, 2, 432, 433,
	7, 116, 2, 2, 433, 434, 7, 99, 2, 2, 434, 435, 7, 101, 2, 2, 435, 436,
	7, 118, 2, 2, 436, 70, 3, 2, 2, 2, 437, 438, 7, 117, 2, 2, 438, 439, 7,
	103, 2, 2, 439, 440, 7, 110, 2, 2, 440, 441, 7, 103, 2, 2, 441, 442, 7,
	101, 2, 2, 442, 443, 7, 118, 2, 2, 443, 72, 3, 2, 2, 2, 444, 445, 7, 107,
	2, 2, 445, 446, 7, 112, 2, 2, 446, 447, 7, 114, 2, 2, 447, 448, 7, 119,
	2, 2, 448, 449, 7, 118, 2, 2, 449, 74, 3, 2, 2, 2, 450, 451, 7, 60, 2,
	2, 451, 452, 7, 63, 2, 2, 452, 76, 3, 2, 2, 2, 453, 454, 7, 63, 2, 2, 454,
	78, 3, 2, 2, 2, 455, 456, 7, 63, 2, 2, 456, 457, 7, 63, 2, 2, 457, 80,
	3, 2, 2, 2, 458, 459, 7, 35, 2, 2, 459, 460, 7, 63, 2, 2, 460, 82, 3, 2,
	2, 2, 461, 462, 7, 62, 2, 2, 462, 463, 7, 63, 2, 2, 463, 84, 3, 2, 2, 2,
	464, 465, 7, 64, 2, 2, 465, 466, 7, 63, 2, 2, 466, 86, 3, 2, 2, 2, 467,
	468, 7, 45, 2, 2, 468, 88, 3, 2, 2, 2, 469, 470, 7, 47, 2, 2, 470, 90,
	3, 2, 2, 2, 471, 472, 7, 44, 2, 2, 472, 92, 3, 2, 2, 2, 473, 474, 7, 49,
	2, 2, 474, 94, 3, 2, 2, 2, 475, 476, 7, 62, 2, 2, 476, 96, 3, 2, 2, 2,
	477, 478, 7, 64, 2, 2, 478, 98, 3, 2, 2, 2, 479, 480, 7, 35, 2, 2, 480,
	100, 3, 2, 2, 2, 481, 482, 7, 96, 2, 2, 482, 102, 3, 2, 2, 2, 483, 484,
	7, 39, 2, 2, 484, 104, 3, 2, 2, 2, 485, 486, 7, 126, 2, 2, 486, 106, 3,
	2, 2, 2, 487, 488, 7, 126, 2, 2, 488, 489, 7, 126, 2, 2, 489, 108, 3, 2,
	2, 2, 490, 491, 7, 37, 2, 2, 491, 110, 3, 2, 2, 2, 492, 493, 7, 40, 2,
	2, 493, 112, 3, 2, 2, 2, 494, 495, 7, 40, 2, 2, 495, 496, 7, 40, 2, 2,
	496, 114, 3, 2, 2, 2, 497, 498, 7, 107, 2, 2, 498, 499, 7, 112, 2, 2, 499,
	508, 7, 118, 2, 2, 500, 501, 7, 107, 2, 2, 501, 502, 7, 112, 2, 2, 502,
	503, 7, 118, 2, 2, 503, 504, 7, 103, 2, 2, 504, 505, 7, 105, 2, 2, 505,
	506, 7, 103, 2, 2, 506, 508, 7, 116, 2, 2, 507, 497, 3, 2, 2, 2, 507, 500,
	3, 2, 2, 2, 508, 116, 3, 2, 2, 2, 509, 510, 7, 104, 2, 2, 510, 511, 7,
	110, 2, 2, 511, 518, 7, 118, 2, 2, 512, 513, 7, 104, 2, 2, 513, 514, 7,
	110, 2, 2, 514, 515, 7, 113, 2, 2, 515, 516, 7, 99, 2, 2, 516, 518, 7,
	118, 2, 2, 517, 509, 3, 2, 2, 2, 517, 512, 3, 2, 2, 2, 518, 118, 3, 2,
	2, 2, 519, 520, 7, 117, 2, 2, 520, 521, 7, 118, 2, 2, 521, 529, 7, 116,
	2, 2, 522, 523, 7, 117, 2, 2, 523, 524, 7, 118, 2, 2, 524, 525, 7, 116,
	2, 2, 525, 526, 7, 107, 2, 2, 526, 527, 7, 112, 2, 2, 527, 529, 7, 105,
	2, 2, 528, 519, 3, 2, 2, 2, 528, 522, 3, 2, 2, 2, 529, 120, 3, 2, 2, 2,
	530, 531, 7, 100, 2, 2, 531, 532, 7, 113, 2, 2, 532, 533, 7, 113, 2, 2,
	533, 542, 7, 110, 2, 2, 534, 535, 7, 100, 2, 2, 535, 536, 7, 113, 2, 2,
	536, 537, 7, 113, 2, 2, 537, 538, 7, 110, 2, 2, 538, 539, 7, 103, 2, 2,
	539, 540, 7, 99, 2, 2, 540, 542, 7, 112, 2, 2, 541, 530, 3, 2, 2, 2, 541,
	534, 3, 2, 2, 2, 542, 122, 3, 2, 2, 2, 543, 544, 7, 46, 2, 2, 544, 124,
	3, 2, 2, 2, 545, 546, 7, 42, 2, 2, 546, 126, 3, 2, 2, 2, 547, 548, 7, 43,
	2, 2, 548, 128, 3, 2, 2, 2, 549, 550, 7, 125, 2, 2, 550, 130, 3, 2, 2,
	2, 551, 552, 7, 127, 2, 2, 552, 132, 3, 2, 2, 2, 553, 554, 7, 93, 2, 2,
	554, 134, 3, 2, 2, 2, 555, 556, 7, 95, 2, 2, 556, 136, 3, 2, 2, 2, 557,
	558, 7, 47, 2, 2, 558, 559, 7, 64, 2, 2, 559, 138, 3, 2, 2, 2, 560, 561,
	7, 60, 2, 2, 561, 140, 3, 2, 2, 2, 562, 563, 7, 48, 2, 2, 563, 142, 3,
	2, 2, 2, 564, 565, 7, 48, 2, 2, 565, 566, 7, 48, 2, 2, 566, 567, 7, 48,
	2, 2, 567, 144, 3, 2, 2, 2, 568, 569, 7, 45, 2, 2, 569, 570, 7, 45, 2,
	2, 570, 146, 3, 2, 2, 2, 571, 572, 7, 47, 2, 2, 572, 573, 7, 47, 2, 2,
	573, 148, 3, 2, 2, 2, 574, 575, 7, 104, 2, 2, 575, 576, 7, 110, 2, 2, 576,
	577, 7, 113, 2, 2, 577, 578, 7, 99, 2, 2, 578, 579, 7, 118, 2, 2, 579,
	150, 3, 2, 2, 2, 580, 581, 7, 117, 2, 2, 581, 582, 7, 118, 2, 2, 582, 583,
	7, 116, 2, 2, 583, 584, 7, 107, 2, 2, 584, 585, 7, 112, 2, 2, 585, 586,
	7, 105, 2, 2, 586, 152, 3, 2, 2, 2, 587, 588, 7, 100, 2, 2, 588, 589, 7,
	113, 2, 2, 589, 590, 7, 113, 2, 2, 590, 591, 7, 110, 2, 2, 591, 154, 3,
	2, 2, 2, 592, 593, 7, 112, 2, 2, 593, 594, 7, 119, 2, 2, 594, 595, 7, 110,
	2, 2, 595, 596, 7, 110, 2, 2, 596, 156, 3, 2, 2, 2, 597, 598, 7, 101, 2,
	2, 598, 599, 7, 106, 2, 2, 599, 600, 7, 99, 2, 2, 600, 601, 7, 116, 2,
	2, 601, 158, 3, 2, 2, 2, 602, 611, 7, 50, 2, 2, 603, 607, 9, 2, 2, 2, 604,
	606, 9, 3, 2, 2, 605, 604, 3, 2, 2, 2, 606, 609, 3, 2, 2, 2, 607, 605,
	3, 2, 2, 2, 607, 608, 3, 2, 2, 2, 608, 611, 3, 2, 2, 2, 609, 607, 3, 2,
	2, 2, 610, 602, 3, 2, 2, 2, 610, 603, 3, 2, 2, 2, 611, 160, 3, 2, 2, 2,
	612, 627, 7, 50, 2, 2, 613, 617, 9, 2, 2, 2, 614, 616, 9, 3, 2, 2, 615,
	614, 3, 2, 2, 2, 616, 619, 3, 2, 2, 2, 617, 615, 3, 2, 2, 2, 617, 618,
	3, 2, 2, 2, 618, 620, 3, 2, 2, 2, 619, 617, 3, 2, 2, 2, 620, 622, 7, 48,
	2, 2, 621, 623, 9, 3, 2, 2, 622, 621, 3, 2, 2, 2, 623, 624, 3, 2, 2, 2,
	624, 622, 3, 2, 2, 2, 624, 625, 3, 2, 2, 2, 625, 627, 3, 2, 2, 2, 626,
	612, 3, 2, 2, 2, 626, 613, 3, 2, 2, 2, 627, 162, 3, 2, 2, 2, 628, 629,
	7, 61, 2, 2, 629, 164, 3, 2, 2, 2, 630, 631, 7, 15, 2, 2, 631, 634, 7,
	12, 2, 2, 632, 634, 9, 4, 2, 2, 633, 630, 3, 2, 2, 2, 633, 632, 3, 2, 2,
	2, 634, 166, 3, 2, 2, 2, 635, 637, 9, 5, 2, 2, 636, 635, 3, 2, 2, 2, 637,
	640, 3, 2, 2, 2, 638, 636, 3, 2, 2, 2, 638, 639, 3, 2, 2, 2, 639, 641,
	3, 2, 2, 2, 640, 638, 3, 2, 2, 2, 641, 645, 9, 6, 2, 2, 642, 644, 9, 7,
	2, 2, 643, 642, 3, 2, 2, 2, 644, 647, 3, 2, 2, 2, 645, 643, 3, 2, 2, 2,
	645, 646, 3, 2, 2, 2, 646, 168, 3, 2, 2, 2, 647, 645, 3, 2, 2, 2, 648,
	649, 9, 8, 2, 2, 649, 170, 3, 2, 2, 2, 650, 651, 9, 9, 2, 2, 651, 172,
	3, 2, 2, 2, 652, 653, 9, 10, 2, 2, 653, 174, 3, 2, 2, 2, 654, 656, 9, 11,
	2, 2, 655, 654, 3, 2, 2, 2, 656, 657, 3, 2, 2, 2, 657, 655, 3, 2, 2, 2,
	657, 658, 3, 2, 2, 2, 658, 659, 3, 2, 2, 2, 659, 660, 8, 87, 2, 2, 660,
	176, 3, 2, 2, 2, 661, 662, 9, 12, 2, 2, 662, 663, 3, 2, 2, 2, 663, 664,
	8, 88, 3, 2, 664, 178, 3, 2, 2, 2, 665, 666, 7, 49, 2, 2, 666, 667, 7,
	49, 2, 2, 667, 671, 3, 2, 2, 2, 668, 670, 10, 4, 2, 2, 669, 668, 3, 2,
	2, 2, 670, 673, 3, 2, 2, 2, 671, 669, 3, 2, 2, 2, 671, 672, 3, 2, 2, 2,
	672, 675, 3, 2, 2, 2, 673, 671, 3, 2, 2, 2, 674, 676, 7, 15, 2, 2, 675,
	674, 3, 2, 2, 2, 675, 676, 3, 2, 2, 2, 676, 677, 3, 2, 2, 2, 677, 690,
	7, 12, 2, 2, 678, 679, 7, 49, 2, 2, 679, 680, 7, 44, 2, 2, 680, 684, 3,
	2, 2, 2, 681, 683, 11, 2, 2, 2, 682, 681, 3, 2, 2, 2, 683, 686, 3, 2, 2,
	2, 684, 685, 3, 2, 2, 2, 684, 682, 3, 2, 2, 2, 685, 687, 3, 2, 2, 2, 686,
	684, 3, 2, 2, 2, 687, 688, 7, 44, 2, 2, 688, 690, 7, 49, 2, 2, 689, 665,
	3, 2, 2, 2, 689, 678, 3, 2, 2, 2, 690, 691, 3, 2, 2, 2, 691, 692, 8, 89,
	4, 2, 692, 180, 3, 2, 2, 2, 693, 695, 9, 4, 2, 2, 694, 693, 3, 2, 2, 2,
	695, 696, 3, 2, 2, 2, 696, 694, 3, 2, 2, 2, 696, 697, 3, 2, 2, 2, 697,
	698, 3, 2, 2, 2, 698, 699, 8, 90, 3, 2, 699, 182, 3, 2, 2, 2, 700, 701,
	7, 36, 2, 2, 701, 702, 3, 2, 2, 2, 702, 703, 8, 91, 5, 2, 703, 184, 3,
	2, 2, 2, 704, 705, 11, 2, 2, 2, 705, 186, 3, 2, 2, 2, 706, 707, 7, 94,
	2, 2, 707, 708, 7, 36, 2, 2, 708, 188, 3, 2, 2, 2, 709, 710, 7, 94, 2,
	2, 710, 711, 7, 94, 2, 2, 711, 190, 3, 2, 2, 2, 712, 713, 7, 94, 2, 2,
	713, 714, 7, 112, 2, 2, 714, 192, 3, 2, 2, 2, 715, 716, 7, 94, 2, 2, 716,
	717, 7, 37, 2, 2, 717, 194, 3, 2, 2, 2, 718, 719, 7, 36, 2, 2, 719, 720,
	3, 2, 2, 2, 720, 721, 8, 97, 6, 2, 721, 196, 3, 2, 2, 2, 722, 723, 7, 37,
	2, 2, 723, 724, 7, 125, 2, 2, 724, 725, 3, 2, 2, 2, 725, 726, 8, 98, 7,
	2, 726, 198, 3, 2, 2, 2, 727, 729, 10, 13, 2, 2, 728, 727, 3, 2, 2, 2,
	729, 730, 3, 2, 2, 2, 730, 728, 3, 2, 2, 2, 730, 731, 3, 2, 2, 2, 731,
	200, 3, 2, 2, 2, 732, 733, 11, 2, 2, 2, 733, 734, 3, 2, 2, 2, 734, 735,
	8, 100, 8, 2, 735, 202, 3, 2, 2, 2, 736, 737, 7, 127, 2, 2, 737, 738, 3,
	2, 2, 2, 738, 739, 8, 101, 6, 2, 739, 204, 3, 2, 2, 2, 34, 2, 3, 4, 208,
	214, 216, 222, 228, 230, 262, 273, 324, 363, 507, 517, 528, 541, 607, 610,
	617, 624, 626, 633, 638, 645, 657, 671, 675, 684, 689, 696, 730, 9, 2,
	4, 2, 2, 3, 2, 2, 5, 2, 7, 3, 2, 6, 2, 2, 7, 4, 2, 9, 85, 2,
}

var lexerDeserializer = antlr.NewATNDeserializer(nil)
var lexerAtn = lexerDeserializer.DeserializeFromUInt16(serializedLexerAtn)

var lexerChannelNames = []string{
	"DEFAULT_TOKEN_CHANNEL", "HIDDEN", "WHITESPACE", "COMMENT_CH",
}

var lexerModeNames = []string{
	"DEFAULT_MODE", "MODE_IN_STRING", "MODE_IN_INTERPOLATION",
}

var lexerLiteralNames = []string{
	"", "", "", "", "'var'", "'array'", "", "", "'display'", "'return'", "'if'",
	"'then'", "'and'", "'or'", "'in'", "'else'", "", "'while'", "'for'", "'true'",
	"'false'", "", "'class'", "'let'", "'trait'", "'def'", "'protocol'", "'enum'",
	"'import'", "'from'", "'package'", "'as'", "'break'", "'abstract'", "'select'",
	"'input'", "':='", "'='", "'=='", "'!='", "'<='", "'>='", "'+'", "'-'",
	"'*'", "'/'", "'<'", "'>'", "'!'", "'^'", "'%'", "'|'", "'||'", "'#'",
	"'&'", "'&&'", "", "", "", "", "','", "'('", "')'", "'{'", "", "'['", "']'",
	"'->'", "':'", "'.'", "'...'", "'++'", "'--'", "'float'", "'string'", "'bool'",
	"'null'", "'char'", "", "", "", "", "", "", "'\\\"'", "'\\\\'", "'\\n'",
	"'\\#'", "", "'#{'",
}

var lexerSymbolicNames = []string{
	"", "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", "VAR", "ARRAY",
	"CONST", "LOCAL", "DISPLAY", "RETURN", "IF", "THEN", "AND", "OR", "IN",
	"ELSE", "ELSEIF", "WHILE", "FOR", "TRUE", "FALSE", "FUNCTION", "CLASS",
	"LET", "TRAIT", "DEFINE", "PROTOCOL", "ENUM", "IMPORT", "FROM", "PACKAGE",
	"AS", "BREAK", "ABSTRACT", "SELECT", "INPUT", "ASSIGN", "EQUALS", "EQEQ",
	"NOTEQUAL", "LTEQUALS", "GTEQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE",
	"LESSTHAN", "GREATERTHAN", "BANG", "POWER", "MODULUS", "VERTICAL", "ORSYMBOL",
	"HASH", "AMBERSAND", "ANDSYMBOL", "TYPE_INT", "TYPE_DECIMAL", "TYPE_STRING",
	"TYPE_BOOLEAN", "COMMA", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET",
	"RSQRBRACKET", "ARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS",
	"FLOAT", "STRING", "BOOLEAN", "NULL", "CHAR", "INT_LITERAL", "FLOAT_LITERAL",
	"COMMENT", "TERMINATOR", "STRING_OPEN", "UNMATCHED", "SCAPE_STRING_DELIMITER",
	"ESCAPE_SLASH", "ESCAPE_NEWLINE", "ESCAPE_SHARP", "STRING_CLOSE", "INTERPOLATION_OPEN",
	"STRING_CONTENT", "INTERPOLATION_CLOSE",
}

var lexerRuleNames = []string{
	"ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", "VAR", "ARRAY", "CONST",
	"LOCAL", "DISPLAY", "RETURN", "IF", "THEN", "AND", "OR", "IN", "ELSE",
	"ELSEIF", "WHILE", "FOR", "TRUE", "FALSE", "FUNCTION", "CLASS", "LET",
	"TRAIT", "DEFINE", "PROTOCOL", "ENUM", "IMPORT", "FROM", "PACKAGE", "AS",
	"BREAK", "ABSTRACT", "SELECT", "INPUT", "ASSIGN", "EQUALS", "EQEQ", "NOTEQUAL",
	"LTEQUALS", "GTEQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN",
	"GREATERTHAN", "BANG", "POWER", "MODULUS", "VERTICAL", "ORSYMBOL", "HASH",
	"AMBERSAND", "ANDSYMBOL", "TYPE_INT", "TYPE_DECIMAL", "TYPE_STRING", "TYPE_BOOLEAN",
	"COMMA", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET",
	"ARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS", "FLOAT",
	"STRING", "BOOLEAN", "NULL", "CHAR", "INT_LITERAL", "FLOAT_LITERAL", "SEMICOLON",
	"NEWLINE", "ID", "DIGIT_CONT", "HEXDIGIT", "BINARY", "WHITESPACE", "UNICODE_WS",
	"COMMENT", "TERMINATOR", "STRING_OPEN", "UNMATCHED", "SCAPE_STRING_DELIMITER",
	"ESCAPE_SLASH", "ESCAPE_NEWLINE", "ESCAPE_SHARP", "STRING_CLOSE", "INTERPOLATION_OPEN",
	"STRING_CONTENT", "STR_UNMATCHED", "INTERPOLATION_CLOSE",
}

type JingleLexer struct {
	*antlr.BaseLexer
	channelNames []string
	modeNames    []string
	// TODO: EOF string
}

var lexerDecisionToDFA = make([]*antlr.DFA, len(lexerAtn.DecisionToState))

func init() {
	for index, ds := range lexerAtn.DecisionToState {
		lexerDecisionToDFA[index] = antlr.NewDFA(ds, index)
	}
}

func NewJingleLexer(input antlr.CharStream) *JingleLexer {

	l := new(JingleLexer)

	l.BaseLexer = antlr.NewBaseLexer(input)
	l.Interpreter = antlr.NewLexerATNSimulator(l, lexerAtn, lexerDecisionToDFA, antlr.NewPredictionContextCache())

	l.channelNames = lexerChannelNames
	l.modeNames = lexerModeNames
	l.RuleNames = lexerRuleNames
	l.LiteralNames = lexerLiteralNames
	l.SymbolicNames = lexerSymbolicNames
	l.GrammarFileName = "JingleLexer.g4"
	// TODO: l.EOF = antlr.TokenEOF

	return l
}

// JingleLexer tokens.
const (
	JingleLexerENDSTATEMENT           = 1
	JingleLexerSEMICOLONTERMINATE     = 2
	JingleLexerSPEECHMARKS            = 3
	JingleLexerVAR                    = 4
	JingleLexerARRAY                  = 5
	JingleLexerCONST                  = 6
	JingleLexerLOCAL                  = 7
	JingleLexerDISPLAY                = 8
	JingleLexerRETURN                 = 9
	JingleLexerIF                     = 10
	JingleLexerTHEN                   = 11
	JingleLexerAND                    = 12
	JingleLexerOR                     = 13
	JingleLexerIN                     = 14
	JingleLexerELSE                   = 15
	JingleLexerELSEIF                 = 16
	JingleLexerWHILE                  = 17
	JingleLexerFOR                    = 18
	JingleLexerTRUE                   = 19
	JingleLexerFALSE                  = 20
	JingleLexerFUNCTION               = 21
	JingleLexerCLASS                  = 22
	JingleLexerLET                    = 23
	JingleLexerTRAIT                  = 24
	JingleLexerDEFINE                 = 25
	JingleLexerPROTOCOL               = 26
	JingleLexerENUM                   = 27
	JingleLexerIMPORT                 = 28
	JingleLexerFROM                   = 29
	JingleLexerPACKAGE                = 30
	JingleLexerAS                     = 31
	JingleLexerBREAK                  = 32
	JingleLexerABSTRACT               = 33
	JingleLexerSELECT                 = 34
	JingleLexerINPUT                  = 35
	JingleLexerASSIGN                 = 36
	JingleLexerEQUALS                 = 37
	JingleLexerEQEQ                   = 38
	JingleLexerNOTEQUAL               = 39
	JingleLexerLTEQUALS               = 40
	JingleLexerGTEQUALS               = 41
	JingleLexerPLUS                   = 42
	JingleLexerMINUS                  = 43
	JingleLexerMULTIPLY               = 44
	JingleLexerDIVIDE                 = 45
	JingleLexerLESSTHAN               = 46
	JingleLexerGREATERTHAN            = 47
	JingleLexerBANG                   = 48
	JingleLexerPOWER                  = 49
	JingleLexerMODULUS                = 50
	JingleLexerVERTICAL               = 51
	JingleLexerORSYMBOL               = 52
	JingleLexerHASH                   = 53
	JingleLexerAMBERSAND              = 54
	JingleLexerANDSYMBOL              = 55
	JingleLexerTYPE_INT               = 56
	JingleLexerTYPE_DECIMAL           = 57
	JingleLexerTYPE_STRING            = 58
	JingleLexerTYPE_BOOLEAN           = 59
	JingleLexerCOMMA                  = 60
	JingleLexerLBRACKET               = 61
	JingleLexerRBRACKET               = 62
	JingleLexerLBRACE                 = 63
	JingleLexerRBRACE                 = 64
	JingleLexerLSQRBRACKET            = 65
	JingleLexerRSQRBRACKET            = 66
	JingleLexerARROW                  = 67
	JingleLexerCOLON                  = 68
	JingleLexerDOT                    = 69
	JingleLexerELLIPSIS               = 70
	JingleLexerPLUSPLUS               = 71
	JingleLexerMINUSMINUS             = 72
	JingleLexerFLOAT                  = 73
	JingleLexerSTRING                 = 74
	JingleLexerBOOLEAN                = 75
	JingleLexerNULL                   = 76
	JingleLexerCHAR                   = 77
	JingleLexerINT_LITERAL            = 78
	JingleLexerFLOAT_LITERAL          = 79
	JingleLexerCOMMENT                = 80
	JingleLexerTERMINATOR             = 81
	JingleLexerSTRING_OPEN            = 82
	JingleLexerUNMATCHED              = 83
	JingleLexerSCAPE_STRING_DELIMITER = 84
	JingleLexerESCAPE_SLASH           = 85
	JingleLexerESCAPE_NEWLINE         = 86
	JingleLexerESCAPE_SHARP           = 87
	JingleLexerSTRING_CLOSE           = 88
	JingleLexerINTERPOLATION_OPEN     = 89
	JingleLexerSTRING_CONTENT         = 90
	JingleLexerINTERPOLATION_CLOSE    = 91
)

// JingleLexer channels.
const (
	JingleLexerWHITESPACE = 2
	JingleLexerCOMMENT_CH = 3
)

// JingleLexer modes.
const (
	JingleLexerMODE_IN_STRING = iota + 1
	JingleLexerMODE_IN_INTERPOLATION
)
