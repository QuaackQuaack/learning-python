#in this program we will learn passing arguments in  decorators 
#using *args and **kwargs we can pass arguments in decoratos

def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs) #args pass tuple and kwargs pass dictionary key value
        print("it was nice running this program\n")
    return mfx

@greet
def hello():
    print("hello, welcome to this program")
hello()

@greet
def add(a,b):
    print(a+b)

add(1,2)
