"""In the Abastract Factory pattern we avoid dependencies: instantiatio must not be done
in public. Tying code to a concrete class can make the code more fragile, and less flexible.not
Example of bad code:

if(condition):
    duck = RolledDuck()
elif(condition):
    duck = DecoyDuck()

This code have to be changed as new concrete classes are added.
It is not  "closed for modification"

"""

"""" In making Pizza we identify what varies:
- it varies the type of Pizza
- it stay the same the method, how a Pizza is made

We have to move the creation code into another object.
if we move the previouse code, out, it becomes "SimplePizzaFactory"
   
Factories handle the details of object creation.

OrderPizza method becomes a client of the object Factory.

"""

class Pizza():
    pass

class SimplePizzaFactory():
    def create_pizza(self) -> Pizza:
        pass

import abc



""" create_pizza is the method that all clients will use to instantiate new objects. 
This is how I use the Factory we just created:"""

my_factory = SimplePizzaFactory()

class PizzaStore(SimplePizzaFactory):
    # We pass the factory in the constructor
    def __init__(self, factory):
        self.factory = factory


"""If we want to control the process, we want to create different PizzaStores.
We put back create_pizza inside the Store, but now the PizzaStore is Abstract, we well as the
method create_pizza(string)

"""

class PizzaStoreAbstract(abc.ABC):
    @abc.abstractmethod
    def create_pizza(self):
        pass

    @abc.abstractmethod
    def order_pizza(self):
        pass


class NewYorkPizzaStore(PizzaStoreAbstract):
    def order_pizza(self):
        pass

    def create_pizza(self):
        print("I implement the american pizza, so you are going to die, they dont know what how to cook")


class RomePizzaStore(PizzaStoreAbstract):
    def order_pizza(self):
        pass

    def create_pizza(self):
        print("I implement the italian pizza, the only one, the best")

"""We allow the subclasses of PizzaStore to decide.
Each PizzaStore defines the method create_pizza, they create their own variation of Pizza
"""

"""order_pizza calls create_pizza but it has no idea of what real cocnrete class is involve.
It's when I choose the Store, that I decide the concrete Pizzas that are going to be made."""

"""The method create_pizza has the responsibility to instantiate the Pizza.
It acts like a Factor, in fact it is our Factory method"""

"""A Factory method handles object creation and encapsulate it in a subclass"""

"""All Factory patterns encapsulate object creation. The factory method pattern
encapsulate object creation by letting subclasses decide what objects to create."""