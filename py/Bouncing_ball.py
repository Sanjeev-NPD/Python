from turtle import *
import random

# Ball setup
speed(0)
bgcolor("black")
color("red")
shape("circle")
penup()

# Initial position and speed
x_speed = random.randint(2, 5)
y_speed = random.randint(2, 5)
x = 0
y = 0

while True:
    x += x_speed
    y += y_speed
    goto(x, y)
    
    # Bounce on edges
    if x > 300 or x < -300:
        x_speed = -x_speed
    if y > 300 or y < -300:
        y_speed = -y_speed
