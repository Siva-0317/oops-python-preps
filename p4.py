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

#actual demo:
class Employee:
    # Public variable
    company_name = "TechCorp"

    def __init__(self, name, salary):
        # Public attribute
        self.name = name

        # Protected attribute (single underscore)
        self._salary = salary

        # Private attribute (double underscore)
        self.__bank_account = "1234-5678-9999"

    # Public method
    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary (Protected): {self._salary}")
        # Accessing private variable inside class
        print(f"Bank Account (Private): {self.__bank_account}")

    # Protected method
    def _increase_salary(self, amount):
        self._salary += amount
        print(f"Salary increased to {self._salary}")

    # Private method
    def __secret_method(self):
        print("This is a private method, accessible only inside the class.")

    # Public wrapper to access private method
    def access_secret(self):
        self.__secret_method()


# -------------------------------
# Usage Demo
# -------------------------------
emp = Employee("Maddy", 50000)

# Public variable access
print(emp.company_name)   # ✅ Allowed
print(emp.name)           # ✅ Allowed

# Protected variable access
print(emp._salary)        # ⚠️ Allowed but discouraged (convention)

# Private variable access
# print(emp.__bank_account)  # ❌ Error: Attribute not accessible directly
# Correct way: use class method
emp.show_details()

# Access protected method
emp._increase_salary(5000)   # ⚠️ Works, but not recommended outside class

# Access private method
# emp.__secret_method()       # ❌ Error
emp.access_secret()           # ✅ Allowed via public wrapper
