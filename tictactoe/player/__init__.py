from abc import ABC
from abc import abstractmethod


class Player(ABC):
    """
    Abstract class for a player of the Tic Tac Toe game, such as a manual
    player, or an AI.

    Attributes:
        player (int): Player 1 or 2, can be used by AI players for strategy.
        letter (str): Letter the player will use to place on the board.
        name (str): Name of the player.
    """

    def __init__(self, player: int, letter: str, name: str):
        self._player = player
        self._letter = letter
        self._name = name
    
    @property
    def letter(self) -> str:
        """
        Letter the player will use to place on the board.

        Returns:
            str
        """

        return self._letter
    
    @property
    def name(self) -> str:
        """
        Name of the player.

        Returns:
            str
        """

        return self._name

    @abstractmethod
    def get_move(self, grid: list[list[str]]) -> tuple[int]:
        """
        Gets the move from the player given the Tic Tac Toe grid.

        Arguments:
            grid (list[list[str]]): The Tic Tac Toe grid.
        
        Returns:
            tuple[int]
        """

        pass
