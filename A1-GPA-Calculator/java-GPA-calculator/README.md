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
