#!/bin/python3
import turtle
from random import *
from turtle import *

penup()
goto(-140,140) #positioning the pen

for sp in range(15): #loop for creating the lines labelled with numbers
  speed(10)
 #setting the speed
  write(sp)
 #writing the int
  right(90)
 #setting right at 90 degrees
  forward(10)
 #forward at 10 units
  pendown()
 #ready to draw
  forward(150)
 #forward at 150 units
  penup()
 #not ready to draw
  backward(160)
 #back at 160 units
  left(90)
 #left set at 90 degrees
  forward(20)
 #forward at 20 units


propratham = Turtle() #inheriting the turtle
propratham.color('green') #setting the color to green for the first turtle
propratham.shape('turtle') #setting the shape to "turtle"
propratham.penup() #not ready to draw
propratham.goto(-160,100) #positioning the turtle
propratham.pendown() #ready todraw


tarun = Turtle() #inheriting another turtle
tarun.color('red') #setting the color og the turtle to red
tarun.shape('turtle') #declaring the shape of the turtle to "turtle"
tarun.penup() #not ready to draw
tarun.goto(-160,80) #positioning
tarun.pendown() #ready to draw

tarun2 = Turtle() #inheriting the last turtle
tarun2.color('blue') #setting the color of the turtle as "blue"
tarun2.shape('turtle') #declaring the shape of the turtle
tarun2.penup() #not ready to draw
tarun2.goto(-160,60) #positioning
tarun2.pendown() #ready

pratham = Turtle() #inheriting the last turtle
pratham.color('yellow') #setting the color of the turtle as "yellow"
pratham.shape('turtle') #declaring the shape of the turtle
pratham.penup() #not ready to draw
pratham.goto(-160,120) #positioning
pratham.pendown() #ready

for turn in range(100): #loop for the racew
  propratham.forward(randint(1,5)) #setting the speed randomly with the "random" module
  tarun.forward(randint(1,5)) #setting the speed randomly with the "random" module
  tarun2.forward(randint(1,5)) #setting the speed randomly with the "random" module
  pratham.forward(randint(1,5)) #setting the speed randomly with the "random" module

turtle.done()
print("Thank you all for participating")
