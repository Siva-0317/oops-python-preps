#Polymorphism demo (both compile-time and runtime) using method overriding 
# and overloading in python:
#method overriding (runtime polymorphism):
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def eat(self):
        print("Dog eats")
a= Animal()
d=Dog()
a.eat() #calls parent method
d.eat() #calls child method, overrides parent method

#method overloading (compile-time polymorphism) using default arguments:
class Animal:
    def eat(self,food=None):
        if food:
            print(f"Animal eats {food}")
        else:
            print("Animal eats")
a= Animal()
a.eat() #no argument, default behavior
a.eat("meat") #with argument, overloaded behavior
