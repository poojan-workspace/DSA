file = open("order.txt", "w")

try:
    file.write("Masala chai is ready....")
finally:
    file.close()

file = open("order.txt", "w")
try:
    file.write("Lemon chai is ready....")
finally:
    file.close()