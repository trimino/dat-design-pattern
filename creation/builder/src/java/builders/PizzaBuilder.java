package builders;

import product.Pizza;
import java.util.ArrayList;
import java.util.List;

// Concrete Builder A: PizzaBuilder
public class PizzaBuilder implements Builder {
    private String size;
    private String crustType;
    private List<String> toppings;

    public PizzaBuilder() {
        this.toppings = new ArrayList<>();
    }

    @Override
    public Builder setSize(String size) {
        this.size = size;
        return this;
    }

    @Override
    public Builder setType(String crustType) {
        this.crustType = crustType;
        return this;
    }

    @Override
    public Builder addTopping(String topping) {
        this.toppings.add(topping);
        return this;
    }

    public Pizza build() {
        Pizza pizza = new Pizza(this.size, this.crustType, this.toppings);
        this.toppings = new ArrayList<>();
        return pizza;
    }
}