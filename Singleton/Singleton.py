class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def mthod(self):
        pass




# Since the self.__dict__ of any instance can be re-bound, just
# re-bind it in __init__ to a class-attribute dictionary

class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

obj = Singleton()
obj2 = Singleton()

if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    # Should print True
    print(s1 == s2)