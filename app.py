class Board:
    def __init__(self):
        self.grid = []  

        for i in range(3):
            row = []

            for j in range(3):
                row.append(" ")
            self.grid.append(row)
        
    def reset_board(self): # resets the data in the board
        self.grid = []  
        for i in range(3):
            row = []

            for j in range(3):
                row.append(" ")
            self.grid.append(row)
    def display_board(self): # prints the separators
        for row_index in range(3):
            row = self.grid[row_index]

            print ("|".join(row))

            if row_index < 2:
                print ("--+---+--")
            
    def place_mark(self, row, col, mark): # checks if chosen one is empty and if it is marks it
        if self.grid[row][col] == " ":
            self.grid[row][col] = mark
            return True
        return False
    
    def check_win(self):
        for row in self.grid:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != " ":
                return self.grid[0][col]

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]            

        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]

        return None

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == " ":
                    return False
                return True


        
class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        

    def get_move(self, board):
        while True:
            try:
                move = input(f"{self.name} ({self.mark}), enter your move as row, col (0-2): ")
                row, col = map(int, move.split(","))

                if row in range(3) and col in range(3):
                    if board.grid[row][col] == " ":
                        return row, col
                    else:
                        print("Spot taken. Try again later")

                else:
                    print("Row and column must be between 0 and 2")

            except ValueError:
                print ("Invalid input. enter in this format: row, col(e.g., 1,2)")

class Computer:
    def __init__(self, mark):
    def get_move(self, board):

#class Game:
#    def __init__(self):
#    def switch_turn(self):
#    def is_over(self):
#    def play_turn(self):
