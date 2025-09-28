import tkinter as tk

TILE_SIZE = 100


class GridCanvas(tk.Canvas):
    """
    Tkinter canvas specifically for the grid.

    Arguments:
        tic_tac_toe (:class:`~TicTacToe`): Tic tac toe object for business
            logic.
        parent: Parent widget to pass to the :class:`~tk.Canvas` class.
    """

    def __init__(self, tic_tac_toe, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self._tic_tac_toe = tic_tac_toe

    def redraw(self):
        """
        Redraws the grid.
        """
        
        # Clear the canvas and start with a fresh slate
        self.delete(tk.ALL)

        for i in range(len(self._tic_tac_toe.grid)):
            canvas_y = TILE_SIZE * i
            
            for j in range(self._grid_size):
                canvas_x = TILE_SIZE * j

                cell = self._tic_tac_toe.grid[i][j]
                if cell:
                    self.create_text(canvas_x, canvas_y, text=cell)

    def on_click(self, canvas_x, canvas_y):
        """
        Handles canvas click events.

        Arguments:
            canvas_x (int): Canvas X coordinate.
            canvas_y (int): Canvas Y coordinate.
        """

        x_grid, y_grid = canvas_x // TILE_SIZE, canvas_y // TILE_SIZE

        # Don't allow input outside the grid
        grid_size = len(self._tic_tac_toe.grid)
        if 0 <= x_grid < grid_size and 0 <= y_grid < grid_size:
            self.select(x_grid, y_grid)

    def place(self, letter, x, y):
        """
        Places a position on the grid and returns the result.

        Arguments:
            letter (str): The letter to place.
            x (int): Grid X coordinate.
            y (int): Grid Y coordinate.

        Returns:
            bool
        """

        valid = self._tic_tac_toe.place(letter, x, y)
        if valid:
            canvas_x, canvas_y = x * TILE_SIZE, y * TILE_SIZE
            self.create_text(canvas_x, canvas_y, text=letter)
        
        return valid
