'''
Scopes and Name Resolutions:
1. Local - inside a function
2. Enclosing from outer function if nested
3. Global - Top level script
4. Built in

'''

# 1. Local Scopes
def chai_order():
    chai_type = "lemon"
    print(f"Inner local scope variable: {chai_type}")

chai_type = "Mint"
print(f"Outer global scope variable: {chai_type}")
chai_order()


# 2. Enclosing from outer function if nested
def chai_counter():
    chai_order = "Lemon" # Enclosing

    def print_order(): # It can access the varibales only inside its own function and Global variables, and not its parent function.
        chai_order = "Mint"
        print(f"Nested function: {chai_order}")
        print(f"{chai_type}") # from global variable

    print_order()

    print(f"Outer function: {chai_order}")

chai_counter()