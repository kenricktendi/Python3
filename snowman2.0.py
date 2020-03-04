#Kenrick Tendi 
#Exercise 21 
#3/3/20

from turtle import *
from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 400

bottom_diameter = canvas_height/2
middle_diameter = bottom_diameter/2
top_diameter = middle_diameter/2

# Create canvas
screen = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
screen.pack()

# Add shapes here!
screen.create_oval((canvas_width/2)- 20, top_diameter - 30, (canvas_width/2) + 20, top_diameter + 10, fill="gray")

screen.create_oval((canvas_width/2)- 40, middle_diameter - 40, (canvas_width/2) + 40, middle_diameter + 40, fill="gray")

screen.create_oval((canvas_width/2)- 60, bottom_diameter - 60, (canvas_width/2) + 60, bottom_diameter + 60, fill="gray")

# Add shapes to canvas
mainloop()