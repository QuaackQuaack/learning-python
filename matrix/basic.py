a = [[1,2,3],[4,5,6],[7,8,9]] # this is actually 2 by 3 matrix.\
print(a)
print(a[0]) # row by coloum so this represents first row 
print(a[1][1])# this represent 2nd row , 2nd coloumn
print(type(a[1][1]))
print(type(a))

#to print coloumn for example 3rd coloumn
coloumn = list()
for row in a:
    #print(row)
    coloumn.append(row[2])
    #print(coloumn)

print(f'so the 3rd coloumn element are {coloumn}')
