# Creational Design Patterns

Creational design patterns simplify the way objects are created in a system. They make it easy to change how objects are created without affecting the system's overall structure.

There are two types: class creational patterns, which use inheritance to create different classes, and object creational patterns, which use another object to handle instantiation.

As systems rely more on composing objects rather than inheriting from classes, creational patterns become increasingly important. Instead of hardcoding specific behaviors, these patterns focus on defining fundamental behaviors that can be combined to create more complex ones. This means creating objects with specific behaviors involves more than just making an instance of a class.

These patterns share two main ideas. First, they package information about the specific classes used in the system. Second, they conceal the details of how instances of these classes are made and combined. The system only interacts with these objects through their defined interfaces, typically abstract classes.

As a result, creational patterns offer flexibility in *what*, *who*, *how*, and *when* objects are created. They enable configuring a system with variously structured and functional "product" objects. This configuration can be either fixed (determined during compilation) or adjustable (set during runtime).

Designs that use [Abstract Factory](./abstract_factory/README.md), [Prototype](./prototype/README.md), [Builder](./builder/README.md) are even more flexible than those that use the [Factory Method](./factory_method/README.md), but they are also more complex. Often designs start out using the [Factory Method](./factory_method/README.md) and evolve toward the other creational patterns as the designer discovers where more flexibility is needed.

***The creational patterns show how to make this design more flexible, not necessarily smaller.***