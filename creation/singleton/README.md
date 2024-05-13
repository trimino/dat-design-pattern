# Prototype

## Introduction
**ThreadSafeSingleton**, ensure a class only has one instance, and provide a global point of access to it.

### Problem
How to create at most one, or a limited number of globally accessible instances of a class

### Solution
Hide the constructor of a class, and define a static operation that returns the sole instance of a class.

## Applicability
* There must be exactly one instance of a class, and it must be accessible to clients from a well known access point


* When the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code


## Benefits
&nbsp;&nbsp;&nbsp;&nbsp;***Controlled access to sole instance***. Because the *ThreadSafeSingleton* class encapsulates its sole instance, it can have strict control over how and when clients access it.


&nbsp;&nbsp;&nbsp;&nbsp;***Reduced name space***. The *ThreadSafeSingleton* pattern is an improvement over global variables. It avoids polluting the name space with global variables that store sole instances.


&nbsp;&nbsp;&nbsp;&nbsp;***Permits refinement of operations and representation***. The *ThreadSafeSingleton* class may be subclassed, and it's easy to configure an application with an instance of this extended class. You can configure the application with an instance of the class you need at run-time.


&nbsp;&nbsp;&nbsp;&nbsp;***Permits a variable number of instances***. The pattern makes it easy to change your mind and allow more than one instance of the *ThreadSafeSingleton* class. Moreover, you can use the same approach to control the number of instances that the application uses. Only the operation that grants access to the *ThreadSafeSingleton* instance needs change.


&nbsp;&nbsp;&nbsp;&nbsp;***More flexible than class operations***. Another way to package a threadSafeSingleton's functionality is to use class operations (static member functions). Static member functions cannot be overwritten, so subclasses can't override them polymorphically.


## Liabilities

Singletons create a tight coupling between different parts of your code that rely on the threadSafeSingleton instance. This can make unit testing and code maintainability more difficult.

> [!CAUTION]
> Tight coupling


Unit testing code that relies on singletons can be challenging. Mocking or stubbing the threadSafeSingleton instance can add complexity to your tests.

> [!CAUTION]
> Testability issues


Singletons often become a central point for storing global state. This can make debugging issues harder as changes to the threadSafeSingleton can have widespread effects.

> [!CAUTION]
> Global state management issues

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
