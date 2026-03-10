'''Data types:

Objects and mutability:

Objects have identity, type and value.

Mutable and Immutable means that it is changable and it is not changable resp.
**We can know if an object is mutuable or not based on the identity of the object and never based on the value of the object.**

'''

sugar_amount = 2
print(f"Initial amount: {sugar_amount}")

sugar_amount = 13
print(f"Second amount: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")


'''2 and 12 here are immutable because the ID or 2 and 12 numbers within the computer never changes.'''
'''So our computer or system has the ID of 2 and 12 or any number fixed.'''

'''Only the sugar_amount which is the variable here is mutable because our system only changes the reference that it's pointed at
So first sugar_amount var was pointed at 2 in our computer and then it was pointed at 12 in our computer.'''


spices_mix = set()
print(f"Spice mix: {spices_mix}")
print(f"Spices mix id: {id(spices_mix)}")

spices_mix.add('Ginger')
spices_mix.add('Cardamom')

print(f"Spices mix: {spices_mix}")
print(f"Spices mix id: {id(spices_mix)}")