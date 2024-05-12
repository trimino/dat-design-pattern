package factory;

import beverage.Beverage;
import topping.Topping;

// Concrete Factory: PrototypeFactory
public class PrototypeFactory implements ProductFactory {
    private final Beverage beverage;
    private final Topping topping;

    public PrototypeFactory(Beverage bp, Topping tp) {
        this.beverage = bp;
        this.topping = tp;
    }

    @Override
    public Beverage createBeverage() {
        return beverage.cloneBeverage();
    }

    @Override
    public Topping createTopping() {
        return topping.cloneTopping();
    }
}