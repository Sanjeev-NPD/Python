from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(360):
    color(colorsys.hsv_to_rgb(h, 1, 1))
    h += 0.002
    forward(i * 0.5)  # Increase step size for the spiral
    right(59)         # Change the angle for the hypnotic effect

done()
