from abc import ABC
from abc import abstractmethod

from tictactoe import TicTacToe


class Renderer(ABC):
    """
    Abstract class for rendering the game, such as the console or Tkinter.
    """

    def __init__(self, tic_tac_toe: TicTacToe):
        self._tic_tac_toe = tic_tac_toe

    @abstractmethod
    def render(self):
        """
        Renders the current state of the game.
        """

        pass
