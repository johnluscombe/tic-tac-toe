import unittest

from tictactoe import TicTacToe
from tictactoe.player.manual import ManualPlayer


class TestTicTacToe(unittest.TestCase):
    
    def setUp(self):
        self._tic_tac_toe = TicTacToe()
        self._tic_tac_toe.add_player(ManualPlayer, "X", "John")
        self._tic_tac_toe.add_player(ManualPlayer, "O", "Jill")
    
    def test_grid(self):
        grid = self._tic_tac_toe.grid
        for i in range(len(grid)):
            for j in range(len(grid)):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_players(self):
        players = self._tic_tac_toe.players
        self.assertEqual(2, len(players))
        self.assertIsInstance(players[0], ManualPlayer)
        self.assertEqual(players[0].letter, "X")
        self.assertEqual(players[0].name, "John")
        self.assertIsInstance(players[1], ManualPlayer)
        self.assertEqual(players[1].letter, "O")
        self.assertEqual(players[1].name, "Jill")
    
    def test_place_valid_move(self):
        self.assertTrue(self._tic_tac_toe.place(0, 0))
        self.assertEqual(self._tic_tac_toe.grid[0][0], "X")
        self.assertTrue(self._tic_tac_toe.place(2, 0))
        self.assertEqual(self._tic_tac_toe.grid[0][2], "O")
        self.assertTrue(self._tic_tac_toe.place(0, 2))
        self.assertEqual(self._tic_tac_toe.grid[2][0], "X")
        self.assertTrue(self._tic_tac_toe.place(2, 2))
        self.assertEqual(self._tic_tac_toe.grid[2][2], "O")
            
    def test_place_accepts_capitals(self):
        self.assertTrue(self._tic_tac_toe.place(0, 0))
        self.assertTrue(self._tic_tac_toe.place(1, 0))
    
    def test_place_too_far_left(self):
        grid = self._tic_tac_toe.grid

        self.assertFalse(self._tic_tac_toe.place(-1, 0))
        self.assertFalse(self._tic_tac_toe.place(-1, 0))

        for i in range(len(grid)):
            for j in range(len(grid)):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_place_too_far_right(self):
        grid = self._tic_tac_toe.grid

        self.assertFalse(self._tic_tac_toe.place(len(grid), 0))
        self.assertFalse(self._tic_tac_toe.place(len(grid), 0))
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_place_too_far_up(self):
        grid = self._tic_tac_toe.grid

        self.assertFalse(self._tic_tac_toe.place(0, -1))
        self.assertFalse(self._tic_tac_toe.place(0, -1))
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_place_too_far_down(self):
        grid = self._tic_tac_toe.grid

        self.assertFalse(self._tic_tac_toe.place(0, len(grid)))
        self.assertFalse(self._tic_tac_toe.place(0, len(grid)))
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_place_zero_players(self):
        with self.assertRaises(Exception):
            TicTacToe().place(0, 0)
    
    def test_place_one_player(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.add_player(ManualPlayer, "X", "John")
        with self.assertRaises(Exception):
            tic_tac_toe.place(0, 0)
    
    def test_add_player_too_many_players(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.add_player(ManualPlayer, "X", "John")
        tic_tac_toe.add_player(ManualPlayer, "O", "Jill")
        with self.assertRaises(Exception):
            tic_tac_toe.add_player(ManualPlayer, "A", "Jack")
    
    def test_add_player_same_letter(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.add_player(ManualPlayer, "X", "John")
        with self.assertRaises(Exception):
            tic_tac_toe.add_player(ManualPlayer, "X", "Jill")
    
    def test_reset(self):
        grid = self._tic_tac_toe.grid

        self._fill_grid()
        self._tic_tac_toe.reset()
            
        for i in range(len(grid)):
            for j in range(len(grid)):
                self.assertEqual(self._tic_tac_toe.grid[i][j], "")
    
    def test_winner_rows_x(self):
        grid = self._tic_tac_toe.grid
        for row in range(len(grid)):
            for i in range(len(grid) - 1):
                # Place X in current row
                self._tic_tac_toe.place(i, row)
                # Place O in one row down (or top row if at the bottom)
                self._tic_tac_toe.place(i, (row + 1) % len(grid))
            # Place winning piece for X in current row
            self._tic_tac_toe.place(len(grid) - 1, row)
            self.assertEqual("X", self._tic_tac_toe.winner.letter)

            # Reset for next game
            self.setUp()
    
    def test_winner_rows_o(self):
        grid = self._tic_tac_toe.grid
        for row in range(len(grid)):
            # Place X two rows down to keep it out of the way
            # (loops around to top if necessary)
            self._tic_tac_toe.place(0, (row + 2) % len(grid))
            for i in range(len(grid) - 1):
                # Place O in current row
                self._tic_tac_toe.place(i, row)
                # Place X in one row down (or top row if at the bottom)
                self._tic_tac_toe.place(i, (row + 1) % len(grid))
            # Place winning piece for O in current row
            self._tic_tac_toe.place(len(grid) - 1, row)
            self.assertEqual("O", self._tic_tac_toe.winner.letter)

            # Reset for next game
            self.setUp()
    
    def test_winner_cols_x(self):
        grid = self._tic_tac_toe.grid
        for col in range(len(grid)):
            for i in range(len(grid) - 1):
                # Place X in current column
                self._tic_tac_toe.place(col, i)
                # Place O one column to the right (or left column if at the bottom)
                self._tic_tac_toe.place((col + 1) % len(grid), i)
            # Place winning piece for X in current column
            self._tic_tac_toe.place(col, len(grid) - 1)
            self.assertEqual("X", self._tic_tac_toe.winner.letter)

            # Reset for next game
            self.setUp()
    
    def test_winner_cols_o(self):
        grid = self._tic_tac_toe.grid
        for col in range(len(grid)):
            # Place X two columns to the right to keep it out of the way
            # (loops around to left if necessary)
            self._tic_tac_toe.place((col + 2) % len(grid), 0)
            for i in range(len(grid) - 1):
                # Place O in current column
                self._tic_tac_toe.place(col, i)
                # Place O one column to the right (or left column if at the bottom)
                self._tic_tac_toe.place((col + 1) % len(grid), i)
            # Place winning piece for O in current column
            self._tic_tac_toe.place(col, len(grid) - 1)
            self.assertEqual("O", self._tic_tac_toe.winner.letter)

            # Reset for next game
            self.setUp()
    
    def test_winner_diag1_x(self):
        grid = self._tic_tac_toe.grid
        for i in range(len(grid) - 1):
            # Place X
            self._tic_tac_toe.place(i, i)
            # Place O one column to the right (or left column if at the bottom)
            self._tic_tac_toe.place((i + 1) % len(grid), i)
        # Place winning piece for X in the bottom-right corner
        self._tic_tac_toe.place(len(grid) - 1, len(grid) - 1)
        self.assertEqual("X", self._tic_tac_toe.winner.letter)
    
    def test_winner_diag1_o(self):
        grid = self._tic_tac_toe.grid
        # Place X in the bottom-left corner to keep it out of the way
        self._tic_tac_toe.place(0, len(grid) - 1)
        for i in range(len(grid) - 1):
            # Place O
            self._tic_tac_toe.place(i, i)
            # Place X one column to the right (or left column if at the bottom)
            self._tic_tac_toe.place((i + 1) % len(grid), i)
        # Place winning piece for O in the bottom-right corner
        self._tic_tac_toe.place(len(grid) - 1, len(grid) - 1)
        self.assertEqual("O", self._tic_tac_toe.winner.letter)
    
    def test_winner_diag2_x(self):
        grid = self._tic_tac_toe.grid
        for i in range(len(grid) - 1):
            # Place X
            self._tic_tac_toe.place(len(grid) - i - 1, i)
            # Place O one column to the right (or left column if at the bottom)
            self._tic_tac_toe.place(i, (i + 1) % len(grid))
        # Place winning piece for X in the bottom-left corner
        self._tic_tac_toe.place(0, len(grid) - 1)
        self.assertEqual("X", self._tic_tac_toe.winner.letter)
    
    def test_winner_diag2_o(self):
        grid = self._tic_tac_toe.grid
        # Place X in the bottom-right corner to keep it out of the way
        self._tic_tac_toe.place(len(grid) - 1, len(grid) - 1)
        for i in range(len(grid) - 1):
            # Place O
            self._tic_tac_toe.place(i, len(grid) - i - 1)
            # Place X one column to the right (or left column if at the bottom)
            self._tic_tac_toe.place((i + 1) % len(grid), i)
        # Place winning piece for O in the bottom-left corner
        self._tic_tac_toe.place(len(grid) - 1, 0)
        self.assertEqual("O", self._tic_tac_toe.winner.letter)
    
    def test_winner_no_winner(self):
        self.assertIsNone(self._tic_tac_toe.winner)
    
    def test_winner_stalemate(self):
        self.assertIsNone(self._tic_tac_toe.winner)
    
    def test_game_over_winner_rows_x(self):
        grid = self._tic_tac_toe.grid
        for row in range(len(grid)):
            for i in range(len(grid) - 1):
                # Place X in current row
                self._tic_tac_toe.place(i, row)
                # Place O in one row down (or top row if at the bottom)
                self._tic_tac_toe.place(i, (row + 1) % len(grid))
            # Place winning piece for X in current row
            self._tic_tac_toe.place(len(grid) - 1, row)
            self.assertTrue(self._tic_tac_toe.game_over)

            # Reset for next game
            self.setUp()
    
    def test_game_over_winner_rows_o(self):
        grid = self._tic_tac_toe.grid
        for row in range(len(grid)):
            # Place X two rows down to keep it out of the way
            # (loops around to top if necessary)
            self._tic_tac_toe.place(0, (row + 2) % len(grid))
            for i in range(len(grid) - 1):
                # Place O in current row
                self._tic_tac_toe.place(i, row)
                # Place X in one row down (or top row if at the bottom)
                self._tic_tac_toe.place(i, (row + 1) % len(grid))
            # Place winning piece for O in current row
            self._tic_tac_toe.place(len(grid) - 1, row)
            self.assertTrue(self._tic_tac_toe.game_over)

            # Reset for next game
            self.setUp()
    
    def test_game_over_winner_cols_x(self):
        grid = self._tic_tac_toe.grid
        for col in range(len(grid)):
            for i in range(len(grid) - 1):
                # Place X in current column
                self._tic_tac_toe.place(col, i)
                # Place O one column to the right (or left column if at the bottom)
                self._tic_tac_toe.place((col + 1) % len(grid), i)
            # Place winning piece for X in current column
            self._tic_tac_toe.place(col, len(grid) - 1)
            self.assertTrue(self._tic_tac_toe.game_over)

            # Reset for next game
            self.setUp()
    
    def test_game_over_winner_cols_o(self):
        grid = self._tic_tac_toe.grid
        for col in range(len(grid)):
            # Place X two columns to the right to keep it out of the way
            # (loops around to left if necessary)
            self._tic_tac_toe.place((col + 2) % len(grid), 0)
            for i in range(len(grid) - 1):
                # Place O in current column
                self._tic_tac_toe.place(col, i)
                # Place O one column to the right (or left column if at the bottom)
                self._tic_tac_toe.place((col + 1) % len(grid), i)
            # Place winning piece for O in current column
            self._tic_tac_toe.place(col, len(grid) - 1)
            self.assertTrue(self._tic_tac_toe.game_over)

            # Reset for next game
            self.setUp()
    
    def test_game_over_winner_diag1_x(self):
        grid = self._tic_tac_toe.grid
        for i in range(len(grid) - 1):
            # Place X
            self._tic_tac_toe.place(i, i)
            # Place O one column to the right (or left column if at the bottom)
            self._tic_tac_toe.place((i + 1) % len(grid), i)
        # Place winning piece for X in the bottom-right corner
        self._tic_tac_toe.place(len(grid) - 1, len(grid) - 1)
        self.assertTrue(self._tic_tac_toe.game_over)
    
    def test_game_over_winner_diag1_o(self):
        grid = self._tic_tac_toe.grid
        # Place X in the bottom-left corner to keep it out of the way
        self._tic_tac_toe.place(0, len(grid) - 1)
        for i in range(len(grid) - 1):
            # Place O
            self._tic_tac_toe.place(i, i)
            # Place X one column to the right (or left column if at the bottom)
            self._tic_tac_toe.place((i + 1) % len(grid), i)
        # Place winning piece for O in the bottom-right corner
        self._tic_tac_toe.place(len(grid) - 1, len(grid) - 1)
        self.assertTrue(self._tic_tac_toe.game_over)
    
    def test_game_over_winner_diag2_x(self):
        grid = self._tic_tac_toe.grid
        for i in range(len(grid) - 1):
            # Place X
            self._tic_tac_toe.place(len(grid) - i - 1, i)
            # Place O one column to the right (or left column if at the bottom)
            self._tic_tac_toe.place(i, (i + 1) % len(grid))
        # Place winning piece for X in the bottom-left corner
        self._tic_tac_toe.place(0, len(grid) - 1)
        self.assertTrue(self._tic_tac_toe.game_over)
    
    def test_game_over_winner_diag2_o(self):
        grid = self._tic_tac_toe.grid
        # Place X in the bottom-right corner to keep it out of the way
        self._tic_tac_toe.place(len(grid) - 1, len(grid) - 1)
        for i in range(len(grid) - 1):
            # Place O
            self._tic_tac_toe.place(i, len(grid) - i - 1)
            # Place X one column to the right (or left column if at the bottom)
            self._tic_tac_toe.place((i + 1) % len(grid), i)
        # Place winning piece for O in the bottom-left corner
        self._tic_tac_toe.place(len(grid) - 1, 0)
        self.assertTrue(self._tic_tac_toe.game_over)
    
    def test_game_over_board_stalemate(self):
        self._fill_grid()
        self.assertTrue(self._tic_tac_toe.game_over)
    
    def test_game_over_board_not_full(self):
        self.assertFalse(self._tic_tac_toe.game_over)
    
    def _fill_grid(self):
        self._tic_tac_toe.place(1, 0)
        self._tic_tac_toe.place(0, 0)
        self._tic_tac_toe.place(0, 1)
        self._tic_tac_toe.place(2, 0)
        self._tic_tac_toe.place(1, 1)
        self._tic_tac_toe.place(2, 1)
        self._tic_tac_toe.place(0, 2)
        self._tic_tac_toe.place(1, 2)
        self._tic_tac_toe.place(2, 2)
