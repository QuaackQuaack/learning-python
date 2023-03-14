a = [[1,2,3],[4,5,6]] #this matirx is 2*3
b= [[9,8],[6,5],[3,2]]# this matrix is of 3*2

result = [[0,0],[0,0]] #result will be of 2*2
try:
    for i in range(len(a)): 
        for j in range(0,len(b[0])): 
            for k in range(0,len(b)): #for k range we need len of formed one
                #print(f'[k][j] = [{k}][{j}]')
                result[i][j] += a[i][k] * b[k][j]
except:
    print("please enter a valid matrix for mulitple ")

for r in result:
    print(r)

