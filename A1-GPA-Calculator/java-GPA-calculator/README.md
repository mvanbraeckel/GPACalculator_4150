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

Test Name | Current Status
- | -
`test100percent__A_plus__high` | PASS
`test095percent__A_plus__midrange` | PASS
`test090percent__A_plus__low` | FAIL
`test089percent__A__high` | PASS
`test087percent__A__midrange` | PASS
`test085percent__A__low` | FAIL
`test084percent__A_minus__high` | PASS
`test082percent__A_minus__midrange` | PASS
`test080percent__A_minus__low` | FAIL
`test079percent__B_plus__high` | PASS
`test078percent__B_plus__midrange` | PASS
`test077percent__B_plus__low` | FAIL
`test076percent__B__high` | PASS
`test075percent__B__midrange` | PASS
`test073percent__B__low` | FAIL
`test072percent__B_minus__high` | PASS
`test071percent__B_minus__midrange` | PASS
`test070percent__B_minus__low` | FAIL
`test069percent__C_plus__high` | PASS
`test068percent__C_plus__midrange` | PASS
`test067percent__C_plus__low` | FAIL
`test066percent__C__high` | PASS
`test065percent__C__midrange` | PASS
`test063percent__C__low` | FAIL
`test062percent__C_minus__high` | PASS
`test061percent__C_minus__midrange` | PASS
`test060percent__C_minus__low` | FAIL
`test059percent__D_plus__high` | PASS
`test058percent__D_plus__midrange` | PASS
`test057percent__D_plus__low` | FAIL
`test056percent__D__high` | PASS
`test055percent__D__midrange` | PASS
`test053percent__D__low` | FAIL
`test052percent__D_minus__high` | PASS
`test051percent__D_minus__midrange` | PASS
`test050percent__D_minus__low` | FAIL
`test049percent__F__high` | PASS
`test025percent__F__midrange` | PASS
`test000percent__F__low` | FAIL
