from turtle import *
from tkinter import * 

speed(10)
penup()
setposition(-60,-393)
pendown()

#The code starts off at a set position and creates the first circle and brings the pen up and moves forward and puts the pen down and repeats the process
for i in range(3):
    circle(50)
    penup()
    forward(100)
    pendown()

penup()
setposition(-16,-305)
pendown()

#At the set position it starts off drawing the circle with a radius of 50 and brings pen up and moves forward and puts the pen down and repeats the code 
for i in range(2):
    circle(50)
    penup()
    forward(100)
    pendown()

#Draws one circle at the set position
penup()
setposition (30,-215)
pendown()
circle(50)