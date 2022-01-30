public class new_for {
    public static void main(String[] args) {

        String[] months =
                {"January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"};

        // new way of writing for loops
        for (var month: months) {
            System.out.println(month);
        }

    }
}
