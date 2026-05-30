#Constructor chaining using the super() function
"""What is constructor chaining?
Constructor chaining is a technique in object-oriented programming where a 
constructor of a class calls another constructor of the same class or 
a constructor of its parent class.
how does super() function work in constructor chaining?
The super() function is used to call a method from the parent class.
In constructor chaining, the super() function is typically used to call the
constructor of the parent class to ensure that the parent class is properly
initialized before the child class adds its own initialization.
why super() ? and in which class the data will be stored?
The super() function is used to ensure that the parent class's constructor is
called, which allows the child class to inherit and initialize the 
attributes of the parent class. The data will be stored in the instance 
of the child class, but it will have access to the attributes and methods 
of the parent class through inheritance."""

class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
class Car(Vehicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make,model)#calls parent constructor vehicle
        self.num_doors=num_doors
my_car= Car("Toyota","Camry",4)
print(my_car.make)
print(my_car.model)
print(my_car.num_doors)
