from turtle import*
import colorsys

# set the speed of drawing and background color 
speed (0)
bgcolor("black")

# intialize hue value
h = 0

# Outer loop for 16 repetitions
for i in range(24):
#inner loop for drawing 18 shapes 
 for j in range(26):
  #Get the color using HSY to RBG conversion
  c = colorsys.hsv_to_rgb(h, 1, 1)
  color(c)

  #increment hue for the next color
  h += 0.005

#draw shapes 
  right(90)
  circle(150 - j * 6, 90)
  left(90)
  circle(150 - j * 6, 90)
  right(180)
  circle(75,45)

# complete the drawing 
done() 