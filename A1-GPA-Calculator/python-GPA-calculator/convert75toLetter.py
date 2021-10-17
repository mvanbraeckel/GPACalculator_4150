#!/usr/bin/env python3

import gpa_calculator


grade = 75 
letter = gpa_calculator.gpa_converter.getLetterForNumericGrade(grade)
print("Grade", grade, "becomes letter:", letter)

