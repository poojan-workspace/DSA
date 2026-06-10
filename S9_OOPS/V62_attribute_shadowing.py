'''
A variable of an object is called 'Attribute'
A variable of a class is called 'property'
'''


class Chai:
    temperature = 'hot'
    strength = 'strong'

cutting = Chai() # Object
print(cutting.temperature)

# changing the object attribute value
cutting.temperature = 'mild'
print(cutting.temperature)
print(Chai.temperature)


# what if we delete the object attribute itself
del cutting.temperature
print(cutting.temperature) # It falls back to the original value from the "class"


# what if we delete something that is not in class only in object
cutting.cup = 'small'
print(cutting.cup)

del cutting.cup
print(cutting.cup)