import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor('#1d1d1d')

# Draw the boundaries
boundary = turtle.Turtle()
boundary.speed(0)
boundary.pensize(4)
boundary.color("red")
boundary.penup()
boundary.goto(-310, 250)
boundary.pendown()
for _ in range(2):
    boundary.forward(600)
    boundary.right(90)
    boundary.forward(500)
    boundary.right(90)
boundary.hideturtle()

# Set initial score and delay
score = 0
delay = 0.1

# Create the snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# Create the fruit
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(30, 30)

# Lists to keep track of old fruits and their positions
old_fruit = []

# Create the score display
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color('white')
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: 0", align="center", font=("Courier", 24, "bold"))

# Functions to handle snake movement
def snake_up_go():
    if snake.direction != "down":
        snake.direction = "up"

def snake_down_go():
    if snake.direction != "up":
        snake.direction = "down"

def snake_right_go():
    if snake.direction != "left":
        snake.direction = "right"

def snake_left_go():
    if snake.direction != "right":
        snake.direction = "left"

# Function to move the snake
def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(snake_up_go, "Up")
screen.onkeypress(snake_down_go, "Down")
screen.onkeypress(snake_right_go, "Right")
screen.onkeypress(snake_left_go, "Left")

while True:
    screen.update()

    # Check if the snake has eaten the fruit
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        score += 1
        scoring.clear()
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

        # Add a new fruit to the old_fruit list
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("circle")
        new_fruit.color("green")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # Update the positions of old fruits
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    # If there are old fruits, update the position of the first old fruit to the snake's position
    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    # Move the snake
    snake_move()

    # Check for collision with the boundaries
    if (
        snake.xcor() > 290
        or snake.xcor() < -310
        or snake.ycor() > 240
        or snake.ycor() < -240
    ):
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("Game Over\nYour Score is {}".format(score), align="center", font=("Courier", 24, "bold"))
        screen.update()
        time.sleep(6) 
        break

    # Check for collision with old fruits
    for food in old_fruit:
        if food.distance(snake) < 20:
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("Game Over\nYour Score is {}".format(score), align="center", font=("Courier", 24, "bold"))
            screen.update()
            time.sleep(6) 
            break

    time.sleep(delay)