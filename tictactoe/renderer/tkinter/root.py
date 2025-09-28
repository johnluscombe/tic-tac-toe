import tkinter as tk

from tictactoe import TicTacToe
from tictactoe.player import Player
from tictactoe.renderer.tkinter.canvas.grid import GridCanvas
from tictactoe.renderer.tkinter.event import BUTTON_1
from tictactoe.renderer.tkinter.event import CONFIGURE
from tictactoe.renderer.tkinter.style import BLACK
from tictactoe.renderer.tkinter.style import BOLD
from tictactoe.renderer.tkinter.style import WHITE
from tictactoe.util import resource_path

TITLE = "Tic Tac Toe"

PLAY = "PLAY"
PLAY_AGAIN = "PLAY AGAIN"

GAME_OVER_DELAY = 3500
AI_DELAY = 1000


class TicTacToeRoot(tk.Tk):
    """
    Root widget of the Tkinter window.
    """

    def __init__(self, tic_tac_toe: TicTacToe, players: list[Player]):
        super().__init__()

        self.title(TITLE)
        self.minsize(600, 600)
        self.configure(padx=50, pady=25)

        self._tic_tac_toe = tic_tac_toe
        self._players = players

        game_container = tk.Frame(self)

        grid_canvas = GridCanvas(self._tic_tac_toe, game_container, highlightthickness=0)
        grid_canvas.pack(fill=tk.BOTH, expand=True, pady=(0, 25))

        game_container.place(relx=0.5, rely=0.5, width=500, height=550, anchor=tk.CENTER)

        self._show_start_frame(grid_canvas)

        grid_canvas.bind(BUTTON_1, lambda event: self._on_grid_canvas_click(event, grid_canvas))
        grid_canvas.bind(CONFIGURE, lambda *args: grid_canvas.redraw())
    
    def _show_start_frame(self, grid_canvas):
        """
        Shows the starting screen with the "play" button.

        Arguments:
            grid_canvas (:class:`~GridCanvas`): Grid canvas object.
        """

        frame = tk.Frame(self, bg=PRIMARY_COLOR)
        label_container = tk.Frame(frame, bg=PRIMARY_COLOR)
        play_button_border = tk.Frame(label_container, borderwidth=2, bg=SECONDARY_COLOR, relief=tk.FLAT)
        play_button_padding = tk.Frame(play_button_border, bg=PRIMARY_COLOR)
        play_button_label = tk.Label(play_button_padding, text=PLAY, width=10, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, font=(None, 16, BOLD), relief=tk.FLAT)
        play_button_label.pack(padx=10, pady=10)
        play_button_padding.pack()
        play_button_border.pack(side=tk.TOP, pady=(20, 0))
        label_container.place(relx=0.5, rely=0.5, relwidth=1, anchor=tk.CENTER)
        frame.place(x=0, y=0, relwidth=1, relheight=1)

        play_button_border.bind(BUTTON_1, lambda *args: self._on_play(frame, grid_canvas))
        play_button_padding.bind(BUTTON_1, lambda *args: self._on_play(frame, grid_canvas))
        play_button_label.bind(BUTTON_1, lambda *args: self._on_play(frame, grid_canvas))
    
    def _show_game_over(self, grid_canvas):
        """
        Shows the "game over" frame.

        Arguments:
            grid_canvas (:class:`~GridCanvas`): Grid canvas object.
        """

        frame = tk.Frame(self, bg=WHITE)
        label_container = tk.Frame(frame, bg=WHITE)

        winner = None
        for player in self._players:
            if player.letter == self._tic_tac_toe.winner:
                winner = player
        
        if winner is None:
            winner_text = "Stalemate!"
        else:
            winner_text = winner.name + " wins!"
        
        winner_label = tk.Label(label_container, text=winner_text, font=(None, 16))
        winner_label.pack()
        
        play_button_border = tk.Frame(label_container, borderwidth=2, bg=BLACK, relief=tk.FLAT)
        play_button_padding = tk.Frame(play_button_border, bg=WHITE)
        play_button_label = tk.Label(play_button_padding, text=PLAY_AGAIN, width=10, bg=WHITE, fg=BLACK, font=(None, 16, BOLD), relief=tk.FLAT)
        play_button_label.pack(padx=10, pady=10)
        play_button_padding.pack()
        play_button_border.pack(side=tk.TOP, pady=(20, 0))

        label_container.place(relx=0.5, rely=0.5, relwidth=1, anchor=tk.CENTER)
        frame.place(x=0, y=0, relwidth=1, relheight=1)

        play_button_border.bind(BUTTON_1, lambda *args: self._on_play(frame, grid_canvas))
        play_button_padding.bind(BUTTON_1, lambda *args: self._on_play(frame, grid_canvas))
        play_button_label.bind(BUTTON_1, lambda *args: self._on_play(frame, grid_canvas))
    
    def _on_play(self, start_frame, grid_canvas):
        """
        Called when the "play" button is clicked.

        Arguments:
            start_frame (:class:`~tk.Frame`): :class:`~tk.Frame` for the
                Tkinter start screen.
            grid_canvas (:class:`~GridCanvas`): Grid canvas object.
        """

        self._tic_tac_toe.reset()
        start_frame.place_forget()
        grid_canvas.redraw()
    
    def _on_grid_canvas_click(self, event, grid_canvas):
        """
        Called when the grid is clicked.

        Arguments:
            event: Tkinter click event.
            grid_canvas (:class:`~GridCanvas`): Grid grid_canvas object.
        """

        grid_canvas.on_click(event.x, event.y)

        if self._tic_tac_toe.game_over:
            self.after(GAME_OVER_DELAY, lambda: self._show_game_over(grid_canvas))
