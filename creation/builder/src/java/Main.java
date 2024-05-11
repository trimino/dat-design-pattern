import builders.PizzaBuilder;
import builders.SandwichBuilder;
import director.Director;

public class Main {
    public static void main(String[] args) {
        Director director = new Director();

        PizzaBuilder pizzaBuilder = new PizzaBuilder();
        SandwichBuilder sandwichBuilder = new SandwichBuilder();

        director.buildHawaiianPizza(pizzaBuilder);
        director.buildVeggieSandwich(sandwichBuilder);

        System.out.print(pizzaBuilder.build());
        System.out.print(sandwichBuilder.build());

        director.buildItalianPizza(pizzaBuilder);
        System.out.println(pizzaBuilder.build());
    }
}
