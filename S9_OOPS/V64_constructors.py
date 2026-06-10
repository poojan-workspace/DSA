'''
"__init__" are constructors in python.
"__init__" method are class initializers.
'''

class ChaiOrder:

    def __init__(self, type_, size): # __init__ methods are basically for taking arguments while calling the class.
        # We can put all the important properties(variables) in this __init__ method for the class.
        self.type = type_
        self.size = size
    
    def summary(self):
        return f"The size is {self.size} and the type is {self.type}"

order = ChaiOrder("Masala", 100)
print(order.summary()) # We are calling via the "order" object, so it already has a reference.

order_2 = ChaiOrder("Lemon", 200)
print(order_2.summary())

