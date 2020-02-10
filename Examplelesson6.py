from turtle import *
"""
This code will draw hash marks at 25, 50, 100, and 200 pixels.
The color of each hash mark will be determined from user input.
"""

# Set initial value of length variable to 25
speed(5)
length = 25

# This function will ask the user for a color.
# It will then draw a hash mark of that color.
def draw_hash_mark():
    color(color_choice)
    pensize(mark_thickness)
    circle()
    
    
   
  
    color("black")
    pensize(1)

# Send Tracy to starting position
penup()
setposition(-200,0)
pendown()
mark_thickness=int(input("What is the thickness of the marks? (1-20): "))

# Move Tracy forward by the value of 'length' and draw a hash mark
# Repeat this 4 times, doubling the length each time
for i in range(4):
    forward(length)
    color_choice = input("What color should this mark be?: ")
    draw_hash_mark()
    length = length * 2