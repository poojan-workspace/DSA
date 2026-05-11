'''
List are the exact same thing as Array in python.
List are mutable data types. So we can add, remove or do anything with our lists after it has been intialised unlike tupels.
'''

ingredients = ["water", "sugar", "chai", "ginger"]

ingredients.append("cardomom")
print(f"The ingredients after adding cardomom: {ingredients}")

ingredients.remove("water")
print(f"The ingredients after removing water: {ingredients}")

#### Extend the chai and add spices variable
spices = ["ginger", "cardomom"]
chai = ["water", "tea"]

chai.extend(spices)
print(f"Chai spices have been added to chai: {chai}")


#### Insert >> Append only adds it to the list at the very last index, Insert can add it to the particular index
chai.insert(2, "black tea")
print(f"Inserted black tea at index 2: {chai}")


#### Pop >> It can remove the last element of the string from the list and you can used that element in another variable as well, unlike .remove which only removes it from the list

popped_string = chai.pop()
print(f"Popped string: {popped_string}")
print(f"Original string: {chai}")

#### Reverse >> rveerses the whole list
chai.reverse()
print(f"Chai: {chai}")

#### Sort >> sorts based on the alphabetical order
chai.sort()
print(f"Chai: {chai}")


#### Maximum and Minimum
sugar_level=[1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_level)}")
print(f"Minimum sugar level: {min(sugar_level)}")


#### Operator Overloading in List >> +, -, *, /
base_liquid = ["water", "milk"]
spices = ["ginger", "cardomom"]

full_chai = base_liquid + spices
print(f"Full Chai mix: {full_chai}")

spices = spices * 3
print(f"Spices: {spices}")


#### Bytearray >> every aplhabet or letter is treated individually instead of a whole string
spice = bytearray(b"CINNAMOM")
spice = spice.replace(b"CINNA", b"CARDA")
print(f"Spice: {spice}")