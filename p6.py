#abstraction = exposing what smthg does, hiding how it does. demo using python
#demo using interface concept - pure what contract
from abc import ABC,abstractmethod
class paymentmethod(ABC):
    @abstractmethod
    def pay(self,amount:float):
        pass
class creditcard(paymentmethod):
    def __init__(self,cardno:str,expiry:str):
        self.cardno=cardno
        self.expiry=expiry
    def pay(self,amount:float):
        print(f"Paid {amount} using credit card {self.cardno}")
    
class paypal(paymentmethod):
    def __init__(self,email:str):
        self.emamil=email
    def pay(self,amount:float):
        print(f"Paid {amount} using PayPal account {self.emamil}")
def process_payment(payment_method:paymentmethod,amount:float):
    payment_method.pay(amount)
cc= creditcard("1234-5678-9012-3456","12/25")
pp= paypal("abc@gmail.com")
process_payment(cc,100.0)
process_payment(pp,50.0)
"""working of the program:
1. We define an abstract base class paymentmethod with an abstract method pay.
2. We create two concrete classes, creditcard and paypal, that inherit from 
paymentmethod and implement the pay method.
3. We define a function process_payment that takes a payment_method object 
and an amount, and calls the pay method on the payment_method object.
4. We create instances of creditcard and paypal, and call process_payment 
with each instance to demonstrate polymorphism and abstraction. The client 
code does not need to know the details of how the payment is processed; 
it only needs to know that it can call the pay method on any object that 
implements the paymentmethod interface."""

#abstract class vs interface in python demo: 
#abstract class example:
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius:float):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius**2
class rectangle(shape):
    def __init__(self,width:float,height:float):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height
c=circle(5)
r=rectangle(4,6)
print(f"Area of circle: {c.area()}")
print(f"Area of rectangle: {r.area()}")