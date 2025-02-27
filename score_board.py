from turtle import Turtle

# Configuration
POSITION = (0, 280)
FONT = ("Arial", 12, "normal")
ALIGNMENT = "center"
TEXT_COLOR = "white"

class ScoreBoard(Turtle):
    def __init__(self):
        """Displays a Score on the upper boundary of the screen"""
        super().__init__()
        self.setpos(POSITION)
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()
