a = [[1,2,3],[4,5,6]]
result = [[0,0],[0,0],[0,0]]

for i in range(len(a[0])):
    for j in range(0,len(result[0])):
        result[i][j] = a[j][i]

for r in result:
    print(r)
        
