# Python Design Patterns



|Creational| Structural | Behavioral|
---

| Design Patterns fell into 3 categories:                                  |
|--------------------------------------------------------------------------|
| Creational                                                               |
| Structural                                                               |
| Behavioral |

#### With patterns we promote code quality, reuse design ideas, lowering the cost of the development.

### General concepts
**Inheritance**: relation between parent and child The child class keeps
the attributes and the methods of its parent, add new attributes, overrides the existing
methods. 

The **polymorfism** enables a parent class to be manifested into any of its child classes.
The true nature of the object is hidden until its method is invoked.

What is an **instance** in Python: it's an identity, that we can also print with
the id() method. The instance has a state, that is whollly mantained by 

    instance.__dict__

An instance has its behaviour, coded by its methods

So an instance has: an identity,a statem a behaviour.

The "state" of an instance can be retrieved by_
    
    ... . instance.__class__.dict


