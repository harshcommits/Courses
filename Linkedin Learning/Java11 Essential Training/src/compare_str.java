public class compare_str {
    public static void main(String[] args) {

        String s1 = "Hello";
        String s2 = "Hello";

        //not the best way to compare strings; or objects in general
        if (s1 == s2) {
            System.out.println("Match");  //here we get this as output; seems to work correctly
        } else {
            System.out.println("No match");
        }

        //read up on in-turning
        String s3 = new String("Hello");
        String s4 = new String("Hello");
        //wrong way
        if (s3 == s4) {
            System.out.println("Match");
        } else {
            System.out.println("No match"); //here we get this as output; doesn't work correctly
        }
        //right way
        if (s3.equals(s4)) {
            System.out.println("Match");
        } else {
            System.out.println("No match"); //here we get this as output; doesn't work correctly
        }


    }
}
