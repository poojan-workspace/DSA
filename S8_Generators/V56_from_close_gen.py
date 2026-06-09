'''
Yield from
close
'''

def local_chai():
    yield "Masala Chai"
    yield "Ginger chai"

def imported_chai():
    yield "Oolong Tea"
    yield "Matacha"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

'''
Iteration 1: yield from local_chai() >>> exit
Iteration 2: yield from local_chai() >>> exit
Iteration 3: yield from imported_chai() >>> exit
Iteration 4: yield from imported_chai() >>> exit
'''



def chai_stall():
    try:
        while True:
            order  = yield "Preparing order"
    except:
        print("Order done!!")


stall = chai_stall()
print(next(stall))
stall.close()