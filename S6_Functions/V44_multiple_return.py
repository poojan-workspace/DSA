'''
1. return Nothing
2. return One value
3. return Multiple values
4. return Early from a function
'''

# 1. return Nothing

def chai_1():
    pass # or return None
print(chai_1())

# 2. return One value

def chai_2():
    return 120
print(chai_2())

# 3. return Multiple values

def chai_3():
    return 100, 20 # sold, remaining

sold, remaining = chai_3()
print(sold, remaining)

# 4. return Early from a function

def chai_4(chai_type):
    if chai_type == 0:
        return 0
    return chai_type

print(chai_4(4))
print(chai_4(0))


