from tkinter import *

root = Tk()

# Constant values
canvas_height = 300
canvas_width = 400
balloon_height = canvas_height/4
balloon_width = canvas_height/5
balloon_tie_size = balloon_width/4

# Create canvas
screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()

# This function will draw an oval and triangle to create a balloon centered on
# a given coordinate point and with a given color.
def draw_balloon(center_x, center_y, color):
    screen.create_oval(center_x-balloon_width/2, center_y-balloon_height/2, center_x+balloon_width/2, center_y+balloon_height/2, fill=color, outline="")
    screen.create_polygon(center_x, center_y+balloon_height/2, center_x+balloon_tie_size/2, center_y+balloon_height/2+balloon_tie_size, center_x-balloon_tie_size/2, center_y+balloon_height/2+balloon_tie_size, center_x, center_y+balloon_height/2, fill=color, outline="")

# Draws three balloons to the canvas
draw_balloon(100, 150, "red")  
draw_balloon(200, 100, "yellow")
draw_balloon(300, 200, "blue")


# Add shapes to canvas
mainloop()