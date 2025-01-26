import turtle
import time

# Function to draw a rectangle of a specific color
def draw_rectangle(t, color, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


# Function to write text in a specific color
def write_text(t, color, x, y, text, font_size=50):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.write(text, align="center", font=("Arial", font_size, "bold"))
    t.pendown()
    
def draw_tricolor_background():
    # Setup the screen
    screen = turtle.Screen()
    screen.title("Tricolor Background")
    screen.setup(width=800, height=600)
    screen.tracer(0)  # Disable animation for faster drawing

    # Create the turtle pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    # Draw the tricolor background
    draw_rectangle(pen, "orange", -400, 200, 800, 200)  # Saffron (Top)
    draw_rectangle(pen, "white", -400, 0, 800, 200)     # White (Middle)
    draw_rectangle(pen, "green", -400, -200, 800, 200)  # Green (Bottom)

# Main function
def draw_republic_day_graphics():
    # Setup the screen
    screen = turtle.Screen()
    screen.title("Happy Republic Day")
    screen.bgcolor("#bb88ca")
    screen.setup(width=800, height=600)
    time.sleep(5)

    # Create the turtle pen
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(3)

    # Write the text in tricolor
    write_text(pen, "#FF9920", 0, 150, "Happy Republic Day")     # Saffron
    write_text(pen, "white", 0, 70, "26th January 2025")    # White (use black on white background)
    write_text(pen, "green", 0, -5, "Rapid Prototyping Pvt. Ltd.")          # Green

    # Draw the Ashoka Chakra
    pen.penup()
    pen.goto(0, -250)
    pen.pendown()
    pen.color("blue")
    pen.width(8)
    pen.circle(101)  # Outer circle of the Chakra

    # Draw 24 spokes of the Chakra
    for _ in range(24):
        pen.penup()
        pen.goto(0, -150)
        pen.setheading(360 / 24 * _)
        pen.pendown()
        pen.forward(100)

    # Keep the window open
    screen.mainloop()

# Run the program
draw_republic_day_graphics()
