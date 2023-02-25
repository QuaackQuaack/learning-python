t = [ 3,4,2,4,5,6,7,7,2,4]
ok = list()
for x in range(0,len(t)):
    word = t[x]
    if (word in ok) == False:
        ok.append(word)
        
ok.sort()
print(ok)
