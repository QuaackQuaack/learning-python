a = 'banana'
index = 0 

def count(word,counter):
    for letter in word:
        if letter == "a":
            counter = counter + 1
    return counter

result = count(a,index)
print(result)
