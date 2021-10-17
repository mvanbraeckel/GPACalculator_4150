
package GPAcalculator;

import java.lang.*;
import java.util.*;
import java.awt.*;
import GPAcalculator.*;

/**
 * Do the basic conversion back and forth work
 */

public class GPAcalculator {

	public static final int GPA_MAX_COURSES_PER_TERM	= 5;
	public static final int GPA_MAX_TERMS_PER_STUDENT	= 4;

	private class TermInfo {
		private String termName;
		private int nCourses;
		private String[] letterGrades = new String[GPA_MAX_COURSES_PER_TERM];
		private float[] percentageGrades = new float[GPA_MAX_COURSES_PER_TERM];
	};

	private String studentName = null;
	private String studentID = null;
	private int nTerms;
	private TermInfo[] terms = null;

	private GPAconverterTool gpaConverter = null;

	/**
	 * Constructor.  Initialize with zeros, internally generate a converter..
	 * @param studentName full name of student
	 * @param studentID student ID number
	 */
	public GPAcalculator(String studentName, String studentID)
	{
		this.gpaConverter = GPAconverterTool.getReference();
		this.initialize(studentName, studentID);
	}

	/**
	 * Constructor.  Initialize with zeros and accept a GPAconverterTool
	 * @param studentName full name of student
	 * @param studentID student ID number
	 * @param converter the GPAconverterTool object to use
	 */
	public GPAcalculator(
			String studentName,
			String studentID,
			GPAconverterTool converter
		)
	{
		this.gpaConverter = converter;
		this.initialize(studentName, studentID);
	}


	/**
	 * Initialize the class with the given values.
	 * @param studentName full name of student
	 * @param studentID student ID number
	 */
	private void initialize(String studentName, String studentID)
	{
		this.nTerms = 0;
		terms = new TermInfo[GPA_MAX_TERMS_PER_STUDENT];
		for (int i = 0; i < GPA_MAX_TERMS_PER_STUDENT; i++)
		{
			terms[i] = new TermInfo();
		}

		this.studentName = studentName;
		this.studentID = studentID;
	}

	/**
	 * Remove all of the information describing a particular term.  The
	 * state of the system should be the same as if this term had never
	 * been added in the first place.
	 * @param term string describing the term, e.g.; "Fall 2017"
	 * @return negative if term not found
	 */
	public int removeInfoForTerm(String term)
	{
		/** search for other uses of this term */
		for (int i = 0 ; i < GPA_MAX_TERMS_PER_STUDENT && i < this.nTerms; i++)
		{
			if (this.terms[i] != null)
				if (this.terms[i].termName.equals(term))
				{
					/** delete this term */
					this.terms[i] = null;
					return i;
				}
		}

		/** not found -- return -1 */
		return -1;
	}


	/**
	 * Add a letter grade to the list
	 * @param term string describing the term, e.g.; "Fall 2017"
	 * @param lettergrade a grade letter, such as "B+"
	 * @return negative on failure
	 */
	public int addLetterGrade(
			String term,
			String lettergrade)
	{
		int i, found = (-1);

		/** search for other uses of this term */
		for (i = 0 ; i < GPA_MAX_TERMS_PER_STUDENT && i < this.nTerms; i++)
		{
			if (this.terms[i] != null)
				if (this.terms[i].termName.equals(term))
				{
					found = i;
					break;
				}
		}

		/** if this term is new, add it */
		if (found < 0)
		{
			if (this.nTerms >= GPA_MAX_TERMS_PER_STUDENT)
			{
				return -1;
			}
			found = this.nTerms++;
			this.terms[found].termName = term;
		}

		/** we have now found the right term, so add the course */
		this.terms[found].letterGrades[ this.terms[found].nCourses++ ] = lettergrade;

		return found;
	}

	/**
	 * Add a numeric grade to the list
	 * @param term string describing the term, e.g.; "Fall 2017"
	 * @param percentageGrade a numeric grade, such as 78 (percent)
	 * @return negative on failure
	 */
	public int addNumericGrade(
			String term,
			int percentageGrade)
	{
		String letterGrade;

		letterGrade = this.gpaConverter.getLetterForNumericGrade(percentageGrade);

		return ( this.addLetterGrade(term, letterGrade) );
	}

	/**
	 * Access the internally managed state for the grade point average.  Should
	 * return the GPA (mean) for the indicated term.
	 * @return GPA calculated for the matching term
	 * @param term string describing the term, e.g.; "Fall 2017"
	 */
	public float getTermGPA(String term)
	{
		int i, found = (-1);
		float gpaSummation;

		/** search for other uses of this term */
		for (i = 0 ; i < this.nTerms; i++)
		{
			if (this.terms[i] != null)
				if (this.terms[i].termName.equals(term))
				{
					found = i;
					break;
				}
		}

		/** if this term is not found, GPA is negative infinity */
		if (found < 0)
		{
			return java.lang.Float.POSITIVE_INFINITY;
		}

		/** calculate the average over this term */
		gpaSummation = this.gpaConverter.getGPAforLetterGrade( this.terms[found].letterGrades[0] );
		for (i = 1; i < this.terms[found].nCourses; i++)
		{
			gpaSummation += this.gpaConverter.getGPAforLetterGrade( this.terms[found].letterGrades[i] );
		}

		return gpaSummation / (float) this.terms[found].nCourses;
	}

	/**
	 * Access the internally managed state for the grade point average.  Should
	 * return the GPA (mean) for all courses across all terms.
	 * @return overall GPA, calculated across all terms
	 */
	public float getOverallGPA()
	{
		float gpaSummation;
		int i;

		gpaSummation = this.getTermGPA(this.terms[0].termName);
		for (i = 1; i < this.nTerms && this.terms[i] != null; i++)
		{
			gpaSummation += this.getTermGPA(this.terms[i].termName);
		}
		return gpaSummation / (float) this.nTerms;
	}

}
