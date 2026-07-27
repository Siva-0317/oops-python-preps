#constructor chaining using super() function calling parent class method
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
class Car(Vehicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make,model)
        self.num_doors=num_doors
my_car= Car("Toyota","Camry",4)
print(my_car.make)
print(my_car.model)
print(my_car.num_doors)

#Access modifiers example , public private protected
class Bankaccount:
    def __init__(self,name:str,balance:float=0.0):
        self.name=name
        self.__balance=balance #private
    def deposit(self,amount:float):
        if amount>0:
            self.__balance+=amount
            print("Amount added")
        else:
            print("Deposit must be positive")
    def get_balance(self):
        return self.__balance

#subclass showing it can't access private var of parent class
class savingsaccount(Bankaccount):
    def __init__(self,name:str,balance:float=0.0,interest_rate:float=0.5):
        super().__init__(name,balance)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        return self.__balance * self.interest_rate #this will raise an error because __balance is private in Bankaccount class and cannot be accessed 
    #directly in savingsaccount class.
sa= savingsaccount("Alice",1000.0,0.05)
print(sa.get_balance()) #this will work because we are using the public method get_balance()
print(sa.calculate_interest()) #this will raise an error because __balance is private in Bankaccount class and cannot be accessed directly in savingsaccount class.
