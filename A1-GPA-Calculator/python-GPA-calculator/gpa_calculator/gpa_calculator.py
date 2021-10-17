
import sys

##
## Do the basic conversion back and forth work
##

class gpa_calculator:

	GPA_MAX_COURSES_PER_TERM	= 6
	GPA_MAX_TERMS_PER_STUDENT	= 32

	class TermInfo:
		def __init__(self, termName):
			self.termName = termName
			self.letterGrades = []

	##
	## Constructor.  Initialize with zeros.
	## @param studentName full name of student
	## @param studentID student ID number
	def __init__(studentName, studentID):

		self.terms = []
		self.studentName = studentName
		self.studentID = studentID


	##
	## Add a letter grade to the list
	## @param term string describing the term, e.g.; "Fall 2017"
	## @param lettergrade a grade letter, such as "B+"
	## @return negative on failure
	def addLetterGrade(termName, lettergrade):
		found = (-1)

		## search for other uses of this term
		for dummy, i in enumerate(self.terms):
			if self.terms[i].termName == termName:
				found = i
				break

		## if self term is new, add it
		if found < 0:
			if len((self.terms) >= GPA_MAX_TERMS_PER_STUDENT):
				return -1

			# add a new term
			self.terms.append(TermInfo())
			found = len(self.terms)

		## we have now found the right term, so add the course
		self.terms[found].letterGrades.append(lettergrade)

		return found

	##
	## Add a numeric grade to the list
	## @param term string describing the term, e.g.; "Fall 2017"
	## @param percentageGrade a numeric grade, such as 78 (percent)
	## @return negative on failure
	def addNumericGrade(term, percentageGrade):

		letterGrade = gpa_calculator.gpa_converter.getLetterForNumericGrade(percentageGrade)

		return ( this.addLetterGrade(term, letterGrade) )


	##
	## @return GPA calculated for the matching term
	## @param term string describing the term, e.g.; "Fall 2017"
	## @return GPA calculated for self term
	def getTermGPA(termName):

		found = (-1)

		## search for other uses of this term
		for dummy, i in enumerate(self.terms):
			if self.terms[i].termName == termName:
				found = i
				break

		##  if self term is not found, GPA is negative infinity
		if found < 0:
			return float('-inf')

		## calculate the average over self term
		gpaSummation = 0
		for grade in self.terms[found].letterGrades:
			gpaSummation += gpa_converter.getGPAforLetterGrade( grade )

		return gpaSummation / float(len(self.terms[found].letterGrades))


	##
	## @return overall GPA, calculated across all terms
	def getOverallGPA():

		gpaSummation = 0
		for term in self.terms:
			gpaSummation += self.getTermGPA(term.termName)

		return gpaSummation / float(len(self.terms))

