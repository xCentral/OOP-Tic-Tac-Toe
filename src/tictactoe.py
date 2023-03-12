import random
from src.users import User
from src.board import Board
from src.turns import Turn
from src.exceptions import GameOverError
from src.checker import check_for_valid_move


class TicTacToe:

    def __init__(self, user_1=User, user_2=User, board=Board()):
        self.users = [user_1, user_2]
        self.board = board
        self._winner = None
       # self._game_history = {}
        self.first_to_go = random.choice(self.users)
        self._board_state = self.board.game_state
        self.current_user = self.first_to_go

    # update current user by switching to the next user not equal to the current user
    def update_current_user(self):
        current_user = self.current_user
        next_turn = [user for user in self.users if user != current_user][0]
        self.current_user = next_turn

    def user_turn(self, index):
        # check for winner
        if self._winner:
            raise GameOverError('Game is over, {} is the winner'.format(self._winner))
        if check_for_valid_move(self, index):
            # Move with Turn instance
            #user_turn = Turn(self.current_user, index)
            # create an id for player turn in game history
            #turn_id = len(self._game_history) + 1
            # add turn to game history
            #self._game_history[turn_id] = user_turn
            # place user piece on board
            self.board[index] = self.current_user.piece
            self.update_current_user()
            self.check_for_winners()

    #@property
    #def winner(self):
    #    return self._winner

    #@winner.setter
    #def winner(self, winner):
    #    self._winner = winner




