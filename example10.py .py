"""
This program will draw two lines across the canvas in an X formation.
"""



from tkinter import *
root = Tk()
screen=Canvas(root, width = 200, height = 200)
screen.pack()
screen.create_line(0, 0, 100, 100, 200, 0)
mainloop()
