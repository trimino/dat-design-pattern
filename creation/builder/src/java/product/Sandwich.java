package product;

import java.util.List;

// Product B: Sandwich
public class Sandwich {
    private final String size;
    private final String breadType;
    private final List<String> sauces;

    public Sandwich(String size, String breadType, List<String> sauces) {
        this.size = size;
        this.breadType = breadType;
        this.sauces = sauces;
    }

    @Override
    public String toString() {
        return "Sandwich: "+
                "size = " + size + ", " +
                "breadType = " + breadType + ", " +
                "toppings = " + sauces + "\n";
    }
}