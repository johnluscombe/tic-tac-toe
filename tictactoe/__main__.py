from tictactoe import TicTacToe
from tictactoe import VALID_LETTERS
from tictactoe.player.ai import AIPlayer
from tictactoe.player.ai.easy import EasyAIPlayer
from tictactoe.player.ai.medium import MediumAIPlayer
from tictactoe.player.ai.hard import HardAIPlayer
from tictactoe.player.manual import ManualPlayer
from tictactoe.renderer.console import ConsoleRenderer


def main():
    tic_tac_toe = TicTacToe()

    player1_name = input("Player 1's name: ")
    player1_letter = input(player1_name + ", would you like to be X or O? ").lower()
    while player1_letter not in VALID_LETTERS:
        print("Invalid letter.")
        player1_letter = input("Player 1, would you like to be X or O? ").lower()
    
    player2_name = input("Player 2's name: ")
    player2_letter = VALID_LETTERS[int(not bool(VALID_LETTERS.index(player1_letter)))]

    player1 = ManualPlayer(1, player1_letter, player1_name)
    player2 = HardAIPlayer(2, player2_letter, player2_name)

    renderer = ConsoleRenderer(tic_tac_toe)
    renderer.render()

    while not tic_tac_toe.game_over:
        move = player1.get_move(tic_tac_toe.grid)
        while not tic_tac_toe.place(player1.letter, *move):
            if isinstance(player1, AIPlayer):
                print("An AI player picked an invalid move!", player2_name, "wins!")
                return
            print("Invalid move.")
            move = player1.get_move(tic_tac_toe.grid)
        renderer.render()

        if not tic_tac_toe.game_over:
            move = player2.get_move(tic_tac_toe.grid)
            while not tic_tac_toe.place(player2.letter, *move):
                if isinstance(player2, AIPlayer):
                    print("An AI player picked an invalid move!", player1_name, "wins!")
                    return
                print("Invalid move.")
                move = player2.get_move(tic_tac_toe.grid)
            renderer.render()
    
    if tic_tac_toe.winner is None:
        print("Stalemate!")
    elif player1_letter == tic_tac_toe.winner:
        print(player1_name, "wins!")
    else:
        print(player2_name, "wins!")


if __name__ == "__main__":
    main()
