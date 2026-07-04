from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt", "r") as data:
            content = int(data.read())
        self.high_score=content
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.current_score()

    def current_score(self):
        self.clear()
        self.write(f" Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 20, "normal"))


    def reset_scoreboard(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as data:
                data.write(str(self.high_score))
        self.score=0
        self.current_score()


    #def game_over(self):
        #self.goto(0, 0)
        #self.write("Game Over", align="center", font=("Courier", 20, "bold"))


    def increase(self):
        self.score += 1
        self.current_score()


    def challenge(self,score,expected_score):
        if score>expected_score:
            print(f"You 've expected {expected_score} You got {score}\n More than expectations!")
        elif score==expected_score:
            print(f"You 've expected {expected_score} You got {score}\nYou expected the exact score!")
        else:
            print(f"You 've expected {expected_score} You got {score}\nLess than expectations!")

