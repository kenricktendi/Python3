

from tkinter import *

root = Tk()

# Create canvas
screen = Canvas(root, width = 400, height = 300, bg="white")
screen.pack()

# Draw red circle
screen.create_line(50, 50, 150, 50, 100, 100, 50, 50, fill="red")

# Add shapes to canvas
mainloop()