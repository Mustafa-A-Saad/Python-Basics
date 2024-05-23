"""#Basics

# Similar to Iterators but better ( Generators )
def remote_control_next():
    yield "cnn"
    yield "espn"

itr = remote_control_next()
print(itr) # Generator Object
print(next(itr))
print(next(itr))

for c in remote_control_next():
    print(c)
"""

"""
def fib():
    a,b = 0,1
    while True:
        yield a
        a,b =b,a+b

for f in fib():
    if f>50:
        break
    print(f)
"""


def fetch_lines(filename):
    with open(filename,"r") as file:
        lines = []
        for line in file:
            lines.append(line)
        return lines

zen = fetch_lines("Poem.txt")
print(zen)

# Yield is memory efficient here you can just take a couple of lines that you need , not return the whole file lines
def fetch_lines2(filename):
    with open(filename,"r") as file:
        for line in file:
            yield line

# When you print (next) we erased the previous line from memory
zen2 = fetch_lines2("Poem.txt")

print(next(zen2))
print(next(zen2))
print(next(zen2))
print(next(zen2))
print(next(zen2))


""""# Squaring numbers

def next_square():
    i = 1
    while True:
        yield i * i
        i += 1

for n in next_square():
    if n > 2100:
        break
    print(n)
"""
