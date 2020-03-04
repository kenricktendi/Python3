from tkinter import *

root =Tk()
# Create canvas
screen = Canvas(root, width = 200, height = 200, background = "red")
screen.pack()

# Draw black lines
screen.create_line(75, 25, 75, 175)
screen.create_line(125, 25, 125, 175)
screen.create_line(25, 75, 175, 75)
screen.create_line(25, 125, 175, 125)


# Add shapes to canvas
mainloop()






