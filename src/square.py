from src.exceptions import SpotAlreadyTakenError


class Square:
    def __init__(self, index, symbol):
        self._index = index
        self._symbol = symbol

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        if self._symbol is not '':
            raise SpotAlreadyTakenError('Spot {} already has a piece'.format(self._symbol))
        self._symbol = symbol
