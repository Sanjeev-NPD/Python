from turtle import *
import random

speed(1)
bgcolor("black")
color("white")
pensize(2)

for _ in range(50):
    for _ in range(4):
        forward(50)
        right(90)
    penup()
    goto(random.randint(-300, 300), random.randint(-300, 300))
    pendown()

done()
