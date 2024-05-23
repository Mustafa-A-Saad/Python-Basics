# Decorators = allows you wrap your function in another function
import time

#Explaintion of *args and **kwargs
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__+" took "+str((end-start)*1000)+" milliseconds")
        return result
    return wrapper

@time_it # this to decrorate an class or method
def cal_square(numbers):
   # start = time.time() # to calculate how much time the method takes
    result = []
    for number in numbers:
        result.append(number*number)
   # end = time.time()
   # print("calc_square took "+str((end-start)*1000) + " milliseconds")  # *1000 to convert from second to millisecond
    return result
@time_it
def calc_cube(numbers):
  #  start = time.time() # calculates how much time it takes
    result = []
    for number in numbers:
        result.append(pow(number,3))

   # end = time.time()
   # print("calc_cube took " + str((end - start) * 1000) + " milliseconds")  # *1000 to convert from second to millisecond
    return result

array = range(1,10000)
out_square = cal_square(array)
out_cube = calc_cube(array)



"""#Factorial Decorater Project
def check(func):
    def helper(x):
        if type(x) == int and x >= 0:
            return func(x)
        else:
            raise ValueError("Argument is not a non-negative integer")
    return helper

# func = factorial ( the function that is passed )
# the x parameter in helper is = n parameter in factorial
@check
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

nums = [3,2.7,4,5,-5,10,-2,3.14]

for i in nums:
    try:
        result = factorial(i)
        print(f"the Factorial of {i} is : {result}")
    except ValueError:
        print(f"Error {ValueError}")
"""