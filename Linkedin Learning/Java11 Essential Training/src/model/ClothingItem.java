package model;

public class ClothingItem {

    public static final String SHIRT = "Shirt"; //static final value declared as constant
    public static final String HAT = "Hat";

    private String type;
    private ClothingSize size; //declared as enum
    private double price;
    private int quantity;

    //following declaration requires all parameters to be entered when instantiating the class in Main
    public ClothingItem(String type, ClothingSize size, double price, int quantity) {
        this.type = type;
        this.size = size;
        this.price = price;
        this.quantity = quantity;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ClothingSize getSize() {
        return size;
    }

    public void setSize(ClothingSize size) {
        this.size = size;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

}
