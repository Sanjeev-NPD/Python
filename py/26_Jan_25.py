import turtle
import time 

# Function to draw a rectangle
def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw the Ashoka Chakra
def draw_ashoka_chakra(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius) 
    turtle.pendown()
    turtle.color("blue")
    turtle.width(2)
    turtle.circle(radius) 

    # Draw 24 spokes
    for i in range(24):
        turtle.penup()
        turtle.goto(x-20, y-20)  
        turtle.setheading(15 * i) 
        turtle.pendown()
        turtle.forward(radius) 
        turtle.backward(radius) 

# Function to draw the flag
def draw_flag(x, y):
    # Saffron stripe
    draw_rectangle("orange", x, y, 50, -300)
    # White stripe
    draw_rectangle("white", x, y - 50, 50, -300)
    # Green stripe
    draw_rectangle("green", x, y - 100, 50, -300)
    # Ashoka Chakra
    draw_ashoka_chakra(x + 173 , y - 5, 20)

# Function to draw the flagpost with 3 levels
def draw_flag_post(x, y):
    # Reset heading to default (facing right)
    turtle.setheading(0)

    # Bottom rectangle (widest)
    draw_rectangle("green", x - 80, y, 160, 25)

    # Middle rectangle (smaller width)
    draw_rectangle("white", x - 60, y + 25, 120, 25)

    # Add your name on the white area of the flag post
    turtle.penup()
    turtle.goto(x , y + 28) 
    turtle.pendown()
    turtle.color("blue")
    turtle.write("Sanjeev Kumar", align="center", font=("Arial", 12, "bold"))

    # Top rectangle (narrowest)
    draw_rectangle("orange", x - 40, y + 50, 80, 25)

# Function to draw the flagpole
def draw_flag_pole(x, y, height):

    turtle.setheading(0)   
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.width(8)
    turtle.setheading(90)
    turtle.forward(height)

# Main function to draw the hoisted flag
def hoisted_flag():
    screen = turtle.Screen()
    screen.title("Hoisted Indian Flag")
    screen.bgcolor("skyblue")
    turtle.speed(5)
    turtle.hideturtle()

    # Flagpole base position
    flagpole_x = -200
    flagpole_y = -300
    flagpole_height = 500

    # Draw the flagpost
    draw_flag_post(flagpole_x, flagpole_y-78)

    # Draw the flag at the top of the pole
    draw_flag_pole(flagpole_x, flagpole_y, flagpole_height)
    draw_flag(flagpole_x, flagpole_y + flagpole_height - 50)

# Loop to repeat the drawing process with a 1-second delay
while True:
    hoisted_flag()
    time.sleep(1)  
    turtle.clear() 
