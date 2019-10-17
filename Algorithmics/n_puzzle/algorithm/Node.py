class Node:
    def __init__(self,state):
        self.state = state
        self.parent = None
        self.H = 0
        self.G = 0
    def __eq__(self, other):
        return self.state == other.state
    def __lt__(self, other):
        return self.H + self.G < other.H + other.G
