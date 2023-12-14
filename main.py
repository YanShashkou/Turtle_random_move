import turtle
import random

Jimmy = turtle.Turtle()
Jimmy.shape("turtle")
colors=['midnight blue','lime green', 'cyan','red','blue','green','pink','yellow','orange','brown','grey']
angle = [90,180,270,360]
def random_move():
    stop = 1
    while stop == 1:
        left_or_right=(random.randint(1,2))
        Jimmy.color(random.choice(colors))
        if left_or_right == 1:
            Jimmy.left(random.choice(angle))
        else:
            Jimmy.right(random.choice(angle))
        Jimmy.forward(50)

random_move()









screen = turtle.Screen()
screen.exitonclick()