import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
print()

# same as below
for cell in a.flatten():
    print(cell)
print()
# Same as above
for cell in a.flat:
    print(cell)
print()
# Same as Above
for row in a:
    for cell in row:
        print(cell)
print()
# Same as above with using nditer
for x in np.nditer(a, order='C'):  # C order is going row by row
    print(x)
print()
for x in np.nditer(a, order='F', ):  # Fortran order is going by cols
    print(x)
print()
for x in np.nditer(a, order='F', flags=['external_loop']):  # puts every row as a list again
    print(x)
print()
for x in np.nditer(a, op_flags=["readwrite"]): # this modifies the original array
    x[...] = x * x
print(a)

b = np.arange(3,15,4).reshape(3,1)

for x,y in np.nditer([a,b]): # iterate 2 arrays ( they must have the same number of rows )
    print(x,y)