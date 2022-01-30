import java.util.Scanner;

public class method_overload {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        var i1 = getInput(sc, "Enter first value");
        var i2 = getInput(sc, "Enter second value");

        double result = addValues(i1, i2);
        System.out.println("The sum is " + result);

        double mult_result = addValues(i1, i2, i1, i2);
        System.out.println("Sum of multiple values is: " + mult_result);

    }

    private static int getInput(Scanner sc, String prompt) {
        System.out.println(prompt);
        return sc.nextInt();
    }

    private static double addValues(int val1, int val2) {
        return val1 + val2;
    }

    //method to add multiple values
    private static double addValues(int... values) {
        int result = 0;
        for (var value: values) {
            result += value;
        }

        return result;
    }
}
