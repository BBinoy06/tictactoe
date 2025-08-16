class Board:
    def __init__(self):
        self.grid = []  

        for i in range(3):
            row = []

            for j in range(3):
                row.append(" ")
            self.grid.append(row)
        
    def reset_board(self):
        self.grid = []  

        for i in range(3):
            row = []

            for j in range(3):
                row.append(" ")
            self.grid.append(row)
    def display_board(self):
        for row_index in range(3):
            row = self.grid[row_index]

            print ("|".join(row))

            if row_index < 2:
                print ("--+---+--")

            
    def place_mark(self, row, col, mark):
    def check_win(self):
    def is_full(self):

class Player:
    def __init__(self, name, mark):
    def get_move(self, board):

class Computer:
    def __init__(self, mark):
    def get_move(self, board):

class Game:
    def __init__(self):
    def switch_turn(self):
    def is_over(self):
    def play_turn(self):
