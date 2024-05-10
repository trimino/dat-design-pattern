package product;

// Concrete Product A: Car
public class Car extends Vehicle {
    @Override
    public void drive() {
        System.out.println("Driving a car!");
    }
}