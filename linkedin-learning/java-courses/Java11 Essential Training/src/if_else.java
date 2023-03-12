import java.time.LocalDateTime;
import java.util.Scanner;

public class if_else {
    public static void main(String[] args) {
        /*
        var scanner = new Scanner(System.in);
        System.out.println("Enter a month number");
        var monthNumber = scanner.nextInt();
        */

        var now = LocalDateTime.now();
        var monthNumber = now.getMonthValue();

        String message; //scope for message defined for this if-else block
        if (monthNumber < 1 || monthNumber > 12) {
            message = "This is not a valid month";
        } else if (monthNumber <= 3) {
            message = "This is the first quarter";
        } else {
            message = "This is not the first quarter";
        }
        System.out.println(message);

    }
}
