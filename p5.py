#Encapsulation demo bundling state + behavior and protecting data from outside access
class bankaccount:
    def __init__(self,name:str,balance:float=0.0):
        self.name=name
        self.__balance=balance #private variable
    def deposit(self,amount:float):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be greater than zero.")
    def get_balance(self):
        return self.__balance
#immutablity class demo cannot change after construction (uses final keyword in java but in
#python we can use property decorator to make it immutable)
"""how immutability works using property keyword here: In the immutablebankacct
 class, we define two private variables _name and _balance. We then use 
 the @property decorator to create getter methods for these variables, 
 allowing us to access their values without providing setter methods."""
#getter methods are: The getter methods are defined using the @property 
# decorator, which allows us to access the private variables _name and 
# _balance as if they were public attributes. The name() method returns 
# the value of _name, and the balance() method returns the value of _balance.
#  Since there are no setter methods defined, we cannot modify these values 
# after the object has been created, making the class immutable.
#what are setter methods: Setter methods are used to set or update the 
# value of a private variable in a class.
"""if we want to make the class mutable, we can add setter methods using the @property decorator. 
For example, we can add a setter method for the balance 
variable like this:"""
class immutablebankacct:
    def __init__(self,name:str,balance:float=0.0):
        self._name=name
        self._balance=balance
    @property #getter method, cannot modify name and balance
    def name(self):
        return self._name
    @property
    def balance(self):
        return self._balance

#Defensive copying demo: creating a copy of an object to prevent 
# unintended modifications to the original object.
import copy
class bk:
    def __init__(self,name:str,balance:float=0.0):
        self.name=name
        self.balance=balance
    def get_copy(self):
        return copy.deepcopy(self) #caller is not trusted to modify 
    #the original object, so we return a deep copy of the object 
    # instead of the original object itself.
original_account= bk("Alice",1000.0)
copied_account= original_account.get_copy()
print(copied_account.name) # Output: Alice
print(copied_account.balance) # Output: 1000.0

#tell dont ask, principle of OOP: The "Tell, Don't Ask" 
# principle is a design guideline in object-oriented programming that 
# encourages developers to tell objects what to do rather than asking 
# them for information and making decisions based on that information.

class bankaccount:
    def __init__(self,name:str,balance:float=0.0):
        self.name=name
        self._balance=balance
    def deposit(self,amount:float):
        if amount>0:
            self._balance+=amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("amount must be greater than zero")
    def withdraw(self,amount:float):
        if amount>0 and amount<=self._balance: #we tell the object to 
            #perform the withdrawal action, and the object itself is 
            # responsible for checking if the withdrawal is 
            # valid and updating its state accordingly.
            self._balance-=amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount.")
acct= bankaccount("Alice",1000.0)
acct.deposit(500.0)
acct.withdraw(200.0)
print(acct._balance) # Output: 1300.0
