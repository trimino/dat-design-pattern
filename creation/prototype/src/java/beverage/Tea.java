package beverage;

// Concrete Product A1: Coffee
public class Tea implements Beverage {
    private String teaType;

    public Tea() {
        this.teaType = "Prototype Coffee";
    }

    @Override
    public void setBeverageType(String type) {
        this.teaType = type;
    }

    @Override
    public void serve() {
        System.out.println("Here's your " + this.teaType + " coffee!");
    }

    @Override
    public Beverage cloneBeverage() {
        return new Coffee();
    }
}
