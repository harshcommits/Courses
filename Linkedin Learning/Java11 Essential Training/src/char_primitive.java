public class char_primitive {
    public static void main(String[] args) {

        char c1 = '1';
        var c2 = 'a';
        char dollar = '\u0024'; //u is for unicode; unicode 24 is $ sign
        System.out.println("dollar: " + dollar);

        var upper = Character.toUpperCase(c1);
        c1 = 'a';
        System.out.println(c1);

        char[] chars = {'h', 'e', 'l', 'l', 'o'}; //prints array of chars
        System.out.println(chars);
        String s = new String(chars); //prints above array as string
        System.out.println(chars);

        //convert string to array
        var charArray = s.toCharArray();
        System.out.println(charArray);

    }
}
