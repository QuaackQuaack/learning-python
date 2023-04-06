
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)): #1 to 4
            if a[i] < a[i-1]: #this compare first letter of the elements
               a[i], a[i-1] = a[i-1] , a[i] 

names = ['pretzels','carrots','argula','bacon']
bubble_sort(names)
print(names)

