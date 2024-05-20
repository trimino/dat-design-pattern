from abc import ABC, abstractmethod

class ImplementationInterface(ABC):
    @abstractmethod
    def operation1() -> None:
        pass
    @abstractmethod
    def operation2() -> None:
        pass

class ConcreteImplementationA(ImplementationInterface):
    def operation1(self) -> None:
        print("Concrete Implemenation A: operation 1")
    
    def operation2(self) -> None:
        print("Concrete Implemenation A: operation 2")

class ConcreteImplementationB(ImplementationInterface):
    def operation1(self) -> None:
        print("Concrete Implemenation B: operation 1")
    
    def operation2(self) -> None:
        print("Concrete Implemenation B: operation 2")

class ClientInterface:
    def __init__(self) -> None:
        self.imp = ConcreteImplementationA()
    
    def operation1(self) -> None:
        self.imp.operation1()
    
    def operation2(self) -> None:
        self.imp.operation2()

    def swithImp(self, imp) -> None:
        self.imp = imp

def main():
    cif = ClientInterface()

    cif.operation1()
    cif.operation2()

    print("\nChaning Implementation...\n")

    cif.swithImp(ConcreteImplementationB())
    cif.operation1()
    cif.operation2()


if __name__ == "__main__":
    main()