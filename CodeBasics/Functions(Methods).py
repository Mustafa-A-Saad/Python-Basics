def area(side1,side2,type):
    if type == "triangle":
        return (1/2)*side1*side2
    elif type == "rectangle":
        return side1*side2

print(area(5,5,"triangle"))
print(area(5,5,"rectangle"))