package topping;

// Concrete Product B1: Milk
public class Milk implements Topping {
    private String name;

    public Milk() {
        this.name = "Prototype Milk";
    }

    @Override
    public void setToppingName(String name) {
        this.name = name;
    }

    @Override
    public void add() {
        System.out.println("Adding " + this.name + " Milk...");
    }

    @Override
    public Topping cloneTopping() {
        return new Milk();
    }
}
