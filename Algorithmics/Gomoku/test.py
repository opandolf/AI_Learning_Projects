from Game import Game
from Minimax import Minimax
import time
import numpy as np

game1 = Game(4, 0.5)
minimax1 = Minimax(game1, 10)
game2 = Game(5, 0.5)
game2.zobrist = game1.zobrist
minimax2 = Minimax(game2, 2)

humain = 1

root = game1.init()

node = root
tour = 0
while not game1.end(node):
    start = time.time()

    if node.player != humain:
        node = minimax1.iterative_deepening(node)
    else:
        valid_mooves = game1.valid_moves(node)
        while True:
            y = int(input("Select y"))
            x = int(input("Select x"))
            if 0 <= y < game1.size and 0 <= x < game1.size:
                child = game1.player_move(node,(y,x))
                if child != None:
                    break
            print("Not a valid move")

        node = child
    end = time.time()

    game1.print_node(node)
    print(node.position)
    print("time: ", end - start)
    print("---------------------------------------------")
    # tour += 1
print("hourra")


## human vs human
# node = root
# tour = 0
# while not game1.end(node):
#     y = int(input("Select y"))
#     x = int(input("Select x"))
#     node = game1.player_move(node, (y,x))
#     game1.print_node(node)
#     print("---------------------------------------------")


# win = 0
# lose = 0
# draw = 0

# for i in range(1):
#     node = root
#     while not(game1.end(node)):
#         if node.player == 1:
#             node = minimax1.iterative_deepening(node)
#         else:
#             node = minimax2.iterative_deepening(node)
#     if node.value == np.inf:
#         win += 1
#     elif node.value == -np.inf:
#         lose += 1
#     else:
#         draw += 1
    
#     game1.print_node(node)

#     node = root
#     while not(game1.end(node)):
#         if node.player == 1:
#             node = minimax2.iterative_deepening(node)
#         else:
#             node = minimax1.iterative_deepening(node)
#     if node.value == -np.inf:
#         win += 1
#     elif node.value == np.inf:
#         lose += 1
#     else:
#         draw += 1
#     game1.print_node(node)

# print("wins: %d, lose: %d, draw: %d" % (win, lose, draw))