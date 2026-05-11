'''
Strings are immutable. We can only change the reference of the string.
'''

chai_type = "Ginger chai"
customer_name = "Poojan"

print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"First word : {chai_description[0:8]}") # [0:8] : [first index : last - 1 index]
print (f"Word : {chai_description[0:8:2]}") # [0:8:2] it will go from Oth index to 7th index and skip every second character >> Aoai

# Go till the 7th index
print(f"Word: {chai_description[:8]}")

# Start from 12th index and go till end
print(f"Word: {chai_description[12:]}")

# Reverse a string using ::-1
print(f"Reverse string: {chai_description[::-1]}")

# Encoding and Decoding a string to and from different languages
label_name = "Chai SpÈcial"
encoded_label = label_name.encode("utf-8")

print(f"Encoded text: {encoded_label}")
decoded_text = encoded_label.decode("utf-8")

print(f"Decoded text: {decoded_text}")