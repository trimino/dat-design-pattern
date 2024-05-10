import customer.Customer;
import factory.BeverageFactory;
import factory.CoffeeFactory;
import factory.TeaFactory;

public class Main {
    public static void main(String[] args) {
        // Create a coffee order
        BeverageFactory coffeeFactory = new CoffeeFactory();
        Customer coffeeLover = new Customer(coffeeFactory);
        coffeeLover.enjoy();

        System.out.println();

        // Create a tea order
        BeverageFactory teaFactory = new TeaFactory();
        Customer teaLover = new Customer(teaFactory);
        teaLover.enjoy();
    }
}
