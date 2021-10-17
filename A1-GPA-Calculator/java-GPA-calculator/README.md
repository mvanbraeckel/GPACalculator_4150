# GPA Calculator Java Testsuite

This directory contains the GPA calculator library within the jarfile
`GPAcalculator.jar` as well as a copy of the JUnit 4 implementation
`junit-4.10.jar`.

Also provided within the `jarcode` directory is the source for the
`GPAcalculator` class - however note that you are *NOT* intended to
edit the source code within the jar file.  It intentionally has flaws,
so that you have something to fine.

Javadoc for the code in the jarfile is provided within the
`GPAcalculator-classdocs1.1` directory.  Use a web browser to explore
this HTML documentation.

## An example

Also in this directory is a Java class `Convert75toLetterExample.java`
that demonstrates calling for a grade to be converted in this library.

Build and run this example by running the `buildAndRunExample` script.

# How to build and run the test suite

## Building the test suite
To build the Java test suite, run

	buildJavaTests.sh

This script runs the command line

	javac -cp GPAcalculator.jar:junit-4.10.jar:. RunTests.java TestConversions.java

This command line adds both the `GPAcalculator.jar` and `junit-4.10.jar` jarfile to the `CLASSPATH` and then compiles the Java code

## Running the test suite1

Similarly

	runJavaTests.sh

will run the test suite, using the command

	java -cp GPAcalculator.jar:junit-4.10.jar:. RunTests

As above, this command loads the appropriate jar files for you.

## A1 Info

 - Course: Software Reliability and Testing (CIS*4150) - Assignment 1
 - Date: October 17, 2021
 - Author: Mitchell Van Braeckel (1002297, mvanbrae@uoguelph.ca)

# Test Status

This section lists each test in the suite, and its current status (PASS or FAIL)

Test Name | Input | Expected | Actual | Current Status
- | - | - | - | -
`test100percent__A_plus__high` | 100 | A+ | A+  | PASS
`test095percent__A_plus__midrange` | 95 | A+ | A+ | PASS
`test090percent__A_plus__low` | 90 | A+ | null | FAIL
`test089percent__A__high` | 89 | A | A | PASS
`test087percent__A__midrange` | 87 | A | A | PASS
`test085percent__A__low` | 85 | A | null | FAIL
`test084percent__A_minus__high` | 85 | A- | A- | PASS
`test082percent__A_minus__midrange` | 82 | A- | A- | PASS
`test080percent__A_minus__low` | 80 | A- | null | FAIL
`test079percent__B_plus__high` | 79 | B+ | B+ | PASS
`test078percent__B_plus__midrange` | 78 | B+ | B+ | PASS
`test077percent__B_plus__low` | 77 | B+ | null | FAIL
`test076percent__B__high` | 76 | B | B | PASS
`test075percent__B__midrange` | 75 | B | B | PASS
`test073percent__B__low` | 73 | B | null | FAIL
`test072percent__B_minus__high` | 72 | B- | B- | PASS
`test071percent__B_minus__midrange` | 71 | B- | B- | PASS
`test070percent__B_minus__low` | 70 | B- | null | FAIL
`test069percent__C_plus__high` | 69 | C+ | C+ | PASS
`test068percent__C_plus__midrange` | 68 | C+ | C+ | PASS
`test067percent__C_plus__low` | 67 | C+ | null | FAIL
`test066percent__C__high` | 66 | C | C | PASS
`test065percent__C__midrange` | 65 | C | C | PASS
`test063percent__C__low` | 63 | C | null | FAIL
`test062percent__C_minus__high` | 62 | C- | C- | PASS
`test061percent__C_minus__midrange` | 61 | C- | C- | PASS
`test060percent__C_minus__low` | 60 | C- | null | FAIL
`test059percent__D_plus__high` | 59 | D+ | D+ | PASS
`test058percent__D_plus__midrange` | 58 | D+ | D+ | PASS
`test057percent__D_plus__low` | 57 | D+ | null | FAIL
`test056percent__D__high` | 56 | D | D | PASS
`test055percent__D__midrange` | 55 | D | D | PASS
`test053percent__D__low` | 53 | D | null | FAIL
`test052percent__D_minus__high` | 52 | D- | D- | PASS
`test051percent__D_minus__midrange` | 51 | D- | D- | PASS
`test050percent__D_minus__low` | 50 | D- | null | FAIL
`test049percent__F__high` | 49 | F | F | PASS
`test025percent__F__midrange` | 25 | F | F | PASS
`test000percent__F__low` | 0 | F | null | FAIL

### Detailed Test Status

#### Grade Letter A+ Tests

1. Test 100% (`test100percent__A_plus__high`)
	- Percentage Grade Input: 100
	- Expected Output: A+
	- Actual Output: A+
	- Test Result: PASS

2. Test 95% (`test095percent__A_plus__midrange`)
	- Percentage Grade Input: 95
	- Expected Output: A+
	- Actual Output: A+
	- Test Result: PASS

3. Test 90% (`test090percent__A_plus__low`)
	- Percentage Grade Input: 90
	- Expected Output: A+
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter A Tests

1. Test 89% (`test089percent__A__high`)
	- Percentage Grade Input: 89
	- Expected Output: A
	- Actual Output: A
	- Test Result: PASS

2. Test 87% (`test087percent__A__midrange`)
	- Percentage Grade Input: 87
	- Expected Output: A
	- Actual Output: A
	- Test Result: PASS

3. Test 85% (`test085percent__A__low`)
	- Percentage Grade Input: 85
	- Expected Output: A
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter A- Tests

1. Test 84% (`test084percent__A_minus__high`)
	- Percentage Grade Input: 84
	- Expected Output: A-
	- Actual Output: A-
	- Test Result: PASS

2. Test 82% (`test082percent__A_minus__midrange`)
	- Percentage Grade Input: 82
	- Expected Output: A-
	- Actual Output: A-
	- Test Result: PASS

3. Test 80% (`test080percent__A_minus__low`)
	- Percentage Grade Input: 80
	- Expected Output: A-
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter B+ Tests

1. Test 79% (`test079percent__B_plus__high`)
	- Percentage Grade Input: 79
	- Expected Output: B+
	- Actual Output: B+
	- Test Result: PASS

2. Test 78% (`test078percent__B_plus__midrange`)
	- Percentage Grade Input: 78
	- Expected Output: B+
	- Actual Output: B+
	- Test Result: PASS

3. Test 77% (`test077percent__B_plus__low`)
	- Percentage Grade Input: 77
	- Expected Output: B+
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter B Tests

1. Test 76% (`test076percent__B__high`)
	- Percentage Grade Input: 76
	- Expected Output: B
	- Actual Output: B
	- Test Result: PASS

2. Test 75% (`test075percent__B__midrange`)
	- Percentage Grade Input: 75
	- Expected Output: B
	- Actual Output: B
	- Test Result: PASS

3. Test 73% (`test073percent__B__low`)
	- Percentage Grade Input: 73
	- Expected Output: B
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter B- Tests

1. Test 72% (`test072percent__B_minus__high`)
	- Percentage Grade Input: 72
	- Expected Output: B-
	- Actual Output: B-
	- Test Result: PASS

2. Test 71% (`test071percent__B_minus__midrange`)
	- Percentage Grade Input: 71
	- Expected Output: B-
	- Actual Output: B-
	- Test Result: PASS

3. Test 70% (`test070percent__B_minus__low`)
	- Percentage Grade Input: 70
	- Expected Output: B-
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter C+ Tests

1. Test 69% (`test069percent__C_plus__high`)
	- Percentage Grade Input: 69
	- Expected Output: C+
	- Actual Output: C+
	- Test Result: PASS

2. Test 68% (`test068percent__C_plus__midrange`)
	- Percentage Grade Input: 68
	- Expected Output: C+
	- Actual Output: C+
	- Test Result: PASS

3. Test 67% (`test067percent__C_plus__low`)
	- Percentage Grade Input: 67
	- Expected Output: C+
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter C Tests

1. Test 66% (`test066percent__C__high`)
	- Percentage Grade Input: 66
	- Expected Output: C
	- Actual Output: C
	- Test Result: PASS

2. Test 65% (`test065percent__C__midrange`)
	- Percentage Grade Input: 65
	- Expected Output: C
	- Actual Output: C
	- Test Result: PASS

3. Test 63% (`test063percent__C__low`)
	- Percentage Grade Input: 63
	- Expected Output: C
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter C- Tests

1. Test 62% (`test062percent__C_minus__high`)
	- Percentage Grade Input: 62
	- Expected Output: C-
	- Actual Output: C-
	- Test Result: PASS

2. Test 61% (`test061percent__C_minus__midrange`)
	- Percentage Grade Input: 61
	- Expected Output: C-
	- Actual Output: C-
	- Test Result: PASS

3. Test 60% (`test060percent__C_minus__low`)
	- Percentage Grade Input: 60
	- Expected Output: C-
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter D+ Tests

1. Test 59% (`test059percent__D_plus__high`)
	- Percentage Grade Input: 59
	- Expected Output: D+
	- Actual Output: D+
	- Test Result: PASS

2. Test 58% (`test058percent__D_plus__midrange`)
	- Percentage Grade Input: 58
	- Expected Output: D+
	- Actual Output: D+
	- Test Result: PASS

3. Test 57% (`test057percent__D_plus__low`)
	- Percentage Grade Input: 57
	- Expected Output: D+
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter D Tests

1. Test 56% (`test056percent__D__high`)
	- Percentage Grade Input: 56
	- Expected Output: D
	- Actual Output: D
	- Test Result: PASS

2. Test 55% (`test055percent__D__midrange`)
	- Percentage Grade Input: 55
	- Expected Output: D
	- Actual Output: D
	- Test Result: PASS

3. Test 53% (`test053percent__D__low`)
	- Percentage Grade Input: 53
	- Expected Output: D
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter D- Tests

1. Test 52% (`test052percent__D_minus__high`)
	- Percentage Grade Input: 52
	- Expected Output: D-
	- Actual Output: D-
	- Test Result: PASS

2. Test 51% (`test051percent__D_minus__midrange`)
	- Percentage Grade Input: 51
	- Expected Output: D-
	- Actual Output: D-
	- Test Result: PASS

3. Test 50% (`test050percent__D_minus__low`)
	- Percentage Grade Input: 50
	- Expected Output: D-
	- Actual Output: null
	- Test Result: FAIL

#### Grade Letter F Tests

1. Test 49% (`test049percent__F__high`)
	- Percentage Grade Input: 49
	- Expected Output: F
	- Actual Output: F
	- Test Result: PASS

2. Test 25% (`test025percent__F__midrange`)
	- Percentage Grade Input: 25
	- Expected Output: F
	- Actual Output: F
	- Test Result: PASS

3. Test 0% (`test000percent__F__low`)
	- Percentage Grade Input: 0
	- Expected Output: F
	- Actual Output: null
	- Test Result: FAIL
