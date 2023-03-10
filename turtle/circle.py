import turtle

screen = turtle.Screen() #this is to make screen with white background
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(1) #this is the fastest speed of turtle

pen.fillcolor('red') #this is to fill the pen
pen.begin_fill()

pen.circle(100) #this means draw a circle with radius 100 

pen.end_fill() #this fill the inside of outline
pen.hideturtle() #this hide the turtle and good to make complex drawing

turtle.done() # it keeps turtule winod open untill it's permanetly close






