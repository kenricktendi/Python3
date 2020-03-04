"""
This program will draw a division symbol in the center of the canvas on top
of a blue diamond shape.
"""

from tkinter import *

root = Tk()

# Constant values
# Try changing the height or width of the canvas here and see how the image changes!
canvas_height = 300
canvas_width = 400
rectangle_width = canvas_width/2
rectangle_height = canvas_height/6
circle_radius = canvas_height/6
circle_offset = circle_radius/2


# Create canvas
screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()

# Draw blue diamond background
screen.create_polygon(canvas_width/2, 0, canvas_width, canvas_height/2, canvas_width/2, canvas_height, 0, canvas_height/2, canvas_width/2, 0, fill="blue")

# Draw orange rectangle with 5pt outline
screen.create_rectangle(canvas_width/2 - rectangle_width/2, canvas_height/2 - rectangle_height/2, canvas_width/2 + rectangle_width/2, canvas_height/2 + rectangle_height/2, fill="orange", width=5)

# Draw top circle with 5pt outline
screen.create_oval(canvas_width/2 - circle_radius/2, canvas_height/2 - rectangle_height/2 - circle_offset - circle_radius, canvas_width/2 + circle_radius/2, canvas_height/2 - rectangle_height/2 - circle_offset, fill="orange", width=5)

# Draw bottom circle with 5pt outline
screen.create_oval(canvas_width/2 - circle_radius/2, canvas_height/2 + rectangle_height/2 + circle_offset, canvas_width/2 + circle_radius/2, canvas_height/2 + rectangle_height/2 + circle_offset + circle_radius, fill="orange", width = 5)


# Add shapes to canvas
mainloop()