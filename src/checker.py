from src.exceptions import SpotAlreadyTakenError
from src.index import store


def check_for_valid_move(self, move):
    if int(move) not in range(0, 10):  # range between 0 and 9
        self.board.show_game_board()
        print("Please enter a number between 1 and 9, no letters")
        return False
    elif self.board[int(move)] != ' ':  # if the board is not blank
        self.board.show_game_board()
        print(("Spot {} already has a piece".format(move)))
        return False
    else:
        return True


# update user function to change the current user
def update_user(current_user, users_list):
    for user in users_list:
        if user != current_user:
            return user


# check if all moves have been made
def check_if_all_moves_made(self):
    if len(self.board.game_state) == 9:
        return True
    else:
        return False
