import time
import numpy as np

class Minimax:
    def __init__(self, game, maxdepth):
        self.game = game
        self.maxdepth = maxdepth

    def minimax(self, node, alpha, beta, depth):

        # if node.key in game.tt.table:
        #     node.value = game.tt.table[node.key]
        

        if depth == 0 or self.game.end(node):
            return node.value
        
        if node.player == 1:
            g = -np.inf
            children = self.game.children(node)
            for child in children:
                g = max(g, self.minimax(child, alpha, beta, depth - 1))
                alpha = max(alpha, g)
                if beta <= alpha:
                    break
            return g
        else:
            g = np.inf
            children = self.game.children(node)
            for child in children:
                g = min(g, self.minimax(child, alpha, beta, depth - 1))
                beta = min(beta, g)
                if beta <= alpha:
                    break
            return g

    def iterative_deepening(self, root):
        
        start = time.time()
        step = start

        children = self.game.children(root)
        
        if len(children) == 1:
            return children[0]

        # for i in range(len(children)):
        #     print("children " + str(i) + ": " + str(children[i].value))
        #     self.game.print_node(children[i])
        #     print()

        evals = [[]] * len(children)

        for d in range(1, self.maxdepth + 1):

            if (step - start) * (self.game.children_size + 1) > self.game.timelimit:
                # print("depth: ",d)
                # print("timeout: ", step - start)
                break

            for i in range(len(children)):
                if d == 1 or abs(evals[i]) != np.inf:
                    evals[i] = self.minimax(children[i], -np.inf, np.inf, d)
                # else:
                    # print("winner")
            step = time.time()

        if root.player == 1:
            return children[np.argmax(evals)]
        else:
            return children[np.argmin(evals)]

    def suggestions(self, root):

        start = time.time()
        step = start

        children = self.game.children(root)

        if len(children) == 1:
            return children[0]

        evals = [[]] * len(children)

        for d in range(1, self.maxdepth + 1):

            if (step - start) * (self.game.children_size + 1) > self.game.timelimit:
                print("depth: ",d)
                # print("timeout: ", step - start)
                break

            for i in range(len(children)):
                if d == 1 or abs(evals[i]) != np.inf:
                    evals[i] = self.minimax(children[i], -np.inf, np.inf, d)
                # else:
                    # print("winner")
            step = time.time()

        suggestions = []
        for i in range(len(evals)):
            suggestions += [[children[i], evals[i]]]

        if root.player == 1:
            suggestions.sort(key=lambda x: x[1], reverse=True)
        else:
            suggestions.sort(key=lambda x: x[1], reverse=False)

        ret = []
        for x in suggestions:
            ret += [x[0]]
        return ret