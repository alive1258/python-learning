
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            return Singleton()
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()

obj3 = Singleton.get_instance()

print(obj1 is obj2)  # True
print(obj1 is obj3)  # True
