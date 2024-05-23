# Related Modulues and Pip
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", " Paul McCartney","George Harrison","Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index("."):]

def roll_dice(num):
    return random.randint(1,num)

print(get_file_ext("funny.txt"))