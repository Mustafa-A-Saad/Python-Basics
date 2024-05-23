basket = {"orange","apple","mango","apple","orange"} # sets doesn't allow duplicate elements , and its unordered , doesn't have index
print(f'type of the basket is {type(basket)}')
print(basket)


# Another way to set up a set
a = set()
a.add(1)
a.add(2)
print(f'a is {a}')

#Another way to set up a set
b = set([1,2,3,4,5,2,3])
print(f'b is {b}')

#print(basket[0]) # Can't because its unordered ,can't use index

# Conversion from list to set
numbers = [1,2,3,4,2,3,4]
unique_numbers = set(numbers)
print(f'unique_numbers is {unique_numbers}')

#Frozen Sets # same as sets but you can't add in frozen sets
fs = frozenset(numbers) # you must assign it to a new variable
print(fs)
#fs.add() # Can't because its a frozen set

x = {"a","b","c"}

print("a" in x)
for i in x:
    print(i)

y = {"a","g","h"}

print(x|y) # Union of x and y and removes duplicates ( "or" )
print(x&y) # Intersection ( "And" )
print(x-y)
print(x.difference(y))
print(y.difference(x))
print(x<y) # x subset y