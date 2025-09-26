import re

from tictactoe.player import Player


class ManualPlayer(Player):

    def get_move(self, grid: list[list[str]]) -> tuple[int]:
        while True:
            i = input(self.name + ", enter your move in the form x, y: ")
            parts = re.split(r" *, *| +", i)
            if len(parts) == 2:
                try:
                    return int(parts[0]), int(parts[1])
                except:
                    pass
            print("Invalid move")
