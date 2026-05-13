'''
Dictionaries: Key or Name & Value pairs
It is a function.
Order does not matter in a dictionary because we reference it the key or name rather than indexes like 0, 1, 2.
'''


chai_order = dict(chai_type="Masala chai", name='Poojan', sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {} # Empty Dict
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"The chai recipe is : {chai_recipe}")
print(f"The base of chai recipe is: {chai_recipe['base']}") # Basically this is saying chai_recipe[1] index 1, so we have to provide index or name or key to get the value at that index.


del chai_recipe["liquid"] # To remove or delete a Key inside a dict.
print(f"The chai recipe is : {chai_recipe}")


print(f"Is sugar in chai_order dictionary? {'sugar' in chai_order}")


chai_order = {"type": "Masala chai", "name": 'Poojan', "sugar": 2}

print(f"Printing the keys of chai_order: {chai_order.keys()}")
print(f"Printing the values of chai_order: {chai_order.values()}")
print(f"Printing the items of chai_order: {chai_order.items()}")

# Pop item in Dict >> it will pop the last item in the dict same as every other datatype
popped_item = chai_order.popitem()
print(f"Popped Item: {popped_item}")

# Update dict >> works exactly as extend in list or array
chai_order.update(chai_recipe)
print(f"The updated order is : {chai_order}")


# .get function allows you to get the key if its present in the dict or send a message if not.
# Better for error handling so that the entire code will not crash.
customer_note = chai_order.get("note", "No note")
print(f"The customer note is : {customer_note}")
customer_note = chai_order.get("type", "No note")
print(f"The customer note is : {customer_note}")

print(f"Id of chai_order is: {id(chai_order)}")
chai_recipe["liquid"] = "milk"
chai_order.update(chai_recipe)
print(f"Id of chai_order is: {id(chai_order)}")