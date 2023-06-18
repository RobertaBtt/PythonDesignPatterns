When we refer to an object, in Python, 
at the end we are referring to an entity that has some data, a "state".

So when we deal with a Singleton class, we want to create the 
objects from this class that have the same "state data".

As long as all the objects refer to this same "state information", we reach
the goal of the Singleton.

In the Singleton, is not the programmer that creates the object, but the class Singleton.

It is important to notice that it is not important to literally have 
always the same object and to be sure to retrieve the same "id", but the concept
here is to retrieve always the same "state".

The focus on "identity" here is wrong. We can eventually create
more than one object from that class, as long as they share the same state!

**Metaclasses**

The type of x is class Foo, as you would expect.
But the type of Foo, the class itself, is type. In general, the type of any new-style class is type.


- x is an instance of class Foo.
- Foo is an instance of the type metaclass.
- _type_ is also an instance of the type metaclass, so it is an instance of itself.



    class Foo:
        pass

    x = Foo()
    
    type(x)
    <class '__main__.Foo'>

    type(Foo)
    <class 'type'>

![class-chain.png](class-chain.png)

You can also call type() with three arguments—type(<name>, <bases>, <dct>):

- <name> specifies the class name. This becomes the __name__ attribute of the class.

- <bases> specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class.

- <dct> specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the class.


    class Meta(type):
        def __new__(cls, name, bases, dct):
          x = super().__new__(cls, name, bases, dct)
          x.attr = 100
          return x

The definition header class Meta(type): specifies that Meta derives from type. 
Since type is a metaclass, that makes Meta a metaclass as well.