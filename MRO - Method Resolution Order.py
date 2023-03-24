# MRO - Multiple Resolution Order
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.mro()) # Check the MRO
print(D.num) # Check the value of num