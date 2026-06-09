from functools import wraps

def auth_function(func):
    @wraps(func)

    def wrapper(user_role):
        if user_role != 'admin':
            print("Access denied!!")
        else:
            return func(user_role)
    return wrapper

@auth_function
def access_inventory(role):
    print(f"Access is granted to {role}")

access_inventory("Member")
access_inventory("admin")