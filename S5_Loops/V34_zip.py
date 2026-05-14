'''
Zip is used when we have 2 lists and want to showcase both at the same time.

>>> for item in zip([1, 2, 3], ["sugar", "spice", "salt"])
    print(item)
>>> (1, 'sugar')
    (2, 'spice')
    (3, 'salt')
'''

names = ["Suresh", "Ramesh", "Rajesh", "Rakesh"]

bills = [40, 50, 60, 20]

for item in zip(names, bills):
    print(f"{item}")

# Or we can write it like this

for name, amount in zip(names, bills):
    print(f"{name} paid ${amount}")
    