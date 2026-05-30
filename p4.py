#Access modifiers in python similar to Java.
"""Demo for private, package, protected and public using bank account class."""
class Bankaccount:
    def __init__(self,name:str,balance:float=0.0):
        self.name=name #public variable
        self.__balance=balance #private variable
    def deposit(self,amount:float):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be greater than zero.")
    def get_balance(self):
        return self.__balance
#protected variable example:
class bankaccount:
    def __init__(self,name:str,balance:float=0.0):
        self.name=name #public variable
        self._balance=balance #protected variable
    def deposit(self,amount:float):
        if amount>0:
            self._balance+=amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be greater than zero.")
#accessing protected variable from outside the class (subclass & same package)
class SavingsAccount(bankaccount):
    def __init__(self,name:str,balance:float=0.0,interest_rate:float=0.01):
        super().__init__(name,balance)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        return self._balance * self.interest_rate
#package variable example:
"""working of package variable: In Python, there is no strict concept of package
variables like in Java. However, by convention, a single underscore prefix 
(e.g., _balance) is used to indicate that a variable is intended for internal 
use within a module or class and should not be accessed directly from outside."""

class Bankaccount:
    def __init__(self,name:str,balance:float=0.0):
        self.name=name #public variable
        self._balance=balance #package variable
    def deposit(self,amount:float):
        if amount>0:
            self._balance+=amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be greater than zero.")
