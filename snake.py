import turtle
import time
import math
import random

delay = 0.1

# set up screen
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=1200, height=1200)
wn.tracer(0)

# square
t = turtle.Turtle()
t.speed(0)
t.color('white')
t.penup()
t.setposition(-500, -500)
t.pensize(3)
t.pendown()
for side in range(4):
    t.fd(1000)
    t.lt(90)
t.hideturtle()

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "up"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Functions
# up
def go_up():
    head.direction = "up"

# down
def go_down():
    head.direction = "down"

# left
def go_left():
    head.direction = "left"

# right
def go_right():
    head.direction = "right"

# moving the turtle
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# eating the food
def is_eat(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 30:
        return True
    else:
        return False

# coalition the food
def is_col(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 10:
        return True
    else:
        return False

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # check for collision
    if is_eat(head, food):

        # move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # put the body on it
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segments
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # move the snake
    move()

    # delay the snake a little
    time.sleep(delay)

wn.mainloop()
