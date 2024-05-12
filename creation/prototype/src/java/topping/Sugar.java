package topping;

// Concrete Product B2: Sugar
public class Sugar implements Topping {
    String name;

    public Sugar() {
        this.name = "Prototype Sugar";
    }

    @Override
    public void setToppingName(String name) {
        this.name = name;
    }

    @Override
    public void add() {
        System.out.println("Adding " + this.name + " Sugar...");
    }

    @Override
    public Topping cloneTopping() {
        return new Sugar();
    }
}