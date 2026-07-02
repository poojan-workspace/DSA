class InvalidChaiError(Exception): pass

def order_chai(flavor, cups):

    menu =  {"masala": 20, "ginger": 30, "lemon": 40}

    try:
        if flavor not in menu:
            raise InvalidChaiError("Unknown flavor...")
        if not isinstance(cups, int):
            raise TypeError("Number of cups should be whole number")
        
        total = menu[flavor] * cups
        print(f"The total bill is: {total}")

    except Exception as e:
        print("Error: ", e)

    finally:
        print("Next customer...")

order_chai("masala", 4)
order_chai("elaichi", 4)
order_chai("lemon", "four")
