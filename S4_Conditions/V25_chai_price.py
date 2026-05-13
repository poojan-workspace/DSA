chai_size = input("Enter your chai cup size (Small, Medium, Large): ").lower()

if chai_size == "small":
    print(f"Your chai price is $10")
elif chai_size == "medium":
    print(f"Your chai price is $15")
elif chai_size == "large":
    print(f"Your chai price is $20")
else:
    print(f"Please input a valid size!!")