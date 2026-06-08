'''
Generators are like a stream. It gives you value one by one.
>>> Yield instead of return

Yield actually pasues the generator function from the first yield and 

'''


def print_chais():
    yield "Chai 1: Masala Chai"
    yield "Chai 2: Ginger Chai"
    yield "Chai 3: Elaichi Chai"

stall = print_chais()

for x in stall:
    print(x)


def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))

print(next(chai))