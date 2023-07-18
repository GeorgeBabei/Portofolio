from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.shapesize(1, 1)
        self.x_move = 5
        self.y_move = 5
        self.velocity = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.velocity *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.velocity = 0.05
        self.bounce_x()

