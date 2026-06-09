from functools import wraps

def logger_function(func):
    @wraps(func)

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger_function
def chai_type(type):
    print(f"Brewing {type} chai")

chai_type("Masala")