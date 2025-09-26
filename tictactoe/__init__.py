GRID_SIZE = 3
VALID_LETTERS = ["x", "o"]


class TicTacToe:
    """
    Class for encapsulating the state of the game grid and performing actions
    on it.
    """

    def __init__(self):
        self._grid = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
    
    @property
    def grid(self) -> list[list[str]]:
        """
        Returns the grid.

        Returns:
            list[list[str]]
        """

        return self._grid
    
    @property
    def winner(self) -> str | None:
        """
        Returns the winner of the game. Returns None if the game is still in
        progress.

        Returns:
            str or None
        """

        diag_one = []
        diag_two = []

        for i in range(GRID_SIZE):
            # Check rows
            if len(set(self._grid[i])) == 1 and not not self._grid[i][0]:
                return self._grid[i][0]
            
            # Check cols
            col = []
            for j in range(GRID_SIZE):
                col.append(self._grid[j][i])
            if len(set(col)) == 1 and not not col[0]:
                return col[0]

            diag_one.append(self._grid[i][i])
            diag_two.append(self._grid[GRID_SIZE - i - 1][i])
        
        # Check diagonal one
        if len(set(diag_one)) == 1 and not not diag_one[0]:
            return diag_one[0]
        
        # Check diagonal two
        if len(set(diag_two)) == 1 and not not diag_two[0]:
            return diag_two[0]
        
        return None
    
    @property
    def game_over(self):
        board_full = True
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if not self._grid[i][j]:
                    board_full = False
        
        return board_full or self.winner is not None
    
    def place(self, letter: str, x: int, y: int) -> bool:
        """
        Places the given letter at the given coordinates. Returns whether the
        move was successfully placed.

        Arguments:
            letter (str): The letter to place.
            x (int): X grid coordinate.
            y (int): Y grid coordinate.
        """

        if letter.lower() in VALID_LETTERS and self._is_valid_move(x, y):
            self._grid[y][x] = letter
            return True
        
        return False
    
    def reset(self):
        """
        Resets the game.
        """

        self._grid = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
    
    def _is_valid_move(self, x: int, y: int) -> bool:
        """
        Returns whether the given grid coordinates represent a valid move.
        In order to be valid, the grid coordinates must be within bounds and
        not already occupied.

        Arguments:
            x (int): X grid coordinate.
            y (int): Y grid coordinate.

        Returns:
            bool
        """

        within_bounds = (0 <= x < GRID_SIZE) and (0 <= y < GRID_SIZE)
        if within_bounds:
            return not self._grid[y][x]
        return False
