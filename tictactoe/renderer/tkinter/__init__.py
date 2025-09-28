from tictactoe.renderer import Renderer
from tictactoe.renderer.tkinter.root import TicTacToeRoot


class TkinterRenderer(Renderer):

    def __init__(self, *args):
        super().__init__(*args)

        self._app = None
    
    def render(self):
        if self._app is None:
            self._app = TicTacToeRoot()
            self._app.mainloop()
