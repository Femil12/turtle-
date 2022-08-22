import turtle
from turtle import Screen
import random
import math
b=turtle.Turtle()
#n=int(input())


b.speed(100)
screen=Screen()
screen.colormode(255)

for i in range(1,1601):
  
    b.forward((math.sqrt(i)))
    b.left(i%180)
    if(i%100==0):
         t1=random.randint(0,255)
         t2=random.randint(0,255)
         t3=random.randint(0,255)
         b.color((t1,t2,t3))

   
    
    
    
    
