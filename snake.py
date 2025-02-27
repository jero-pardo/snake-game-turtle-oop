from turtle import Turtle

# Configuration
SNAKE_SHAPE = "square"
SNAKE_COLOR = "white"
MOVE_DISTANCE = 20
HEAD_ANGLE = {
    "UP": 90,
    "DOWN": 270,
    "LEFT": 180,
    "RIGHT": 0,
}


class Snake:
    def __init__(self, x_pos=0, y_pos=0):
        """
        Creates a Snake with the head on a given x-axis and y-axis. if none is given, x and y has a default value of 0.
        the body is created on the x-axis
        """
        self.segments = []
        self.create_snake(x_pos, y_pos)
        self.head = self.segments[0]

    def create_snake(self, x, y):
        new_x_pos = x
        for i in range(3):
            position = (new_x_pos, y)
            self.add_segment(position)
            new_x_pos -= MOVE_DISTANCE

    def add_segment(self, position):
        snake_turtle = Turtle(shape=SNAKE_SHAPE)
        snake_turtle.penup()
        snake_turtle.color(SNAKE_COLOR)
        snake_turtle.setpos(position)
        self.segments.append(snake_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    # Snake control functions
    def up(self):
        if self.head.heading() != HEAD_ANGLE["DOWN"]:
            self.head.setheading(HEAD_ANGLE["UP"])

    def down(self):
        if self.head.heading() != HEAD_ANGLE["UP"]:
            self.head.setheading(HEAD_ANGLE["DOWN"])

    def left(self):
        if self.head.heading() != HEAD_ANGLE["RIGHT"]:
            self.head.setheading(HEAD_ANGLE["LEFT"])

    def right(self):
        if self.head.heading() != HEAD_ANGLE["LEFT"]:
           self.head.setheading(HEAD_ANGLE["RIGHT"])