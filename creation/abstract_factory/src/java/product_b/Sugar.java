package product_b;

// Concrete Product B2: Sugar
public class Sugar implements Topping {
    @Override
    public void add() {
        System.out.println("Adding Sugar...");
    }
}
