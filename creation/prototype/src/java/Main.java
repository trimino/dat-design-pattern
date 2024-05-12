import beverage.Beverage;
import beverage.Coffee;
import beverage.Tea;
import customer.Customer;
import factory.PrototypeFactory;
import topping.Milk;
import topping.Sugar;
import topping.Topping;

public class Main {
    public static void main(String[] args) {
        // Create Prototypes
        Beverage coffeePrototype = new Coffee();
        Beverage teaPrototype = new Tea();
        Topping milkPrototype = new Milk();
        Topping sugarPrototype = new Sugar();

        // Construct Factory with Prototypes
        PrototypeFactory coffeeMilkFactory = new PrototypeFactory(coffeePrototype, milkPrototype);
        PrototypeFactory teaSugarFactory = new PrototypeFactory(teaPrototype, sugarPrototype);

        // Construct Customer
        Customer coffeeLover = new Customer(coffeeMilkFactory);
        Customer teaLover = new Customer(teaSugarFactory);

        // Change attribute of Prototype and perform operations
        coffeeLover.order("dark roast", "Almond");
        coffeeLover.enjoy();
        teaLover.order("earl grey", "Brown");
        teaLover.enjoy();
    }
}
