# from enum import Enum


class User:
    def __init__(self, name: str, piece: str, store: dict):
        self.name = name
        self.piece = piece
        user_id = len(store['users']) + 1
        store['users'][user_id] = self
        self.id = user_id

