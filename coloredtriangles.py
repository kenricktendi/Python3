from turtle import * 
from tkinter import * 

speed(1)
penup()
setposition(-120,0)
pendown()
pensize(5)
#Code will draw triangles
def draw_the_triangles():
    for i in range(4):
        color("red")
        forward(50)
        right(120)
        color("green")
        forward(50)
        right(120)
        color("blue")
        forward(50)
        right(120)
        color("red")
        forward(50)
        penup()
        forward(20)
        pendown()
draw_the_triangles()