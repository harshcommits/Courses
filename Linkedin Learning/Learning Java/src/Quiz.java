import java.util.Scanner;

public class Quiz {
    public static void main (String[] args) {
        String question = "What is the best stack?";
        String choiceOne = "spring";
        String choiceTwo = "django";
        String choiceThree = "depends";

        String correctChoice = choiceTwo;

        Scanner input = new Scanner(System.in);
        System.out.println(question + "\nEnter your choice");
        String value = input.next();

        if (correctChoice.equals(value)) {
            System.out.println("Correct choice");
        }
        else {
            System.out.println("Incorrect choice. The right answer is: " + correctChoice);
        }

    }
}
