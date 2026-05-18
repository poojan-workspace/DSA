'''
Pure vs Impure functions:
>>> Pure functions are those who does not hinder or touch any of the global variables in the code.
>>> Impure functions are those who does hinder or update global variable in the code. 
'''

def pure_func(count):
    count = 2
    return count

total_bill = 100

def impure_func(count):
    global total_bill
    total_bill += count
    return count, total_bill

'''
Recursive function: A function that calls itself in a loop until some condition is satified to stop it.
'''

def start_func(count):
    if count == 0:
        return "Count is 0"
    print(count)
    return start_func(count-1)
print(start_func(4))


'''
Lambda function: Anonymous functions
'''

chai_types = ["ginger", "mint", "black", "mint"]

mint_chai = list(filter(lambda chai_order: chai_order == "mint", chai_types))
non_mint_chai = list(filter(lambda chai_order: chai_order != "mint", chai_types))

print(mint_chai)
print(non_mint_chai)