# Try and Catch
try:
    value=10
    number = int(input("Enter a number "))
    print(number)
    print(value)
    answer = value/number
except ZeroDivisionError as err: # you can put the error as a variable
    print("You can't divide by Zero")
    print(err)
except ValueError:
    print("Invaild Input")
finally:
    print("This gonna print anyway")


