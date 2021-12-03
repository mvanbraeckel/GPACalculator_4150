#!/usr/bin/env python3

"""
Course: Software Reliability and Testing (CIS*4150) - Assignment 3
Date: December 3, 2021
Author: Mitchell Van Braeckel (1002297, mvanbrae@uoguelph.ca)
"""

import gpa_calculator
import unittest
from unittest import mock
import math

# =========================================== Objective Bullet 1 ===========================================

## 1. do the lettergrades function correctly over their entire range?
## -> for each of A+ through F work on their full range

#
# 1.1 - Entire range of numeric grades converted to letter grades (0-100)
# Tests the conversion of percentage grades to letter values for each letter's low, midrange, and high values
# according to official grading system at the University of Guelph (https://www.uoguelph.ca/registrar/calendars/undergraduate/2020-2021/c08/c08-grds.shtml)
#
class TestGetLetterForNumericGrade(unittest.TestCase):

    # Invalid numeric grade too high (greater than 100)
    def test__convert_numeric_to_letter_grade__101percent__invalid__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(101), None)

    # "Outstanding",        4.3,    "A+",        90,    100    ))
    def test__convert_numeric_to_letter_grade__100percent__A_plus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(100), "A+")

    def test__convert_numeric_to_letter_grade__095percent__A_plus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(95), "A+")

    def test__convert_numeric_to_letter_grade__090percent__A_plus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(90), "A+")

    # "Excellent",        4.0,    "A",        85,    89    ))
    def test__convert_numeric_to_letter_grade__089percent__A__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(89), "A")

    def test__convert_numeric_to_letter_grade__087percent__A__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(87), "A")

    def test__convert_numeric_to_letter_grade__085percent__A__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(85), "A")

    # "Very Good",        3.7,    "A-",        80,    84    ))
    def test__convert_numeric_to_letter_grade__084percent__A_minus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(84), "A-")

    def test__convert_numeric_to_letter_grade__082percent__A_minus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(82), "A-")

    def test__convert_numeric_to_letter_grade__080percent__A_minus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(80), "A-")

    # "Good",                3.3,    "B+",        77,    79    ))
    def test__convert_numeric_to_letter_grade__079percent__B_plus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(79), "B+")

    def test__convert_numeric_to_letter_grade__078percent__B_plus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(78), "B+")

    def test__convert_numeric_to_letter_grade__077percent__B_plus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(77), "B+")

    # "Good",                3.0,    "B",        73,    76    ))
    def test__convert_numeric_to_letter_grade__076percent__B__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(76), "B")

    def test__convert_numeric_to_letter_grade__075percent__B__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(75), "B")

    def test__convert_numeric_to_letter_grade__073percent__B__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(73), "B")

    # "Good",                2.7,    "B-",        70,    72    ))
    def test__convert_numeric_to_letter_grade__072percent__B_minus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(72), "B-")

    def test__convert_numeric_to_letter_grade__071percent__B_minus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(71), "B-")

    def test__convert_numeric_to_letter_grade__070percent__B_minus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(70), "B-")

    # "Satisfactory",        2.3,    "C+",        67,    69    ))
    def test__convert_numeric_to_letter_grade__069percent__C_plus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(69), "C+")

    def test__convert_numeric_to_letter_grade__068percent__C_plus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(68), "C+")

    def test__convert_numeric_to_letter_grade__067percent__C_plus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(67), "C+")

    # "Satisfactory",        2.0,    "C",        63,    66    ))
    def test__convert_numeric_to_letter_grade__066percent__C__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(66), "C")

    def test__convert_numeric_to_letter_grade__065percent__C__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(65), "C")

    def test__convert_numeric_to_letter_grade__063percent__C__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(63), "C")

    # "Satisfactory",        1.7,    "C-",        60,    62    ))
    def test__convert_numeric_to_letter_grade__062percent__C_minus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(62), "C-")

    def test__convert_numeric_to_letter_grade__061percent__C_minus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(61), "C-")

    def test__convert_numeric_to_letter_grade__060percent__C_minus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(60), "C-")

    # "Marginal Pass",    1.3,    "D+",        57,    59    ))
    def test__convert_numeric_to_letter_grade__059percent__D_plus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(59), "D+")

    def test__convert_numeric_to_letter_grade__058percent__D_plus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(58), "D+")

    def test__convert_numeric_to_letter_grade__057percent__D_plus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(57), "D+")

    # "Marginal Pass",    1.0,    "D",        53,    56    ))
    def test__convert_numeric_to_letter_grade__056percent__D__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(56), "D")

    def test__convert_numeric_to_letter_grade__055percent__D__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(55), "D")

    def test__convert_numeric_to_letter_grade__053percent__D__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(53), "D")

    # "Marginal Pass",    0.7,    "D-",        50,    52    ))
    def test__convert_numeric_to_letter_grade__052percent__D_minus__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(52), "D-")

    def test__convert_numeric_to_letter_grade__051percent__D_minus__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(51), "D-")

    def test__convert_numeric_to_letter_grade__050percent__D_minus__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(50), "D-")

    # "Failure",            0.0,    "F",        0,    49    ))
    def test__convert_numeric_to_letter_grade__049percent__F__high(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(49), "F")

    def test__convert_numeric_to_letter_grade__025percent__F__midrange(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(25), "F")

    def test__convert_numeric_to_letter_grade__000percent__F__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(0), "F")

    # Invalid grade too low (less than 0)
    def test__convert_numeric_to_letter_grade__negative_one_percent__invalid__low(self):
        self.assertEqual(gpa_calculator.gpa_converter.getLetterForNumericGrade(-1), None)

#
# 1.2 - All letter grades' associated GPA values (full coverage of A+ through F)
# Tests the conversion of letter grades to GPA values for each letter grade (plus, normal, and minus decorators as appropriate)
# according to official GPA calculator as indicated by the University of Guelph (https://www.uoguelph.ca/uaic/faq/grades/how-do-i-calculate-gpa-using-my-guelph-grades -> https://www.whatsmygpa.ca/)
# NOTE: This shows that the UoG GPA operates on an official 4.0 scale; however, this GPA calculator code tries to calculate on a 4.3 GPA scale (eg. see Outstanding A+ of 90-100% is evaluated as 4.3 GPA value incorrectly)
#
class TestGetGPAforLetterGrade(unittest.TestCase):

    # "Outstanding",        4.3,    "A+",        90,    100    ))
    # NOTE: UoG actually operates on a 4.0 GPA scale officially, which is why the expected value is 4.0 instead of the 4.3 that has been coded into this calculator
    def test__convert_letter_to_gpa__A_plus(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("A+"), 4.0)

    # "Excellent",        4.0,    "A",        85,    89    ))
    def test__convert_letter_to_gpa__A(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("A"), 4.0)

    # "Very Good",        3.7,    "A-",        80,    84    ))
    def test__convert_letter_to_gpa__A_minus(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("A-"), 3.7)

    # "Good",                3.3,    "B+",        77,    79    ))
    def test__convert_letter_to_gpa__B_plus(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("B+"), 3.3)

    # "Good",                3.0,    "B",        73,    76    ))
    def test__convert_letter_to_gpa__B(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("B"), 3.0)

    # "Good",                2.7,    "B-",        70,    72    ))
    def test__convert_letter_to_gpa__B_minus(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("B-"), 2.7)

    # "Satisfactory",        2.3,    "C+",        67,    69    ))
    def test__convert_letter_to_gpa__C_plus(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("C+"), 2.3)

    # "Satisfactory",        2.0,    "C",        63,    66    ))
    def test__convert_letter_to_gpa__C(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("C"), 2.0)

    # "Satisfactory",        1.7,    "C-",        60,    62    ))
    def test__convert_letter_to_gpa__C_minus(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("C-"), 1.7)

    # "Marginal Pass",    1.3,    "D+",        57,    59    ))
    def test__convert_letter_to_gpa__D_plus(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("D+"), 1.3)

    # "Marginal Pass",    1.0,    "D",        53,    56    ))
    def test__convert_letter_to_gpa__D(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("D"), 1.0)

    # "Marginal Pass",    0.7,    "D-",        50,    52    ))
    def test__convert_letter_to_gpa__D_minus(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("D-"), 0.7)

    # "Failure",            0.0,    "F",        0,    49    ))
    def test__convert_letter_to_gpa__F(self):
        self.assertEqual(gpa_calculator.gpa_converter.getGPAforLetterGrade("F"), 0.0)

    # Invalid letter grade
    def test__convert_letter_to_gpa__X__invalid__letter_grade(self):
        self.assertTrue(math.isnan(gpa_calculator.gpa_converter.getGPAforLetterGrade("X")))

# =========================================== Objective Bullet 2 ===========================================

## 2. do the additions of grades use the lettergrade conversion functions properly?
## -> do they call the lettergrade conversion functions the appropriate number of times and with the correct parameters?

#
# 2.1 - The letter grade conversion functions are correctly called when adding grades (uses 1.1)
# Tests that the lettergrade conversion functions are called the appropriate number of times with the correct parameters when adding grades by using a mock.patch.object to replace a method to see if it was called correctly
# since we already did `getLetterForNumericGrade()` on the full range for bullet objective 1
#
class TestAddNumericGrade(unittest.TestCase):

    # Mocks that both functions (i.e. lettergrade conversion functions) when adding a grade are called properly the appropriate number of times and with the correct arguments
    @mock.patch.object(gpa_calculator.gpa_calculation_mgr.calc_manager, "addLetterGrade", autospec=True)
    @mock.patch.object(gpa_calculator.gpa_converter, "getLetterForNumericGrade", autospec=True)
    def test__add_numeric_grade__calls__get_letter_for_numeric_grade_and_add_letter_grade(self, mock_get_letter_for_numeric_grade, mock_add_letter_grade):
        numeric_grade = 88
        letter_grade = "A"
        term_name = "F21"
        # Mock the return value of the numeric grade to letter grade conversion to because it will be necessary for adding the grade
        mock_get_letter_for_numeric_grade.return_value = letter_grade

        # Create a calculation manager for a student and add a grade (note that a grade of 88% is an A)
        gpa_calc_manager = gpa_calculator.gpa_calculation_mgr.calc_manager("Mitchell Van Braeckel", 1002297)
        gpa_calc_manager.addNumericGrade(term_name, numeric_grade)

        # Check to make sure that addNumericGrade() reaches the getLetterForNumericGrade() and addLetterGrade() functions
        # such that they are each called once and with the correct arguments
        # NOTE: We use sub tests here to isolate the two assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(numeric_grade=numeric_grade):
            mock_get_letter_for_numeric_grade.assert_called_once_with(numeric_grade)
        with self.subTest(term_name=term_name, letter_grade=letter_grade):
            mock_add_letter_grade.assert_called_once_with(gpa_calc_manager, term_name, letter_grade)

    # # | `test__add_numeric_grade__calls__get_letter_for_numeric_grade` | `@mock.patch.object(gpa_calculator.gpa_converter, "getLetterForNumericGrade", autospec=True)` | `calc_manager("Mitchell Van Braeckel", 1002297)`, `addNumericGrade("F21", 88)`, `assert_called_once_with(88)` | `assert_called_once_with()` assertion passes for `getLetterForNumericGrade()` | `assert_called_once_with()` assertion passes for `getLetterForNumericGrade()` | PASS |
    # # Mocks that getLetterForNumericGrade() function (i.e. it's called for lettergrade conversion functions) when adding a grade is called properly the appropriate number of times and with the correct arguments
    # @mock.patch.object(gpa_calculator.gpa_converter, "getLetterForNumericGrade", autospec=True)
    # def test__add_numeric_grade__calls__get_letter_for_numeric_grade(self, mock_get_letter_for_numeric_grade):
    #     # Create a calculation manager for a student and add a grade (note that a grade of 88% is an A)
    #     gpa_calc_manager = gpa_calculator.gpa_calculation_mgr.calc_manager("Mitchell Van Braeckel", 1002297)
    #     gpa_calc_manager.addNumericGrade("F21", 88)

    #     # Check to make sure that addNumericGrade() reaches the getLetterForNumericGrade() function
    #     # such that it is called once and with the correct arguments
    #     mock_get_letter_for_numeric_grade.assert_called_once_with(88)

    # # | `test__add_numeric_grade__calls__add_letter_grade` | `@mock.patch.object(gpa_calculator.gpa_calculation_mgr.calc_manager, "addLetterGrade", autospec=True)` | `calc_manager("Mitchell Van Braeckel", 1002297)`, `addNumericGrade("F21", 88)`, `assert_called_once_with(gpa_calc_manager, "F21", "A")` | `assert_called_once_with()` assertion passes for `addLetterGrade()` | `assert_called_once_with()` assertion passes for `addLetterGrade()` | PASS |
    # # Mocks that addLetterGrade() function (i.e. it's called for lettergrade conversion functions) when adding a grade is called properly the appropriate number of times and with the correct arguments
    # @mock.patch.object(gpa_calculator.gpa_calculation_mgr.calc_manager, "addLetterGrade", autospec=True)
    # def test__add_numeric_grade__calls__add_letter_grade(self, mock_add_letter_grade):
    #     # Create a calculation manager for a student and add a grade (note that a grade of 88% is an A)
    #     gpa_calc_manager = gpa_calculator.gpa_calculation_mgr.calc_manager("Mitchell Van Braeckel", 1002297)
    #     gpa_calc_manager.addNumericGrade("F21", 88)

    #     # Check to make sure that addNumericGrade() reaches the addLetterGrade() function
    #     # such that it is called once and with the correct arguments
    #     mock_add_letter_grade.assert_called_once_with(gpa_calc_manager, "F21", "A")

# =========================================== Objective Bullet 3 ===========================================

## 3. do the term objects get created and cleaned up properly?
## -> are the right grades placed in the terms?
## -> does term removal operate correctly?

#
# 3.1 - In order to test if term objects are created properly, we need to first verify that `addTerm()` is working correctly before testing `addLetterGrade()`
# which also covers part of verifying that the right grades are placed in the terms
# -> i.e. The creation of term objects occurs properly
# Tests that adding a term to a term list works correctly
#
class TestAddTerm(unittest.TestCase):
    def setUp(self):
        # Create an empty term list, an empty term info, and declare the term name that will be used
        self.term_name = "F21"
        self.term_list = gpa_calculator.gpa_term_info.TermList(gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_TERMS_PER_STUDENT, gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM)
        self.empty_term_info = gpa_calculator.gpa_term_info.TermInfo("", gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM)

    def test__add_term__adds_term_to_term_list(self):
        # Add a term to the term list
        added_term_info = self.term_list.addTerm(self.term_name)

        # Calculate new number of terms in the term list and retrieve the added term's name
        num_terms = len(self.term_list.dict)
        added_term_name = self.term_list.dict.get(self.term_name, self.empty_term_info).termName

        # Check that the number of terms is correct and the added term info's term name is as expected after adding a term
        # NOTE: We use sub tests here to isolate the two assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(num_terms=num_terms):
            self.assertEqual(num_terms, 1)
        with self.subTest(added_term_name=added_term_name):
            self.assertEqual(added_term_name, self.term_name)

    def test__add_term__adds_multiple_terms_to_term_list(self):
        w22_term_name = "W22"
        # Add the two terms to the term list
        added_term_info1 = self.term_list.addTerm(self.term_name)
        added_term_info2 = self.term_list.addTerm(w22_term_name)

        # Calculate new number of terms in the term list and retrieve the added terms' name
        num_terms = len(self.term_list.dict)
        added_term_name1 = self.term_list.dict.get(self.term_name, self.empty_term_info).termName
        added_term_name2 = self.term_list.dict.get(w22_term_name, self.empty_term_info).termName

        # Check that the number of terms is correct and the added term infos' term names are as expected after adding a term
        # NOTE: We use sub tests here to isolate the three assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(num_terms=num_terms):
            self.assertEqual(num_terms, 2)
        with self.subTest(added_term_name=added_term_name1):
            self.assertEqual(added_term_name1, self.term_name)
        with self.subTest(added_term_name=added_term_name2):
            self.assertEqual(added_term_name2, w22_term_name)

    def test__add_term__adds_multiple_terms_with_same_term_name_to_term_list(self):
        # Add the same term twice to the term list
        added_term_info1 = self.term_list.addTerm(self.term_name)
        added_term_info2 = self.term_list.addTerm(self.term_name)

        # Calculate new number of terms in the term list
        num_terms = len(self.term_list.dict)

        # Check that the number of terms is correct after adding a term
        self.assertEqual(num_terms, 1)

    def test__add_term__does_not_add_more_than_max_terms_per_student(self):
        # Create a list of 33 (note: 32 is max terms per student) term info objects to be added to the term list
        added_term_info_list = []
        for i in range(gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_TERMS_PER_STUDENT + 1):
            added_term_info_list.append(self.term_list.addTerm(f"{i}"))

        # Calculate new number of terms in the term list and retrieve the added term's name
        num_terms = len(self.term_list.dict)
        over_max_added_term_info = added_term_info_list[gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_TERMS_PER_STUDENT]

        # Check that the number of terms is correct (i.e. 32 is max) and the 33rd term attempted to be added did not work such that `addTerm()` returned None
        # NOTE: We use sub tests here to isolate the two assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(num_terms=num_terms):
            self.assertEqual(num_terms, gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_TERMS_PER_STUDENT)
        with self.subTest(over_max_added_term_info=over_max_added_term_info):
            self.assertIsNone(over_max_added_term_info)

#
# 3.2 - In order to test if the right grades are placed in the terms, we need to first verify that `getTerm()` is working correctly before testing `addLetterGrade()`
# -> i.e. The retrieval of terms occurs properly
# Tests that getting a term from a term list works correctly
#
class TestGetTerm(unittest.TestCase):
    def setUp(self):
        # Create an empty term list, and declare the term name that will be used
        self.term_name = "F21"
        self.term_list = gpa_calculator.gpa_term_info.TermList(gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_TERMS_PER_STUDENT, gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM)

    def test__get_term__retrieves_term_in_term_list(self):
        # Add a term to the term list
        added_term_info = self.term_list.addTerm(self.term_name)

        # Get the term from the term list
        retrieved_term_info = self.term_list.getTerm(self.term_name)

        # Check that the retrieve term info matches what we expected after
        self.assertEqual(retrieved_term_info, added_term_info)

    def test__get_term__retrieves_term_in_term_list_when_multiple_terms_are_added(self):
        w22_term_name = "W22"
        # Add a term to the term list
        added_term_info1 = self.term_list.addTerm(self.term_name)
        added_term_info2 = self.term_list.addTerm(w22_term_name)

        # Get the term from the term list
        retrieved_term_info1 = self.term_list.getTerm(self.term_name)
        retrieved_term_info2 = self.term_list.getTerm(w22_term_name)

        # Check that retrieve term info's term name is as expected after getting a term
        # NOTE: We use sub tests here to isolate the two assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(retrieved_term_info=retrieved_term_info1, added_term_info=added_term_info1):
            self.assertEqual(retrieved_term_info1, added_term_info1)
        with self.subTest(retrieved_term_info=retrieved_term_info2, added_term_info=added_term_info2):
            self.assertEqual(retrieved_term_info2, added_term_info2)

    def test__get_term__does_not_retrieve_term_not_in_term_list(self):
        # Attempt to get a term from an empty term list
        retrieved_term_info = self.term_list.getTerm(self.term_name)

        # Check that the retrieved term info is none
        self.assertIsNone(retrieved_term_info)

#
# 3.3 - In order to test if the right grades are placed in the terms, we need to first verify that `addGrade()` is working correctly before testing `addLetterGrade()`
# -> i.e. All letter grades (A+ through F) can be properly added to a term info
# Tests that adding a grade to a term info works correctly
#
class TestAddGrade(unittest.TestCase):
    def setUp(self):
        # Create a term info, and declare the term name that will be used
        self.term_name = "F21"
        self.term_info = gpa_calculator.gpa_term_info.TermInfo(self.term_name, gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM)

    def test__add_grade__A_plus(self):
        self.term_info.addGrade("A+")
        self.assertEqual(self.term_info.getGrades(), ["A+"])

    def test__add_grade__A(self):
        self.term_info.addGrade("A")
        self.assertEqual(self.term_info.getGrades(), ["A"])

    def test__add_grade__A_minus(self):
        self.term_info.addGrade("A-")
        self.assertEqual(self.term_info.getGrades(), ["A-"])

    def test__add_grade__B_plus(self):
        self.term_info.addGrade("B+")
        self.assertEqual(self.term_info.getGrades(), ["B+"])

    def test__add_grade__B(self):
        self.term_info.addGrade("B")
        self.assertEqual(self.term_info.getGrades(), ["B"])

    def test__add_grade__B_minus(self):
        self.term_info.addGrade("B-")
        self.assertEqual(self.term_info.getGrades(), ["B-"])

    def test__add_grade__C_plus(self):
        self.term_info.addGrade("C+")
        self.assertEqual(self.term_info.getGrades(), ["C+"])

    def test__add_grade__C(self):
        self.term_info.addGrade("C")
        self.assertEqual(self.term_info.getGrades(), ["C"])

    def test__add_grade__C_minus(self):
        self.term_info.addGrade("C-")
        self.assertEqual(self.term_info.getGrades(), ["C-"])

    def test__add_grade__D_plus(self):
        self.term_info.addGrade("D+")
        self.assertEqual(self.term_info.getGrades(), ["D+"])

    def test__add_grade__D(self):
        self.term_info.addGrade("D")
        self.assertEqual(self.term_info.getGrades(), ["D"])

    def test__add_grade__D_minus(self):
        self.term_info.addGrade("D-")
        self.assertEqual(self.term_info.getGrades(), ["D-"])

    def test__add_grade__F(self):
        self.term_info.addGrade("F")
        self.assertEqual(self.term_info.getGrades(), ["F"])

    def test__add_grade__adds_multiple_grades_to_term_info(self):
        letter_grade1 = "A"
        letter_grade2 = "B+"
        # Add two grades to the term info
        added_grade_result1 = self.term_info.addGrade(letter_grade1)
        added_grade_result2 = self.term_info.addGrade(letter_grade2)

        # Check the grades added to the term info
        term_info_grades = self.term_info.getGrades()
        num_grades = len(term_info_grades)

        # Check that the number of grades is correct and the added grades are as expected after adding them such that the return values are also true
        # NOTE: We use sub tests here to isolate the five assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(num_grades=num_grades):
            self.assertEqual(num_grades, 2)
        with self.subTest(added_grade_result1=added_grade_result1):
            self.assertTrue(added_grade_result1)
        with self.subTest(added_grade_result2=added_grade_result2):
            self.assertTrue(added_grade_result2)
        with self.subTest(letter_grade1=letter_grade1, term_info_grades=term_info_grades):
            self.assertIn(letter_grade1, term_info_grades)
        with self.subTest(letter_grade2=letter_grade2, term_info_grades=term_info_grades):
            self.assertIn(letter_grade2, term_info_grades)

    def test__add_grade__does_not_add_more_than_max_courses_per_term(self):
        # Create a list of 7 (note: 6 is max courses/grades per term) grades' return values after adding grades to the term info
        added_grade_list_return_values = []
        for i in range(gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM + 1):
            added_grade_list_return_values.append(self.term_info.addGrade("B"))

        # Check the grades added to the term info
        term_info_grades = self.term_info.getGrades()
        num_grades = len(term_info_grades)
        over_max_added_grades_return_value = added_grade_list_return_values[gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM]

        # Check that the number of grades is correct (i.e. 6 is max) and the 7th grade attempted to be added did not work such that `addGrade()` returned false
        # NOTE: We use sub tests here to isolate the two assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(num_grades=num_grades):
            self.assertEqual(num_grades, gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM)
        with self.subTest(over_max_added_grades_return_value=over_max_added_grades_return_value):
            self.assertFalse(over_max_added_grades_return_value)

#
# 3.4 - Adding grades to terms properly creates terms and adds the right grades to the right terms (uses 3.1, 3.2, 3.3)
# Tests adding letter grades properly create term objects
# -> Tests 2 mocks (if statement accounted for whether the term already existed or not), and 1 functional integration test
#
class TestAddLetterGrade(unittest.TestCase):
    def setUp(self):
        # Create a GPA calculation manager for a student, term info, and declares the term name that will be used
        self.term_name = "F21"
        self.gpa_calc_manager = gpa_calculator.gpa_calculation_mgr.calc_manager("Mitchell Van Braeckel", 1002297)
        self.term_info = gpa_calculator.gpa_term_info.TermInfo(self.term_name, gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM)

    # Mocks that the `addGrade()`, `getTerm()`, `addTerm()` functions are called properly the appropriate number of times and with the correct arguments
    # since we have already confirmed that each of these functions work correctly (for when the term a grade is being added to does not exist yet)
    @mock.patch.object(gpa_calculator.gpa_term_info.TermInfo, 'addGrade', autospec=True)
    @mock.patch.object(gpa_calculator.gpa_term_info.TermList, 'addTerm', autospec=True)
    @mock.patch.object(gpa_calculator.gpa_term_info.TermList, 'getTerm', autospec=True)
    def test__add_letter_grade__when_term_does_not_exist_yet__calls_get_term_and_add_term_and_add_grade(self, mock_get_term, mock_add_term, mock_add_grade):
        mock_get_term.return_value = None # Mock that the term being added to does not exist yet in the term list
        mock_add_term.return_value = self.term_info

        # Add a grade
        letter_grade = "A"
        self.gpa_calc_manager.addLetterGrade(self.term_name, letter_grade)

        # Check to make sure that addLetterGrade() reaches the getTerm(), addTerm(), and addGrade() functions
        # such that they are each called once and with the correct arguments
        # NOTE: We use sub tests here to isolate the three assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(gpa_calc_manager=self.gpa_calc_manager, term_name=self.term_name):
            mock_get_term.assert_called_once_with(self.gpa_calc_manager.terms, self.term_name)
        with self.subTest(gpa_calc_manager=self.gpa_calc_manager, term_name=self.term_name):
            mock_add_term.assert_called_once_with(self.gpa_calc_manager.terms, self.term_name)
        with self.subTest(term_info=self.term_info, term_name=self.term_name):
            mock_add_grade.assert_called_once_with(self.term_info, letter_grade)

    # Mocks that the `addGrade()`, `getTerm()`, `addTerm()` functions are called properly the appropriate number of times and with the correct arguments
    # since we have already confirmed that each of these functions work correctly (for when the term a grade is being added to already exists)
    @mock.patch.object(gpa_calculator.gpa_term_info.TermInfo, 'addGrade', autospec=True)
    @mock.patch.object(gpa_calculator.gpa_term_info.TermList, 'addTerm', autospec=True)
    @mock.patch.object(gpa_calculator.gpa_term_info.TermList, 'getTerm', autospec=True)
    def test__add_letter_grade__when_term_already_exists__calls_get_term_and_add_grade(self, mock_get_term, mock_add_term, mock_add_grade):
        mock_get_term.return_value = self.term_info # Mock that the term being added to already exists in the term list, so addTerm() won't be called

        # Add a grade
        letter_grade = "A"
        self.gpa_calc_manager.addLetterGrade(self.term_name, letter_grade)

        # Check to make sure that addLetterGrade() reaches the getTerm(), addTerm(), and addGrade() functions
        # such that they are each called once and with the correct arguments
        # NOTE: We use sub tests here to isolate the three assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(gpa_calc_manager=self.gpa_calc_manager, term_name=self.term_name):
            mock_get_term.assert_called_once_with(self.gpa_calc_manager.terms, self.term_name)
        with self.subTest():
            mock_add_term.assert_not_called()
        with self.subTest(term_info=self.term_info, term_name=self.term_name):
            mock_add_grade.assert_called_once_with(self.term_info, letter_grade)

    # This represents an integration test to verify that functionality is correct when adding grades to terms
    def test__add_letter_grade__to_multiple_terms(self):
        # Add two grades to one term, and one grade to another
        w22_term_name = "W22"
        letter_grade1 = "A"
        letter_grade2 = "B"
        letter_grade3 = "C"
        self.gpa_calc_manager.addLetterGrade(self.term_name, letter_grade1)
        self.gpa_calc_manager.addLetterGrade(self.term_name, letter_grade2)
        self.gpa_calc_manager.addLetterGrade(w22_term_name, letter_grade3)

        # Get the grades for each term
        term_grades_list1 = self.gpa_calc_manager.terms.getTerm(self.term_name).getGrades()
        term_grades_list2 = self.gpa_calc_manager.terms.getTerm(w22_term_name).getGrades()

        # Check to make sure that a term was created correctly and contains the two expected grades, while the other term is also properly created and contains the one expected grade
        # NOTE: We use sub tests here to isolate the three assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest(term_grades_list1=term_grades_list1, letter_grade1=letter_grade1, letter_grade2=letter_grade2):
            self.assertEqual(term_grades_list1, [letter_grade1, letter_grade2])
        with self.subTest(term_grades_list2=term_grades_list2, letter_grade3=letter_grade3):
            self.assertEqual(term_grades_list2, [letter_grade3])

#
# 3.5 - In order to test if term objects are cleaned up properly, we need to first verify that `removeTerm()` is working correctly before testing `removeInfoForTerm()`
# which also covers verifying that term removal operates correctly
# -> i.e. The removal of a term occurs properly such that term removal operates correctly for `removeTerm()`
# Tests that removing a term info works correctly
#
class TestRemoveTerm(unittest.TestCase):
    def setUp(self):
        # Create an empty term list, and declare the term name that will be used
        self.term_name = "F21"
        self.term_list = gpa_calculator.gpa_term_info.TermList(gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_TERMS_PER_STUDENT, gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM)

    def test__remove_term__removes_term_from_term_list(self):
        # Add a term to the term list
        added_term_info = self.term_list.addTerm(self.term_name)

        # Remove the term from the term list
        retrieved_term_info = self.term_list.removeTerm(self.term_name)

        # Check that the term is no longer in the term list
        self.assertIsNone(self.term_list.getTerm(self.term_name))

    def test__remove_term__removes_term_from_term_list_when_multiple_terms_are_added(self):
        w22_term_name = "W22"
        # Add a term to the term list
        added_term_info1 = self.term_list.addTerm(self.term_name)
        added_term_info2 = self.term_list.addTerm(w22_term_name)

        # Remove the term from the term list
        retrieved_term_info1 = self.term_list.removeTerm(self.term_name)

        # Check that the term is no longer in the term list while the other is still present
        # NOTE: We use sub tests here to isolate the two assertion tests as units that are not directly dependent on each other such that
        # each is independent and will run regardless of any previous failures
        with self.subTest():
            self.assertIsNone(self.term_list.getTerm(self.term_name))
        with self.subTest():
            self.assertEqual(self.term_list.getTerm(w22_term_name), added_term_info2)

    def test__remove_term__works_correctly_if_term_name_not_in_term_list(self):
        # Remove a term from the term list that does not exist
        retrieved_term_info = self.term_list.removeTerm(self.term_name)

        # Check that the term is no longer in the term list
        self.assertIsNone(self.term_list.getTerm(self.term_name))

#
# 3.6 - Term objects are cleaned up properly when removing terms such that term removal operates correctly for `removeInfoForTerm()` (uses 3.5)
# Tests that removing an entire term works correctly
#
class TestRemoveInfoForTerm(unittest.TestCase):
    def setUp(self):
        # Create a GPA calculation manager for a student, term info, and declares the term name that will be used
        self.term_name = "F21"
        self.gpa_calc_manager = gpa_calculator.gpa_calculation_mgr.calc_manager("Mitchell Van Braeckel", 1002297)
        self.term_info = gpa_calculator.gpa_term_info.TermInfo(self.term_name, gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM)

    # Mocks that the `removeTerm()` function is called properly the appropriate number of times and with the correct arguments
    # since we have already confirmed that `removeTerm()` functions correctly and removes a term
    @mock.patch.object(gpa_calculator.gpa_term_info.TermList, "removeTerm", autospec=True)
    def test__remove_info_for_term__calls_remove_term(self, mock_remove_term):
        # # We don't need to because we are mocking it, but we could add a grade
        # letter_grade = "A"
        # self.gpa_calc_manager.addLetterGrade(self.term_name, letter_grade)

        # Remove the entire term
        self.gpa_calc_manager.removeInfoForTerm(self.term_name)

        # Check to make sure that removeInfoForTerm() reaches the removeTerm() function
        # such that it is called once and with the correct arguments
        mock_remove_term.assert_called_once_with(self.gpa_calc_manager.terms, self.term_name)

if __name__ == '__main__':
    unittest.main()
