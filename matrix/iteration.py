import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
for i in a:
    for y in i:
        print(y)

#iterating through nditer()
for i in np.nditer(a):
    print(i)
