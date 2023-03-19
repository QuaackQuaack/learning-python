n = int(input())
b = list()
for i in range(0,n): 
    a = input('')
    b.append(a)

maximum = max(b)
result = [x for x in b if x != maximum]
final_result = max(result)
print(final_result)


