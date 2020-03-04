#Kenrick Tendi 
#Exercise 21.1
#3/3/20

from tkinter import *

root = Tk()



canvas_width = 300
canvas_height = 400
light_radius = 35
yellow light = canvas_height/2
dist_between_lights = 50

screen = Canvas(root, width= canvas_width, height=canvas_height, bg= "white")
screen.pack()

def draw_circle(x1, y1, x2, y2, color):
    screen.create_oval(x1, y1, x2, y2, color)


screen.create_oval(170, 30, 220, 80, fill="red")
screen.create_rectangle(160, 10, 230, 280, fill ="light gray")
screen.create_oval(170, 120, 220, 170, fill="yellow")
screen.create_oval(170, 210 , 220, 260 , fill="green")
draw_circle()



mainloop()