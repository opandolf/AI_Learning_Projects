import numpy as np
from TicTacToe.Board import Board

class GameRules:
    def __init__(self):
        self.player_coefficient = -1            #Sign of MCTS backpropagation : 1 player - > 1, 2 player - > -1
        self.player1_value = 1
        self.player2_value = -1
        self.movecount = 9
        self.shape = (3,3)

    def init_board(self):
        return Board(np.zeros(self.shape, dtype = int), self.player1_value, self.player2_value)
    
    def ended(self, board):
        if (not(board.lost()) and not(board.full())):
            return False
        return True
    
    def rewards(self, board):
        if (board.lost()):
            return -1
        return 0
    
    def evaluation_play(self, player, opponant):        
        board = self.init_board()
        board.player = player
        board.opponant = opponant
        while not(self.ended(board)):
            # p = board.player.mcts.probabilities(board, temp=1)
            p, v = board.player.nn.predict(board)
            a = np.argmax(p)
            board = board.play(a)
        if board.lost():
            reward = self.rewards(board)
            score = reward if board.player == player else -reward
            return score
        return 0
    
    def training_play(self, player, opponant):
        board = self.init_board()
        board.player = player
        board.opponant = opponant
        records = []
        while not(self.ended(board)):
            p = board.player.mcts.probabilities(board, temp=1)
            a = np.random.choice(np.arange(self.movecount), p=p)
            records += board.symetries(p)
            board = board.play(a)
        result = board.lost()
        for x in records:
            if result == 0:
                x[2] = 0
            else:
                x[2] = 1 if x[2] != board.player.value else -1
        return records
    
    def human_play(self, human, computer):
        board = self.init_board()
        board.player = human
        board.opponant = computer
        while not(self.ended(board)):
            board.print()
            if (board.player == human):
                a = int(input("move: "))
                while (a not in board.valid_moves()):
                    a = int(input("not a valid move, replay: "))
            else:
                p = board.player.mcts.probabilities(board, temp=1)
                a = np.argmax(p)
            board = board.play(a)
        board.print()
        if board.lost():
            if board.player == human:
                print("DEFAITE")
            else:
                print("VICTOIRE")
        else:
            print("MATCH NUL")