from math import sqrt
import numpy as np

class MCTS:
    def __init__(self, game, NN, args):
        self.NN = NN
        self.game = game
        self.simulations = args['mcts_simulations']
        self.visited = set()
        self.c_puct = args['mcts_cpuct']        # exploration coefficient
        self.P = {}                             # policies for each node
        self.Q = {}                             # Q value for each node (Q = W/N) = mean values
        self.N = {}                             # number of times each node was visited


    def probabilities(self, board, temp=1):

        for _ in range(self.simulations):
            self.search(board)
        
        b = hash(board)

        print(self.Q[b])

        counts = np.asarray([self.N[b][a] if a in self.N[b] else 0 for a in range(self.game.movecount)])

        if temp == 0:                               # if temp - > inf then one_hot with 1 as the max value
            a = np.argmax(counts)
            probabilities = counts * 0
            probabilities[a] = 1
            return probabilities
        
        counts = counts ** (1 / temp)
        probabilities = counts / sum(counts)
        return probabilities

    def search(self, board):

        b = hash(board)
        
        if self.game.ended(board):
            # print("sortie reward")
            return -self.game.rewards(board)
        
        if b not in self.visited:
            # EXPENSION
            self.visited.add(b)

            # initialise Q and N for each child
            self.Q[b] = {}
            self.N[b] = {}
            for a in board.valid_moves():
                self.Q[b][a] = 0
                self.N[b][a] = 0
            
            # get probabilites and value for this leaf node from NN
            self.P[b], v = self.NN.predict(board)

            return -v
        
        # SELECTION

        u = np.full((self.game.movecount), -np.inf, dtype=float)
        for a in range(self.game.movecount):
            if a in board.valid_moves():
                u[a] =  self.Q[b][a] + self.P[b][a] * self.c_puct * sqrt(sum(self.N[b]))/(1 + self.N[b][a])
        a = np.argmax(u)


        v = self.search(board.play(a))

        # BACKPROPAGATION
        self.Q[b][a] = (self.N[b][a] * self.Q[b][a] + v) / (self.N[b][a] + 1)
        self.N[b][a] += 1

        # print("sortie EOF")
        return -v

    def reset(self):
        self.visited = set()
        self.P = {}
        self.Q = {}
        self.N = {}