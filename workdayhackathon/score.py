import random

#Written by Rory Flynn
#github : github.com/roryflynn

class Scorer:
    CHARS = ['L', 'R', 'U', 'D']
    def __init__(self):
        self.level = 1
        self.rows_left = self.level * 2
        self.lives = 10
        self.score = 0


    @property
    def speed(self):
        return self.level * 3

    def get_row(self):
        if self.rows_left != 0:
            self.rows_left -=1
        else:
            self.level_up()
        return random.choice(self.CHARS)

    def level_up(self):
        self.level += 1
        self.rows_left = self.level * 2

    def miss(self):
        self.lives -= 1
    def hit(self):
        self.score +=10
