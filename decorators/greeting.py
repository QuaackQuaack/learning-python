#this program is to understand and revise decorator
#decorators takes function, modify them and return it
def greeting(fx): # fx represents the function 
    def mfx():
        print("good morning")
        fx()
        print('thanks for using our program')
    return mfx

@greeting
def hello():
    print("hello world")
    
hello()
