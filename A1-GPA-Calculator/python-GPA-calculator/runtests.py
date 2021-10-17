#!/usr/bin/env python3

import gpa_calculator
import unittest

#
# Tests the conversion of percentage grades to letter values for each letter's low, midrange, and high values
#
class TestPercentageGradeToLetterConversion(unittest.TestCase):

    # "Outstanding",        4.3,    "A+",        90,    100    ))
    def test__A_plus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(100), "A+")

    def test__A_plus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(95), "A+")

    def test__A_plus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(90), "A+")

    # "Excellent",        4.0,    "A",        85,    89    ))
    def test__A__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(89), "A")

    def test__A__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(87), "A")

    def test__A__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(85), "A")

    # "Very Good",        3.7,    "A-",        80,    84    ))
    def test__A_minus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(84), "A-")

    def test__A_minus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(82), "A-")

    def test__A_minus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(80), "A-")

    # "Good",                3.3,    "B+",        77,    79    ))
    def test__B_plus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(79), "B+")

    def test__B_plus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(78), "B+")

    def test__B_plus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(77), "B+")

    # "Good",                3.0,    "B",        73,    76    ))
    def test__B__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(76), "B")

    def test__B__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(75), "B")

    def test__B__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(73), "B")

    # "Good",                2.7,    "B-",        70,    72    ))
    def test__B_minus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(72), "B-")

    def test__B_minus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(71), "B-")

    def test__B_minus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(70), "B-")

    # "Satisfactory",        2.3,    "C+",        67,    69    ))
    def test__C_plus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(69), "C+")

    def test__C_plus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(68), "C+")

    def test__C_plus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(67), "C+")

    # "Satisfactory",        2.0,    "C",        63,    66    ))
    def test__C__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(66), "C")

    def test__C__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(65), "C")

    def test__C__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(63), "C")

    # "Satisfactory",        1.7,    "C-",        60,    62    ))
    def test__C_minus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(62), "C-")

    def test__C_minus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(61), "C-")

    def test__C_minus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(60), "C-")

    # "Marginal Pass",    1.3,    "D+",        57,    59    ))
    def test__D_plus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(59), "D+")

    def test__D_plus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(58), "D+")

    def test__D_plus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(57), "D+")

    # "Marginal Pass",    1.0,    "D",        53,    56    ))
    def test__D__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(56), "D")

    def test__D__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(55), "D")

    def test__D__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(53), "D")

    # "Marginal Pass",    0.7,    "D-",        50,    52    ))
    def test__D_minus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(52), "D-")

    def test__D_minus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(51), "D-")

    def test__D_minus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(50), "D-")

    # "Failure",            0.0,    "F",        0,    49    ))
    def test__F__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(49), "F")

    def test__F__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(25), "F")

    def test__F__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(0), "F")


if __name__ == '__main__':
    unittest.main()
