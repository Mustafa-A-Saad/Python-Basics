


# Pizza Project

# size have a definite range ( S,M,L ) and only 1 can be picked
# putting *before something unpacks an iterator (for,while,list,etc..) ( Unpacking Operator )
nums = [1,2,3,4]
print(*nums)
print()
# but topping can be multiple , so we must *args to put as many topping as we want
# *args can be named smth else like *topping , but its the standard to use *args
# *args puts them in a tuple

# **kwargs can also be multiple parameters but this need to have key,value pairs
# **kwargs puts them in a dictionary


def order_pizza(size,*toppings,**details):
    print(f'Ordered a {size} pizza with the following toppings')
    for topping in toppings:
        print(f'- {topping}')
    # print(toppings) # *args tuple example
    print("Details of the Delivery")
    for key,value in details.items():
        print(f"-{key} : {value}")
   # print(details) # **kwargs dictionary example



order_pizza("Large","Pepperoni","olives",Delivery = True,Tip = 5)