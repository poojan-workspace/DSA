'''
"Method" is just a function inside a class. Whenever we define a function inside a class its called "method".
A method always has "self" in its arguments.
'''

class Chaicup:
    size = 150 #property

    def describe(self):
        return f"The size of the cup is {self.size}"
    
cup = Chaicup() #object
print(cup.describe())
'''print(Chaicup.describe())''' # this will give an error as it does not have any reference on who is calling it..

# Fix:
print(Chaicup.describe(cup))

cup_2 = Chaicup()
cup_2.size = 100
print(Chaicup.describe(cup_2)) # that is why reference is very necessary as the same method or property can have different values