public class data_types {

    public class test_class{

        public void test_class(){

        }
    }

    public static void main(String[] args) {

        byte b = 1;
        short sh = 1;
        int i = 1;

        //inferred types
        var v = 1;
        var longValue = 3_000_000_000L; //the 'L' initializes value as long
        var floatValue = 33.23f; //float value


        System.out.println("Entered values: " + floatValue);
    }
}
