import java.math.BigDecimal;
import java.util.Arrays;

public class big_decimal {

    public static void main(String[] args) {
        double value = 0.012;
        double total = value + value + value;
        System.out.println("total: " + total); //Expected: 0.036; Actual: 0.036000000000000004 due to rounding errors

        //to avoid this, we use BigDecimal()
        var value_mod = Double.toString(value);  //outputs to "0.012"
        var bigValue = new BigDecimal(value);  //outputs to 0.012
        var bigSum = bigValue.add(bigValue).add(bigValue);  //outputs to 0.036
        System.out.println("bigSum: " + bigSum);

    }

}
