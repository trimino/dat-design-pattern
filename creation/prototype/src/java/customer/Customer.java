package customer;

import beverage.Beverage;
import factory.ProductFactory;
import topping.Topping;

// Client: Customer
public class Customer {
    private final Beverage beverage;
    private final Topping topping;

    public Customer(ProductFactory beverageFactory) {
        this.beverage = beverageFactory.createBeverage();
        this.topping = beverageFactory.createTopping();
    }

    public void order(String beverageType, String toppingName) {
        beverage.setBeverageType(beverageType);
        topping.setToppingName(toppingName);
    }

    public void enjoy() {
        beverage.serve();
        topping.add();
    }
}