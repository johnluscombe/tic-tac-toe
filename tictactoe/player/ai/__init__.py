from abc import ABC
from abc import abstractmethod

from tictactoe.player import Player


class AIPlayer(Player):

    def get_move(self, grid: list[list[str]]) -> tuple[int]:
        move = self._get_move(grid)
        print(self.name + f" plays ({move[0]}, {move[1]})")
        return move

    @abstractmethod
    def _get_move(self, grid: list[list[str]]) -> tuple[int]:
        """
        Gets the move from the player given the Tic Tac Toe grid.

        Arguments:
            grid (list[list[str]]): The Tic Tac Toe grid.
        
        Returns:
            tuple[int]
        """

        pass
