
import turtle
wn = turtle.Screen()
wn.bgcolor('light green')
pen = turtle.Turtle()
pen.color('blue')

def sqrfunc(size):
    for i in range(4):
        pen.fd(size)
        pen.left(90)
        size += 5

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
turtle.done()

