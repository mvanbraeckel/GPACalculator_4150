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
