"""
Code taken from: refactorguru.com
"""
from threading import Lock, Thread

class SingletonMeta(type):
    """
    This a thread safe implementation of Singleton.
    The Lock object is used to synchronize threads during first access to the Singleton
    """

    _instances = {}
    _lock: Lock = Lock()

    """
    This defines the __call__ method for a metaclass.
    When you call the metaclass(e.g. Singleton()) this method is invoked.
    """
    def __call__(cls, *args, **kargs):
        # with cls._lock
        # Ensures that only one thread can execute the critical section of code at a time
        # thus making the creation of the Singleton thread safe
        with cls._lock:
            # This condition checks if the class (not instance) is already in the _instances
            # dictionary. If the class is not present, it means that no instance of this class
            # has been created yet.
            if cls not in cls._instances:
                # If new instance needs to be created, this line invokes the __call__ method
                # of the superclass (typically type), effectively creating a new instance
                # of the class (cls) . The *args and **kargs are passed to the constructor
                instance = super().__call__(*args, **kargs)
                
                # After creating the instance, it adds the class itself(cls) as a key and the
                # newly created instance as its value in the _instances dictionary. This ensures
                # that only one instance of the class is ever created and stored
                cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value) -> None:
        self.value = value

def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)

if __name__ == "__main__":
    print('If you see the same value, then singleton was reused (yay!)')
    print('If you see diferrent values, then 2 singletons were created (boo!)')
    print('Result: ')

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))

    process1.start()
    process2.start()