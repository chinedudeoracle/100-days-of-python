from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 18, 'normal')
X_POS = 0
Y_POS = 270

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(X_POS, Y_POS)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", True, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", True, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(X_POS, Y_POS)
        self.update_scoreboard()


