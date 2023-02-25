word = 'banana'
result = {}
for repeat in word:
    result[repeat] = result.get(repeat,0) + 1
print(result)


