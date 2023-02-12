class jump():
    def __init__(self):
        self.start=None
        self.end=None

class board():
    def __init__(self,number_of_snake,number_of_ladder):
        self.define_board()
        print(self.cells[10].start)
    def define_board(self):
        self.cells=[jump() for i in range (100)]
        print(self.cells[0],self.cells[1])
        for i in range(len(self.cells)):
            self.cells[i].start=i
            self.cells[i].end=-i

board(1,1)