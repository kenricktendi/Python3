from turtle import *

#Set radius value to 50
speed(1)
length = 50
penup()
right(45)
pendown()



while length < 350:
    circle(length, 360, 4)
    penup()
    left(45)
    backward(35)
    right(90)
    forward(35)
    left(45)
    pendown()
    length = length + 50 