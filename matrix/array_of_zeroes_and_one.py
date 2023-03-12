import numpy as np 

zero = np.zeros((2,3)) # here (2,3) means matrix of 2 by 3
print(zero)

one = np.ones((3,3)) #here (3,3) means matrix of 3 by 3

for r in one:
    print(r)

#we can specify dtype(data type) of matrix for e.g
one = np.ones((2,2), dtype = np.int32) #specific dtype i.e integer 32 byte
