package factory;

import product_a.Beverage;
import product_a.Tea;
import product_b.Sugar;
import product_b.Topping;

// Concrete Factory A2 and B2: TeaFactory
public class TeaFactory extends BeverageFactory {
    @Override
    public Beverage createBeverage() {
        return new Tea();
    }

    @Override
    public Topping createTopping() {
        return new Sugar();
    }
}
