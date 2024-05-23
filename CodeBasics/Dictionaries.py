"""    #Population Dictionary Project

population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add: ")
    country = country.lower()
    country = country.strip()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()

def remove():
    country = input("Enter country name to remove: ")
    country = country.lower()
    country = country.strip()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country] # Same as below
   # population.pop(country)
    print_all()

def query():
    country = input("Enter country name to query: ")
    country = country.lower()
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} ")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

op=input("Enter operation (add, remove, query or print): ")
if op.lower() == 'add':
    add()
elif op.lower() == 'remove':
    remove()
elif op.lower() == 'query':
    query()
elif op.lower() == 'print':
    print_all()

"""
import pprint

"""  #Stock Prices Project

import statistics
stocks = {
    "info" : [600,630,620],
    "ril" : [1430,1490,1567],
    "mtl" : [234,180,160]
}

def print_all():
    for stock,price_list in stocks.items():
        avg = statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg: ",round(avg,2))

def add():
    ticker = input("Enter a Stock Name: ")
    price1 = int(input("Enter a price for Your stock: "))
    price2 = int(input("Enter a price for Your stock: "))
    price3 = int(input("Enter a price for Your stock: "))
    ticker = ticker.lower().strip()
    if ticker in stocks:
        stocks[ticker].append(price1)
        stocks[ticker].append(price2)
        stocks[ticker].append(price3)
    else:
        stocks[ticker] = [price1, price2, price3]
    print_all()

op = input("Input a Operator('print or add'): ")
op.lower()
if op == "print":
    print_all()
if op == "add":
    add()
"""

"""
# tips

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.') # a get() method that takes two arguments: the key of the value to retrieve
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.') # and a fallback value to return if that key does not exist.

#The first argument passed to the method is the key to check for, and the second argument is the value to set at that key if the key does not exist.
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)

# Counts of char
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}
for character in message:
    count.setdefault(character, 0) # does all the commented below part in 1 line
    #if character not in count:
    #    count[character] = 1
    #else:
    count[character] += 1

print(count)

pprint.pprint(count) # Pretty Print , displays it better
# print(pprint.pformat(count)) # same as above
"""

""" # Nest Data Structure

allGuests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}


def totalBrought(guests,fruit):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(fruit,0) # v is the dictionary of fruits , thats why u can use .get()
    return numBrought


print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
"""



