import turtle

rows = ['a','b','c','d']
cols = ['1','2','3','4']

for row in rows:
    turtle.write(row, move = False, align = 'left', font=('Georgia',40,'normal'))
    turtle.sety(turtle.ycor() - 40)

turtle.goto(-65, 75)
for col_name in cols:
        turtle.write(col_name, move=False, align='left', font=('Georgia', 40, 'normal'))
        turtle.setx(turtle.xcor() + 40)


turtle.done()
