import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board(self):
        expected_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(self.game.board, expected_board)
        self.assertIsNone(self.game.current_winner)

    def test_make_move(self):
        self.assertTrue(self.game.make_move(0, 'X'))
        self.assertEqual(self.game.board, ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

    def test_make_invalid_move(self):
        self.assertTrue(self.game.make_move(0, 'X'))
        self.assertFalse(self.game.make_move(0, 'O'))
        self.assertEqual(self.game.board, ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

    def test_winner_row(self):
        self.assertTrue(self.game.make_move(0, 'X'))
        self.assertTrue(self.game.make_move(1, 'X'))
        self.assertTrue(self.game.make_move(2, 'X'))
        self.assertTrue(self.game.winner(2, 'X'))

    def test_winner_column(self):
        self.assertTrue(self.game.make_move(0, 'O'))
        self.assertTrue(self.game.make_move(3, 'O'))
        self.assertTrue(self.game.make_move(6, 'O'))
        self.assertTrue(self.game.winner(6, 'O'))

    def test_winner_diagonal(self):
        self.assertTrue(self.game.make_move(0, 'X'))
        self.assertTrue(self.game.make_move(4, 'X'))
        self.assertTrue(self.game.make_move(8, 'X'))
        self.assertTrue(self.game.winner(8, 'X'))

    def test_no_winner(self):
        self.assertTrue(self.game.make_move(0, 'X'))
        self.assertTrue(self.game.make_move(1, 'O'))
        self.assertTrue(self.game.make_move(2, 'X'))
        self.assertFalse(self.game.winner(2, 'X'))

if __name__ == '__main__':
    unittest.main()
