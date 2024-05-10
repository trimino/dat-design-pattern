package factory;

import product.Car;
import product.Vehicle;

// Concrete Factory A: CarFactory
public class CarFactory extends VehicleFactory {
    @Override
    public Vehicle createVehicle() {
        return new Car();
    }
}
