import unittest

from tictactoe import TicTacToe
from tictactoe.player.ai.easy import EasyAIPlayer
from tictactoe.player.ai.medium import MediumAIPlayer
# from tictactoe.player.ai.medium import HardAIPlayer
from tictactoe.player.manual import ManualPlayer


class TestAIs(unittest.TestCase):
    
    def setUp(self):
        self._tic_tac_toe = TicTacToe()
        self._tic_tac_toe.add_player(ManualPlayer, "X", "John")
    
    def test_easy_picks_first_available_spot(self):
        self._tic_tac_toe.add_player(EasyAIPlayer, "O", "AI")

        self._tic_tac_toe.place(0, 0)

        grid = self._tic_tac_toe.grid
        ai = self._tic_tac_toe.players[1]
        self.assertEqual(ai.get_move(grid), (1, 0))
    
    def test_medium_picks_self_winning_move_if_available(self):
        self._tic_tac_toe.add_player(MediumAIPlayer, "O", "AI")

        # Set up for both players to be able to win
        self._tic_tac_toe.place(0, 0)
        self._tic_tac_toe.place(1, 0)
        self._tic_tac_toe.place(0, 1)
        self._tic_tac_toe.place(1, 1)

        # Place X in the bottom-right corner to keep it out of the way
        self._tic_tac_toe.place(2, 2)

        grid = self._tic_tac_toe.grid
        ai = self._tic_tac_toe.players[1]
        self.assertEqual(ai.get_move(grid), (1, 2))
    
    def test_medium_picks_opponent_winning_move_if_available(self):
        self._tic_tac_toe.add_player(MediumAIPlayer, "O", "AI")

        # Set up for both players to be able to win
        self._tic_tac_toe.place(0, 0)
        self._tic_tac_toe.place(1, 0)
        self._tic_tac_toe.place(0, 1)
        self._tic_tac_toe.place(1, 1)

        # Place X in the bottom-right corner to keep it out of the way
        self._tic_tac_toe.place(2, 2)

        grid = self._tic_tac_toe.grid
        ai = self._tic_tac_toe.players[1]
        self.assertEqual(ai.get_move(grid), (1, 2))
