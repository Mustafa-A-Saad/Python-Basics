import argparse

# this program should take 2 numbers and an operation ( + - * )
# run on cmd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1",help="first number")
    parser.add_argument("number2",help="second number")
    parser.add_argument("operation",help="operation",choices=["add","subtract","multiply"]) # choices is a limiter user can only choice those
    # If you add an Positional Argument like above u must add it in CMD
    parser.add_argument("--number3",help="Thrid number ( Optional )")
    # Two types of Arguments = Positional,Optional

    args = parser.parse_args() # haves the value of argument that the user pass through CommandLine

    # to run this cmd ( make sure of directory ) python Argparse.py -h
    print(args.number1)
    print(args.number2)
    print(args.number3)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    n3 = int(args.number3)
    result = None
    if args.operation == "add":
        result = n1+n2
    elif args.operation == "subtract":
        result = n1-n2
    elif args.operation == "multiply":
        result = n1*n2
    print(result)

# for optional Arguments you must add --(name of arguemnt(--number3)) and your number
    if args.operation == "add":
        result = n3**3
        print(result)

"""
import argparse

def valid_mark(mark):
    mark = int(mark)
    if mark < 0 or mark > 100:
        raise argparse.ArgumentTypeError("Marks must be between 0 and 100")
    return mark

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", type=valid_mark, help="Grade of Physics") # type here is to restrict user to put from 0-100
    parser.add_argument("--chemistry", type=valid_mark, help="Grade of Chemistry")
    parser.add_argument("--maths", type=valid_mark, help="Grade of Maths")
    parser.add_argument("average", help="gets the average of 3")

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)

    m1 = args.physics
    m2 = args.chemistry
    m3 = args.maths
    result = 0

    if args.average == "avg":
        result = (m1 + m2 + m3) / 3
        print(result)
"""