from tictactoe.renderer import Renderer


class ConsoleRenderer(Renderer):

    def render(self):
        for row in self._tic_tac_toe.grid:
            print(row)
