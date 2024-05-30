# Abstract Factory

## Introduction

**Abstract Factory** provides an interface for creating families of related or dependent objects without specifying their concrete class.

### Problem

How to create objects of different families and hide from the client which family of objects is created?

### Solution

Define an object creation interface and let each subclass create one family objects.

## Applicability

* ***Decoupling of Product creation***
  * The system can work without needing to know exactly how each product is made or organized.

* ***Configuration with Product families***
  * The system can be configured to select from various groups of related products, each intended to seamlessly collaborate.

* ***Enforcing Product Compatibility***
  * The system can ensure related products are used together smoothly, preventing any mix-ups that might cause problems.

* ***Abstraction of Product Implementations***
  * Shows just the product interfaces, keeping users from dealing with the nitty-gritty of how they're made

## Benefits

* ***Isolates Concrete Classes***
  * Clients work with abstract interfaces rather than specific classes.
  * Concrete class names are hidden from client code.
  * Enhances code maintainability and flexibility.

* ***Easy to Exchange Product Families***
  * Change the factory class once to switch product families.
  * Simplifies reconfiguration for different product sets.
  * Example: Switch from `MortgageLoanProcessor` to `AutoLoanProcessor` by changing the factory.

* ***Promotes Product Consistency***
  * Ensures all products in a family are used together.
  * Enforces uniform product usage within an application.

## Liabilities

* ***Difficult to Support New Products***
  * Adding new products requires extending the factory interface.
  * Involves changes to the `AbstractFactory` class and all subclasses.
  * May introduce complexity with additional interfaces and classes.

## UML

<div style="text-align:center">
  <img src="diagrams/AbstractFactory.png"  alt="UML Diagram of Abstract Factory"/>
</div>

## Code Example

```java
// Abstract Product A: Beverage
interface Beverage {
    void serve();
}

// Concrete Product A1: Coffee
class Coffee implements Beverage {
    @Override
    public void serve() {
        System.out.println("Here's your coffee!");
    }
}

// Concrete Product A2: Tea
class Tea implements Beverage {
    @Override
    public void serve() {
        System.out.println("Here's your tea!");
    }
}
```

```java
// Abstract Product B: Topping
interface Topping {
    void add();
}

// Concrete Product B1: Milk
class Milk implements Topping {
    @Override
    public void add() {
        System.out.println("Adding Milk...");
    }
}

// Concrete Product B2: Sugar
class Sugar implements Topping { 
    @Override
    public void add() {
        System.out.println("Adding Sugar...");
    }
}
```

```java
// Abstract Factory: BeverageFactory
abstract class BeverageFactory { 
    abstract public Beverage createBeverage();
    abstract public Topping createTopping();
    void coreBusinessLogic() {
        System.out.println("Some core business logic that does with creation");
    }
}

// Concrete Factory A1 and B1: Coffee Factory
class CoffeeFactory extends BeverageFactory { 
    @Override 
    public Beverage createBeverage() {
        return new Coffee();
    }
    
    @Override 
    public Topping createTopping() {
        return new Milk();
    }
}

// Concrete Factory A2 and B2: Tea Factory
class TeaFactory extends BeverageFactory { 
    @Override
    public Beverage createBeverage() {
        return new Tea();
    }
    
    @Override
    public Topping createTopping() {
        return new Sugar();
    }
}
```

```java
// Client: Customer
class Customer { 
    private final Beverage beverage;
    private final Topping topping;
    
    public Customer(BeverageFactory beverageFactory) {
        this.beverage = beverageFactory.createBeverage();
        this.topping = beverageFactory.createTopping();
    }

    public void enjoy() {
        beverage.serve();
        topping.add();
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        // Create a coffee order
        BeverageFactory coffeeFactory = new CoffeeFactory();
        Customer coffeeLover = new Customer(coffeeFactory);
        coffeeLover.enjoy();
        
        // Create a tea order
        BeverageFactory teaFactory = new TeaFactory();
        Customer teaLover = new Customer(teaFactory);
        teaLover.enjoy();
    }
}
```

## Implementation Notes

### Factories as Singletons

An application typically only needs one instance of a Concrete Factory per product family!

#### Code Example With CoffeeFactory

```java
// Concrete Factory A1 and B1: Coffee Factory
class CoffeeFactory extends BeverageFactory {
    private static CoffeeFactory instance;
    
    private CoffeeFactory() {}
    
    public static CoffeeFactory getInstance() {
        if (instance == null) {
            instance = new CoffeeFactory();
        }
        return instance;
    }
    
    @Override
    public Beverage createBeverage() {
        return new Coffee();
    }

    @Override
    public Topping createTopping() {
        return new Milk();
    }
}
```

### Creating the Products

&nbsp;&nbsp;&nbsp;&nbsp;*AbstractFactory* only declares an interface for creating products. It's up to *ConcreteProduct* subclasses to actually create them. The most common way to do this is to define a factory method for each product. A concrete factory will specify its products by overridding the factory method for each. This method was implemented in the [coding example](#code-example).

> [!CAUTION]
> This is a simple implementation, but requires a concrete factoy subclass for each product family (even if the products differ slightly)

&nbsp;&nbsp;&nbsp;&nbsp;Using the [Prototype Pattern](../prototype/README.md) on the *ConcreteFactory* when having many product families will reduce the number of *ConcreteFactory* subclasses.

> [!NOTE]
> The Prototype-based approach eliminates the need for a new concrete factory subclass for each product family

## Related Patterns

* Abstract Factory often uses the Factory Method.
  * The Abstract Factory is an abstract class with factory methods; the concrete factories implement the factory methods to the vary the brand of products created.

* Abstract Factory can use Prototype if the products of different brands **share the same behaviour**.
  * For example, car components of different brands share the same behaviour. Therefore, Prototype can be used to eliminate the product hierarchy.

* Builder can be used to produce complex products for *Abstract Factory*.
  * *Abstract Factory* can produce the products used by *Builder*.
