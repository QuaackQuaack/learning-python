
codes = 'ABC'
symbol = [ ord(x) for x in codes]
print(symbol) 

symbol = [ last := ord(x) for x in codes] # := this is walrus operator and remain accessible after comprehension 
print(symbol)
print(last) # walrus operator agadi ko value bhayera this last and give last value of  x 


#another example of walrus operator is that 

while(user_input := input('enter you name dwag? , leaving blank will abort')):
    print(f'you have entererd {user_input}')

#doing same program by normal way

while True:
    user_inputs = input('enter you name dwag?, leaving blank will abort it')
    if not user_inputs:
        break
    print(f'you have entered {user_input}')
