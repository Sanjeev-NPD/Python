from turtle import *
import random
import colorsys

speed(0)
bgcolor("black")

def fireworks(x, y):
    penup()
    goto(x, y)
    pendown()
    for i in range(36):
        color(colorsys.hsv_to_rgb(random.random(), 1, 1))
        forward(100)
        backward(100)
        right(10)

for _ in range(10):
    fireworks(random.randint(-300, 300), random.randint(-300, 300))

done()
