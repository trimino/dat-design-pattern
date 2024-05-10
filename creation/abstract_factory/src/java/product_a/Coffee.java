package product_a;

// Concrete Product A1: Coffee
public class Coffee implements Beverage {
    @Override
    public void serve() {
        System.out.println("Here's your coffee!");
    }
}
