'''
Enumerate: Numbered list in python
Whenever we want to use a numbered list in a for loop or to make another loop then we use enumerate().

>>> seasons = ['Summer', 'Winter', 'Monsoon', 'Fall']
>>> list(enumerate(seasons)) # make another list but this time number each element of "seasons" list
>>> [(0, 'Summer'), (1, 'Winter'), (2, 'Monsoon'), (3, 'Fall')]

>>> list(enumerate(seasons, start=1)) # this makes the enumerate start from 1 instead of default 0
>>> [(1, 'Summer'), (2, 'Winter'), (3, 'Monsoon'), (4, 'Fall')]

'''

menu = ["Lemon", "Green", "Spiced", "Mint"]

for index, item in enumerate(menu, start=1):
    print(f"{index}: {item} chai")