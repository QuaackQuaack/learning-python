#! usr/bin/env/python3
import numpy as np

#to check data types of numpy, we use dtype

a = np.array([1,2,3,4,5]) #this is int64
print(a.dtype) 
b = np.array(['apple','banana','cat']) #this is <U6 , little edian Unicode of 6 byte 
print(b.dtype)

#creating data type with defined data type

arr = np.array([1,2,3,4], dtype = 'S')
print(arr.dtype)
print(arr)
arr = np.array([[1,2,3,4],[1,2,3,4]],dtype = 'S1')
print(arr.dtype)
print(arr)

#we can also define size along with data types
arr = np.array([1,2,3,4], dtype = 'i2') # i2 = int16 , i4 = int32 , i8 = int64 
print(arr.dtype)
