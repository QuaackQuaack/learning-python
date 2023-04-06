import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
print(a.shape)
print(a.reshape(4,3)) #this means 4 array of 3 elements 
#big bracket bitra 4 out ani inner big bracket bitra 3 ota elements 
print(a.reshape(2,3,2).base)

b = np.array([1,2,3,4,5,6,7,8])
x = b.reshape(2,4)
print(x)
