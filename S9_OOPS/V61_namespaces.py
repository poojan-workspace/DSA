class Chai:
    origin = 'India' # this is a "property" of a class, whenever we have a variable inside a Class we call it as property

print(Chai.origin)

Chai.is_hot = "Yes"

print(Chai.is_hot)

# Creating objects from class. Objects can possess all properties (variables) from the class

masala = Chai() # masala >> object, Chai >> class

print(masala.origin)
print(masala.is_hot)


# If we change the value of object namespace will it change the namespace in the class as well? >> NO
# The object namespace and class namespace act independently.
# So even if we change the property of an object it will not change the value of the same property in class

masala.is_hot = 'No'

print(Chai.is_hot)
print(masala.is_hot)

# If we create a new property for an object, it does not create them for the class

masala.flavor = 'masala'
print(masala.flavor)