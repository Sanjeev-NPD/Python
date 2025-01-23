from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(36):
    color(colorsys.hsv_to_rgb(h, 1, 1))
    h += 0.02
    begin_fill()
    for _ in range(6):
        circle(50, 60)
        left(120)
        circle(50, 60)
        left(120)
    end_fill()
    right(10)

done()
