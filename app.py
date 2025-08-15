import tkinter as tk

# class Board:
#   def reset_board()
#   def place_mark(row, col, player)
#   def check_win()
#   def is_full()
# class Player:
#   def get_more
# class Computer:
#   def play_turn
#   def is_over
#   def switch_turn
# class Game:
#   def get_more(booard)

class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
    
    def reset_board(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
    
    def place_mark(self, row, col, player):
        if self.grid[row][col] == " ":
            self.grid[row][col] = player
            return True
        return False
    
    def check_win(self):
        # Check rows, columns, diagonals
        # Return "X", "O" if someone wins, or None
        pass
    
    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    
    def get_move(self, board):
        # Ask player for input (row, col)
        pass


class Computer:
    def __init__(self, mark):
        self.mark = mark
    
    def get_move(self, board):
        # For MVP: return a random empty cell
        # Later: implement Minimax AI
        pass


class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player("Human", "X")
        self.computer = Computer("O")
        self.current_turn = self.player
    
    def switch_turn(self):
        self.current_turn = self.computer if self.current_turn == self.player else self.player
    
    def is_over(self):
        return self.board.check_win() is not None or self.board.is_full()
    
    def play_turn(self):
        if self.current_turn == self.player:
            row, col = self.player.get_move(self.board)
            self.board.place_mark(row, col, self.player.mark)
        else:
            row, col = self.computer.get_move(self.board)
            self.board.place_mark(row, col, self.computer.mark)
        self.switch_turn()

