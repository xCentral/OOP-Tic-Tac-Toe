from src.board import Board
from src.users import User
from src.exceptions import SpotAlreadyTakenError


class Game:
    def __init__(self, user_1=User, user_2=User, board=Board()):
        self.users = [user_1, user_2]
        self.board = board

    @staticmethod
    def check_line(i, user):
        return all(map(lambda piece: piece == user, i))

    def check_for_winners(self, piece):
        #check user pieces in rows, columns, and diagonals
        #users_pieces = [user.piece for user in self.users if user.piece == piece]
        for user in piece:
            for row in self.board.game_state:
                if self.check_line(row, user):
                    # self._winner = user
                    return True

            for col in zip(*self.board.game_state):
                if self.check_line(col, user):
                    # self._winner = user
                    return True

            diagonal_wins = [[self.board[0], self.board[4], self.board[8]],
                             [self.board[2], self.board[4], self.board[6]]]
            for diagonal in diagonal_wins:
                if self.check_line(diagonal, user):
                    # self._winner = user
                    return True
        return False
