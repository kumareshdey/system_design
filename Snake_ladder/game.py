import random

class jump():
    def __init__(self):
        self.start=None
        self.end=None

class players():
    def __init__(self,id,curr_pos):
        self.id=id
        self.curr_pos=curr_pos


class dice():
    def __init__(self):
        self.value= random.randint(1, 6)

class board():
    def __init__(self,number_of_snake,number_of_ladder):
        self.number_of_snake=number_of_snake
        self.number_of_ladder=number_of_ladder
        self.define_board()
    def define_board(self):
        self.cells=[jump() for i in range (100)]
    def snake_ladder(self):
        for i in range(self.number_of_ladder):
            strt=random.randint(0,99)
            end=random.randint(strt,99)
            self.cells



class game():
    def __init__(self,number_of_snake,number_of_ladder,no_of_player):

