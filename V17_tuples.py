'''
Tuples >> ()
They are immutable, we cannot change anything in a tuple.
'''

masala_chai = ("Ginger", "Cardomom", "Sugar")

(spices_1, spices_2, spices_3) = masala_chai

print(f"The main spices are: {spices_1}, {spices_2}, {spices_3}")
print(f"The tuple is: {masala_chai}")


#### Variable swaping
ginger, cardomom = 2, 1
print(f"The ratio of ginger and cardomom is: {ginger}, {cardomom}")

ginger, cardomom = cardomom, ginger
print(f"Swapped values of ginger and cardomom: {ginger}, {cardomom}")


#### Membership testing >> Case sensitive

print(f"Is ginger present in masala_chai ? {'ginger' in masala_chai}")
print(f"Is Ginger present in masala chai ? {'Ginger' in masala_chai}")