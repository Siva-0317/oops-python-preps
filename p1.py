class Bankaccount:
    def __init__(self,name:str,balance:float=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount:float):
        if amount>0:
            self.balance+=amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")
    def __eq__(self,other):
        """working of override __eq__ method: it checks if the other object 
        is an instance of Bankaccount and then compares the name and 
        balance attributes for equality. If both attributes are equal, 
        it returns True; otherwise, it returns False. 
        If the other object is not an instance of Bankaccount, 
        it returns False."""
        if isinstance(other,Bankaccount):
            return self.name==other.name and self.balance==other.balance
        return False
alice_acct= Bankaccount("Alice",1000.0)
alice_acct.deposit(500.0)
bob_acct= Bankaccount("Alice",1500.0)
a1=alice_acct
print(a1 is alice_acct)
print(a1 is bob_acct)
# proving a1 is equal to bob_acct using override __eq__ method
print(a1==bob_acct)

