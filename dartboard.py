from turtle import * 
from tkinter import * 

speed(9)
#set radius to 25 
circle_radius= 25
#draws first circle
circle(circle_radius)
#change radius to 50 
circle_radius= circle_radius + 25
penup()
setposition(0,-25)
pendown()
#draws the second circle
circle(circle_radius)
#changes the radius to 75 
circle_radius= circle_radius + 25 
penup()
setposition(0,-50)
pendown()
#draws the third circle
circle(circle_radius)
#changes the radius to 100 
circle_radius= circle_radius + 25 
penup()
setposition(0,-75)
pendown()
#draws the fourth circle 
circle(circle_radius)

