#inheritance all types demo in python: single, multilevel, 
# hierarchical, multiple, hybrid
#in the end explaining the relationships between classes like is-a has-a and uses-a
#single inheritance demo:
class Animal:
    def eat(self):
        print("Animal is eating")
class dog(Animal):
    def bark(self):
        print("dog barks")
my_dog=dog()
my_dog.eat()
my_dog.bark()

#multilevel inheritance demo:
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("dog barks")
class puppy(Dog):
    def weep(self):
        print("Puppy weeps")
my_puppy=puppy()
my_puppy.eat() #parent
my_puppy.bark() #child
my_puppy.weep() #grandchild

#hierarchical inheritance demo:
class Animal:
    def eat(self):
        print("animal eats")
class Dog(Animal):
    def bark(self):
        print("dog barks")
class Cat(Animal):
    def meow(self):
        print("cat meows")
#one parent class, two child classes - follows hierarchy
my_dog=Dog()
my_cat=Cat()
my_dog.eat()
my_dog.bark()
my_cat.eat()
my_cat.meow()

#multiple inheritance demo:
class Animal:
    def eat(self):
        print("animal eats")
class Flyable:
    def fly(self):
        print("can fly")
class Bird(Animal,Flyable):
    def chirp(self):
        print("bird chirps")
mybird=Bird()
mybird.eat()
mybird.fly()
mybird.chirp()

#hybrid inheritance demo:
class animal:
    def eat(self):
        print("animal eats")
class flyable:
    def fly(self):
        print("can fly")
class bird(animal,flyable): # multiple inheritance
    def chirp(self):
        print("bird chirps")
class parrot(bird): # multilevel inheritance
    def talk(self):
        print("parrot talks")
myparrot= parrot()
myparrot.eat()
myparrot.fly()
myparrot.chirp()
myparrot.talk()


