
def simpleGenerator():
    yield 1 
    yield 2 
    yield 3

for value in simpleGenerator():
    print(value)
