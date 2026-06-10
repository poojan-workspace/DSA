'''
Tree:

BaseChai >> base class or parent class
MasalaChai >> inherits BaseChai
ChaiShop >> has a reference to BaseChai "This is called composition"
FancyChaiShop >> inherits ChaiShop & has a reference to MasalaChai (which has inherited BaseChai)
'''


class BaseChai:

    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        return f"Preparing {self.type} chai in the BaseChai shop"
    
class MasalaChai(BaseChai): # class will have parenthesis only when we are inheriting a parent class, otherwise wrong syntax

    def add_spices(self):
        return f"Adding ginger, cardamom and cloves...."
    

# Composition:
class ChaiShop:
    chai_cls = BaseChai # When we are inheriting all the variables and methods inside a class we dont need () as this is not an object, 
    #we are copying the whole class itself.

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        self.chai.prepare()
        return f"Serving {self.chai.type} chai in the shop"
    

order = ChaiShop()
print(order.serve())


class FancyChaiShop(ChaiShop):

    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve() # straightforward to serve()
fancy.serve() # fancy inherits ChaiShop >> serve()
fancy.chai.add_spices() # fancy has chai_cls >> which is a reference to MasalaChai >> add_spices()
# whenever we create a object it is refered to the constructor, if it doesnot have any constructor then it creates one for us.

