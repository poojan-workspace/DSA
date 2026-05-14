'''
continue: skips the current loop that satisfies the continue condition and goes on to the next step.
break: completely breaks out of the loop.
'''

flavors = ["mango", "orange", "apple"]
discontinued = ["banana", "strawberry"]
out_of_stock = ["kiwi"]

temp = True

while temp == True:
    user = input("Enter the flavor you want: ").lower()

    if user in flavors:
        print(f"Great choice! {user} flavor ice cream is on the way.")
    
    if user in discontinued:
        continue

    if user in out_of_stock:
        break