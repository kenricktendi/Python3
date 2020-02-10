from turtle import *
"""
This code will fill the canvas with light blue circles.

Now add a function that will draw a white highlight on each bubble.
"""
speed(1)

# This function will draw one row of 10 circles
def draw_circle_row():
    for i in range(10):
        pendown()
        begin_fill()
        color("light blue")
        circle(20)
        end_fill()
        begin_fill()
        left(50)
        forward(21)


        color("white")
        make_highlight= 10 
        circle(make_highlight)
        end_fill()
        penup()
        backward(21)
        right(50)
        forward(40)

        
# This function will move Tracy from end of row up to beginning of the row on top        
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
    
# Send Tracy to starting position in bottom left corner
penup()
setposition(-180,-200)

# Call circle drawing function 10 times to fill ten rows
for i in range(10):
    draw_circle_row()
    move_up_a_row()