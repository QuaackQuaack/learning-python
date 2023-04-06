import numpy as np

arr = np.array([1,2,3,4,5,6])
x= arr.copy()
print(x.base)
arr[0] = 32
print(arr)
print(x)

x = arr.view()
print(x.base) 
arr[0] = 21
print(x)
print(arr)


