package builders;

// Builder Interface: Builder
public interface Builder {
    Builder setSize(String size);

    Builder setType(String type);

    Builder addTopping(String topping);
}