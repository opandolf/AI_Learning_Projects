class Node:
    def __init__(self, state, size, cost, parent, move):
        self.state = state
        self.size = size
        self.cost = cost
        self.parent = parent
        self.move = move

    def __hash__(self):
        return(str(self.state))

    def __str__(self):
        return(str(self.state))
    
    def __lt__(self, other):
        return(self.cost < other.cost)

    def nextstate(self, move):
        idx = self.state.index(0)
        ret = self.state.copy()
        if (move == "UP"):
            ret[idx] = self.state[idx - self.size]
            ret[idx - self.size] = 0
        elif (move == "LEFT"):
            ret[idx] = self.state[idx - 1]
            ret[idx - 1] = 0
        elif (move == "DOWN"):
            ret[idx] = self.state[idx + self.size]
            ret[idx + self.size] = 0
        else:
            ret[idx] = self.state[idx + 1]
            ret[idx + 1] = 0
        return(ret)
    
    def validmove(self):
        idx = self.state.index(0)
        ret = []
        x = int(idx % self.size)
        y = int(idx / self.size)
        if (y - 1 >= 0 and self.move != "DOWN"):
            ret += ["UP"]
        if (y + 1 < self.size and self.move != "UP"):
            ret += ["DOWN"]
        if (x - 1 >= 0 and self.move != "RIGHT"):
            ret += ["LEFT"]
        if (x + 1 < self.size and self.move != "LEFT"):
            ret += ["RIGHT"]
        return (ret)