#kenrick tendi 
#exercise 3 unit 2 
#3/12/20

from tkinter import * 
from turtle import * 

num1 = int(input("what is the first number"))
num2 = int(input("What is the second number"))



def multiply(num1, num2):
    total1 = num1 * num2 
    print (str(total1))
def add(num1, num2):
    total2 = num1 + num2 
    print (str(total2))
def subtract(num1, num2):
    total3 = num1 - num2
    print(str(total3))
opt = input("What do you want to do? (subtract, add, multiply)")

if (opt=="add"):
    add(num1, num2)
elif (opt=="multiply"):
    multiply(num1, num2)
elif (opt=="subtract"):
    subtract(num1, num2)


