# the best of converting existing array is to make copy of array with the astype() method

import numpy as np 
arr = np.array([1.1,2.2,3.3])
print(arr.dtype)

#using astype to convert
new_arr = arr.astype('S')
print(new_arr)
print(new_arr.dtype)

new_arr = arr.astype(int)
print(new_arr) # this convert arr to int so output will be in int like [1,2,3]
print(new_arr.dtype)


new_arr = arr.astype(bool)
print(new_arr)
