import turtle

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
    turtle.goto(x, y - radius)  # Move to the bottom of the circle
    turtle.pendown()
    turtle.color("blue")
    turtle.width(2)
    turtle.circle(radius)  # Draw the outer circle

    # Draw 24 spokes
    for i in range(24):
        turtle.penup()
        turtle.goto(x-20, y-20)  # Start at the center of the circle
        turtle.setheading(15 * i)  # Rotate to the correct angle for each spoke
        turtle.pendown()
        turtle.forward(radius)  # Draw the spoke
        turtle.backward(radius)  # Return to the center

# Function to draw the flag
def draw_flag(x, y):
    # Saffron stripe
    draw_rectangle("orange", x, y, 50, -300)
    # White stripe
    draw_rectangle("white", x, y - 50, 50, -300)
    # Green stripe
    draw_rectangle("green", x, y - 100, 50, -300)
    # Ashoka Chakra
    draw_ashoka_chakra(x+173 , y-5, 20)

# Function to draw the flagpole
def draw_flag_pole(x, y, height):
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
    flagpole_height = 450

    # Draw the flagpole
    draw_flag_pole(flagpole_x, flagpole_y, flagpole_height)

    # Draw the flag at the top of the pole
    draw_flag(flagpole_x , flagpole_y + flagpole_height-50)

    # Keep the window open
    turtle.done()

# Run the program
hoisted_flag()
