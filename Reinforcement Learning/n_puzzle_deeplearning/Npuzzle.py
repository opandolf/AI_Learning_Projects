import math
from Node import Node
from random import choice

class Npuzzle:
    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.goal = self.init_goal()

    def init_goal(self):
        ret = [x for x in range(1, self.size**2)]
        ret += [0]
        return(ret)
    
    def solved(self, state):
        if (state == self.goal):
            return True
        return False
    
    def scramble(self, n):
        node = Node(self.goal, self.size,0, None, None)
        ret = [[self.goal, 0]]
        for i in range(n):
            move = choice(node.validmove())
            state = node.nextstate(move)
            node = Node(state, node.size,0, node, move)
            ret += [[state,i + 1]]
        return(ret)

    def print(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.start[y * self.size + x], end=" ")
            print()