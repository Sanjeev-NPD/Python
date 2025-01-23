from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(360):
    color(colorsys.hsv_to_rgb(h, 1, 1))
    h += 0.01
    forward(100)
    right(144)  # Angle for star
    forward(100)
    right(72)   # Rotate the star slowly
    right(1)

done()
