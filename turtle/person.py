import turtle

pen = turtle.Turtle()
turtle.title('cute person be like')
pen.speed(2)
pen.pensize(2)
def body():
    pen.up()
    pen.goto(0,50)
    pen.down()
    pen.color('blue')
    pen.right(90)
    pen.forward(150)

def leg():
    pen.color('brown')
    #pen.up()
    #pen.goto(-150,0) #we don't need to do it twice, cuz turtle is already there
    pen.right(45)
    pen.fd(100)
    pen.backward(100)
    pen.left(95)
    pen.fd(100)

def hand():
    pen.color('yellow')
    pen.up()
    pen.goto(0,0)
    pen.down()
    pen.left(30)
    pen.fd(100)
    pen.backward(100)
    pen.left(200)
    pen.fd(100)

def head():
    pen.up()
    pen.goto(-7,150)
    pen.down()
    pen.color('purple')
    pen.circle(50)
    pen.hideturtle()

def eye(a,b):
    pen.up()
    pen.goto(a,b)
    pen.down()
    pen.fillcolor('red')
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()
def mouth():
    pen.up()
    pen.goto(9,80)
    pen.down()
    pen.color('brown')
    pen.pensize(2)
    pen.fd(20)



body()
leg()
hand()
head()
eye(-18,110)
eye(18,110)
mouth()
turtle.done()
