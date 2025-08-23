import unittest
from app import Board, Player, Computer

class TestBoard(unittest.TestCase):
    def test_board_initialisation(self):
        board = Board()
        self.assertEqual(board.grid, [[" "] * 3 for _ in range(3)]

class TestPlayer(unittest.TestCase):
    def test_player_initialistion(self):
        player = Player("BB", "X")
        self.assertEqual(player.name, "BB")
        self.assertEqual(player.mark, "X")

if __name__ == "__main__":
    unittest.main()
