def add(x,y):
    return x+y
print(add(4,5))

# Lambda Function : they work like a simple function ( Method ) but it is usually used when we want to pass it on a higher-order function
# higher-order function is a function which returns a function or takes a function as a argument or both
# Lambda Function can only have a single line expression like ( x + y ) and it doesn't have return as this acts like it
# Also called Anonymous functions , which mean they can work without an identifer ( variable ) , but you can add a variable ( not recommanded )

add2 = lambda x,y:x+y
print(add2(4,5))

print((lambda x,y:x+y)(4,5))

# higher-order function ex:

def my_map(my_func,my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return(result)

nums = [3,4,5,6,7]

cubed = my_map(lambda x:x**3,nums)
print(cubed)




