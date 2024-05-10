from abc import ABC, abstractmethod

"""
Implementation of Abstract Factory in python (3.12.1)
Run using the following command:
    python3 main.py
"""

# Abstract Product A: Beverage
class Beverage(ABC):
    @abstractmethod
    def serve():
        pass

# Concrete Product A1: Coffee
class Coffee(Beverage):
    def serve(self):
        print('Here\'s your coffee!')

# Concrete Product A2: Tea
class Tea(Beverage):
    def serve(self):
        print('Here\'s your tea!')

# Abstract Product B: Topping
class Topping(ABC):
    @abstractmethod
    def add(self):
        pass

# Concrete Product B1: Milk
class Milk(Topping):
    def add(self):
        print('Adding Milk...')

# Concrete Product B2: Sugar
class Sugar(Topping):
    def add(self):
        print('Adding Sugar...')

# Abstract Factory: BeverageFactory
class BeverageFactory(ABC):
    @abstractmethod
    def createBeverage(self):
        pass

    @abstractmethod
    def createTopping(self):
        pass

# Concrete Factory A1 and B1: CoffeeFactory
class CoffeeFactory(BeverageFactory):
    def createBeverage(self):
        return Coffee()

    def createTopping(self):
        return Milk()

# Concrete Factory A2 and B2: TeaFactory
class TeaFactory(BeverageFactory):
    def createBeverage(self):
        return Tea()

    def createTopping(self):
        return Sugar()

# Client
class Customer:
    def __init__(self, bev: Beverage):
        self.bev = bev.createBeverage()
        self.top = bev.createTopping()
    
    def enjoy(self):
        self.bev.serve()
        self.top.add()

# Application
def main():
    coffee_factory = CoffeeFactory()
    tea_factory = TeaFactory()

    coffee_lover = Customer(coffee_factory)
    coffee_lover.enjoy()

    print()
    
    tea_lover = Customer(tea_factory)
    tea_lover.enjoy()

if __name__ == '__main__':
    main()