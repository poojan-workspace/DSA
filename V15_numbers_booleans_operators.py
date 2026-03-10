'''
Numbers:
    1. Integers
    2. Booleans
    3. Real >> Floating or Decimal
    4. Complex or Imaginary Number >> 2+3i


* is multiply
/ is divide
// is divide without decimals
% is remainder
** is exponential
    
'''


#### Integers

tea_grams = 14
ginger_grams = 3

total_tea_grams = tea_grams + ginger_grams
print(f"Total tea grams is {total_tea_grams}")

remaining_grams = tea_grams - ginger_grams
print(f"Remaining grams is {remaining_grams}")


milk_litres = 7
servings = 4
tea_per_serving = milk_litres / servings
print(f"Tea per servings is {tea_per_serving}")

total_tea_bags = 9
pots = 4
bags_per_pot = total_tea_bags // pots #rounded off by removing the decimals no matter higher or lower
print(f"Whole bags per pot is {bags_per_pot}")

total_cardomom_pods = 10
pods_per_cups = 3
leftover_pods = total_cardomom_pods % pods_per_cups # % gives you the remainder of the division, so 10/3 remainder is 1.
print(f"Leftover pods are {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor # ** gives you the exponential value so like here 2 to the power of 3.
print(f"Powerful flavor is {powerful_flavor}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves are {total_tea_leaves_harvested}")




#### Boolean

is_boiling = True # True is also counted as 1 and False as 0 in python
stiring = False

stir_count = 5
total = stir_count + is_boiling #upcasting where True is converted into 1 as integer and False will be 0
print(f"Total is {total}")

# similarly reverse is also true, if we have 1 or 0 as a var then it can convert into True or False resp. using bool() function
milk_present = 0
print(f"Is milk present? {bool(milk_present)}")

# logical operations in boolean are (and, or, not)
water_hot = True
tea_added = True

can_serve = water_hot and tea_added
print(f"Can we serve tea? {can_serve}")



#### Real or FLoating or Decimal numbers

import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
curr_temp = 95.49999999999

print(f"Difference between both temp: {ideal_temp - curr_temp}")
print(sys.float_info)