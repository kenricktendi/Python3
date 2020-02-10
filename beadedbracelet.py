from turtle import *
from tkinter import *

speed(10)
#This function will draw circles 
def draw_the_circles(): 
    for i in range(36):
        color("black")
        begin_fill()
        circle(10)
        end_fill()
        penup()

        forward(20)
        pendown()
        right(10)

draw_the_circles()
print("done")  