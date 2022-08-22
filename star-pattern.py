import turtle
from turtle import Screen
import random
import math
def re(b1,sx):
    if(sx<=1):
        return
    else:
            b1.forward(sx)
            re(b1,sx/3)
            b1.left(216)
        
b=turtle.Turtle()
#n=int(input())

b.getscreen().bgcolor("cyan")
b.speed(100)
screen=Screen()
screen.colormode(255)
re(b,200)

