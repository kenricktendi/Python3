#Kenrick Tendi 
#Exercise 21.1
#3/3/20

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 400
light_radius = 35
stoplight_width = 120
stoplight_height = 350
dist_between_lights = 50

yellow_center = canvas_height/2
centerX = canvas_width/2
red_center = yellow_center - dist_between_lights - (light_radius * 2)
green_center = yellow_center + dist_between_lights + (light_radius * 2)


def draw_circle(x1, y1, x2, y2, color):
        screen.create_oval(x1, y1, x2, y2, fill=color)

# Create canvas
screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()

# Write your program here!

screen.create_rectangle(canvas_width/2 - 60, canvas_height/2 - 175, canvas_width/2 + 60, canvas_height/2 + 175, fill='#808080')

canvas_width/2 -35, canvas_height/2 - 35, canvas_width/2 + 35, canvas_height/2 + 35
draw_circle(centerX - light_radius, red_center - light_radius, centerX + light_radius, red_center + light_radius, 'red')
draw_circle(centerX - light_radius, yellow_center - light_radius, centerX + light_radius, yellow_center + light_radius, 'yellow')
draw_circle(centerX - light_radius, green_center - light_radius, centerX + light_radius, green_center + light_radius, 'green')
# Add shapes to canvas
mainloop()