
class Singleton:

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)