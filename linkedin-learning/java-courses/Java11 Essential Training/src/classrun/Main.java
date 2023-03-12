package classrun;

import java.text.NumberFormat;
import java.util.*;

import model.ClothingItem; //this requires import since it's in a different package
import model.ClothingSize;
import model.Hat;
import model.Shirt;  //imported after shirt created

public class Main {
    public static void main(String[] args) {

        //section for the calculator using CalcHelper class; imports not required for classes in same package
        /* uncomment for running the calculator app
        var sc = new Scanner(System.in);

        double d1, d2;
        try {
            System.out.println("Enter a value: ");
            d1 = sc.nextDouble();
            sc.nextLine();

            System.out.println("Enter a value: ");
            d2 = sc.nextDouble();
            sc.nextLine();
        } catch (InputMismatchException e) {
            System.out.println("Can't format as a number");
            return;
        }

        System.out.println("Select an operation: + - * /");
        var operation = sc.nextLine();

        double result;
        switch (operation) {
            case "+":
                result = CalcHelper.addValues(d1, d2);
                break;
            case "-":
                result = CalcHelper.subtractValues(d1, d2);
                break;
            case "*":
                result = CalcHelper.multiplyValues(d1, d2);
                break;
            case "/":
                result = CalcHelper.divideValues(d1, d2);
                break;
            default:
                System.out.println("You didn't choose a value");
                return; //important to return value out of switch block
        }
        System.out.println("The result is : " + result);
        end calculator segment */

        //section for the imported clothing items data; importing arraylist, map from collections framework
        List<String> colors = new ArrayList<>();
        colors.add("Red");
        colors.add("Green");
        colors.add("Blue");
        /*
        String[] colors = new String[3];
        colors[0] = "Red";
        colors[1] = "Green";
        colors[2] = "Blue";
         */
        for (var color: colors) {
            System.out.println(color);
        }

        //declaring items as ArrayList
        /*
        List<ClothingItem> items = new ArrayList<>();
        items.add(new Shirt(ClothingSize.L, //declared as separate enum; type parameter declared in inherited shirt class
                29.33,
                2));
        items.add(new Hat(ClothingSize.M,
                23.0,
                1));

        //loop through values
        for (ClothingItem item: items) {
            displayItemDetails(item);
        }
        */

        //declaring values using Map
        Map<String, ClothingItem> items = new HashMap<>();
        items.put("shirt", new Shirt(ClothingSize.L, //declared as separate enum; type parameter declared in inherited shirt class
                29.33,
                2));
        items.put("hat", new Hat(ClothingSize.M,
                23.0,
                1));

        //get an item from Map declaration
        /*
        var anItem = items.get("hat");
        displayItemDetails(anItem);
         */

        //loop through map items
        var keys = items.keySet();
        for (String key: keys) {
            var item = items.get(key);
            displayItemDetails(item);
        }
        /*
        item.setType("Shirt");
        item.setSize("M");
        item.setPrice(29.33);
        item.setQuantity(2);
        */

    }

    private static void displayItemDetails(ClothingItem item) {
        var totalPrice = item.getPrice()* item.getQuantity();
        var formatter = NumberFormat.getCurrencyInstance();
        //System.out.println(formatter.format(totalPrice));
        var output = String.format("Your order for %d %s %s will cost %s", item.getQuantity(),
                item.getSize(),
                item.getType(),
                formatter.format(totalPrice));
        System.out.println(output);
    }
}
