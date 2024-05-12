package beverage;

// Abstract Product A: Beverage
public interface Beverage {
    void setBeverageType(String type);
    void serve();
    Beverage cloneBeverage();
}