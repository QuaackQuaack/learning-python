a = [[1,2,9],[4,5,6]]
b = [[9,8,7],[6,5,4]]

result = [[0,0,0],[0,0,0]]

for i in range(len(a)):
    #print('the value of i is',i)
    for j in range(0,len(a[0])):
        print("the value of j is ",j)
        result[i][j] = a[i][j] + b[i][j]

for r in result:
    print(r)
