def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(2, 40)

print(f"{my_bill}")

print(f"My total bill is: ",calculate_bill(2, 40))


# Example 2: Traceablility

def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)

    print(f"The original price is: {price}, and final amount is {final_amount}")
