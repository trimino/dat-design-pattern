package factory;

import product.Motorcycle;
import product.Vehicle;

// Concrete Factory B: MotorcycleFactory
public class MotorcycleFactory extends VehicleFactory {
    @Override
    public Vehicle createVehicle() {
        return  new Motorcycle();
    }
}