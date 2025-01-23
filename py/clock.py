from turtle import *
import time

speed(0)
bgcolor("black")
color("white")
pensize(2)

def draw_clock():
    penup()
    goto(0, -200)
    pendown()
    circle(200)  # Clock boundary
    penup()
    goto(0, 0)

def draw_hand(length, angle):
    penup()
    goto(0, 0)
    setheading(angle)
    pendown()
    forward(length)
    penup()
    backward(length)

draw_clock()

while True:
    for i in range(12):  # Hours hand (example loop)
        draw_hand(100, -i * 30)  # Adjust for hour marks
        time.sleep(1)
        draw_hand(100, -i * 30)  # Clear previous position

done()
