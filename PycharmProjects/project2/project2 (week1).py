
import turtle

s=turtle.Screen() #흰 픽셀 창 띄움
t=turtle.Turtle()
t.shape("turtle")

t.forward(100)
t.left(90)

u=turtle.Turtle()
u.shape("turtle")
u.left(90)
u.forward(100)
t.forward(100)
u.right(45)

turtle.done()

import turtle

s=turtle.Screen() #흰 픽셀 창 띄움
t=turtle.Turtle()
t.shape("turtle")

t.pensize(3)
x=-100
y=100
t.goto(x,y)
t.undo()

t.penup()
t.goto(x,y)
t.pendown()

t.dot()
t.circle(100) #반지름 100인 원을 그림


