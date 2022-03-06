import java.io.*;

public class finally_try_catch {
    public static void main(String[] args) {
        var file = new File("hello.txt");
        System.out.println("File exists: " + file);

        //since br and reader are not closed, they can cause memory leak
        //to avoid that, we can pass them in try as shown below:
        try (FileReader reader = new FileReader(file);
             BufferedReader bf = new BufferedReader(reader)){
            var text = bf.readLine();
            System.out.println(text);
        } catch (IOException e) {
            System.out.println("File not found: " + e.getMessage());
        }
    }
}
