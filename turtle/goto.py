import turtle
import random
pen = turtle.Turtle()
pen.color('blue')
pen.pensize(2)
pen.speed(1)
def moving(x,y):
    pen.up()
    pen.goto(x,y) # goto is used with .up and .down to move turtle without drawing 
    pen.down()

for i in range(0,4):
    pen.forward(100) #also can be written as fd(100)
    pen.stamp()
    x = random.randint(20,100)
    y = random.randint(50,200)
    moving(x,y)


turtle.done()
