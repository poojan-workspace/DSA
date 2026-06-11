'''
@property: is just a getter and setter decorator for the properties inside the class.
We can set unique functions to perform for that particualr property.
'''

class TeaLeaf:

    def __init__(self, age):
        self._age = age

    # We can assign unique properties or functions for our "_age" using this decorator.
    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Age is more than 5")
        

leaf = TeaLeaf(2)
print(leaf.age)