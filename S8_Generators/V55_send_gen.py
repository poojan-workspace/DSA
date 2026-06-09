def chai_order():
    print("What would you like to have?")

    order  = yield # Every yield just pauses the function there until the next instruction is sent.

    while True:
        print(f"Preparing {order}")
        order = yield # This just pause the function in between

stall = chai_order()
next(stall)

stall.send("Masala chai")
stall.send("Lemon tea")