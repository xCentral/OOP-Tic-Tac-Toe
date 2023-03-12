BLANK = ' '


class Board:

    def __init__(self):
        self.game_state = [[BLANK] * 3, [BLANK] * 3, [BLANK] * 3]

    def __getitem__(self, index):
        return self.game_state[index // 3][index % 3]

    def __setitem__(self, index, value):
        self.game_state[index // 3][index % 3] = value

    def get_game_state(self):
        return self.game_state

    def update_game_state(self, value):
        self.game_state = value

    def show_game_board(self):
        return '\n'.join([' | '.join(row) for row in self.game_state])

# board = Board()
# board.game_state[0][0] = 'X'
# board.game_board[0][1] = 'O'
# print(board.show_game_board())
