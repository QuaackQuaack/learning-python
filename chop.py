word = input('enter a word \t')
def chop(wo):
    wo = list(wo)
    del wo[0]
    del wo[-1]

def middle(mid):
    mid = list(mid)
    del mid[0]
    del mid[-1]
    return mid 
    
result = chop(word)
print(result)

mid_result = middle(word)
space = ''
mid_result = space.join(mid_result)
print(mid_result)
