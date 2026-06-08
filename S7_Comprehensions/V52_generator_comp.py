'''
Generator comprehension sytax: ( expression/variable for variable in iterable if condition ).

Like list when we write [ x for x in iterable ] >>> this is a direct memory in our system and it creates a list directly.
But for generators ( x for x in iterable ) >>> this is like a stream, it doesnot give you the result directly, 
it rather behaves as a stream and can be used afterwards

'''

daily_sales = [3, 5, 18, 39, 20, 6, 8]

total_cups = sum( sale for sale in daily_sales if sale > 5 )

print(total_cups)