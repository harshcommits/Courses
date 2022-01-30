public class placeholder {
    public static void main(String[] args) {
        var item = "Shirt";
        var size = "M";
        var price = 14.99;
        var color = "Red";

        //placeholder makes it easier to manipulate string components; in this case the order of values
        var template = "Clothing item: %s, size %s, color %s, $%f";  //%s: string; %d: int; %f: float
        var itemString = String.format(template,
                item, size, color, price);
        System.out.println(itemString);

    }
}
