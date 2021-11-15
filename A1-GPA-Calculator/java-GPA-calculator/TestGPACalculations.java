/**
 * Course: Software Reliability and Testing (CIS*4150) - Assignment 2
 * Date: November 15, 2021
 * Author: Mitchell Van Braeckel (1002297, mvanbrae@uoguelph.ca)
 */

import org.junit.Test;
import org.junit.Before;
import org.junit.BeforeClass;
import static org.junit.Assert.assertEquals;

import GPAcalculator.*;

/**
 * Tests the GPA calculation for one term with up to two courses (possible letter grades: "A", "B", "F")
 */
public class TestGPACalculations
{
    // Set up anything that you need prior to the tests in the @Before
    // declaration area
    static GPAcalculator gpaCalculator = null;

    // @BeforeClass public static void setUpClass() {
	// }

    @Before public void setup() {
        gpaCalculator = new GPAcalculator("Mitchell Van Braeckel", "1002297");
    }

    // ======================================================

    @Test public void test__calc_gpa__A__letter() {
        this.gpaCalculator.addLetterGrade("F21", "A");
        assertEquals(4.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__A__low() {
        this.gpaCalculator.addNumericGrade("F21", 85);
        assertEquals(4.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__A__midrange() {
        this.gpaCalculator.addNumericGrade("F21", 87);
        assertEquals(4.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__A__high() {
        this.gpaCalculator.addNumericGrade("F21", 89);
        assertEquals(4.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }

    @Test public void test__calc_gpa__B__letter() {
        this.gpaCalculator.addLetterGrade("F21", "B");
        assertEquals(3.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__B__low() {
        this.gpaCalculator.addNumericGrade("F21", 73);
        assertEquals(3.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__B__midrange() {
        this.gpaCalculator.addNumericGrade("F21", 75);
        assertEquals(3.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__B__high() {
        this.gpaCalculator.addNumericGrade("F21", 76);
        assertEquals(3.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }

    @Test public void test__calc_gpa__F__letter() {
        this.gpaCalculator.addLetterGrade("F21", "F");
        assertEquals(0.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__F__low() {
        this.gpaCalculator.addNumericGrade("F21", 0);
        assertEquals(0.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__F__midrange() {
        this.gpaCalculator.addNumericGrade("F21", 25);
        assertEquals(0.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__F__high() {
        this.gpaCalculator.addNumericGrade("F21", 49);
        assertEquals(0.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }

    @Test public void test__calc_gpa__AA__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "A");
        this.gpaCalculator.addLetterGrade("F21", "A");
        assertEquals(4.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__AA__low_letter() {
        this.gpaCalculator.addNumericGrade("F21", 85);
        this.gpaCalculator.addLetterGrade("F21", "A");
        assertEquals(4.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__AB__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "A");
        this.gpaCalculator.addLetterGrade("F21", "B");
        assertEquals(3.5, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__AF__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "A");
        this.gpaCalculator.addLetterGrade("F21", "F");
        assertEquals(2.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }

    @Test public void test__calc_gpa__BB__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "B");
        this.gpaCalculator.addLetterGrade("F21", "B");
        assertEquals(3.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__BB__low_letter() {
        this.gpaCalculator.addNumericGrade("F21", 73);
        this.gpaCalculator.addLetterGrade("F21", "B");
        assertEquals(3.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__BA__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "B");
        this.gpaCalculator.addLetterGrade("F21", "A");
        assertEquals(3.5, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__BF__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "B");
        this.gpaCalculator.addLetterGrade("F21", "F");
        assertEquals(1.5, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }

    @Test public void test__calc_gpa__FF__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "F");
        this.gpaCalculator.addLetterGrade("F21", "F");
        assertEquals(0.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__FF__low_letter() {
        this.gpaCalculator.addNumericGrade("F21", 0);
        this.gpaCalculator.addLetterGrade("F21", "F");
        assertEquals(0.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__FA__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "F");
        this.gpaCalculator.addLetterGrade("F21", "A");
        assertEquals(2.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__calc_gpa__FB__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "F");
        this.gpaCalculator.addLetterGrade("F21", "B");
        assertEquals(1.5, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }

    @Test public void test__calc_gpa__term_does_not_exist() {
        assertEquals(java.lang.Float.NEGATIVE_INFINITY, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
    @Test public void test__remove_term__term_does_not_exist() {
        assertEquals(-1, this.gpaCalculator.removeInfoForTerm("F21"));
    }
    @Test public void test__remove_term__one_grade__A__letter() {
        this.gpaCalculator.addLetterGrade("F21", "A");
        assertEquals(0, this.gpaCalculator.removeInfoForTerm("F21"));
    }
    @Test public void test__remove_term__one_grade__F__low() {
        this.gpaCalculator.addNumericGrade("F21", 0);
        assertEquals(0, this.gpaCalculator.removeInfoForTerm("F21"));
    }
    @Test public void test__remove_term__two_grades__AB__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "A");
        this.gpaCalculator.addLetterGrade("F21", "B");
        assertEquals(0, this.gpaCalculator.removeInfoForTerm("F21"));
    }
    @Test public void test__remove_term__two_grades__FF__low_letter() {
        this.gpaCalculator.addNumericGrade("F21", 0);
        this.gpaCalculator.addLetterGrade("F21", "F");
        assertEquals(0, this.gpaCalculator.removeInfoForTerm("F21"));
    }

    @Test public void test__calc_overall_gpa__BA__letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "B");
        this.gpaCalculator.addLetterGrade("F21", "A");
        assertEquals(3.5, this.gpaCalculator.getOverallGPA(), 0.001);
    }
    @Test public void test__calc_gpa_equals_overall_gpa__FA_letter_letter() {
        this.gpaCalculator.addLetterGrade("F21", "F");
        this.gpaCalculator.addLetterGrade("F21", "A");
        assertEquals(this.gpaCalculator.getTermGPA("F21"), this.gpaCalculator.getOverallGPA(), 0.001);
        assertEquals(2.0, this.gpaCalculator.getTermGPA("F21"), 0.001);
    }
}