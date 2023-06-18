**The Observer Patter**

| "Observer is a behavioral design pattern that allows some objects
to notify other objects about changes in their state.
The Observer pattern provides a way to subscribe and unsubscribe to 
and from these events for any object that implements a subscriber interface
"|

---


Keeps objects in the known when something they
might care about, happens.
Objects can even check at runtime whether they want to keep informed.

For the metereological data, for example, display data must be updated each time
WheatherData has been measurement.


The observer pattern defines a one-to-many dependency between
objects so that when one object changes its state, all of its dependants
are notified and updated automatically