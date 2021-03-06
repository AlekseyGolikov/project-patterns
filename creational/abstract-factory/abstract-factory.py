"""
    Паттерн "Абстрактная фабрика" (Abstract Factory) предоставляет интерфейс для создания семейств взаимосвязанных
    объектов с определенными интерфейсами без указания конкретных типов данных объектов. Тогда как фабричный метод
    позволяет создавать лишь экземпляр.

    Когда использовать абстрактную фабрику:
    1) когда система не должна зависеть от способа создания и компоновки новых объектов
    2) когда создаваемые объекты должны использоваться вместе и являются взаимосвязанными

"""
from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def cook(self):
        pass

class DuckAlOrange(Product):
    name = "Duck A L'Orange"

    def cook(self):
        print('French main course prepared: %s' % self.name)

class CremeBrulee(Product):
    name = 'Creme brulee'

    def cook(self):
        print('French desert prepared: %s' % self.name)

class FettuccineAlfredo(Product):
    name = 'Fettuccine Alfredo'
    def cook(self):
        print('Italian main course prepared: %s' % self.name)

class Tiramisu(Product):
    name = 'Tiramisu'
    def cook(self):
        print('Italian desert prepared: %s' % self.name)


class AbstractFactory(ABC):

    @abstractmethod
    def get_dish(type_of_meal):
        pass

class ItalianDishesFactory(AbstractFactory):

    @classmethod
    def create_desert(cls):
        return Tiramisu()

    def get_dish(type_of_meal):
        if type_of_meal == 'main':
            return FettuccineAlfredo()
        if type_of_meal == 'desert':
            return Tiramisu()


class FrenchDishesFactory(AbstractFactory):

    def get_dish(type_of_meal):
        if type_of_meal == 'main':
            return DuckAlOrange()
        if type_of_meal == 'desert':
            return CremeBrulee()

class FactoryProducer:

    def get_factory(self, type_of_factory):
        if type_of_factory == 'italian':
            return ItalianDishesFactory
        if type_of_factory == 'french':
            return FrenchDishesFactory

if __name__ == '__main__':

    # fp = FactoryProducer()
    #
    # fac = fp.get_factory('italian')
    # main = fac.get_dish('main')
    # main.cook()
    # desert = fac.get_dish('desert').cook()
    #
    # fac1  = fp.get_factory('french')
    # main = fac1.get_dish('main')
    # main.cook()
    # desert = fac1.get_dish('desert').cook()
    FactoryProducer().get_factory('italian').get_dish('main').cook()
    FactoryProducer().get_factory('italian').get_dish('desert').cook()
    FactoryProducer().get_factory('french').get_dish('main').cook()
    FactoryProducer().get_factory('french').get_dish('desert').cook()
    FactoryProducer().get_factory('italian').create_desert().cook()