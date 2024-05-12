from abc import ABC, abstractmethod

# Abstract Product A: Beverage
class Beverage(ABC):
    @abstractmethod
    def setBeverageType(type: str) -> None:
        pass

    @abstractmethod
    def serve() -> None:
        pass

    @abstractmethod
    def cloneBeverage():
        pass

# Concrete Product A1: Coffee
class Coffee(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.coffeeType = "Prototype Coffee"

    def setBeverageType(self, type: str) -> None:
        self.coffeeType = type
    
    def serve(self) -> None:
        print(f"Here's your {self.coffeeType} coffee!")
    
    def cloneBeverage(self) -> Beverage:
        return Coffee()

# Concrete Product A2: Tea
class Tea(Beverage):
    def __init__(self) -> None:
        super().__init__()
        self.teaType = "Prototype Tea"

    def setBeverageType(self, type: str) -> None:
        self.teaType = type
    
    def serve(self) -> None:
        print(f"Here's your {self.teaType} tea!")
    
    def cloneBeverage(self) -> Beverage:
        return Tea()

# Abstract Product B: Topping
class Topping(ABC):
    @abstractmethod
    def setToppingName(name: str) -> None:
        pass

    @abstractmethod
    def add() -> None:
        pass

    @abstractmethod
    def cloneTopping():
        pass

# Concrete Product B1: Milk
class Milk(Topping):
    def __init__(self) -> None:
        super().__init__()
        self.name = " Prototype Milk"

    def setToppingName(self, name: str) -> None:
        self.name = name
    
    def add(self) -> None:
        print(f"Adding {self.name} Milk...")
    
    def cloneTopping(self) -> Topping:
        return Milk()

# Concrete Product B2: Sugar
class Sugar(Topping):
    def __init__(self) -> None:
        super().__init__()
        self.name = " Prototype Sugar"
    
    def setToppingName(self, name: str) -> None:
        self.name = name
    
    def add(self) -> None:
        print(f"Adding {self.name} Sugar...")

    def cloneTopping(self) -> Topping:
        return Sugar()

# Abstract Factory: ProductFactory
class ProductFactory(ABC):
    @abstractmethod
    def createBeverage() -> Beverage:
        pass

    @abstractmethod
    def createTopping() -> Topping:
        pass

# Concrete Factory: PrototypeFactory
class PrototypeFactory(ProductFactory):
    def __init__(self, beverage: Beverage, topping: Topping) -> None:
        super().__init__()
        self.bp = beverage
        self.tp = topping
    
    def createBeverage(self) -> Beverage:
        return self.bp.cloneBeverage()
    
    def createTopping(self) -> Topping:
        return self.tp.cloneTopping()

# Client: Customer
class Customer:
    def __init__(self, productFactory: ProductFactory) -> None:
        self.beverage = productFactory.createBeverage()
        self.topping = productFactory.createTopping()
    
    def order(self,b: str, t: str):
        self.beverage.setBeverageType(b)
        self.topping.setToppingName(t)
    
    def enjoy(self) -> None:
        self.beverage.serve()
        self.topping.add()

def main():
    coffee = Coffee()
    tea = Tea()
    milk = Milk()
    sugar = Sugar()

    coffeeMilkFactory = PrototypeFactory(coffee, milk)
    teaSugarFactory = PrototypeFactory(tea, sugar)

    coffeeLover = Customer(coffeeMilkFactory)
    teaLover = Customer(teaSugarFactory)

    coffeeLover.order('dark roast', 'Almond')
    coffeeLover.enjoy()

    teaLover.order('earl grey', 'Brown')
    teaLover.enjoy()

if __name__ == "__main__":
    main()

