from turtle import Turtle
COMPUTER_POSITION = [(290, 0), (290, -20), (290, -40), (290, -60), (290, -80)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
LIST = []

class COM(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.lists = []
        self.com_paddle()
        self.speed("fastest")
        self.head = self.lists[0]

    def com_paddle(self):
        for position in COMPUTER_POSITION:
            self.add_seg(position)


    def add_seg(self, position):
        new = Turtle()
        new.speed(self.speed())
        new.penup()
        new.shape("square")
        new.color("green")
        new.goto(position)
        self.lists.append(new)

    def move(self):
        for seg_num in range(len(self.lists) - 1, 0, -1):
            new_x = self.lists[seg_num - 1].xcor()
            new_y = self.lists[seg_num - 1].ycor()
            self.lists[seg_num].goto(new_x, new_y)

    def down(self):
        for seg in range(len(self.lists)):
            self.lists[seg].setheading(DOWN)
            self.lists[seg].forward(20)

    def up(self):
        for seg in range(len(self.lists)):
            self.lists[seg].setheading(UP)
            self.lists[seg].forward(20)