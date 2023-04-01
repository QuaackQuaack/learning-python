
codes = 'ABC'
symbol = [ ord(x) for x in codes]
print(symbol) 

symbol = [ last := ord(x) for x in codes] # := this is walrus operator and remain accessible after comprehension 
print(symbol)
print(last) # walrus operator agadi ko value bhayera this last and give last value of  x 

