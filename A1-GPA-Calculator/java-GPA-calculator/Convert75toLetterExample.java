import GPAcalculator.*;

public class Convert75toLetterExample {

	public static void main(String[] args)
	{

		// get the converter so that the system can function
		GPAconverterTool myGPAconverter = GPAconverterTool.getReference();

		int grade = 75;
		String letter = myGPAconverter.getLetterForNumericGrade(grade);
		System.out.println("Grade " + grade + " becomes letter: " + letter);
	}
}
