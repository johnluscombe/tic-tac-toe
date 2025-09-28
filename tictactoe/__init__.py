from typing import Type

from tictactoe.player import Player

GRID_SIZE = 3
MIN_PLAYERS = 2
MAX_PLAYERS = 2


class TicTacToe:
    """
    Class for encapsulating the state of the game grid and performing actions
    on it.
    """

    def __init__(self):
        self.reset()

        self._players = []
        self._current_player_idx = None
    
    @property
    def grid(self) -> list[list[str]]:
        """
        Returns the grid.

        Returns:
            list[list[str]]
        """

        return self._grid

    @property
    def players(self) -> list[Player]:
        """
        Returns the players.

        Returns:
            list[Player]
        """

        return self._players
    
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

        for i in range(len(self.grid)):
            # Check rows
            if len(set(self._grid[i])) == 1 and not not self._grid[i][0]:
                return self._get_player_from_letter(self._grid[i][0])
            
            # Check cols
            col = []
            for j in range(len(self.grid)):
                col.append(self._grid[j][i])
            if len(set(col)) == 1 and not not col[0]:
                return self._get_player_from_letter(col[0])

            diag_one.append(self._grid[i][i])
            diag_two.append(self._grid[len(self.grid) - i - 1][i])
        
        # Check diagonal one
        if len(set(diag_one)) == 1 and not not diag_one[0]:
            return self._get_player_from_letter(diag_one[0])
        
        # Check diagonal two
        if len(set(diag_two)) == 1 and not not diag_two[0]:
            return self._get_player_from_letter(diag_two[0])
        
        return None
    
    @property
    def game_over(self) -> bool:
        """
        Returns whether or not the game is over, either from a win or a stalemate.

        Returns:
            bool
        """

        board_full = True
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if not self._grid[i][j]:
                    board_full = False
        
        return board_full or self.winner is not None
    
    def place(self, x: int, y: int) -> bool:
        """
        Places the letter of the current player at the given coordinates.
        Returns whether the move was successfully placed.

        Arguments:
            x (int): X grid coordinate.
            y (int): Y grid coordinate.
        """

        if len(self._players) < MIN_PLAYERS:
            raise Exception("Not enough players")
        
        if self.winner is not None:
            raise Exception("A winner has already been declared, please reset the game")
    
        if self._current_player_idx is None:
            self._current_player_idx = 0
        else:
            self._current_player_idx = (self._current_player_idx + 1) % len(self._players)
        
        current_player = self._players[self._current_player_idx]

        if self._is_valid_move(x, y):
            self._grid[y][x] = current_player.letter
            return True
        
        return False

    def add_player(self, player_class: Type[Player], letter: str, name: str):
        """
        Adds a player to the game.

        Arguments:
            player_class: Class of player to add to the game.
            letter (str): Letter to use for the player.
            name (str): Name to use for the player.
        """

        if len(self._players) == MAX_PLAYERS:
            raise Exception("Max number of players already reached")
        
        for other_player in self._players:
            if other_player.letter == letter:
                raise Exception("Letter already used by another player")

        self._players.append(player_class(len(self._players) + 1, letter, name))
    
    def reset(self):
        """
        Resets the game.
        """

        self._grid = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                row.append("")
            self._grid.append(row)
    
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

        within_bounds = (0 <= x < len(self.grid)) and (0 <= y < len(self.grid))
        if within_bounds:
            return not self._grid[y][x]
        return False
    
    def _get_player_from_letter(self, letter: str) -> Player:
        """
        Returns the player corresponding with the given letter.

        Arguments:
            letter (str): Letter to get the player of.
        
        Returns:
            :class:`~Player`
        """

        for player in self._players:
            if player.letter == letter:
                return player

        return None
