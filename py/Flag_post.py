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

# Function to draw the flagpost with 3 levels
def draw_flag_post(x, y):
    # Bottom rectangle (widest)
    draw_rectangle("green", x - 80, y, 160, 25)

    # Middle rectangle (smaller width)
    draw_rectangle("white", x - 60, y + 25, 120, 25)

    # Top rectangle (narrowest)
    draw_rectangle("orange", x - 40, y + 50, 80, 25)

# Main function to draw the flag post
def draw_flag_post_main():
    screen = turtle.Screen()
    screen.title("Flag Post")
    screen.bgcolor("skyblue")
    turtle.speed(5)
    turtle.hideturtle()

    # Flag post position and height
    flagpole_x = 0
    flagpole_y = -200

    # Draw the flag post
    draw_flag_post(flagpole_x, flagpole_y)

    # Keep the window open
    turtle.done()

# Run the program
draw_flag_post_main()
