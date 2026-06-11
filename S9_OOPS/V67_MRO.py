'''
MRO: Method Resolution Order
'''


class A:
    label = "class A"

class B(A):
    label = "class B"

class C(A):
    label = "class C"

class D(B, C):
    pass

cup = D()
print(cup.label)