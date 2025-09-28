import re

from tictactoe.player.ai.easy import EasyAIPlayer


class MediumAIPlayer(EasyAIPlayer):
    """
    A medium AI player that uses the following strategies:

    1. If it can win this turn, picks that move.
    2. If opponent can win next turn, blocks that move (or one of them).
    3. Picks the first available spot on the grid.
    """

    def _get_move(self, grid: list[list[str]]) -> tuple[int]:
        # First determine if I can win this turn
        move = self._get_winning_move(self.letter, grid)
        if move is not None:
            return move
        
        # Then determine if opponent can win their next turn, and if so, block it
        move = self._get_winning_move(None, grid)
        if move is not None:
            return move

        # Otherwise, just pick the first available move
        return self._get_first_available_move(grid)
    
    def _get_winning_move(self, letter: str, grid: list[list[str]]) -> tuple[int]:
        """
        If the opponent is one move away from winning, returns that winning
        move so the AI can block it.

        Arguments:
            letter (str): The letter to get the winning move of.
            grid (list[list[str]]): The grid.
        
        Returns:
            tuple[int]
        """

        # Check rows
        for row_num in range(len(grid)):
            row = grid[row_num]
            letter_counts = self._get_letter_counts(row)
            for l in letter_counts:
                if l == letter and letter_counts[l] == len(grid) - 1 and row.count("") == 1:
                    return row.index(""), row_num
        
        # Check cols
        for col_num in range(len(grid)):
            col = list(map(lambda row: row[col_num], grid))
            letter_counts = self._get_letter_counts(col)
            for l in letter_counts:
                if l == letter and letter_counts[l] == len(grid) - 1 and col.count("") == 1:
                    return col_num, col.index("")
        
        # Check diagonal 1
        diag = []
        for i in range(len(grid)):
            diag.append(grid[i][i])
        letter_counts = self._get_letter_counts(diag)
        for l in letter_counts:
            if l == letter and letter_counts[l] == len(grid) - 1 and diag.count("") == 1:
                idx = diag.index("")
                return idx, idx
        
        # Check diagonal 2
        diag = []
        for i in range(len(grid)):
            diag.append(grid[len(grid) - i - 1][i])
        letter_counts = self._get_letter_counts(diag)
        for l in letter_counts:
            if l == letter and letter_counts[l] == len(grid) - 1 and diag.count("") == 1:
                idx = diag.index("")
                return len(grid) - idx - 1, idx
        
        return None
    
    def _get_letter_counts(self, lst: list[str]) -> dict[str, int]:
        """
        Returns the count of each letter in the given list, ignoring empty
        strings.

        Arguments:
            lst (list[str]): List to use to count letters.
        
        Returns:
            dict
        """

        d = {}
        for letter in lst:
            if letter not in d:
                d[letter] = 0
            d[letter] += 1
        
        return d
