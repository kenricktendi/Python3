from turtle import * 
from tkinter import * 

speed(1)

def draw_circles(color_choice, radius):
    color(color_choice)
    pendown()
    circle(radius)
    penup()

penup()

#first circle
setposition(0,-75)
pendown()
begin_fill()
draw_circles("black", 100)
end_fill()
penup()

#second circle
setposition(0, -50)
pendown()
begin_fill()
draw_circles("yellow", 75)
end_fill()
penup()

#third circle
setposition(0,-25)
pendown()
begin_fill()
draw_circles("blue", 50)
end_fill()
penup()

#fourth circle
setposition(0,0)
pendown()
begin_fill()
draw_circles("red", 25)
end_fill()