package product;

import java.util.List;

// Product A: Pizza
public class Pizza {
    private final String size;
    private final String crustType;
    private final List<String> toppings;

    public Pizza(String size, String crustType, List<String> toppings) {
        this.size = size;
        this.crustType = crustType;
        this.toppings = toppings;
    }

    @Override
    public String toString() {
        return "Pizza: " +
                "size= " + size + ", " +
                "crustType= " + crustType + ", " +
                "toppings= " + toppings + "\n";
    }
}