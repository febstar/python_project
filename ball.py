from turtle import Turtle
import secrets


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.x_move = 10
        self.y_move = 10
        self.setheading(secrets.SystemRandom().randint(0, 360))

    def T1(self):
        self.setheading(secrets.SystemRandom().randint(0, 90))

    def T3(self):
        self.setheading(secrets.SystemRandom().randint(90, 180))

    def T4(self):
        self.setheading(secrets.SystemRandom().randint(180, 270))

    def T2(self):
        self.setheading(secrets.SystemRandom().randint(270, 360))

    def move(self):
        random_x = self.xcor() + self.x_move
        random_y = self.ycor() + self.y_move
        self.goto(random_x, random_y)

    def bounce(self):
        self.y_move *= -1

