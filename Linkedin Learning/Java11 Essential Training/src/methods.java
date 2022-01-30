import java.util.Scanner;

public class methods {
    public static void main(String[] args) {

        var input_data = new Scanner(System.in);

        double d1 = getInput(input_data, "Enter the first number");
        double d2 = getInput(input_data, "Enter the second number");
        double result = d1 / d2;

        System.out.println("The answer is: " + result);
    }

    private static double getInput(Scanner sc, String prompt) {
        System.out.println(prompt);
        return sc.nextDouble();
    }
}
