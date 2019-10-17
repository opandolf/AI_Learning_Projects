from queue import PriorityQueue
from Node import Node
import numpy as np

class Astar:
    def __init__(self, nnet, puzzle):
        self.nnet = nnet
        self.puzzle = puzzle

    def heuristic_single(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def heuristic(self, goal, state):
        ret = 0
        a = np.asarray(goal).reshape(3,3)
        b = np.asarray(state).reshape(3,3)
        for el in range(1, self.puzzle.size**2):
            x1,y1 = np.where(a == el)
            x2,y2 = np.where(b == el)
            ret += self.heuristic_single((x1[0],y1[0]),(x2[0],y2[0]))
        return ret

    def solve(self):
        
        current_node = Node(self.puzzle.start, self.puzzle.size, 0, None, None)
        frontier = PriorityQueue()
        frontier.put(current_node, 0)
        cost_so_far = {str(current_node): 0}

        while not frontier.empty():

            current = frontier.get()

            if current.state == self.puzzle.goal:
                print("finish")
                break
            
            for move in current.validmove():
                cost = current.cost + 1
                new_node = Node(current.nextstate(move), current.size, cost, current, move)
                if (str(new_node) not in cost_so_far or cost < cost_so_far[str(new_node)]) and cost <= 31:
                    cost_so_far[str(new_node)] = cost
                    priority = cost + self.nnet.predict(new_node.state) 
                    frontier.put(new_node, priority)
            


        ret_solution = []
        tmp = current
        while(tmp != None):
            ret_solution += [np.asarray(tmp.state).reshape(3,3)]
            tmp = tmp.parent
        return len(ret_solution), ret_solution[::-1]

        # return came_from, cost_so_far

        #self.heuristic(self.puzzle.goal, new_node.state)
        #