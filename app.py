import random

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
        print("\n   0   1   2")
        for row_index, row in enumerate(self.grid):
            print(f"{row_index}  " + " | ".join(row))
            if row_index < 2:
                print ("  ---+---+---")
        print()
            
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
    def __init__(self, mark, difficulty="easy"):
        self.mark = mark
        self.difficulty = difficulty

    def evaluate(self, board, noMoves):
        winner = board.check_win()
        if winner == self.mark:
            return 10 - noMoves
        elif winner == self.opponent:
            return -10 + noMoves
        return 0

    def minimax(self, board, noMoves):
        score = self.evaluate(board, noMoves)
        if score != 0:
            return score
        if board.is_full():
            return 0
        
    def get_move(self, board):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board.grid[r][c] == " "]

        if self.difficulty == "easy":
            return random.choice(empty_cells)

        if self.difficulty == "medium":
            for (r, c) in empty_cells:
                board.grid[r][c] = self.mark
                if board.check_win() ==self.mark:
                    board.grid[r][c] = " "
                    return r, c
                board.grid[r][c] = " "

            opponent = "X" if self.mark == "O" else "O"
            for r,c in empty_cells:
                board.grid[r][c] = opponent
                if board.check_win() == opponent:
                    board.grid[r][c] = " "
                    return r,c
                board.grid[r][c] = " "

            return random.choice(empty_cells)

        if self.difficulty == "hard":
            return
    
        
class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("B", "X")
        self.player2 = Computer("O")
        self.current_player = self.player1
        
    def switch_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        
    def is_over(self):
        if self.board.check_win() is not None:
            return True
        if self.board.is_full():
            return True
        return False
    
    def play_turn(self):
        row, col = self.current_player.get_move(self.board)
        self.board.place_mark(row, col, self.current_player.mark)
        self.board.display_board()

        if self.board.check_win():
            print(f"{self.current_player.mark} wins!")
            return True
        elif self.board.is_full():
            print("It's a draw!")
            return True
    
        self.switch_turn()
        return False


if __name__ == "__main__":
    
    print("Welcome to tictactoe")

    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    game = Game()

    game.player2 = Computer("O", difficulty)
    
    game.board.display_board()

    while not game.is_over():
        if game.play_turn():
            break
