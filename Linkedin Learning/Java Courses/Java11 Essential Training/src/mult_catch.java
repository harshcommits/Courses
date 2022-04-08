public class mult_catch {
    public static void main(String[] args) {

        String s = "";
        try {
            var sub = s.substring(1);
        } catch(StringIndexOutOfBoundsException e) {
            System.out.println("Index out of bounds: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Issue not clear: " + e.getMessage());
        }

        System.out.println("We passed try-catch stage");

    }
}
