package director;


import builders.Builder;

// Director: Director
public class Director {
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
