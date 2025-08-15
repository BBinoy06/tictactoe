class Board:
    def __init__(self):
    def reset_board(self):
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
