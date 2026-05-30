#method overriding and overloading example demo using python with definition of what it is:
#method overriding: when a child class provides a specific implementation 
# of a method that is already defined in its parent class. 
# The method in the child class has the same name, return type, and 
# parameters as the method in the parent class. This allows the child 
# class to modify or extend the behavior of the parent class method.
class Animal:
    def eat(self):
        print("animal eats")
class Dog(Animal):
    def eat(self):
        print("dog eats")
myanima=Animal()
mydog=Dog()
myanima.eat() #parent method
mydog.eat() #child method, overrides parent method

#method overloading: when a class has multiple methods with the same name 
# but different parameters. This allows the class to perform different tasks 
# based on the number or type of arguments passed to the method. Python 
# does not support method overloading in the traditional sense, but we can 
# achieve similar functionality using default arguments or variable-length 
# arguments.

class Animal:
    def eat(self, food=None):
        if food:
            print(f"Animal eats {food}")
        else:
            print("Animal eats")
my_animal=Animal()
my_animal.eat() #no argument, default behavior

my_animal.eat("grass") #with argument, overloaded behavior

# method overriding using super() function:
class Animal:
    def eat(self):
        print("animal eats")
class Dog(Animal):
    def super_eat(self):
        super().eat() #calls parent
    #separate method in child class
    def eat(self):
        print("dog eats")
mydog=Dog()
mydog.super_eat() #calls parent method using super()
mydog.eat() #calls child method, overrides parent method