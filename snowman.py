from turtle import *
from tkinter import *
speed(1)
penup()
setposition(0,-100)
pendown()
bottom_radius = int(input("What should the size of the Bottom Circle be?"))
top_radius = int(input("What should the size of the Top Circle be?"))
middle_radius = int(bottom_radius/2)


def circ(radius):
 circle(radius)
 left(90)
 penup()
 forward(radius*2)
 pendown()
 right(90)

    
    
circ(bottom_radius)
circ(middle_radius)
circ(top_radius)

