public class builder_str {
    public static void main(String[] args) {
        /* strings are immutable; so modifying string involves discarding old
        * ones and creating new ones. StringBuilder provides an alternative to
        * that without creating those temporary intermediate strings
        */
        var sb = new StringBuilder("Welcome");
        sb.append(" to California");
        System.out.println(sb);
        var str = sb.toString();

        StringBuilder shirt = new StringBuilder();
        shirt.append("Shirt size: ")
                .append("M")
                .append(", Qty: ")
                .append(4);
        var shirt_str = shirt.toString();
        System.out.println(shirt);

    }
}
