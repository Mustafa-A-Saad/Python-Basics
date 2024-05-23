#List Comprehension = a way to transform one list into another
# Dict Comprehension = ''''''''''''''''''''''''

"""
# Traditional Way
number = [1,2,3,4,5,6,7]
even = []

for n in number:
    if n%2==0:
        even.append(n)
print(even)


#Comprehension Way
even = [j for i in number if i%2==0]
print(even)


sqr_numbers=[i*i for i in number]
print(sqr_numbers)

s = set([1,2,3,4,5,2,3]) # an unorder of unique items , doesn't allow duplicate item
print(s)

even = {i for i in s if i%2==0}
print(even)
"""



# Dict Comprehensions
cities = ["mumbai","new york","paris"]
countries = ["india","usa","france"]

z = zip(cities,countries) # Zips together 2 lists and put them in tuples
print(z) # Zip object at adress 0x
for a in z:
    print(a)

d = {city:country for city,country in zip(cities,countries)} # Creates dictionary
print(d)

# Map Function works similar but Comprehensions are better

def make_even(num):
    if num%2==1:
        return num+1
    else:
        return num

x = [551,641,891,122,453,223,234,343,562,115,554,111,679,516]

#instead of this
#y = []
#for num in x:
#    y.append(make_even(num))
#print(y)

# map(function.iterator) applies the function on the iterator
y = list(map(make_even,x))
print(y) # gives map object so make it a list

# Comprehension way
y = [make_even(num) for num in x]
print(y)




