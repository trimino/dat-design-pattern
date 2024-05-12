package beverage;

// Concrete Product A1: Coffee
public class Coffee implements Beverage {
    private String coffeeType;

    public Coffee() {
        this.coffeeType = "Prototype Coffee";
    }

    @Override
    public void setBeverageType(String type) {
        this.coffeeType = type;
    }

    @Override
    public void serve() {
        System.out.println("Here's your " + this.coffeeType + " coffee!");
    }

    @Override
    public Beverage cloneBeverage() {
        return new Coffee();
    }
}
