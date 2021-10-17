import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class RunTests
{
	public static void main(String[] args)
	{
		/** overall conversionResult of this test run */
		Result conversionResult = JUnitCore.runClasses(TestConversions.class);

		System.out.format("Overall conversion result was : %s\n",
				conversionResult.wasSuccessful() ? "SUCESS" : "FAILURE");

		if ( ! conversionResult.wasSuccessful()) {
			System.out.format("List of conversion test failure messages:\n");
			for (Failure failure : conversionResult.getFailures()) {
				System.out.println(failure.toString());
			}
		}
	}
} 

