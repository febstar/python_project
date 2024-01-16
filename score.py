from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.score1 = 0
        self.score2 = 0
        self.write("Scores", move=False, align='center', font=('Arial', 20, 'normal'))



    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=('Spooky', 20, 'normal'))

    def update1(self):
        self.clear()
        self.score1 += 1
        self.write(f"{self.score1} :Score: {self.score2}", move=False, align='center', font=('Arial', 20, 'normal'))

    def update2(self):
        self.clear()
        self.score2 += 1
        self.write(f"{self.score1} :Score: {self.score2}", move=False, align='center', font=('Arial', 20, 'normal'))
