'''
Usually in "if" statements we only put to check Yes and No conditions or True and False.
With walrus operator, we can take input, declare variable, evaluate and check for condition at the same time in one line.
'''


# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Remainder is: {remainder}")

# Example 1:
value = 13

if (remainder := value % 5):
    print(f"Remainder is: {remainder}")


# Example 2: using walrus operator, requested_size variable is auto declared, 
# we can take input on the same line and check if or condition is true on the same line.

available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Your size is available.")
else:
    print(f"Please select a valid size.")



# Example 3: walrus is just used to declare and evaluate at the saem time while checking the condition outside the parenthesis

flavors = ["masala", "mint", "lemon", "black"]

while (flavor := input("Enter your chai flavor: ")) not in flavors:
    print(f"{flavor} is not available, please choose another one.")

print(f"Great choice! Your {flavor} chai is on the way.")