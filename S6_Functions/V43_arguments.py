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