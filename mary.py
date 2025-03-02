import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(2)

# Function to draw a heart
def draw_heart():
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Write the word "I"
pen.penup()
pen.goto(-150, 0)
pen.pendown()
pen.color("black")
pen.write("I ", font=("Arial", 24, "bold"))

# Draw the heart symbol to replace "love"
pen.penup()
pen.goto(-30, -20)  # Position the heart where "love" would be
pen.pendown()
pen.color("red")
draw_heart()

# Write the word "Mary"
pen.penup()
pen.goto(50, 0)
pen.pendown()
pen.color("black")
pen.write(" Mary", font=("Arial", 24, "bold"))

# Hide the turtle after drawing
pen.hideturtle()

# Keep the window open
turtle.done()
