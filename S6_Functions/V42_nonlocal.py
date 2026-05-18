'''
"Nonlocal" variable in python.
'''


def update_order():
    chai_type = "Lemon" # We can access the "nonlocal" variable of the parent function and update it if needed i our child function as well.

    def kitchen():
        nonlocal chai_type
        chai_type = "Mint"
    
    kitchen()
    print(f"The new flavor is: {chai_type}")

update_order()


'''
"Global" variable access in python.
Use it very caustiously
'''

chai_type = "Plain"

def update_order():
    def kitchen():
        global chai_type # We can access the "global" variable as well just how we can access the "nonlocal" one and update it
        chai_type = "Best"
    kitchen()

update_order()
print(f"The updated chai type is : {chai_type}")
