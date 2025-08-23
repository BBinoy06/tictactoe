import unittest
from app import Board, Player, Computer

class TestBoard(unittest.TestCase):
    def test_board_initialisation(self):
        board = Board()
        self.assertEqual(board.grid, [[" "] * 3 for _ in range(3)]

if __name__ == "__main__":
    unittest.main()
