public class widen_shorten {

    public static void main(String[] args) {
        //widening: assigning to a larger data type

        short sh = 100;
        int i = sh;  //more memory than sh

        //shortening: assigning to smaller data type
        long long_value = i;
        short shortValue = (short) long_value;

    }
}
