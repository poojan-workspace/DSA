'''
__ is called dunder in python, so whenever we write __doc__: we say dunder doc


'''

def chai_order(chai_type="masala"):
    """This is a doc string of the function. It always comes on the first line of the function.
    We can access it via .__doc__"""
    return chai_type

print(chai_order.__doc__)
print(chai_order.__name__)