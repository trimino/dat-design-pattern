package factory;

import beverage.Beverage;
import topping.Topping;

// Abstract Factory: ProductFactory
public interface ProductFactory {
    Beverage createBeverage();
    Topping createTopping();
}