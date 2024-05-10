package product_a;

// Concrete Product A2: Tea
public class Tea implements Beverage{
    @Override
    public void serve() {
        System.out.println("Here's your tea!");
    }
}
