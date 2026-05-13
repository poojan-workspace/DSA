# int() method >> converting user input into an integer
# similary float()

# ternary operator is when we put condition while declaring the varibale itself.

order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30 # ternary operator

print(f"The delivery fees is {delivery_fees}")