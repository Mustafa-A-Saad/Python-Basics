import numpy as np

filedata = np.genfromtxt("data.txt",delimiter=",") # works similar to split function
print(filedata) # every new line is his own array too
filedata = filedata.astype("int32") # default like above is float , if u want integer do this
print(filedata)



