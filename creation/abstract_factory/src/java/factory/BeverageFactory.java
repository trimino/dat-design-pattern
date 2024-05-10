package factory;

import product_a.Beverage;
import product_b.Topping;

// Concrete Factory A1 and B1: Coffee Factory
public abstract class BeverageFactory {
    abstract public Beverage createBeverage();
    abstract public Topping createTopping();
}
