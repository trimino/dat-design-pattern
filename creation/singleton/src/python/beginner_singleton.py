"""
Code taken from: refactorguru.com
"""

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Singleton(metaclass=SingletonMeta):
    pass

if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print('Singleton works, both variables contain the same instance')
    else:
        print('Singleton failed, variables contain different instances')