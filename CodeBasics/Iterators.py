"""# Basics
a = ["hey","bro","you're","awesome"]
for i in a:
    print(i)

#for key in {'one':1,'two':2}:
#    print(key)

itr = iter(a) # iterates a one by one
print(itr) # prints the list iterator object at an address
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(dir(a)) # shows u the available methods and attributes u can add to a function

b = ["Tefa","Boogey","Bob","Ricky"]
itr2 = reversed(b) # Starts from backwards
print(next(itr2))

"""

""" #Remote TV Project
"""
class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","CNN","ABC","ESPN"]
        self.index = -1

    def __iter__(self): # if u use this u must have __next__ method
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        # else
        return self.channels[self.index]

r = RemoteControl()
itr = iter(r) # is calling __iter__self method
print(next(itr)) # is calling __next__self method
print(next(itr))
print(next(itr))

""" # Fibonacci Series Project

# Undetermined Series
class Fibonacci:
    def __init__(self, limit):
        # default constructor
        self.previous = 0
        self.current = 1
        self.n = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.limit:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n += 1
            return result
        else:
            raise StopIteration


# init the fib_iterator
fib_iterator = iter(Fibonacci(5))
while True:
    # print the value of next fibonacci up to 5th fibonacci
    try:
        print(next(fib_iterator))
    except StopIteration:
        break
        
"""

""" 
# Determined List Fib_Series
class Fib_Series:
    def __init__(self):
        self.series = [0, 1, 1, 2, 3, 5]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.series):
            raise StopIteration
        #else
        return self.series[self.index]


fs = Fib_Series()
itr = iter(fs)
while True:
    try:
        print(next(fs))
    except StopIteration:
        break
        
"""

