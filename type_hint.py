#still confuse in this part need to looks geeks for geeks
def add1(a,b):
    return(a+b)

a = input('first number')
b = input('second number')

value = add1(a,b)  #here if the input is 3, 4 it will return 43
print(type(value))
#now using type hint we will get

def add2(a: int,b: int) -> int:
    return(a+b)


a = input('first number ')
b = input('second number ')

value2 = add2(a,b)
print(type(value2))
