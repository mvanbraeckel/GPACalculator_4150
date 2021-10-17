# GPA Calculator Python Testsuite

This directory contains the GPA calculator library within the subdirectory
`gpa_calculator` as well as all of the tools required to run the test suite.


### How to run

Run the test suite using this command:

	python3 runtests.py

## A1 Info

 - Course: Software Reliability and Testing (CIS*4150) - Assignment 1
 - Date: October 17, 2021
 - Author: Mitchell Van Braeckel (1002297, mvanbrae@uoguelph.ca)


## Test Status

This section lists each test in the suite, and its current status (PASS or FAIL)

Test Name | Input | Expected | Actual | Current Status
- | - | - | - | -
`test__100percent__A_plus__high` | 100 | A+ | A+  | PASS
`test__095percent__A_plus__midrange` | 95 | A+ | A+ | PASS
`test__090percent__A_plus__low` | 90 | A+ | None | FAIL
`test__089percent__A__high` | 89 | A | A | PASS
`test__087percent__A__midrange` | 87 | A | A | PASS
`test__085percent__A__low` | 85 | A | None | FAIL
`test__084percent__A_minus__high` | 85 | A- | A- | PASS
`test__082percent__A_minus__midrange` | 82 | A- | A- | PASS
`test__080percent__A_minus__low` | 80 | A- | None | FAIL
`test__079percent__B_plus__high` | 79 | B+ | B+ | PASS
`test__078percent__B_plus__midrange` | 78 | B+ | B+ | PASS
`test__077percent__B_plus__low` | 77 | B+ | None | FAIL
`test__076percent__B__high` | 76 | B | B | PASS
`test__075percent__B__midrange` | 75 | B | B | PASS
`test__073percent__B__low` | 73 | B | None | FAIL
`test__072percent__B_minus__high` | 72 | B- | B- | PASS
`test__071percent__B_minus__midrange` | 71 | B- | B- | PASS
`test__070percent__B_minus__low` | 70 | B- | None | FAIL
`test__069percent__C_plus__high` | 69 | C+ | C+ | PASS
`test__068percent__C_plus__midrange` | 68 | C+ | C+ | PASS
`test__067percent__C_plus__low` | 67 | C+ | None | FAIL
`test__066percent__C__high` | 66 | C | C | PASS
`test__065percent__C__midrange` | 65 | C | C | PASS
`test__063percent__C__low` | 63 | C | None | FAIL
`test__062percent__C_minus__high` | 62 | C- | C- | PASS
`test__061percent__C_minus__midrange` | 61 | C- | C- | PASS
`test__060percent__C_minus__low` | 60 | C- | None | FAIL
`test__059percent__D_plus__high` | 59 | D+ | D+ | PASS
`test__058percent__D_plus__midrange` | 58 | D+ | D+ | PASS
`test__057percent__D_plus__low` | 57 | D+ | None | FAIL
`test__056percent__D__high` | 56 | D | D | PASS
`test__055percent__D__midrange` | 55 | D | D | PASS
`test__053percent__D__low` | 53 | D | None | FAIL
`test__052percent__D_minus__high` | 52 | D- | D- | PASS
`test__051percent__D_minus__midrange` | 51 | D- | D- | PASS
`test__050percent__D_minus__low` | 50 | D- | None | FAIL
`test__049percent__F__high` | 49 | F | F | PASS
`test__025percent__F__midrange` | 25 | F | F | PASS
`test__000percent__F__low` | 0 | F | None | FAIL

### Detailed Test Status

#### Grade Letter A+ Tests

1. Test 100% (`test__100percent__A_plus__high`)
	- Percentage Grade Input: 100
	- Expected Output: A+
	- Actual Output: A+
	- Test Result: PASS

2. Test 95% (`test__095percent__A_plus__midrange`)
	- Percentage Grade Input: 95
	- Expected Output: A+
	- Actual Output: A+
	- Test Result: PASS

3. Test 90% (`test__090percent__A_plus__low`)
	- Percentage Grade Input: 90
	- Expected Output: A+
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter A Tests

1. Test 89% (`test__089percent__A__high`)
	- Percentage Grade Input: 89
	- Expected Output: A
	- Actual Output: A
	- Test Result: PASS

2. Test 87% (`test__087percent__A__midrange`)
	- Percentage Grade Input: 87
	- Expected Output: A
	- Actual Output: A
	- Test Result: PASS

3. Test 85% (`test__085percent__A__low`)
	- Percentage Grade Input: 85
	- Expected Output: A
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter A- Tests

1. Test 84% (`test__084percent__A_minus__high`)
	- Percentage Grade Input: 84
	- Expected Output: A-
	- Actual Output: A-
	- Test Result: PASS

2. Test 82% (`test__082percent__A_minus__midrange`)
	- Percentage Grade Input: 82
	- Expected Output: A-
	- Actual Output: A-
	- Test Result: PASS

3. Test 80% (`test__080percent__A_minus__low`)
	- Percentage Grade Input: 80
	- Expected Output: A-
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter B+ Tests

1. Test 79% (`test__079percent__B_plus__high`)
	- Percentage Grade Input: 79
	- Expected Output: B+
	- Actual Output: B+
	- Test Result: PASS

2. Test 78% (`test__078percent__B_plus__midrange`)
	- Percentage Grade Input: 78
	- Expected Output: B+
	- Actual Output: B+
	- Test Result: PASS

3. Test 77% (`test__077percent__B_plus__low`)
	- Percentage Grade Input: 77
	- Expected Output: B+
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter B Tests

1. Test 76% (`test__076percent__B__high`)
	- Percentage Grade Input: 76
	- Expected Output: B
	- Actual Output: B
	- Test Result: PASS

2. Test 75% (`test__075percent__B__midrange`)
	- Percentage Grade Input: 75
	- Expected Output: B
	- Actual Output: B
	- Test Result: PASS

3. Test 73% (`test__073percent__B__low`)
	- Percentage Grade Input: 73
	- Expected Output: B
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter B- Tests

1. Test 72% (`test__072percent__B_minus__high`)
	- Percentage Grade Input: 72
	- Expected Output: B-
	- Actual Output: B-
	- Test Result: PASS

2. Test 71% (`test__071percent__B_minus__midrange`)
	- Percentage Grade Input: 71
	- Expected Output: B-
	- Actual Output: B-
	- Test Result: PASS

3. Test 70% (`test__070percent__B_minus__low`)
	- Percentage Grade Input: 70
	- Expected Output: B-
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter C+ Tests

1. Test 69% (`test__069percent__C_plus__high`)
	- Percentage Grade Input: 69
	- Expected Output: C+
	- Actual Output: C+
	- Test Result: PASS

2. Test 68% (`test__068percent__C_plus__midrange`)
	- Percentage Grade Input: 68
	- Expected Output: C+
	- Actual Output: C+
	- Test Result: PASS

3. Test 67% (`test__067percent__C_plus__low`)
	- Percentage Grade Input: 67
	- Expected Output: C+
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter C Tests

1. Test 66% (`test__066percent__C__high`)
	- Percentage Grade Input: 66
	- Expected Output: C
	- Actual Output: C
	- Test Result: PASS

2. Test 65% (`test__065percent__C__midrange`)
	- Percentage Grade Input: 65
	- Expected Output: C
	- Actual Output: C
	- Test Result: PASS

3. Test 63% (`test__063percent__C__low`)
	- Percentage Grade Input: 63
	- Expected Output: C
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter C- Tests

1. Test 62% (`test__062percent__C_minus__high`)
	- Percentage Grade Input: 62
	- Expected Output: C-
	- Actual Output: C-
	- Test Result: PASS

2. Test 61% (`test__061percent__C_minus__midrange`)
	- Percentage Grade Input: 61
	- Expected Output: C-
	- Actual Output: C-
	- Test Result: PASS

3. Test 60% (`test__060percent__C_minus__low`)
	- Percentage Grade Input: 60
	- Expected Output: C-
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter D+ Tests

1. Test 59% (`test__059percent__D_plus__high`)
	- Percentage Grade Input: 59
	- Expected Output: D+
	- Actual Output: D+
	- Test Result: PASS

2. Test 58% (`test__058percent__D_plus__midrange`)
	- Percentage Grade Input: 58
	- Expected Output: D+
	- Actual Output: D+
	- Test Result: PASS

3. Test 57% (`test__057percent__D_plus__low`)
	- Percentage Grade Input: 57
	- Expected Output: D+
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter D Tests

1. Test 56% (`test__056percent__D__high`)
	- Percentage Grade Input: 56
	- Expected Output: D
	- Actual Output: D
	- Test Result: PASS

2. Test 55% (`test__055percent__D__midrange`)
	- Percentage Grade Input: 55
	- Expected Output: D
	- Actual Output: D
	- Test Result: PASS

3. Test 53% (`test__053percent__D__low`)
	- Percentage Grade Input: 53
	- Expected Output: D
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter D- Tests

1. Test 52% (`test__052percent__D_minus__high`)
	- Percentage Grade Input: 52
	- Expected Output: D-
	- Actual Output: D-
	- Test Result: PASS

2. Test 51% (`test__051percent__D_minus__midrange`)
	- Percentage Grade Input: 51
	- Expected Output: D-
	- Actual Output: D-
	- Test Result: PASS

3. Test 50% (`test__050percent__D_minus__low`)
	- Percentage Grade Input: 50
	- Expected Output: D-
	- Actual Output: None
	- Test Result: FAIL

#### Grade Letter F Tests

1. Test 49% (`test__049percent__F__high`)
	- Percentage Grade Input: 49
	- Expected Output: F
	- Actual Output: F
	- Test Result: PASS

2. Test 25% (`test__025percent__F__midrange`)
	- Percentage Grade Input: 25
	- Expected Output: F
	- Actual Output: F
	- Test Result: PASS

3. Test 0% (`test__000percent__F__low`)
	- Percentage Grade Input: 0
	- Expected Output: F
	- Actual Output: None
	- Test Result: FAIL
