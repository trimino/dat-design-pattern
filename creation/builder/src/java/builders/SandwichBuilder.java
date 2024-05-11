package builders;

import product.Sandwich;
import java.util.ArrayList;
import java.util.List;

// Concrete Builder B: Sandwich Builder
public class SandwichBuilder implements Builder {
    private String size;
    private String breadType;
    private final List<String> sauces;

    public SandwichBuilder() {
        this.sauces = new ArrayList<>();
    }

    @Override
    public Builder setSize(String size) {
        this.size = size;
        return this;
    }

    @Override
    public Builder setType(String breadType) {
        this.breadType = breadType;
        return this;
    }

    @Override
    public Builder addTopping(String sauce) {
        this.sauces.add(sauce);
        return this;
    }

    public Sandwich build() {
        return new Sandwich(this.size, this.breadType, this.sauces);
    }
}