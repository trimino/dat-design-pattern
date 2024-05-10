package product_b;

// Concrete Product B1: Milk
public class Milk implements Topping {
    @Override
    public void add() {
        System.out.println("Adding Milk...");
    }
}
