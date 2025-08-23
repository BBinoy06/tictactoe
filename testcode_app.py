import unittest
from app import Board, Player, Computer, Game

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

    def test_first_current_player(self):
        self.assertEqual(self.game.current_player, self.game.player1)

    def test_switch_turn(self):
        original_player = self.game.current_player
        self.game.switch_turn()
        self.assertNotEqual(self.game.current_player, original_player)
        self.game.switch_turn()
        self.assertEqual(self.game.current_player, original_player)

    def test_is_over_empty_board(self):
        self.assertFalse(self.game.board.is_full())
        self.assertIsNone(self.game.board.check_win())


if __name__ == "__main__":
    unittest.main()
