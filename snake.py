from turtle import Turtle
start_position=[(0,0),(-20,0),(-40,0)]
move_distance=20
Up=90
Down=270
Left=180
Right=0
class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head=self.squares[0]

    def create_snake(self):
        for position in start_position:
            self.add_square(position)

    def add_square(self, position):
        snake = Turtle(shape="square")
        snake.color("green")
        snake.penup()
        snake.goto(position)
        self.squares.append(snake)

    def extend_snake(self):
                self.add_square(self.squares[-1].position())

    def reset_snake(self):
        for square in self.squares:
            square.goto(1000,1000)
        self.squares.clear()
        self.create_snake()
        self.head=self.squares[0]

    def move(self):
        # start, stop, step
        for square in range(len(self.squares)-1, 0, -1):
            new_position=self.squares[square-1].position()
            self.squares[square].goto(new_position)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() !=Down:
            self.head.setheading(Up)
    def down(self):
        if self.head.heading() !=Up:
            self.head.setheading(Down)
    def left(self):
        if self.head.heading() !=Right:
            self.head.setheading(Left)
    def right(self):
        if self.head.heading() !=Left:
            self.head.setheading(Right)