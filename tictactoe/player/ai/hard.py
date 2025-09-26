import re

from tictactoe import GRID_SIZE
from tictactoe import VALID_LETTERS
from tictactoe.player.ai.medium import MediumAIPlayer


class HardAIPlayer(MediumAIPlayer):
    """
    A hard AI player that uses the following strategies:
    """

    def _get_move(self, grid: list[list[str]]) -> tuple[int]:
        # First determine if I can win this turn
        move = self._get_winning_move(self._letter, grid)
        if move is not None:
            return move
        
        # Then determine if opponent can win their next turn, and if so, block it
        opponent_letter = VALID_LETTERS[int(not bool(VALID_LETTERS.index(self._letter)))]
        move = self._get_winning_move(opponent_letter, grid)
        if move is not None:
            return move
        
        # Get how many times we've played this game, it will matter for our
        # strategy later
        count = self._get_count(self.letter, grid)

        # Now to our strategy. It varies whether we are the first player to go.
        # If both players are experts, then the first player wins or ties every
        # time. Start with the first player strategy.
        if self._player == 1:
            if count == 0:
                # First move, pick a corner
                return 0, 0
            elif count == 1:
                # Second move, try to pick a corner in the same row or column
                # as our first move, but not a row or column that our opponent
                # picked
                if not grid[0][GRID_SIZE - 1] and not grid[0][1]:
                    return GRID_SIZE - 1, 0
                return 0, GRID_SIZE - 1
            elif count == 2:
                # Third move, try to pick a corner in the same row or column
                # as our first move
                if not grid[0][GRID_SIZE - 1]:
                    return GRID_SIZE - 1, 0
                elif not grid[GRID_SIZE - 1][0]:
                    return 0, GRID_SIZE - 1
                # Otherwise, pick the last remaining corner
                return grid[GRID_SIZE - 1][GRID_SIZE - 1]
        else:
            # Second player strategy, more defensive
            if count == 0:
                # First move, pick the center if available
                if not grid[1][1]:
                    return 1, 1
                # Otherwise, pick a non-corner edge
                return 0, 1
            # elif count == 1:
            
            # # If center picked, pick a non-corner edge - one on the same edge
            # # as the corner the opponent picked if they chose a corner
            # if (grid[0][0] == opponent_letter or
            #     grid[GRID_SIZE - 1][0] == opponent_letter):
            #     return 0, 1
            # if (grid[0][GRID_SIZE - 1] == opponent_letter or
            #     grid[GRID_SIZE - 1][GRID_SIZE - 1] == opponent_letter):
            #     return GRID_SIZE, 1
            
            # Otherwise, if last corner is available, pick it

        # Otherwise, just pick the first available move
        return self._get_first_available_move(grid)
    
    def _get_count(self, letter: str, grid: list[list[str]]) -> int:
        """
        Gets the count of the given letter on the given grid.

        Arguments:
            letter (str): The letter to count.
            grid (list[list[str]]): The grid to count on.

        Returns:
            int
        """

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == letter:
                    count += 1
        
        return count
