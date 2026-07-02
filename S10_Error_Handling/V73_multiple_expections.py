def process_order(item, quantity):

    try:
        price = {"masala": 20}[item]
        cost = price * quantity

        if cost > 0:
            print(f"The total cost is {cost}")
        else:
            raise TypeError
        
    except KeyError:
        print("Flavor is not valid")

    except TypeError:
        print("Quantity should be an integer")


process_order("masala", "two")
process_order("ginger", 2)