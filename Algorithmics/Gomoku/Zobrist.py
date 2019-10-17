import numpy as np

class Zobrist:
    def __init__(self, size):
        self.white = np.random.randint(9223372036854775807, size=(size, size), dtype='int64')
        self.black = np.random.randint(9223372036854775807, size=(size, size), dtype='int64')
        self.board = np.random.randint(9223372036854775807, size=None, dtype='int64')

    
    def next_board(self, boardhashing, position, player):
        if player == 1:
            return boardhashing ^ self.white[position]
        else:
            return boardhashing ^ self.black[position]