import random
from turtle import Turtle

# Configuration
BOUNDARY = 280
FOOD_SHAPE = "circle"
FOOD_COLOR = "orange"

class Food(Turtle):
    def __init__(self):
        """
        Creates a Food object on a random x-axis and y-axis
        """
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape(FOOD_SHAPE)
        self.color(FOOD_COLOR)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        range_of_axis = range(-BOUNDARY, BOUNDARY + 1, 10)
        random_x = random.choice(range_of_axis)
        random_y = random.choice(range_of_axis)
        self.setpos(random_x, random_y)