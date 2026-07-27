#constructors & objs lifecycle
class Loan:
    def __init__(self,p=100,rate=0.5,term_yrs=3):
        self.principal=p
        self.rate=rate
        self.term_yrs=term_yrs
    """what is classmethod here: The classmethod decorator is used to 
    define a method that belongs to the class rather than an instance 
    of the class."""  #is using classmethod good or defining the function normally is good? ans: using classmethod is good when you 
    #want to create alternative constructors or when you want to define a method that operates on the class itself rather than on 
    # instances of the class. It allows you to create objects in different ways while still maintaining a clear and organized structure 
    # for your code.
    @classmethod
    def shorterm_loan(cls,p):
        return cls(p,0.5,1)
def_loan= Loan()
print(def_loan.principal,def_loan.rate,def_loan.term_yrs)
custom_loan= Loan(200,0.75,5)
quick_loan= Loan.shorterm_loan(150)
print(custom_loan.principal,custom_loan.rate,custom_loan.term_yrs)
print(quick_loan.principal,quick_loan.rate,quick_loan.term_yrs)

class loan:
    def __init__(self,p=100,rate=0.5,term=3):
        self.principal=p
        self.rate=rate
        self.term=term
    @classmethod
    def shortloan(cls,p):
        return cls(p,0.5,1)
print(loan.shortloan(150).principal,loan.shortloan(150).rate,loan.shortloan(150).term)

    