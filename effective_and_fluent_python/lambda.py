#lambda is to anonymous function means that function is without  a name 

def cube(x): # this is normal function example 
    return x*x*x 

lambda_cube = lambda y : y*y*y 

print('this is result of normal function', cube(5))

print('this is result of lambda functin ' , lambda_cube(5))
