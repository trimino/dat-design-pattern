package customer;

import factory.BeverageFactory;
import product_a.Beverage;
import product_b.Topping;

// Client: Customer
public class Customer {
    private final Beverage beverage;
    private final Topping topping;

    public Customer(BeverageFactory beverageFactory) {
        this.beverage = beverageFactory.createBeverage();
        this.topping = beverageFactory.createTopping();
    }

    public void enjoy() {
        beverage.serve();
        topping.add();
    }
}
