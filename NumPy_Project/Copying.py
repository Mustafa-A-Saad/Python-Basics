import numpy as np

a = np.array([1,2,3])
print(a)


# don't do the following as it causes problems
#b = a
#b[0] = 100 # so here you acutally change b and a when we want to change only b
#print(b)
#print(a)

# use the copy method
b = a.copy()
b[0] = 100
print(b)
print(a)



