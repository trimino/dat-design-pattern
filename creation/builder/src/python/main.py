from abc import ABC, abstractmethod
"""
This program is using the same domain as the Java program for the Builder.
However the implementation is a LITTLE BIT different!

In the ConcreteBuilder Properties will have a property called "product"
which repressents the product that the class will return. In this case
its Pizza and Sandwich. So instead of the methods taking in a parameter
each option will be its own method inside the Builder.

This is just another way to implement the builder pattern.
"""

# Product A: Pizza
class Pizza:
    def __init__(self) -> None:
        self.size = "N/A"
        self.crustType = "N/A"
        self.toppings = []
    
    def __str__(self) -> str:
        return f"Pizza: size={self.size}, crustType={self.crustType}, toppings={self.toppings}"

# Product B: Sandwich
class Sandwich:
    def __init__(self) -> None:
        self.size = "N/A"
        self.breadType = "N/A"
        self.toppings = []
    
    def __str__(self) -> str:
        return f"Sandwich: size={self.size}, breadType={self.breadType}, toppings={self.toppings}"

# Builder Interface: Builder
class Builder(ABC):
    @abstractmethod
    def setSize():
        pass

    @abstractmethod
    def setType():
        pass

    @abstractmethod
    def addTopping():
        pass

# Concrete Builder A: PizzaBuilder
class PizzaBuilder(Builder):
    def __init__(self) -> None:
        self.reset()
    
    def reset(self):
        self.product = Pizza()
    
    def setSize(self):
        self.product.size = "Large"
        return self
    
    def setType(self):
        self.product.crustType = "Thick"
        return self
    
    def addTopping(self):
        self.product.toppings.append("Italian Sausage")
        return self
    
    def build(self) -> Pizza:
        pizza = self.product
        self.reset()
        return pizza

# Concrete Builder B: SandwichBuilder
class SandwichBuilder(Builder):
    def __init__(self) -> None:
        self.reset()
    
    def reset(self):
        self.product = Sandwich()
    
    def setSize(self):
        self.product.size = "Footlong"
        return self
    
    def setType(self):
        self.product.breadType = "Gluten Free"
        return self
    
    def addTopping(self):
        self.product.toppings.append("Avocado") 
        self.product.toppings.append("Black Beans")
        return self
    
    def build(self) -> Sandwich:
        sandwich = self.product
        self.reset()
        return sandwich

# Director: Director
class Director:
    def buildMinimalPizza(self, builder: Builder):
        builder = builder.setSize().addTopping()
    
    def buildItalianPizza(self, builder: Builder):
        builder = builder.setSize().setType()
    
    def buildVeggieSandwich(self, builder: Builder):
        builder = builder.setSize().setType().addTopping()

def main():
    director = Director()
    pizza_builder = PizzaBuilder()
    sandwich_builder = SandwichBuilder()

    director.buildMinimalPizza(pizza_builder)
    director.buildVeggieSandwich(sandwich_builder)

    print(pizza_builder.build())
    print(sandwich_builder.build())

    director.buildItalianPizza(pizza_builder)
    print(pizza_builder.build())

if __name__ == "__main__":
    main()