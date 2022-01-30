public class bool {

    public static void main(String[] args) {
        boolean aValue = true;
        var b1 = false;
        boolean b3; //defaults to false

        //indirect boolean declaration
        var i = 0;
        var b5 = (i != 0); //sets to false
        System.out.println(b5);

        //parsing strings to boolean
        var s = "true";
        boolean b6 = Boolean.parseBoolean(s);
        System.out.println(b6);

    }
}
