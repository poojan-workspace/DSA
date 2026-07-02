def brew_chai(flavor):

    if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Unknown chai flavor...")
    else:
        print(f"Brewing your {flavor} chai...")


# brew_chai("lemon")
brew_chai("masala")


# Custom Exceptions: to create custom exceptions we need to create a custom class and point it to the class for raising the error.


class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):

    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("Your chai is ready...")

make_chai(0, 1)