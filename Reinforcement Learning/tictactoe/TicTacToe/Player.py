class Player:

    def __init__(self, nn, mcts, value):
        self.nn = nn
        self.mcts = mcts
        self.value = value
    
    def reset_mcts(self):
        self.mcts.reset()