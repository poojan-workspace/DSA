'''
Sets are mutable: that means we can change the values inside the set and the reference will still be the same of that set.
set = {}

Intersection (&) and Union (|): common values or elements and all the values or elements without repitition respectively.
'''

essential_spices = {"cardomom", "ginger", "cinnamom"}
optional_spices = {"ginger", "cloves", "black pepper"}

all_spices = essential_spices | optional_spices # UNION
print(f"Union of both sets: {all_spices}")

common_spices = essential_spices & optional_spices # INTERSECTION
print(f"Intersection of both sets: {common_spices}")


only_in_essentials = essential_spices - optional_spices # A - B
print(f"Only in essential spices set: {only_in_essentials}")

print(f"Is 'cloves' in essential_spices set? {'cloves' in essential_spices}")