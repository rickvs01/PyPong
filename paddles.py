from turtle import Turtle

#STARTING_POSITIONS = [(720, 0), (-720, 0)]
MOVE_DISTANCE = 20
#UP = 90
#DOWN = 270
#LEFT = 180
#RIGHT = 0


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
