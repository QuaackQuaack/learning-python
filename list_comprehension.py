if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    #to print all possible outcome 
    result = list()
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                final = [i,j,k]
                result.append(final)
    result.sort() 
    final_result = list()

    for l in (result):
        if sum(l) != n:
            final_result.append(l)
    
    print(final_result)


                
               
