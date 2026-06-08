menu = [
    "Iced lemon tea",
    "Masala chai",
    "Ginger tea",
    "Cardomom tea",
    "Iced peach tea"
]

# sytax = [ expression/variable for variable in iterable if condition ]

iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea)