# Prototype

## Introduction
**ThreadSafeSingleton**, ensure a class only has one instance, and provide a global point of access to it.

### Problem
How to create at most one, or a limited number of globally accessible instances of a class

### Solution
Hide the constructor of a class, and define a static operation that returns the sole instance of a class.

## Applicability

### When to Use the Singleton Pattern

* **Single Instance Requirement**
  * Ensure only one instance of a class exists and is accessible from a known access point.

* **Extensible Singleton**
  * Allow the singleton to be subclassed, letting clients use the extended instance without changing their code.

## Benefits

* ***Controlled Access***
  * Strictly manages how and when clients access the sole instances.

* ***Reduced Namespace Clutter***
  * Avoids global variables, keeping the namespace clean.

* ***Operation and Representation Refinement***
  * Allows subclassing, making it easy to use an extended instance at runtime.

* ***Variable Number of Instances***
  * Easily changeable to allow more than one instance if needed.

* ***Flexibility Over Class Operations***
  * Provides more flexibility than static methods, as they can't be overridden in subclasses.

## Liabilities

* ***Controlled Access***
  * Strict control over access can introduce complexity.

* ***Variable Number of Instances***
  * Allowing multiple instances can complicate the design and usage.

* ***Flexibility Over Class Operations***
  * The flexibility might lead to misuse or over complication.

## Code Example

```java
public final class ThreadSafeSingleton {
    private static ThreadSafeSingleton instance;
    public String value;
    
    private ThreadSafeSingleton(String value) {
        this.value = value;
    }
    
    public static ThreadSafeSingleton getInstance(String value) {
        ThreadSafeSingleton result = instance;
        if (result != null)
            return result;
        synchronized (ThreadSafeSingleton.class) {
            if (instance == null)
                instance = new ThreadSafeSingleton(value);
            return instance;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("If you see the same value, then threadSafeSingleton was reused (yay!)");
        System.out.println("If you see different values, then 2 singletons were created (boo!)");
        System.out.println("Result: \n");
        
        Thread threadFoo = new Thread(new ThreadFoo());
        Thread threadBar = new Thread(new ThreadBar());
        
        threadFoo.start();
        threadBar.start();
    }
    
    static class ThreadFoo implements Runnable {
        @Override
        public void run() {
            ThreadSafeSingleton threadSafeSingleton = ThreadSafeSingleton.getInstance("FOO");
            System.out.println(threadSafeSingleton.value);
        }
    }
    
    static class ThreadBar implements Runnable {
        @Override
        public void run() {
            ThreadSafeSingleton threadSafeSingleton = ThreadSafeSingleton.getInstance("BAR");
            System.out.println(threadSafeSingleton.value);
        }
    }
}
```

## Related Patterns

Many patterns can be implemented using the *ThreadSafeSingleton* pattern (Abstract Factory, Builder, Prototype).
