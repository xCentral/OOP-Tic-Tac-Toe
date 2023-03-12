from src.board import Board
from src.users import User
from src.turns import Turn
# from src.tictactoe import TicTacToe
from src.game import Game
from src.index import build_store
from src.checker import check_for_valid_move

build = build_store()


def test_len_of_board():
    board = Board()

    assert len(board.game_state) == 3


def test_board_is_list():
    board = Board()
    assert isinstance(board.game_state, list)


def test_for_valid_move():
    board = Board()
    user_input = 5
    board[user_input - 1] = 'X'
    assert [i for j in board.game_state for i in j] == [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']


def test_build_for_users_len():
    board = Board()
    user_1 = User('luke', 'X', build)
    user_2 = User('joe', 'O', build)
    game = Game(user_1, user_2, board)
    assert len(build['users']) == 2


def test_build_for_turns_len():
    board = Board()
    user_1 = User('luke', 'X', build)
    user_2 = User('joe', 'O', build)
    game = Game(user_1, user_2, board)
    Turn(user_1, 2, build)
    Turn(user_2, 3, build)
    game.board[2 - 1] = user_1.piece
    game.board[3 - 1] = user_2.piece
    assert len(build['turn']) == 2


def test_check_valid_move():
    board = Board()
    user_1 = User('luke', 'X', build)
    user_2 = User('joe', 'O', build)
    game = Game(user_1, user_2, board)
    given_move = 5
    assert check_for_valid_move(game, given_move) == True
    # user_move = Turn(user_1, given_move, build)
