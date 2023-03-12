import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Locale;

public class format_classes {
    public static void main(String[] args) {
        var doubleValue = 10_999_844.45;

        var numF = NumberFormat.getNumberInstance();
        System.out.println("Number: " + numF.format(doubleValue)); //shows commas in output unlike in .toString()

        var intF = NumberFormat.getIntegerInstance();
        System.out.println("Integer: " + intF.format(doubleValue)); //shows rounded values since int data type

        intF.setGroupingUsed(false);
        System.out.println("Integer: " + intF.format(doubleValue)); //no commas shown; grouping set to false

        var locale = new Locale("de", "DE");
        var localeformatter = NumberFormat.getNumberInstance(locale); //modifies value to german standard
        System.out.println("Number: " + localeformatter.format(doubleValue));

        //get german currency format
        var currencyFormatter = NumberFormat.getCurrencyInstance(locale); //defaults to rupee;
        System.out.println(currencyFormatter.format(doubleValue)); //prints in german currency

        //get value in dollar format
        var df = new DecimalFormat("$00.00");
        System.out.println(df.format(1)); //prints $01.00

    }
}
