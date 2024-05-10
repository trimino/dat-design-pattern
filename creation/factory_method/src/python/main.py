from abc import ABC, abstractmethod

# Abstract Product: Vehicle
class Vehicle(ABC):
    @abstractmethod
    def drive():
        pass

# Concrete Product A: Car
class Car(Vehicle):
    def drive(self):
        print('Driving a car!')

# Concrete Product B: Motorcycle
class Motorcycle(Vehicle):
    def drive(self):
        print('Driving a motorcycle!')

# Abstract Factory: VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle():
        pass

# Concrete Factory A: CarFactory
class CarFactory(VehicleFactory):
    def createVehicle(self):
        return Car()

# Concrete Factory B: MotorcycleFactory
class MotorcycleFactory(VehicleFactory):
    def createVehicle(self):
        return Motorcycle()

# Client Program
def  main ():
    car_factory = CarFactory()
    car = car_factory.createVehicle()
    car.drive()

    motor_factory = MotorcycleFactory()
    motorcycle = motor_factory.createVehicle()
    motorcycle.drive()

if __name__ == '__main__':
    main()