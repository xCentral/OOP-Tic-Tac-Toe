from src.board import Board
from src.users import User
from src.turns import Turn
from src.tictactoe import TicTacToe
from src.exceptions import *

#board = Board()
#board.game_state[0][0] = 'X'
#print(board.show_game_board())
#print(board.get_game_state())

t = TicTacToe
user_1 = User('random', 'X')
user_2 = User('random_2', 'O')
board = Board()

t = TicTacToe(user_1, user_2, board)
t.user_turn(0)
print(t.board.show_game_board())


#t.winner = 'luke'
#foo = t.winner
#print(foo)
#t.user_turn(5)

