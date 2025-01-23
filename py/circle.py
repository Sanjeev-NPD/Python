from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(36):
    color(colorsys.hsv_to_rgb(h, 1, 1))
    h += 0.03
    penup()
    goto(0, -i * 10)  # Move down as the radius increases
    pendown()
    circle(i * 10)

done()
