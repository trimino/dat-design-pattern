import factory.CarFactory;
import factory.MotorcycleFactory;
import factory.VehicleFactory;
import product.Vehicle;

public class Main {
    public static void main(String[] args) {
        // Create a Car using CarFactory
        VehicleFactory carFactory = new CarFactory();
        Vehicle car = carFactory.createVehicle();
        car.drive();            // Output: Driving a car!
        
        // Create a Motorcycle using MotorcycleFactory
        VehicleFactory motorFactory = new MotorcycleFactory();
        Vehicle motorcycle = motorFactory.createVehicle();
        motorcycle.drive();     // Output: Driving a motorcycle!
    }
}
