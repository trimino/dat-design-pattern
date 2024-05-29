from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    def add(self, component: 'Component') -> None:
        pass

    def remove(self, component: 'Component') -> None:
        pass

    def get(name: str) -> 'Component':
        pass

    def getName() -> str:
        pass
    
    def display() -> None:
        pass

    @abstractmethod
    def operation() -> None:
        pass

# Primitive Component A
class PrimitiveComponentA(Component):
    def __init__(self, name) -> None:
        self.name = name

    def getName(self):
        return self.name
    
    def display(self):
        print(f'Primitive Component: {self.name}')

    def operation(self) -> None:
        print(f'Primitive Component A ({self.name}) operation()')

# Composite Component
class CompositeComponent(Component):
    def __init__(self, name: str) -> None:
        self.name = name
        self.components: List[Component] = []

    def add(self, component: Component) -> None:
        self.components.append(component)

    def remove(self, component: Component) -> None:
        self.components = [comp for comp in self.components if comp.getName() != component.getName()]
    
    def get(self, name: str) -> Component:
        for component in self.components:
            if component.getName() == name:
                return component
        return None
    
    def getName(self) -> str:
        return self.name

    def display(self) -> None:
        print(f'Composite Component: {self.name}')
        for c in self.components:
            c.display()

    def operation(self) -> None:
        print(f'Composite Component ({self.name}) - operation()')

def main():
    component = CompositeComponent("Composite Component Name")
    primitiveComponentA = PrimitiveComponentA("Primitive Component A")
    primitiveComponentB = PrimitiveComponentA("Primitive Component B")

    component.add(primitiveComponentA)
    component.add(primitiveComponentB)

    component.operation()
    primitiveComponentA.operation()
    primitiveComponentB.operation()

    print('\nDisplay Components\n')

    component.display()
    
    print('\nRemove Primitive Component A\n')

    c = component.get("Primitive Component A")
    component.remove(c)
    component.display()


if __name__ == "__main__":
    main()

