# a function that handles multiple tasks

import time
import threading

def calc_square(numbers):
    print("Calculate Square Numbers")
    for n in numbers:
       time.sleep(0.2)
       print("square:",n*n)

def calc_cube(numbers):
    print("Calculate Cube Numbers")
    for n in numbers:
       time.sleep(0.2)
       print("cubed:",n*n*n)

arr = [2,3,7,8]

t = time.time()

#Intialization
t1 = threading.Thread(target=calc_square,args=(arr,))
t2 = threading.Thread(target=calc_cube,args=(arr,))

# Starts the execution of the calc_square and calc_cube functions concurrently in separate threads.
t1.start()
t2.start()

#is used to wait for a thread to complete its execution before moving on to the next steps in the program.
# This means that the main program will wait at these points until the corresponding threads (t1 and t2) complete their tasks or sleeps .
t1.join()
t2.join()

#calc_square(arr) # instead of calling each one alone and be time consuming use Threads
#calc_cube(arr)

print("Done in:",time.time()-t)
print("Hah....Im done with all my work now")
print(threading.active_count())
# Using threading allows the program to perform the square and cube calculations
# simultaneously, potentially reducing the overall execution time compared to
# performing the tasks sequentially.

#Threads Project

import time
import threading
from threading import Thread

def sleepMe(i):
    print(f'Thread {i} will sleep.')
    time.sleep(5)
    print(f'Thread {i} is awake')

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print(f'Current Threads:{threading.active_count()}.')
