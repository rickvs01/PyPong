from turtle import Turtle
import random

class Ball(Turtle):



    def __init__(self, position):
        super().__init__()
        self.move_speed = 0.25
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.penup()
        self.goto(position)
        self.x_move = self.move_speed
        self.y_move = self.move_speed
        #self.move_speed = 0.1

    def move(self):
        #while
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed += 0.05

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.25
