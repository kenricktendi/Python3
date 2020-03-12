'''Kenrick Tendi
#etch and sketch 
#3/11/'''

import turtle
import tkinter as tk

def clear_canvas():
    t.clear()
    t.penup()
    t.setposition(0,0)
    t.pendown()

def forward():
    t.forward(100)

def back():
    t.back(100)

def left():
    t.left(90)

def right():
    t.right(90)


root = tk.Tk()
canvas = tk.Canvas(master = root, width = 500, height = 500)#canvas
canvas.pack()#puts canvas on thing

t = turtle.RawTurtle(canvas) # allows turtle to draw on canvas
t.pencolor("#00ff00") # Red

t.penup()
t.pendown()


tk.Button(master = root, text = "Forward", command = forward).pack(side = tk.LEFT)     #forward
tk.Button(master = root, text = "Back", command = back).pack(side = tk.LEFT)           #back
tk.Button(master = root, text = "Left", command = left).pack(side = tk.LEFT)           #left
tk.Button(master = root, text = "Right", command = right).pack(side = tk.LEFT)         #right
tk.Button(master = root, text = 'Clear', command = clear_canvas).pack(side = tk.RIGHT) #clear
print(root.mainloop())

root.mainloop()
