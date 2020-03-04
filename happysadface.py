from turtle import* 
from tkinter import* 
speed(1)
penup()
setposition(-20,0)
pendown()

happy= int(input("How do you feel from one to ten?"))

num = int(happy)
if (num == 10):
    circle(15)
    penup()
    forward(60)
    pendown()
    circle(15)
    penup()
    setposition(-35,-40)
    pendown()
    right(90)
    circle(40,180)

if (num < 9.9): 
    circle(15)
    penup()
    forward(60)
    pendown()
    circle(15)
    penup()
    setposition(40,-70)
    pendown()
    left(90)
    circle(40,180)