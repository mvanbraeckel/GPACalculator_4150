#!/bin/sh

set -x

# You can modify this line if you wish
javac -cp GPAcalculator.jar:junit-4.10.jar:. Convert75toLetterExample.java
java -cp GPAcalculator.jar:junit-4.10.jar:. Convert75toLetterExample

