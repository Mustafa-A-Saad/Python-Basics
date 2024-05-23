
x =  float(input("Enter Your 1st Number"))
op = input("Enter Operator: ")
y =  float(input("Enter 2nd Number"))

if op == "add":
    print(x+y)
elif op == "sub":
    print(x-y)
elif op == "multi":
    print(x*y)
elif op == "div":
    print(x/y)
else:
    print("Invalid Operator")
