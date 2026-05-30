#Diamond problem for multiple inheritance solution demo using method resolution order (MRO):
class A:
    def method(self):
        print("Method from A")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
myd= D()
myd.method()
print(D.mro()) #shows method resolution order for class D