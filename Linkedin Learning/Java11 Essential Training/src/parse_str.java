public class parse_str {
    public static void main(String[] args) {

        var s1 = "Welcome to Jaipur";
        System.out.println("Length of string: " + s1.length());

        int position = s1.indexOf("Jaipur");
        System.out.println("The position is " + position);

        //trim whitespaces
        String s2 = "Welcome!   ";
        var len_whitespaces = s2.length();
        System.out.println(len_whitespaces);
        var trimmed = s2.trim();
        System.out.println(trimmed.length());

    }
}
