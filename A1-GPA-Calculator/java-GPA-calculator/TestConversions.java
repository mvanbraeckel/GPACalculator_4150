/**
 * Course: Software Reliability and Testing (CIS*4150) - Assignment 1
 * Date: October 17, 2021
 * Author: Mitchell Van Braeckel (1002297, mvanbrae@uoguelph.ca)
 */

import org.junit.Test;
import org.junit.Before;
import org.junit.BeforeClass;
import static org.junit.Assert.assertEquals;

import GPAcalculator.*;

/**
 * Tests the conversion of percentage grades to letter values for each letter's low, midrange, and high values
 */
public class TestConversions
{
    // Set up anything that you need prior to the tests in the @Before
    // declaration area
    static GPAconverterTool gpaConverter = null;

    @BeforeClass public static void setUpClass() {
		gpaConverter = GPAconverterTool.getReference();
	}

    // @Before public void setup() {
    //     this.gpaConverter = GPAconverterTool.getReference();
    // }

    // "Outstanding",		4.3f,	"A+",		90,	100	);
    @Test public void test100percent__A_plus__high() {
        assertEquals("A+", this.gpaConverter.getLetterForNumericGrade(100));
    }
    @Test public void test095percent__A_plus__midrange() {
        assertEquals("A+", this.gpaConverter.getLetterForNumericGrade(95));
    }
    @Test public void test090percent__A_plus__low() {
        assertEquals("A+", this.gpaConverter.getLetterForNumericGrade(90));
    }

    // "Excellent",			4.0f,	"A",		85,	89	);
    @Test public void test089percent__A__high() {
        assertEquals("A", this.gpaConverter.getLetterForNumericGrade(89));
    }
    @Test public void test087percent__A__midrange() {
        assertEquals("A", this.gpaConverter.getLetterForNumericGrade(87));
    }
    @Test public void test085percent__A__low() {
        assertEquals("A", this.gpaConverter.getLetterForNumericGrade(85));
    }

    // "Very Good",			3.7f,	"A-",		80,	84	);
    @Test public void test084percent__A_minus__high() {
        assertEquals("A-", this.gpaConverter.getLetterForNumericGrade(84));
    }
    @Test public void test082percent__A_minus__midrange() {
        assertEquals("A-", this.gpaConverter.getLetterForNumericGrade(82));
    }
    @Test public void test080percent__A_minus__low() {
        assertEquals("A-", this.gpaConverter.getLetterForNumericGrade(80));
    }

    // "Good",				3.3f,	"B+",		77,	79	);
    @Test public void test079percent__B_plus__high() {
        assertEquals("B+", this.gpaConverter.getLetterForNumericGrade(79));
    }
    @Test public void test078percent__B_plus__midrange() {
        assertEquals("B+", this.gpaConverter.getLetterForNumericGrade(78));
    }
    @Test public void test077percent__B_plus__low() {
        assertEquals("B+", this.gpaConverter.getLetterForNumericGrade(77));
    }

    // "Good",				3.0f,	"B",		73,	76	);
    @Test public void test076percent__B__high() {
        assertEquals("B", this.gpaConverter.getLetterForNumericGrade(76));
    }
    @Test public void test075percent__B__midrange() {
        assertEquals("B", this.gpaConverter.getLetterForNumericGrade(75));
    }
    @Test public void test073percent__B__low() {
        assertEquals("B", this.gpaConverter.getLetterForNumericGrade(73));
    }

    // "Good",				2.7f,	"B-",		70,	72	);
    @Test public void test072percent__B_minus__high() {
        assertEquals("B-", this.gpaConverter.getLetterForNumericGrade(72));
    }
    @Test public void test071percent__B_minus__midrange() {
        assertEquals("B-", this.gpaConverter.getLetterForNumericGrade(71));
    }
    @Test public void test070percent__B_minus__low() {
        assertEquals("B-", this.gpaConverter.getLetterForNumericGrade(70));
    }

    // "Satisfactory",		2.3f,	"C+",		67,	69	);
    @Test public void test069percent__C_plus__high() {
        assertEquals("C+", this.gpaConverter.getLetterForNumericGrade(69));
    }
    @Test public void test068percent__C_plus__midrange() {
        assertEquals("C+", this.gpaConverter.getLetterForNumericGrade(68));
    }
    @Test public void test067percent__C_plus__low() {
        assertEquals("C+", this.gpaConverter.getLetterForNumericGrade(67));
    }

    // "Satisfactory",		2.0f,	"C",		63,	66	);
    @Test public void test066percent__C__high() {
        assertEquals("C", this.gpaConverter.getLetterForNumericGrade(66));
    }
    @Test public void test065percent__C__midrange() {
        assertEquals("C", this.gpaConverter.getLetterForNumericGrade(65));
    }
    @Test public void test063percent__C__low() {
        assertEquals("C", this.gpaConverter.getLetterForNumericGrade(63));
    }

    // "Satisfactory",		1.7f,	"C-",		60,	62	);
    @Test public void test062percent__C_minus__high() {
        assertEquals("C-", this.gpaConverter.getLetterForNumericGrade(62));
    }
    @Test public void test061percent__C_minus__midrange() {
        assertEquals("C-", this.gpaConverter.getLetterForNumericGrade(61));
    }
    @Test public void test060percent__C_minus__low() {
        assertEquals("C-", this.gpaConverter.getLetterForNumericGrade(60));
    }

    // "Marginal Pass",		1.3f,	"D+",		57,	59	);
    @Test public void test059percent__D_plus__high() {
        assertEquals("D+", this.gpaConverter.getLetterForNumericGrade(59));
    }
    @Test public void test058percent__D_plus__midrange() {
        assertEquals("D+", this.gpaConverter.getLetterForNumericGrade(58));
    }
    @Test public void test057percent__D_plus__low() {
        assertEquals("D+", this.gpaConverter.getLetterForNumericGrade(57));
    }

    // "Marginal Pass",		1.0f,	"D",		53,	56	);
    @Test public void test056percent__D__high() {
        assertEquals("D", this.gpaConverter.getLetterForNumericGrade(56));
    }
    @Test public void test055percent__D__midrange() {
        assertEquals("D", this.gpaConverter.getLetterForNumericGrade(55));
    }
    @Test public void test053percent__D__low() {
        assertEquals("D", this.gpaConverter.getLetterForNumericGrade(53));
    }

    // "Marginal Pass",		0.7f,	"D-",		50,	52	);
    @Test public void test052percent__D_minus__high() {
        assertEquals("D-", this.gpaConverter.getLetterForNumericGrade(52));
    }
    @Test public void test051percent__D_minus__midrange() {
        assertEquals("D-", this.gpaConverter.getLetterForNumericGrade(51));
    }
    @Test public void test050percent__D_minus__low() {
        assertEquals("D-", this.gpaConverter.getLetterForNumericGrade(50));
    }

    // "Failure",			0.0f,	"F",		0,	49	);
    @Test public void test049percent__F__high() {
        assertEquals("F", this.gpaConverter.getLetterForNumericGrade(49));
    }
    @Test public void test025percent__F__midrange() {
        assertEquals("F", this.gpaConverter.getLetterForNumericGrade(25));
    }
    @Test public void test000percent__F__low() {
        assertEquals("F", this.gpaConverter.getLetterForNumericGrade(0));
    }
}