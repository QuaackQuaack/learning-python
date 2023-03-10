import turtle

parm = turtle.Turtle()
parm.speed(1) # zero is the fastest speed in turtle and 1 is slowest
for i  in range(1,5):
    if i % 2 == 0 :
        parm.forward(100)
        parm.right(45)
    else:
        parm.forward(100)
        parm.right(135)

turtle.done()
