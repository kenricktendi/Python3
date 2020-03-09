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



def draw_circle(x1, y1, x2, y2, color):
    screen.create_oval(x1, y1, x2, y2, color)

screen = Canvas(root, width= canvas_width, height=canvas_height, bg= "white")
screen.pack()

screen.create_rectangle(canvas_width/2 - 60, canvas_height/2 - 175, canvas_width/2 + 60, canvas_height/2 + 175, fill='#808080')


draw_circle(canvas_width/2, canvas_height - circle_radius, canvas_width/2, canvas_height + circle_radius, fill= "red")



mainloop()