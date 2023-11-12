#Create a Screen, Create and move a Paddle,Create the ball and make it move, Detect collision with wall and bounce. detect position with paddle
#Detect when paddle misses and keep score

from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
#import time

scoreboard = ScoreBoard()


# Screen Setup
screen = Screen()
screen.setup(width=1500, height=1000)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((720, 0))
l_paddle = Paddle((-720, 0))
ball = Ball((0, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on == True:
    #time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    if ball.ycor() > 480 or ball.ycor() < -480:
        ball.bounce_y()
    #Detect collission with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 710 or ball.distance(l_paddle) < 50 and ball.xcor() < -710:
        ball.bounce_x()
    if ball.xcor() > 720:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -720:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()