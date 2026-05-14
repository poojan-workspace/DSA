'''
for-else loop is quite interesting and you can see the below example.
If nothing in for loop satifiies the condition or breaks out of the loop then the else will run.
'''

staff = [("Amit", 16), ("Bane", 17), ("Chris", 15)]

for name, age in staff:
    if age <= 18:
        print(f"You are hired! {name}")
        break
else:
    print(f"No one is eligible for the staff position.")