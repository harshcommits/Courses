package model;

public enum ClothingSize {
    S("Small"), M("Medium"), L("Large");
    private String description;

    ClothingSize(String description) {
        this.description = description;
    }

    //returns only description string when called
    @Override
    public String toString() {
        return description;
    }
}
