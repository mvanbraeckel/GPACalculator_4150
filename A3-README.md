# GPACalculator_4150
(Software Reliability and Testing course A3)

Please see my `A3-README.md` for my A3 instructions (uses A1 and A2, with replaced code as instructed by professor). Please also note that you may need to make the bash scripts executables again after unzipping.

Note that all tests are in the same `runtests.py` file. However, classes have been created appropriately to align with the outlined design below. To run all tests, simply do `python3 runtests.py` or `py runtests.py` while in the correct `python-GPA-calculator` directory.

---

## A3 Instructions

We wish to write tests to verify whether the following functionality is correct:

- do the lettergrades function correctly over their entire range?
  - for each of A+ through F work on their full range
- do the additions of grades use the lettergrade conversion functions properly?
  - do they call the lettergrade conversion functions the appropriate number of times and with the correct parameters?
- do the term objects get created and cleaned up properly?
  - are the right grades placed in the terms?
  - does term removal operate correctly?

### Test Case Design Instructions

- what the test case will verify
- whether mocks are used, and if so, how
- what supplied arguments will be provided, and to which functions
- what expected values will be observed
- (based on the results below) whether the test passes

## Objectives

Note that this test design follows a 'leaf' mocking structure where the lowest level function(s) are unit tested to confirm they work properly, while higher level functions reference this and mock those lower level functions to verify they are called the appropriate number of times and with the correct parameters. The higher level functions may also have an integration test for completeness as necessary where the lower level function(s) are not mocked. Any times where a function is used instead of a fake, stub, or mock, it has already been verified by a unit test suite and/or has been confirmed to be a primitive level function without logical branching etc. (eg. such as a simple get).

### Objective Bullet 1

The following test cases are designed to test *bullet objective 1*: Do the lettergrades function correctly over their entire range, such that for each of A+ through F works properly on their full range. This is accomplished by calling `getLetterForNumericGrade()` over its entire full range of A+ through F for low, mid, and high values (0-100, but also include invalid values below 0 and above 100 to show it's handled appropriately). In addition, we also test `getGPAforLetterGrade()` for all letters (A+ through F) to verify the lettergrades function properly over their entire range in terms of calculating their respective GPA values (also include an invalid grade letter such as X to show it's handled appropriately).

#### **Test Case Set 1.1 Description** - `getLetterForNumericGrade()`

These test cases will verify the full range of numeric grades (0-100 inclusive) with respect to their corresponding letter grades (F through A+) correctly function when converted. Note that this is very similar to the tests we wrote for A1. We have also included tests for invalid numeric grades that are outside of the range (i.e. 101 and -1).

- `getLetterForNumericGrade()` - full range (+, normal, - | low, mid, high bounds | -1, 101)

| Test Name | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| `test__letter_for_numeric_grade__101percent__invalid__high` | No mocks used | `getLetterForNumericGrade(101)` | None | None  | PASS |
| `test__letter_for_numeric_grade__100percent__A_plus__high` | No mocks used | `getLetterForNumericGrade(100)` | A+ | A+  | PASS |
| `test__letter_for_numeric_grade__095percent__A_plus__midrange` | No mocks used | `getLetterForNumericGrade(95)` | A+ | A+ | PASS |
| `test__letter_for_numeric_grade__090percent__A_plus__low` | No mocks used | `getLetterForNumericGrade(90)` | A+ | A+ | PASS |
| `test__letter_for_numeric_grade__089percent__A__high` | No mocks used | `getLetterForNumericGrade(89)` | A | A | PASS |
| `test__letter_for_numeric_grade__087percent__A__midrange` | No mocks used | `getLetterForNumericGrade(87)` | A | A | PASS |
| `test__letter_for_numeric_grade__085percent__A__low` | No mocks used | `getLetterForNumericGrade(85)` | A | A | PASS |
| `test__letter_for_numeric_grade__084percent__A_minus__high` | No mocks used | `getLetterForNumericGrade(85)` | A- | A- | PASS |
| `test__letter_for_numeric_grade__082percent__A_minus__midrange` | No mocks used | `getLetterForNumericGrade(82)` | A- | A- | PASS |
| `test__letter_for_numeric_grade__080percent__A_minus__low` | No mocks used | `getLetterForNumericGrade(80)` | A- | A- | PASS |
| `test__letter_for_numeric_grade__079percent__B_plus__high` | No mocks used | `getLetterForNumericGrade(79)` | B+ | B+ | PASS |
| `test__letter_for_numeric_grade__078percent__B_plus__midrange` | No mocks used | `getLetterForNumericGrade(78)` | B+ | B+ | PASS |
| `test__letter_for_numeric_grade__077percent__B_plus__low` | No mocks used | `getLetterForNumericGrade(77)` | B+ | B+ | PASS |
| `test__letter_for_numeric_grade__076percent__B__high` | No mocks used | `getLetterForNumericGrade(76)` | B | B | PASS |
| `test__letter_for_numeric_grade__075percent__B__midrange` | No mocks used | `getLetterForNumericGrade(75)` | B | B | PASS |
| `test__letter_for_numeric_grade__073percent__B__low` | No mocks used | `getLetterForNumericGrade(73)` | B | B | PASS |
| `test__letter_for_numeric_grade__072percent__B_minus__high` | No mocks used | `getLetterForNumericGrade(72)` | B- | B- | PASS |
| `test__letter_for_numeric_grade__071percent__B_minus__midrange` | No mocks used | `getLetterForNumericGrade(71)` | B- | B- | PASS |
| `test__letter_for_numeric_grade__070percent__B_minus__low` | No mocks used | `getLetterForNumericGrade(70)` | B- | B- | PASS |
| `test__letter_for_numeric_grade__069percent__C_plus__high` | No mocks used | `getLetterForNumericGrade(69)` | C+ | C+ | PASS |
| `test__letter_for_numeric_grade__068percent__C_plus__midrange` | No mocks used | `getLetterForNumericGrade(68)` | C+ | C+ | PASS |
| `test__letter_for_numeric_grade__067percent__C_plus__low` | No mocks used | `getLetterForNumericGrade(67)` | C+ | C+ | PASS |
| `test__letter_for_numeric_grade__066percent__C__high` | No mocks used | `getLetterForNumericGrade(66)` | C | C | PASS |
| `test__letter_for_numeric_grade__065percent__C__midrange` | No mocks used | `getLetterForNumericGrade(65)` | C | C | PASS |
| `test__letter_for_numeric_grade__063percent__C__low` | No mocks used | `getLetterForNumericGrade(63)` | C | C | PASS |
| `test__letter_for_numeric_grade__062percent__C_minus__high` | No mocks used | `getLetterForNumericGrade(62)` | C- | C- | PASS |
| `test__letter_for_numeric_grade__061percent__C_minus__midrange` | No mocks used | `getLetterForNumericGrade(61)` | C- | C- | PASS |
| `test__letter_for_numeric_grade__060percent__C_minus__low` | No mocks used | `getLetterForNumericGrade(60)` | C- | C- | PASS |
| `test__letter_for_numeric_grade__059percent__D_plus__high` | No mocks used | `getLetterForNumericGrade(59)` | D+ | D+ | PASS |
| `test__letter_for_numeric_grade__058percent__D_plus__midrange` | No mocks used | `getLetterForNumericGrade(58)` | D+ | D+ | PASS |
| `test__letter_for_numeric_grade__057percent__D_plus__low` | No mocks used | `getLetterForNumericGrade(57)` | D+ | D+ | PASS |
| `test__letter_for_numeric_grade__056percent__D__high` | No mocks used | `getLetterForNumericGrade(56)` | D | D | PASS |
| `test__letter_for_numeric_grade__055percent__D__midrange` | No mocks used | `getLetterForNumericGrade(55)` | D | D | PASS |
| `test__letter_for_numeric_grade__053percent__D__low` | No mocks used | `getLetterForNumericGrade(53)` | D | D | PASS |
| `test__letter_for_numeric_grade__052percent__D_minus__high` | No mocks used | `getLetterForNumericGrade(52)` | D- | D- | PASS |
| `test__letter_for_numeric_grade__051percent__D_minus__midrange` | No mocks used | `getLetterForNumericGrade(51)` | D- | D- | PASS |
| `test__letter_for_numeric_grade__050percent__D_minus__low` | No mocks used | `getLetterForNumericGrade(50)` | D- | D- | PASS |
| `test__letter_for_numeric_grade__049percent__F__high` | No mocks used | `getLetterForNumericGrade(49)` | F | F | PASS |
| `test__letter_for_numeric_grade__025percent__F__midrange` | No mocks used | `getLetterForNumericGrade(25)` | F | F | PASS |
| `test__letter_for_numeric_grade__000percent__F__low` | No mocks used | `getLetterForNumericGrade(0)` | F | F | PASS |
| `test__letter_for_numeric_grade__negative_one_percent__invalid__low` | No mocks used | `getLetterForNumericGrade` | None | None  | PASS |

#### **Test Case Set 1.2 Description** - `getGPAforLetterGrade()`

These test cases will verify the full range of letter grades (A+ through F) function correctly with respect to converting a letter to its appropriate GPA value. Note that according to the official GPA calculator as indicated by the University of Guelph (https://www.uoguelph.ca/uaic/faq/grades/how-do-i-calculate-gpa-using-my-guelph-grades -> https://www.whatsmygpa.ca/), it shows that the UoG GPA operates on an official 4.0 scale; however, this GPA calculator code tries to calculate on a 4.3 GPA scale (eg. see Outstanding A+ of 90-100% is evaluated as 4.3 GPA value incorrectly), which would explain the expected value for a letter grade of A+ below.

- `getGPAforLetterGrade()` - all letters (include invalid letter grade) get evaluated to the official correct GPA value

| Test Case | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| `test__gpa_for_letter_grade__A_plus` | No mocks Used | `getGPAforLetterGrade("A+")` | 4.0 | 4.3 | FAIL |
| `test__gpa_for_letter_grade__A` | No mocks Used | `getGPAforLetterGrade("A")` | 4.0 | 4.0 | PASS |
| `test__gpa_for_letter_grade__A_minus` | No mocks Used | `getGPAforLetterGrade("A-")` | 3.7 | 3.7 | PASS |
| `test__gpa_for_letter_grade__B_plus` | No mocks Used | `getGPAforLetterGrade("B+")` | 3.3 | 3.3 | PASS |
| `test__gpa_for_letter_grade__B` | No mocks Used | `getGPAforLetterGrade("B")` | 3.0 | 3.0 | PASS |
| `test__gpa_for_letter_grade__B_minus` | No mocks Used | `getGPAforLetterGrade("B-")` | 2.7 | 2.7 | PASS |
| `test__gpa_for_letter_grade__C_plus` | No mocks Used | `getGPAforLetterGrade("C+")` | 2.3 | 2.3 | PASS |
| `test__gpa_for_letter_grade__C` | No mocks Used | `getGPAforLetterGrade("C")` | 2.0 | 2.0 | PASS |
| `test__gpa_for_letter_grade__C_minus` | No mocks Used | `getGPAforLetterGrade("C-")` | 1.7 | 1.7 | PASS |
| `test__gpa_for_letter_grade__D_plus` | No mocks Used | `getGPAforLetterGrade("D+")` | 1.3 | 1.3 | PASS |
| `test__gpa_for_letter_grade__D` | No mocks Used | `getGPAforLetterGrade("D")` | 1.0 | 1.0 | PASS |
| `test__gpa_for_letter_grade__D_minus` | No mocks Used | `getGPAforLetterGrade("D-")` | 0.7 | 0.7 | PASS |
| `test__gpa_for_letter_grade__F` | No mocks Used | `getGPAforLetterGrade("F")` | 0.0 | 0.0 | PASS |
| `test__gpa_for_letter_grade__X__invalid__letter_grade` | No mocks Used | `getGPAforLetterGrade("X")` | NaN | NaN | PASS |

### Objective Bullet 2

### **Test Case Set 2.1 Description** - `addNumericGrade()` calls `getLetterForNumericGrade()` and `addLetterGrade()`

The following test cases are designed to test *bullet objective 2*: Do the additions of grades use the lettergrade conversion functions properly such that they also call the lettergrade conversion functions the appropriate number of times with the correct parameters. This is accomplished by calling `getLetterForNumericGrade()` over the entire range (for each of A+ through F on their full range of 0-100 inclusively including what happens for values outside this valid numerical range) and using mocks to verify that `addNumericGrade()` calls `getLetterForNumericGrade()` and `addLetterGrade()` are each called once with the correct parameters.

- Since we already did `getLetterForNumericGrade()` on the full range for bullet objective 1, our test cases listed here mock `getLetterForNumericGrade()` and `addLetterGrade()` such that the mocked functions are called correct number of times once and with the proper parameters when calling `addNumericGrade()`.
- We use sub tests here to isolate the two assertions as units that are not directly dependent on each other such that each is independent and will run regardless of any previous failures (in reference to table rows with multiple expected/actual values)

| Test Case | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| `test__add_numeric_grade__calls__get_letter_for_numeric_grade_and_add_letter_grade` | `@mock.patch.object(gpa_calculator.gpa_calculation_mgr.calc_manager, "addLetterGrade", autospec=True)` & `@mock.patch.object(gpa_calculator.gpa_converter, "getLetterForNumericGrade", autospec=True)` - used to verify that the mocked functions are each called once with the correct parameters when `addNumericGrade()` is called | `calc_manager("Mitchell Van Braeckel", 1002297)`, `addNumericGrade("F21", 88)`, `mock_get_letter_for_numeric_grade.assert_called_once_with(88)`, `mock_add_letter_grade.assert_called_once_with(gpa_calc_manager, "F21", "A")` | Both `assert_called_once_with()` assertions (as sub tests) pass for `getLetterForNumericGrade()` and `addLetterGrade()` because both mocked functions are called correct number of times once and with the proper parameters when calling `addNumericGrade()` (where the numeric grade is 88, the respective letter grade is A, and the term name is F21) | Both `assert_called_once_with()` assertions (as sub tests) pass for `getLetterForNumericGrade()` and `addLetterGrade()` because both mocked functions are called correct number of times once and with the proper parameters when calling `addNumericGrade()` (where the numeric grade is 88, the respective letter grade is A, and the term name is F21) | PASS |

### Objective Bullet 3

The following test cases are designed to test *bullet objective 3*: Do the term objects get created and cleaned up properly such that the right grades are placed in the right terms and term removal operates correctly (by removing the correct term). **This is accomplished by ...** first verifying that each of the underlying functions work correctly (i.e. `addTerm()`, `getTerm()`, `addGrade()`, `removeTerm()`). Afterwards, we can then verify the higher level functions work correctly (i.e. `addLetterGrade()`, `removeInfoForTerm()`).

### **Test Case Set 3.1 Description** - `addTerm()`

In order to test if term objects are created properly, we need to first verify that `addTerm()` is working correctly before testing `addLetterGrade()`. These tests cover part of our objective bullet 3 to verify that the right grades are placed in the correct terms (i.e. the creation of term objects occurs properly). These test cases verify that adding a term to a term list functions correctly.

- Note that we use a `setUp()` to declare a term name (`self.term_name = "F21"`, but since it's easy to do, I replaced these in the 'Functions and Supplied Args' column of the table), initialize an empty term list (`self.term_list`), and initialize an empty term info (`self.empty_term_info`) to use as a default value in a certain case
- We use sub tests here to isolate the multiple assertions as units that are not directly dependent on each other such that each is independent and will run regardless of any previous failures (in reference to table rows with multiple expected/actual values)

| Test Case | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| `test__add_term__adds_term_to_term_list` | No mocks used | `addTerm("F21")`, `len(self.term_list.dict)`, `self.term_list.dict.get("F21", self.empty_term_info).termName` | 1 term in the term list, and the term name that was added is F21 | 1 term in the term list, and the term name that was added is F21 | PASS |
| `test__add_term__adds_multiple_terms_to_term_list` | No mocks used | `addTerm("F21")`, `addTerm("W22")`, `len(self.term_list.dict)`, `self.term_list.dict.get("F21", self.empty_term_info).termName`, `self.term_list.dict.get("W22", self.empty_term_info).termName` | 2 terms in the term list, and the term names added are F21 and W22 | 2 terms in the term list, and the term names added are F21 and W22 | PASS |
| `test__add_term__adds_multiple_terms_with_same_term_name_to_term_list` | No mocks used | `addTerm("F21")`, `addTerm("F21")`, `len(self.term_list.dict)` | 1 term in the term list | 1 term in the term list | PASS |
| `test__add_term__does_not_add_more_than_max_terms_per_student` | No mocks used | `added_term_info_list.append(self.term_list.addTerm(f"{i}"))`, `len(self.term_list.dict)`, `added_term_info_list[gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_TERMS_PER_STUDENT]` | 32 terms in the term list, and the return value of attempting to add a 33rd term is None | 32 terms in the term list, and the return value of attempting to add a 33rd term is None | PASS |

Additional Test Description Info:

- `test__add_term__adds_multiple_terms_to_term_list` - in this test, we add two terms to the term list and verify that the two terms were both created and added correctly as we expect.
- `test__add_term__adds_multiple_terms_with_same_term_name_to_term_list` - in this test, we add the same term twice to the term list and verify that only 1 term is in the term list since we can't have duplicate term names.
- `test__add_term__does_not_add_more_than_max_terms_per_student` - in this test, we use a loop to attempt to add 33 terms for a single student, where we expect only 32 to be successfully added because that is the max per student. Therefore, we expect the 33rd term's result when we try to add it to be `None`.

### **Test Case Set 3.2 Description** - `getTerm()`

In order to test if the right grades are placed in the terms, we need to first verify that `getTerm()` is working correctly before testing `addLetterGrade()`. These tests cover part of our objective bullet 3 to verify that the right grades are placed in the correct terms (i.e. the creation of term objects occurs properly because the retrieval of terms occurs during these operations). These test cases verify that getting a term from a term list works correctly.

- Note that we use a `setUp()` to declare a term name (`self.term_name = "F21"`, but since it's easy to do, I replaced these in the 'Functions and Supplied Args' column of the table) and initialize an empty term list (`self.term_list`)
- We use sub tests here to isolate the multiple assertions as units that are not directly dependent on each other such that each is independent and will run regardless of any previous failures (in reference to table rows with multiple expected/actual values)

| Test Case | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| `test__get_term__retrieves_term_in_term_list` | No mocks used | `addTerm("F21")`, `getTerm("F21")` | The retrieved term info matches what we expected after adding a new term to the term list | The retrieved term info matches what we expected after adding a new term to the term list | PASS |
| `test__get_term__retrieves_term_in_term_list_when_multiple_terms_are_added` | No mocks used | `addTerm("F21")`, `addTerm("W22")`, `getTerm("F21")`, `getTerm("W22")` | Both retrieved term infos match what we expected after adding new terms to the term list | Both retrieved term infos match what we expected after adding new terms to the term list | PASS |
| `test__get_term__does_not_retrieve_term_not_in_term_list` | No mocks used | `getTerm("F21")` | None | None | PASS |

Additional Test Description Info:

- `test__get_term__does_not_retrieve_term_not_in_term_list` - in this test, we try to get a term when the term list is empty, thus we expect that the return value of attempting to retrieve a term that is not in the term list is `None`.

### **Test Case Set 3.3 Description** - `addGrade()`

In order to test if the right grades are placed in the terms, we need to first verify that `addGrade()` is working correctly before testing `addLetterGrade()`. These tests cover part of our objective bullet 3 to verify that the right grades are placed in the correct terms (i.e. the creation of term objects occurs properly because adding grades causes terms to be created if they don't already exist). These test cases verify that all letter grades (A+ through F) can be properly added to a term info such that adding a grade to a term info works correctly.

- Note that we use a `setUp()` to declare a term name (`self.term_name = "F21"`, but since it's easy to do, I replaced these in the 'Functions and Supplied Args' column of the table) and initialize a term info (`self.term_info`) that uses the term name
- We use sub tests here to isolate the multiple assertions as units that are not directly dependent on each other such that each is independent and will run regardless of any previous failures (in reference to table rows with multiple expected/actual values)

| Test Case | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| `test__add_grade__A_plus` | No mocks used | `addGrade("A+")`, `getGrades()` | ["A+"] | ["A+"] | PASS |
| `test__add_grade__A` | No mocks used | `addGrade("A")`, `getGrades()` | ["A"] | ["A"] | PASS |
| `test__add_grade__A_minus` | No mocks used | `addGrade("A-")`, `getGrades()` | ["A-"] | ["A-"] | PASS |
| `test__add_grade__B_plus` | No mocks used | `addGrade("B+")`, `getGrades()` | ["B+"] | ["B+"] | PASS |
| `test__add_grade__B` | No mocks used | `addGrade("B")`, `getGrades()` | ["B"] | ["B"] | PASS |
| `test__add_grade__B_minus` | No mocks used | `addGrade("B-")`, `getGrades()` | ["B-"] | ["B-"] | PASS |
| `test__add_grade__C_plus` | No mocks used | `addGrade("C+")`, `getGrades()` | ["C+"] | ["C+"] | PASS |
| `test__add_grade__C` | No mocks used | `addGrade("C")`, `getGrades()` | ["C"] | ["C"] | PASS |
| `test__add_grade__C_minus` | No mocks used | `addGrade("C-")`, `getGrades()` | ["C-"] | ["C-"] | PASS |
| `test__add_grade__D_plus` | No mocks used | `addGrade("D+")`, `getGrades()` | ["D+"] | ["D+"] | PASS |
| `test__add_grade__D` | No mocks used | `addGrade("D")`, `getGrades()` | ["D"] | ["D"] | PASS |
| `test__add_grade__D_minus` | No mocks used | `addGrade("D-")`, `getGrades()` | ["D-"] | ["D-"] | PASS |
| `test__add_grade__F` | No mocks used | `addGrade("F")`, `getGrades()` | ["F"] | ["F"] | PASS |
| `test__add_grade__adds_multiple_grades_to_term_info` | No mocks used | `addGrade("A")`, `addGrade("B+")`, `getGrades()`, `len(term_info_grades)` | 2 grades in the term info letter grades list, both return values from adding grades are true, A and B+ grades are both in the term info's letter grades list | 2 grades in the term info letter grades list, both return values from adding grades are true, A and B+ grades are both in the term info's letter grades list | PASS |
| `test__add_grade__does_not_add_more_than_max_courses_per_term` | No mocks used | `added_grade_list_return_values.append(self.term_info.addGrade("B"))`, `getGrades()`, `len(term_info_grades)`, `added_grade_list_return_values[gpa_calculator.gpa_calculation_mgr.calc_manager.GPA_MAX_COURSES_PER_TERM]` | 6 grades in the grade list, and the return value of attempting to add a 7th term is False | 6 grades in the grade list, and the return value of attempting to add a 7th term is False | PASS |

Additional Test Description Info:

- `test__add_grade__adds_multiple_grades_to_term_info` - in this test, we add two grades to the same term info, and then verify that they were properly added to the term info by checking the number of grades is 2, the return values are both true when adding the grade, and both grades are in the term info's letter grades list.
- `test__add_grade__does_not_add_more_than_max_courses_per_term` - in this test, we use a loop to attempt to add 7 grades for a single term info, where we expect only 6 to be successfully added because that is the max number of grades/courses per term. Therefore, we expect the 7th grades's result when we try to add it to be `False`.

### **Test Case Set 3.4 Description** - `addLetterGrade()`

Now that we've confirmed that the underlying functions work correctly, we can verify that term objects are created properly such that the right grades are placed in the correct terms. Note that this uses 3.1, 3.2, and 3.3 where we tested `addTerm()`, `getTerm()`, and `addGrade()` (respectively), so that overall, adding grades to terms properly creates terms and adds the right grades to the right terms by using mocks. We also have one integration test that does not use mocking to test the actual functionality since there is some logical condition to verify within the `addLetterGrade()`. These tests verify that adding letter grades properly creates term objects.

- Note that we use a `setUp()` to declare a term name (`self.term_name = "F21"`, but since it's easy to do, I replaced these in the 'Functions and Supplied Args' column of the table), initialize a GPA calculation manager for a student (`self.gpa_calc_manager`), and initialize a term info (`self.term_info`) that uses the term name
- We use sub tests here to isolate the multiple assertions as units that are not directly dependent on each other such that each is independent and will run regardless of any previous failures (in reference to table rows with multiple expected/actual values)

| Test Case | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| `test__add_letter_grade__when_term_does_not_exist_yet__calls_get_term_and_add_term_and_add_grade` | `@mock.patch.object(gpa_calculator.gpa_term_info.TermInfo, 'addGrade', autospec=True)`, `@mock.patch.object(gpa_calculator.gpa_term_info.TermList, 'addTerm', autospec=True)`, `@mock.patch.object(gpa_calculator.gpa_term_info.TermList, 'getTerm', autospec=True)` - used to verify that the mocked functions are each called once with the correct parameters when `addLetterGrade()` is called since we have already confirmed that `addTerm()`, `getTerm()`, and `addGrade()` all function correctly when adding a grade to a term that does not exist yet | `addLetterGrade("F21", "A")`, `mock_get_term.assert_called_once_with(self.gpa_calc_manager.terms, "F21")`, `mock_add_term.assert_called_once_with(self.gpa_calc_manager.terms, "F21")`, `mock_add_grade.assert_called_once_with(self.term_info, "A")` | All 3 `assert_called_once_with()` assertions (as sub tests) pass for `getTerm()`, `addTerm()` and `addGrade()` because all 3 mocked functions are called the correct number of times (once) and with the proper parameters when calling `addLetterGrade()` (where the term name is F21 and the letter grade is A, and the term the grade is being added to does not exist yet so `addTerm()` is called) | All 3 `assert_called_once_with()` assertions (as sub tests) pass for `getTerm()`, `addTerm()` and `addGrade()` because all 3 mocked functions are called the correct number of times (once) and with the proper parameters when calling `addLetterGrade()` (where the term name is F21 and the letter grade is A, and the term the grade is being added to does not exist yet so `addTerm()` is called) | PASS |
| `test__add_letter_grade__when_term_already_exists__calls_get_term_and_add_grade` | `@mock.patch.object(gpa_calculator.gpa_term_info.TermInfo, 'addGrade', autospec=True)`, `@mock.patch.object(gpa_calculator.gpa_term_info.TermList, 'addTerm', autospec=True)`, `@mock.patch.object(gpa_calculator.gpa_term_info.TermList, 'getTerm', autospec=True)` - used to verify that the mocked functions are each called once with the correct parameters when `addLetterGrade()` is called since we have already confirmed that `addTerm()`, `getTerm()`, and `addGrade()` all function correctly when adding a grade to a term that already exists | `addLetterGrade("F21", "A")`, `mock_get_term.assert_called_once_with(self.gpa_calc_manager.terms, "F21")`, `mock_add_term.assert_not_called()`, `mock_add_grade.assert_called_once_with(self.term_info, "A")` | Both 2 `assert_called_once_with()` assertions (as sub tests) pass for `getTerm()` and `addGrade()` while `assert_not_called()` assertion (as a sub test) passes  fpr `addTerm()` because all 3 mocked functions are called the correct number of times and with the proper parameters when calling `addLetterGrade()` (where the term name is F21 and the letter grade is A, but the term the grade is being added to already exists so `addTerm()` is not called) | Both 2 `assert_called_once_with()` assertions (as sub tests) pass for `getTerm()` and `addGrade()` while `assert_not_called()` assertion (as a sub test) passes  fpr `addTerm()` because all 3 mocked functions are called the correct number of times and with the proper parameters when calling `addLetterGrade()` (where the term name is F21 and the letter grade is A, but the term the grade is being added to already exists so `addTerm()` is not called) | PASS |
| `test__add_letter_grade__to_multiple_terms` | No mocks used | `addLetterGrade("F21", "A")`, `addLetterGrade("F21", "B")`, `addLetterGrade("W22", "C")`, `getTerm("F21").getGrades()`, `getTerm("W22").getGrades()` | F21 term contains the grades A and B, while W22 term contains the grade C | F21 term contains the grades A and B, while W22 term contains the grade C | PASS |

Additional Test Description Info:

- `test__add_letter_grade__when_term_does_not_exist_yet__calls_get_term_and_add_term_and_add_grade` - in this test, we add a grade to a term that does not exist yet, where we use mocks to verify that the underlying functions are called the appropriate number of times with the correct arguments when adding a letter grade. Therefore, we expect each of the 3 functions (`addTerm()`, `getTerm()`, and `addGrade()`) to be each called once because add term will be called when get term returns `None` (because the term does not exist in the term list).
- `test__add_letter_grade__when_term_already_exists__calls_get_term_and_add_grade` - in this test, we add a grade to a term already exists in the term list, where we use mocks to verify that the underlying functions are called the appropriate number of times with the correct arguments when adding a letter grade. Therefore, we expect only the 2 functions (`getTerm()` and `addGrade()`) to be each called once because add term will NOT be called when get term returns a term info object (because the term already exists in the term list).
- `test__add_letter_grade__to_multiple_terms` - in this test, we represent an integration test to verify that functionality is correct when adding letter grades to terms by adding 3 grades (2 to one term, 1 to another term) and confirming that the grades in each term are what we expect.

### **Test Case Set 3.5 Description** - `removeTerm()`

In order to test if term objects are cleaned up properly, we need to first verify that `removeTerm()` is working correctly before testing `removeInfoForTerm()`. These tests cover part of our objective bullet 3 to verify that the cleanup of term objects works properly (i.e. the removal of term info objects occurs properly such that term removal operates correctly for `removeTerm()` because removing an entire term list object causes this to also happen). These test cases verify that removing a term info works correctly.

- Note that we use a `setUp()` to declare a term name (`self.term_name = "F21"`, but since it's easy to do, I replaced these in the 'Functions and Supplied Args' column of the table) and initialize a term list (`self.term_list`)
- We use sub tests here to isolate the multiple assertions as units that are not directly dependent on each other such that each is independent and will run regardless of any previous failures (in reference to table rows with multiple expected/actual values)

| Test Case | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| `test__remove_term__removes_term_from_term_list` | No mocks used | `addTerm("F21")`, `removeTerm("F21")`, `getTerm("F21"))`| None | None | PASS |
| `test__remove_term__removes_term_from_term_list_when_multiple_terms_are_added` | No mocks used | `addTerm("F21")`, `addTerm("W22")`, `removeTerm("F21")`, `getTerm("F21")`, `getTerm("W22")` | Getting the removed term returns None, but getting the remaining term returns the expected term info | Getting the removed term returns None, but getting the remaining term returns the expected term info | PASS |
| `test__remove_term__works_correctly_if_term_name_not_in_term_list` | No mocks used | `removeTerm("F21")`, `getTerm("F21")` | None | None | PASS |

Additional Test Description Info:

- `test__remove_term__removes_term_from_term_list` - in this test, we add a term to the term list and then remove it. Therefore, if we try to get that removed term, we should get a return value of `None`.
- `test__remove_term__removes_term_from_term_list_when_multiple_terms_are_added` - in this test, we add two terms to the term list and then remove one of the terms. Therefore, if we try to get that removed term, we should get a return value of `None`, whereas if we try to get the remaining term, it should be the term info that we expect.
- `test__remove_term__works_correctly_if_term_name_not_in_term_list` - in this test, we attempt to remove a term that does not exist in the term list. Therefore, we still expect it to return a value of `None` since that term does not exist in the term list after trying to remove it.

### **Test Case Set 3.6 Description** - `removeInfoForTerm()`

Now that we've confirmed that the underlying functions work correctly, we can verify that term objects are cleaned up properly when removing terms such that term removal operates correctly for `removeInfoForTerm()`. Note that this uses 3.5 where we tested `removeTerm()`, so that overall this tests that removing an entire term works correctly by using mocks.

- Note that we use a `setUp()` to declare a term name (`self.term_name = "F21"`, but since it's easy to do, I replaced these in the 'Functions and Supplied Args' column of the table), initialize a GPA calculation manager for a student (`self.gpa_calc_manager`), and initialize a term info (`self.term_info`) that uses the term name
- We use sub tests here to isolate the multiple assertions as units that are not directly dependent on each other such that each is independent and will run regardless of any previous failures (in reference to table rows with multiple expected/actual values)

| Test Case | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| `test__remove_info_for_term__calls_remove_term` | `@mock.patch.object(gpa_calculator.gpa_term_info.TermList, "removeTerm", autospec=True)` - used to verify that the mocked functions are each called once with the correct parameters when `removeInfoForTerm()` is called since we have already confirmed that `removeTerm()` functions correctly and removes a term | `removeInfoForTerm("F21")`, `assert_called_once_with(self.gpa_calc_manager.terms, "F21")` | `assert_called_once_with()` assertion passes for `removeTerm()` because the mocked function is called correct number of times once and with the proper parameters when calling `removeInfoForTerm()` (where the term name is F21) | `assert_called_once_with()` assertion passes for `removeTerm()` because the mocked function is called correct number of times once and with the proper parameters when calling `removeInfoForTerm()` (where the term name is F21) | PASS |

Additional Test Description Info:

- `test__remove_info_for_term__calls_remove_term` - in this test, we mock the `removeTerm()` function to check if it's called properly the appropriate number of times and with the correct arguments since we have already confirmed that `removeTerm()` functions correctly and removes a term. Thus, we remove the entire term via `removeInfoForTerm()` and confirm that `removeTerm()` was called once with the respective term name.

Point form initial design notes:

- `addLetterGrade()` (once or twice) - mock that `addTerm()` is called the correct number of times with the correct params (also `getTerm()` and `addGrade()`)
  - test out `addTerm()`, `getTerm()`, and `addGrade()` on their own
    - `addTerm()` - have a TermList empty and then add a term and check `self.dict` has 1 item with the correct key name (eg. "F21" manually via dict w/ default empty term info, or by getting the added term)
      - can also have a test that checks if there is already 32+ then add term doesn't actually add a new term
      - can also check the return value is properly None (for the above) or returns a TermInfo object like we expect
      ~~- can also do this for multiple terms into the term list~~
    - `getTerm()` - have a TermList empty and then add a term (i.e. or manually adding it), then get the term and verify it is the correct TermInfo (or None if it didn't exist)
    - `addGrade()` - have a TermInfo empty and then add a grade and check that there are the right number of grades and the correct grades (i.e. by get grades or manually via letter grades)
      - can also have a test that checks if there is already 6+ then add grade doesn't actually add a new grade (returns False)
      ~~- can also do this for multiple grades into the term info~~
      - at least do this for each letter grade A+ through F ~~(and invalid letter grade X)~~
  - when mocking out all 3 at once, we cover if the right grades are added to the right terms
    - we can do adding 1 term (mock a version where get term is none because it hasn't been added yet)
    - we can do adding multiple terms, and/or multiple grades (mock a version where get term is not none because it has already been added)
- similar test, but also call `removeInfoForTerm()` - mock that `removeTerm()` is called the correct number of times with the correct params
  - `removeTerm()` - have a TermList empty then add a term (i.e. or by manually adding it), then remove the term and verify the term was removed (i.e. by getting the removed term with return value null, or manually get via dict)
~~- when doing these, have multiple terms and check that the correct term has the correct GPA via `getTermGPA()` before and/or after adding grades or removing a term~~

| Test Case | Mocks Used & How | Functions and Supplied Args | Expected Value(s) | Actual | Test Result |
| - | - | - | - | - | - |
| a | b | c | d | e | f |
