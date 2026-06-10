'''
Everything in python is an object. Even class is an object though we say class contains objects.
'''

class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

ginger_chai = Chai()

print(type(ginger_chai))
print(type(ginger_chai) is Chai)
print(type(ginger_chai) is ChaiTime)
