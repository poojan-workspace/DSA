'''
Dictionary is not automatically iterable, we have to make it iterable by specifing
what are we iterating through if it's key then .keys(), for values it's .values() and for pair in general its .items()
.items()
.keys()
.values()
'''

tea_prices_rupees = {
    "Masala Chai": 40,
    "Lemon Tea": 50,
    "Mint Tea": 60
}

# synatx is same as set = { expression/variable for variable in iterable if condition }

tea_prices_usd = { tea:prices / 80 for tea, prices in tea_prices_rupees.items() } # Expression is key:value pair here

print(tea_prices_usd)