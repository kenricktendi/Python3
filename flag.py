from tkinter import * 

root= Tk()

screen = Canvas(root, height=300, width= 400, background = "white")
screen.pack()

screen.create_rectangle(-400, 0, 400, 100, fill="black", outline="")
screen.create_rectangle(-400, 200, 400, 100, fill="red", outline="")
screen.create_rectangle(-400, 399, 400, 200, fill="yellow", outline="")


mainloop()

