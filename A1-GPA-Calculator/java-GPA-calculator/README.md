
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

# Test Status

This section lists each test in the suite, and its current status (PASS or FAIL)

