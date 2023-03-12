#from users import User


class Turn:
    def __init__(self, user, square, store):
        self.user = user
        self.id = len(store['turn']) + 1
        store['turn'][self.id] = self
        self.square = square
        self.store = store
        #self.last_placed = None

   # def check_sq(self, index):
    #    if [index] != self.board.BLANK:
     #      raise SpotAlreadyTakenError('Spot {} already has a piece'.format(index))

