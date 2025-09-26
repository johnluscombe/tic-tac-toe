import re

from tictactoe.player.ai import AIPlayer


class EasyAIPlayer(AIPlayer):
    """
    An easy AI player that simply picks the first available spot in the grid.
    """

    def _get_move(self, grid: list[list[str]]) -> tuple[int]:
        self._get_first_available_move(grid)
    
    def _get_first_available_move(self, grid: list[list[str]]) -> tuple[int]:
        """
        Gets the first available spot in the grid.

        Arguments:
            grid (list[list[str]]): The grid.
        
        Returns:
            tuple[int]
        """

        for i in range(len(grid)):
            for j in range(len(grid)):
                if not grid[i][j]:
                    return j, i
        
        return None
