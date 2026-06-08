order = [
    "Masala chai", "Green tea", "Samosa",
    "Masala chai", "Lemon tea", "Green tea", "Samosa"
]

# Set is just a unique list, so in list comprehension we did [], here we have to do {}
# { expression/variable for variable in iterable if condition }

unique = { item for item in order } # we dont need the condition as set automatically contains only unique elements of the list.

unique_with_condition = { item for item in order if len(item)> 10 }

print(unique)
print(unique_with_condition)


recipes = {
    "Masala Chai": ["ginger", "cardamon", "clove"],
    "Elaichi Chai": ["cardamon", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

unique_1 = { spice for ingredients in recipes.values() for spice in ingredients }
print(unique_1)