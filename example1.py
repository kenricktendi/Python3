from turtle import * 

speed(1)
penup()
backward(150)

for i in range(10, 50 ,10):
    forward(i * 2)
    pendown()
    circle(i)
    penup()
