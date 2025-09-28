from tictactoe import TicTacToe
from tictactoe.player.ai import AIPlayer
from tictactoe.player.ai.easy import EasyAIPlayer
from tictactoe.player.ai.medium import MediumAIPlayer
from tictactoe.player.ai.hard import HardAIPlayer
from tictactoe.player.manual import ManualPlayer
from tictactoe.renderer import Renderer
from tictactoe.renderer.console import ConsoleRenderer
from tictactoe.renderer.tkinter import TicTacToeRoot


class ConsoleRenderer(Renderer):

    def render(self):
        for row in self._tic_tac_toe.grid:
            print(row)
