from turtle import *
"""
This code will draw 9 shapes in a line, increasing from 0 points to 9.
"""
speed(5)

# Send Tracy to starting position
penup()
setposition(-180,0)

# Draw shapes where i controls the number of points and then move forward
for radius in range(1,10):
    
    pendown()
    circle(20,360,radius)
    penup()
    forward(40)
    
    