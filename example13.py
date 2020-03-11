from tkinter import *

root = Tk()

# Constant values
canvas_width = 350
canvas_height = 350
bottom_base = 300
left_base = 50
bar_height = 50
bar_width = 30

# Create canvas
screen = Canvas(root, width=canvas_width, height=canvas_height)
screen.pack()

for i in range (5):
   top_x = left_base
   top_y = bottom_base - bar_height
   bottom_x = left_base + bar_width
   bottom_y = bottom_base
   screen.create_rectangle(top_x, top_y, bottom_x, bottom_y, fill="gray")
   bar_height = bar_height + 50
   left_base = left_base + 50

mainloop()