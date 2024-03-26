from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from ai import COM
import time
import secrets

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("blue")
screen.listen()
screen.title("Pong")
screen.tracer(0)

scor = Scoreboard()
pad = Paddle()
com = COM()
ball = Ball()

screen.onkey(pad.up, "Up")
screen.onkey(pad.down, "Down")
screen.onkey(com.up, "w")
screen.onkey(com.down, "s")

computer = []
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    for segment in pad.lists:

        if segment.distance(ball) < 15:
            ran = [ball.T1(), ball.T2()]
            secrets.SystemRandom().choice(ran)

            if ball.ycor() > 280:
                ball.T2()

            if ball.ycor() < -280:
                ball.T1()

    for segment in com.lists:
        if segment.distance(ball) < 15:
            ran = [ball.T4(), ball.T3()]
            secrets.SystemRandom().choice(ran)

            if ball.ycor() > 280:
                ball.T3()

            if ball.ycor() < -280:
                ball.T1()



    if ball.xcor() > 290:
        ball.reset()
        ball.penup()
        scor.update1()

    if ball.xcor() < -290:
        ball.reset()
        ball.penup()
        scor.update2()



screen.exitonclick()
