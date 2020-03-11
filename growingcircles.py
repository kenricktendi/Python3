#Kenrick Tendi 
#Exercise 2
#3/9/20

from tkinter import *

root = Tk()

canvas_height = 300
canvas_width = 300
radius = 20

screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()


# Create canvas

def draw_circle(radius, canvas_width):
    while (radius <= canvas_width):
        screen.create_oval(0, 0, radius, radius)
        radius += 20
# Your code here...

draw_circle(radius, canvas_width)
mainloop()
