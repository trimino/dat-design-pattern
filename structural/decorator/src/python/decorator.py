from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation() -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class BaseDecorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        super().__init__()
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self) -> str:
        return self.component.operation()

class ConcreteDecoratorA(BaseDecorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

class ConcreteDecoratorB(BaseDecorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

def main():
    # This way the client code can support both simple components...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    print(f"RESULT: {simple.operation()}", end="")
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    print(f"RESULT: {decorator2.operation()}", end="")

if __name__ == "__main__":
    main()