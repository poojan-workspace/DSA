snack = input("Enter your preferred snack: ").lower()

if snack in ("cookies", "samosa"):
    print(f"Order confirmed!! Your {snack} is on the way.")
else:
    print(f"{snack} is unavailable.")