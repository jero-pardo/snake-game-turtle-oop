from turtle import Turtle

# Configuration
POSITION = (0, 280)
FONT = ("Arial", 12, "normal")
BTN_FONT = ("Arial", 12, "normal")
ALIGNMENT = "center"
TEXT_COLOR = "white"

class ScoreBoard(Turtle):
    def __init__(self):
        """Displays a Score on the upper boundary of the screen"""
        super().__init__()
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.update_score_board()

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_score_board()


    # Write to screen methods
    def update_score_board(self):
        self.clear()
        self.setpos(POSITION)
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.display_restart_button()

    def display_restart_button(self):
        self.setpos(-40, -60)
        self.pendown()
        for _ in range(2):
            self.forward(80)
            self.left(90)
            self.forward(30)
            self.left(90)

        self.penup()
        self.setpos(0, -55)
        self.write("Restart", align=ALIGNMENT, font=BTN_FONT)