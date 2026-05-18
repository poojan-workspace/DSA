chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42


print(f"{chai}")

edit_chai(chai)

print(f"{chai}")

# Arguments: Positioning and keywords

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Ginger", "Yes", 2) # Positioning
make_chai(sugar=3, tea="Lemon", milk="Yes please") # Keywords


# *args and **kwargs: Arguments and Keyword Arguments

def chai_order(*ingredients, **extras):
    print("Ingredients are:", ingredients)
    print("Extras are:", extras)

chai_order("Cinnamon", "Ginger", sugar='2', masala='Yes') # Write in order, first all without keywords will go under "ingredients" variable
                                                        #   Second all with the keywords will go under "extras" variable


# Default values in function arguments.
def chai_type(order=None): # None means if no arguments are passed in the "order" variable then dont do anything.
    if order is None:
        order = []
    print(order)

chai_type("Lemon")
chai_type()