import unittest
from app import Board, Player, Computer

class TestBoard(unittest.TestCase):
    def test_board_initialisation(self):
        board = Board()
        self.assertEqual(board.grid, [[" "] * 3 for _ in range(3)])

class TestPlayer(unittest.TestCase):
    def test_player_initialistion(self):
        player = Player("BB", "X")
        self.assertEqual(player.name, "BB")
        self.assertEqual(player.mark, "X")

class TestComputer(unittest.TestCase):
    def test_computer_initialisation(self):
        computer = Computer("O")
        self.assertEqual(computer.mark, "O")

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        

if __name__ == "__main__":
    unittest.main()
