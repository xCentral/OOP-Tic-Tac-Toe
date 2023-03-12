import random
from src.users import User
from src.board import Board
from src.turns import Turn
from src.exceptions import GameOverError
from src.checker import check_for_valid_move, update_user
from src.game import Game
from src.index import store

build = store


def tic_tac_toe(user_1, user_2):
    board = Board()
    game = Game(user_1, user_2, board)
    game_winner = None
    current_turn = random.choice(game.users)

    while game_winner is None:
        print(game.board.show_game_board())
        print('It is {}\'s turn'.format(current_turn.name))

        # print([user.piece for user in game.users if current_turn.piece != 'X'])
        index = int(input('Where would you like to place your piece? '))
        if check_for_valid_move(game, index - 1):
            Turn(game, index - 1, build)
            game.board[index - 1] = current_turn.piece
            check_for_winner = game.check_for_winners(current_turn.piece)
            if check_for_winner is False:
                current_turn = update_user(current_turn, game.users)
            else:
                game_winner = current_turn.name
                print(game.board.show_game_board())
                print('Game is over, {} is the winner'.format(game_winner))
                return game_winner
    if game_winner is None:
        print('Game is over, no winner')
        game_winner = 'no winner'


# Turn(current_turn, 2, build)
# game.board[3 - 1] = current_turn.piece

# print(len(build['users']))
# print(build['turn'].values())
# print([v for v in build['turn'].values() if v.user.id == current_turn.id])
# print(build['turn'][1].user.id)
# print([turn.__dict__ for turn in build['turn'].values()])


# winner = None

# tic_tac_toe(User('luke', 'X', build), User('joe', 'O', build))

tic_tac_toe(User('luke', 'X', build), User('joe', 'O', build))
