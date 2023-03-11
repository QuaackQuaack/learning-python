import random
import turtle

def tree(size,pen):
    pen.pensize(size/20)
    if size < random.randint(1,2) * 20:
        pen.color("green")
    else :
        pen.color("brown")

    if size > 5:
        pen.fd(size)
        pen.left(25)
        tree(size - random.randint(10,20),pen)
        pen.right(50)
        tree(size - random.randint(10,20),pen)
        pen.left(25)
        pen.up()
        pen.backward(size)
        pen.down()

pen = turtle.Turtle()
pen.speed(0)
pen.left(90)
pen.up()
pen.goto(0,-300)
pen.down()

tree(135,pen)

turtle.done()
