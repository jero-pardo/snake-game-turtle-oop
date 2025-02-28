from turtle import Turtle

# Configuration
SNAKE_SHAPE = "square"
SNAKE_COLOR = "white"
SNAKE_DEL_LOC = (1000, 1000)
MOVE_DISTANCE = 20
HEAD_ANGLE = {
    "UP": 90,
    "DOWN": 270,
    "LEFT": 180,
    "RIGHT": 0,
}


class Snake:
    def __init__(self, position=(0, 0)):
        """
        Creates a Snake with the head on a given x-axis and y-axis. if none is given, x and y has a default value of 0.
        the body is created on the x-axis
        """
        self.segments = []
        self.head = ""
        self.create_snake(position)

    def create_snake(self, position):
        new_x_pos = position[0]
        new_y_pos = position[1]
        for i in range(3):
            self.add_segment((new_x_pos, new_y_pos))
            new_x_pos -= MOVE_DISTANCE

        self.head = self.segments[0]

    def kill_snake(self):
        for seg in self.segments:
            seg.setpos(SNAKE_DEL_LOC)
        self.segments.clear()

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