import numpy as np


def init_game_board():
    return np.zeros((3, 3))


class TicTacToe:
    def __init__(self):
        self.game_board = init_game_board()
        self.x_turn = True
        self.winner = None

    def change_player(self):
        self.x_turn = not self.x_turn

    def get_winner(self):
        return self.winner

    def get_x_turn(self):
        return self.x_turn

    def get_board(self):
        return self.game_board

    def move(self, move, player):
        x, y = move
        if (player == 1 and self.x_turn) or (player == 2 and not self.x_turn):
            if self.game_board[x, y] == 0:
                self.game_board[x, y] = player
                self.update_winner()
            else:
                raise Exception("Cell not available")
        else:
            raise Exception(f"Error: not player {player}'s turn")

    def check_winner(self):
        for i in range(3):
            if np.array_equal(self.game_board[:, i], np.ones(3)) or np.array_equal(self.game_board[i, :], np.ones(3)):
                return 1
            elif np.array_equal(self.game_board[:, i], 2*np.ones(3)) or np.array_equal(self.game_board[i, :], 2*np.ones(3)):
                return 2
        if np.array_equal(self.game_board.diagonal(), np.ones(3)) or np.array_equal(np.flipud(self.game_board).diagonal(), np.ones(3)):
            return 1
        elif np.array_equal(self.game_board.diagonal(), 2*np.ones(3)) or np.array_equal(np.flipud(self.game_board).diagonal(), 2*np.ones(3)):
            return 2
        return 0

    def is_draw(self):
        return 0 not in self.game_board

    def update_winner(self):
        if self.check_winner() == 1:
            self.winner = 1
        if self.check_winner() == 2:
            self.winner = 2

    def print_board(self):
        print(self.game_board)


def run_test_game():
    game = TicTacToe()
    player = 1

    while game.get_winner() is None and not game.is_draw():
        print(f"Player {player}'s turn")
        game.print_board()
        print(f"Choose cell to play")
        x = int(input("Line: "))
        y = int(input("Col: "))
        game.move((x, y), player)
        if player == 1:
            player = 2
        else:
            player = 1
        game.change_player()
    game.print_board()
    if game.is_draw():
        print("Game is draw")
    else:
        print(f"Player {game.get_winner()} wins!")


if __name__ == '__main__':
    run_test_game()
