import unittest

from tictactoe import GRID_SIZE
from tictactoe import TicTacToe
from tictactoe import VALID_LETTERS


class TestTicTacToe(unittest.TestCase):
    
    def setUp(self):
        self._tic_tac_toe = TicTacToe()
    
    def test_grid(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_place_valid_move(self):
        for letter in VALID_LETTERS:
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    self.assertTrue(self._tic_tac_toe.place(letter, i, j))
            
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    self.assertEqual(self._tic_tac_toe.grid[i][j], letter)
            
            self._tic_tac_toe = TicTacToe()
    
    def test_place_accepts_capitals(self):
        self.assertTrue(self._tic_tac_toe.place("X", 0, 0))
        self.assertTrue(self._tic_tac_toe.place("O", 1, 0))
    
    def test_place_invalid_letter(self):
        self.assertFalse(self._tic_tac_toe.place("a", 0, 0))
        self.assertEqual(self._tic_tac_toe.grid[0][0], "")
    
    def test_place_too_far_left(self):
        self.assertFalse(self._tic_tac_toe.place("x", -1, 0))
        self.assertFalse(self._tic_tac_toe.place("o", -1, 0))

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_place_too_far_right(self):
        self.assertFalse(self._tic_tac_toe.place("x", 3, 0))
        self.assertFalse(self._tic_tac_toe.place("o", 3, 0))
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_place_too_far_up(self):
        self.assertFalse(self._tic_tac_toe.place("x", 0, -1))
        self.assertFalse(self._tic_tac_toe.place("o", 0, -1))
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_place_too_far_down(self):
        self.assertFalse(self._tic_tac_toe.place("x", 0, 3))
        self.assertFalse(self._tic_tac_toe.place("o", 0, 3))
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_reset(self):
        for letter in VALID_LETTERS:
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    self._tic_tac_toe.place(letter, i, j)
            
            self._tic_tac_toe.reset()
            
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_winner_rows(self):
        for letter in VALID_LETTERS:
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    self._tic_tac_toe.place(letter, col, row)
                self.assertEqual(letter, self._tic_tac_toe.winner)
                self._tic_tac_toe = TicTacToe()
    
    def test_winner_cols(self):
        for letter in VALID_LETTERS:
            for col in range(GRID_SIZE):
                for row in range(GRID_SIZE):
                    self._tic_tac_toe.place(letter, col, row)
                self.assertEqual(letter, self._tic_tac_toe.winner)
                self._tic_tac_toe = TicTacToe()
    
    def test_winner_diag1(self):
        for letter in VALID_LETTERS:
            for i in range(GRID_SIZE):
                self._tic_tac_toe.place(letter, i, i)
            self.assertEqual(letter, self._tic_tac_toe.winner)
            self._tic_tac_toe = TicTacToe()
    
    def test_winner_diag2(self):
        for letter in VALID_LETTERS:
            for i in range(GRID_SIZE):
                self._tic_tac_toe.place(letter, GRID_SIZE - i - 1, i)
            self.assertEqual(letter, self._tic_tac_toe.winner)
            self._tic_tac_toe = TicTacToe()
    
    def test_winner_no_winner(self):
        self.assertIsNone(self._tic_tac_toe.winner)
    
    def test_winner_stalemate(self):
        self._tic_tac_toe.place("o", 0, 0)
        self._tic_tac_toe.place("x", 1, 0)
        self._tic_tac_toe.place("o", 2, 0)
        self._tic_tac_toe.place("x", 0, 1)
        self._tic_tac_toe.place("x", 1, 1)
        self._tic_tac_toe.place("o", 2, 1)
        self._tic_tac_toe.place("x", 0, 2)
        self._tic_tac_toe.place("o", 1, 2)
        self._tic_tac_toe.place("x", 2, 2)
        self.assertIsNone(self._tic_tac_toe.winner)
    
    def test_game_over_winner_rows(self):
        for letter in VALID_LETTERS:
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    self._tic_tac_toe.place(letter, col, row)
                self.assertTrue(self._tic_tac_toe.game_over)
                self._tic_tac_toe = TicTacToe()
    
    def test_game_over_winner_cols(self):
        for letter in VALID_LETTERS:
            for col in range(GRID_SIZE):
                for row in range(GRID_SIZE):
                    self._tic_tac_toe.place(letter, col, row)
                self.assertTrue(self._tic_tac_toe.game_over)
                self._tic_tac_toe = TicTacToe()
    
    def test_game_over_winner_diag1(self):
        for letter in VALID_LETTERS:
            for i in range(GRID_SIZE):
                self._tic_tac_toe.place(letter, i, i)
            self.assertTrue(self._tic_tac_toe.game_over)
            self._tic_tac_toe = TicTacToe()
    
    def test_game_over_winner_diag2(self):
        for letter in VALID_LETTERS:
            for i in range(GRID_SIZE):
                self._tic_tac_toe.place(letter, GRID_SIZE - i - 1, i)
            self.assertTrue(self._tic_tac_toe.game_over)
            self._tic_tac_toe = TicTacToe()
    
    def test_game_over_board_stalemate(self):
        self._tic_tac_toe.place("o", 0, 0)
        self._tic_tac_toe.place("x", 1, 0)
        self._tic_tac_toe.place("o", 2, 0)
        self._tic_tac_toe.place("x", 0, 1)
        self._tic_tac_toe.place("x", 1, 1)
        self._tic_tac_toe.place("o", 2, 1)
        self._tic_tac_toe.place("x", 0, 2)
        self._tic_tac_toe.place("o", 1, 2)
        self._tic_tac_toe.place("x", 2, 2)
        self.assertTrue(self._tic_tac_toe.game_over)
    
    def test_game_over_board_not_full(self):
        self.assertFalse(self._tic_tac_toe.game_over)
