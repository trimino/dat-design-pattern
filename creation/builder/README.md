## Introduction
**Builder Pattern** separates the construction of a complex object from its representation so that the same construction process can create different representations.

### Problem
How to vary the construction processes and the individual construction steps, so they can be combined in flexible ways to construct different products.

### Solution
Decouple the construction processes and the construction steps into two separate hierarchies, so they can be combined in more flexible ways.

## Applicability

* When you're making a complicated thing, how you put it together shouldn't depend on what exactly it's made of

* You should be able to build the same thing in different ways, depending on what you need it to do

## Benefits

&nbsp;&nbsp;&nbsp;&nbsp;The builder pattern hides the nitty-gritty details of how the product is put together. By using an abstract interface, it shields the director from knowing the product's internal structure. Changing how the product is made is easy—you just need to create a new type of builder.

> [!TIP]
> The builder hides the representation and internal structure of the product from the director.

&nbsp;&nbsp;&nbsp;&nbsp;The builder pattern makes it easier to manage complex objects by keeping their construction details hidden. Clients don't need to worry about how the object is internally structured since this information is hidden by the builder's interface. Each type of *ConcreteBuilder* knows how to put together a specific kind of object. This code is written once and can be reused by different directors to create various versions of the product using the same building blocks.

> [!TIP]
> Separates the product representation and construction concerns. The builder builds parts and keep the partial product. The director (also called supervisor) controls the construction process.

&nbsp;&nbsp;&nbsp;&nbsp;The builder pattern builds the product gradually, following the director's guidance, instead of creating it all at once like other creational patterns. The director only grabs the product from the builder when it's fully assembled. This approach means the Builder interface reflects the construction process more clearly, giving you precise control over how the product is put together and its internal structure.

> [!TIP]
> The director can control the construction process at any level of detail.

## Liabilities
&nbsp;&nbsp;&nbsp;&nbsp;The overall complexity of the code increases since the pattern requires creating multiple new classes.

> [!CAUTION]
> A few more classes to implement

## UML

### Sequence Diagram

<div style="text-align:center">
  <img src="diagrams/BuilderSequenceDiagram.png"  alt="Sequence Diagram for Builder Pattern"/>
</div>

### Class Diagram

<div style="text-align:center">
  <img src="diagrams/Builder.png"  alt="Sequence Diagram for Builder Pattern"/>
</div>

## Code Example

```java
// Product A: Pizza
class Pizza {
    private String size;
    private String crustType;
    private List<String> toppings;
    
    public Pizza(String size, String crustType, List<String> toppings) {
        this.size = size;
        this.crustType = crustType;
        this.toppings = toppings;
    }
    
    @Override
    public String toString() {
        return "Pizza { " +
                "size= " + size + ", " +
                "crustType= " + crustType + ", " +
                "toppings= " + toppings + "}\n";
    }
}

// Product B: Sandwich
class Sandwich {
    private String size;
    private String breadType;
    private List<String> toppings;
    
    public Sandwich(String size, String breadType, List<String> toppings) {
        this.size = size;
        this.breadType = breadType;
        this.toppings = toppings;
    }
    
    @Override
    public String toString() {
        return "Sandwich { "+
                "size = " + size + ", " +
                "breadType = " + breadType + ", " +
                "toppings = " + toppings + "}\n";
    }
}
```

```java
// Builder Interface: Builder
interface Builder {
    Builder setSize(String size);

    Builder setType(String type);

    Builder addTopping(String topping);
}

// Concrete Builder A: PizzaBuilder
class PizzaBuilder implements Builder {
    private String size;
    private String crustType;
    private List<String> toppings;

    public PizzaBuilder() {
        this.toppings = new ArrayList<>();
    }

    @Override
    public Builder setSize(String size) {
        this.size = size;
        return this;
    }

    @Override
    public Builder setType(String crustType) {
        this.crustType = crustType;
        return this;
    }

    @Override
    public Builder addTopping(String topping) {
        this.toppings.add(topping);
        return this;
    }

    public Pizza build() {
        return new Pizza(this.size, this.crustType, this.toppings);
    }
}

// Concrete Builder B: Sandwich Builder
class SandwichBuilder implements Builder {
    private String size;
    private String breadType;
    private List<String> toppings;

    public SandwichBuilder() {
        this.toppings = new ArrayList<>();
    }

    @Override
    public Builder setSize(String size) {
        this.size = size;
        return this;
    }

    @Override
    public Builder setType(String breadType) {
        this.breadType = breadType;
        return this;
    }

    @Override
    public Builder addTopping(String topping) {
        this.toppings.add(topping);
        return this;
    }
    
    public Sandwich build() {
        return new Sandwich(this.size, this.breadType, this.toppings);
    }
}
```

```java
// Director: Director
class Director {
    public void buildHawaiianPizza(Builder builder) {
        builder.setSize("Large")
                .setType("Thin")
                .addTopping("Ham")
                .addTopping("Pineapple");
    }

    public void buildItalianPizza(Builder builder) {
        builder.setSize("Large")
                .setType("Thick")
                .addTopping("Sausage");
    }

    public void buildVeggieSandwich(Builder builder) {
        builder.setSize("Large")
                .setType("Gluten Free")
                .addTopping("Avocado")
                .addTopping("Black Beans");
    }
}

public class Main {
    public static void main(String[] args) {
        Director director = new Director();
        
        PizzaBuilder pizzaBuilder = new PizzaBuilder();
        SandwichBuilder sandwichBuilder = new SandwichBuilder();
        
        director.buildHawaiianPizza(pizzaBuilder);
        director.buildVeggieSandwhich(sandwichBuilder);
        
        System.out.println(pizzaBuilder.build());
        System.out.println(sandwichBuilder.build());
        
        director.buildItalianPizza(pizzaBuilder);
        System.out.println(pizzaBuilder.build());
    }
}
```

## Implementation Notes

### No Abstract Classes for Products

&nbsp;&nbsp;&nbsp;&nbsp;In the common case, the products produced by the concrete builders differ so greatly in their representation that there is little to gain from giving different products a common parent class.

### Assembly and Construction Interface

&nbsp;&nbsp;&nbsp;&nbsp;Builders use a step-by-step approach to create their products. So, the Builder class interface needs to be flexible enough to work with different kinds of builders. One important consideration is how the construction and assembly process should work. One way is to just add each new part to the product as it's built. However, sometimes you might need to access parts of the product that were built earlier, especially in cases like building tree structures. In those situations, the builder might return child nodes to the director, which then sends them back to the builder to build the parent nodes.

### Empty Methods as Default In BUILDER Interface 

```java
interface Builder {
    default void buildPart1() {}    // Default empty method
    default void buildPart2() {}    // Default empty method
}

class ConcreteBuilder implements Builder {
    @Override
    public void buildPart1() {
        System.out.println("Overriding if needed, building part 1...");
    }
    
    // buildPart2 method is not overwritten, so it uses the default empty implementation
}

class Main {
    public static void main(String[] args) {
        Builder builder = new ConcreteBuilder();
        builder.buildPart1();
        builder.buildPart2();   // This uses the default empty implementation
  }
}
```

## Related Patterns

* *Builder* can build complex objects for *Abstract Factory*. *Abstract Factory* can provide products for *Builder*.
    * *Abstract Factory* is similar to *Builder* in that it too may construct complex objects. The **primary difference** is that the *Builder* pattern focuses on constructing a complex object **step by step**. *Abstract Factory's* emphasis is on **families of product objects (either simple or complex)**. *Builder* returns the product as a **final step**, but as far as *Abstract Factory* pattern is concerned, the product gets returned immediately.

* *Builder* can be used to create the complex *Composite* trees because you can program its construction steps to work recursively.

* Many designs start by using *Factory Method* (less complicated and more customizable via subclasses) and evolve toward *Abstract Factory*, *Prototype*, or *Builder* (more flexible but more complicated). 
