class Node:
    def __init__(self, board, key, player, value, white_capture, black_capture, position, turn_count):
        self.board = board
        self.key = key
        self.player = player
        self.value = value
        self.white_capture = white_capture
        self.black_capture = black_capture
        self.position = position
        self.turn_count = turn_count