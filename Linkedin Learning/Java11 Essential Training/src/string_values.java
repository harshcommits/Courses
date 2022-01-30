import java.nio.charset.StandardCharsets;

public class string_values {
    public static void main(String[] args) {
        var s3 = new String("String declaration using constructor");

        var chars = s3.toCharArray(); //print as array of chars

        String s4 = "Shirt size: ";
        String s5 = "M";
        String s6 = s4 + s5 + ", Qty: " + 4;
        System.out.println(s6);
        s6 += ", very elegant";  //operator overloading; + used to concatenate strings
        System.out.println(s6);
        var charAt = s6.charAt(5);
        System.out.println(charAt);
        System.out.println(s6.getBytes());

    }
}
