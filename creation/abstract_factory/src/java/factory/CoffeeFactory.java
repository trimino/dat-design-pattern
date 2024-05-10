package factory;

import product_a.Beverage;
import product_a.Coffee;
import product_b.Milk;
import product_b.Topping;

// Concrete Factory A1 and B1: CoffeeFactory
public class CoffeeFactory extends BeverageFactory {
    @Override
    public Beverage createBeverage() {
        return new Coffee();
    }

    @Override
    public Topping createTopping() {
        return new Milk();
    }
}
