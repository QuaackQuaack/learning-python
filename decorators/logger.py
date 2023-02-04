#this is an example of closure property of python

import logging
logging.basicConfig(filename='example.log',level = logging.INFO)

def longer(func):
    def log_func(*args):
        logging.info(f'Running "{func.__name__}" with arguments {args}')
        print(func(*args))

    return log_func

def add(x,y):
    return x + y 

def sub(x,y):
    return x - y

add_longer = longer(add)
sub_longer = longer(sub)

add_longer(10,9)
add_longer(19,1)
sub_longer(12,4)
sub_longer(10,2)

