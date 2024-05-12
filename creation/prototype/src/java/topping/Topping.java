package topping;

// Abstract Product B: Topping
public interface Topping {
    void setToppingName(String name);
    void add();
    Topping cloneTopping();
}