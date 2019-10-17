from Game import Game
import time
import numpy as np

game = Game(4,0.5)

root = game.init()

# for y in range(game.size):
#     for x in range(game.size):
#         node = game.init()
#         node.player = -1

#         position = (y,x)
        
#         if x - 3 >= 0:
#             node.board[y, x - 1] = 1
#             node.board[y, x - 2] = 1
#             node.board[y, x - 3] = -1

#         if x + 3 < game.size:
#             node.board[y, x + 1] = 1
#             node.board[y, x + 2] = 1
#             node.board[y, x + 3] = -1
    
#         if y - 3 >= 0:
#             node.board[y - 1, x] = 1
#             node.board[y - 2, x] = 1
#             node.board[y - 3, x] = -1

#         if y + 3 < game.size:
#             node.board[y + 1, x] = 1
#             node.board[y + 2, x] = 1
#             node.board[y + 3, x] = -1

#         if y - 3 >= 0 and x - 3 >= 0:
#             node.board[y - 1, x - 1] = 1
#             node.board[y - 2, x - 2] = 1
#             node.board[y - 3, x - 3] = -1

#         if y + 3 < game.size and x + 3 < game.size:
#             node.board[y + 1, x + 1] = 1
#             node.board[y + 2, x + 2] = 1
#             node.board[y + 3, x + 3] = -1

#         if y - 3 >= 0 and x + 3 < game.size:
#             node.board[y - 1, x + 1] = 1
#             node.board[y - 2, x + 2] = 1
#             node.board[y - 3, x + 3] = -1

#         if y + 3 < game.size and x - 3 >= 0:
#             node.board[y + 1, x - 1] = 1
#             node.board[y + 2, x - 2] = 1
#             node.board[y + 3, x - 3] = -1
        
#         game.print_node(node)
#         value, capture_mask = game.point_eval(node, position)
#         print(value, capture_mask)
#         if value != None:
#             game.print_node(game.new_node(node, position, value, capture_mask))

#         time.sleep(0)
#         print("----------------------------------------------")

# node = game.init()
# y = 2
# x = 2
# position = (y,x)
# if x - 3 >= 0:
#     node.board[y, x - 1] = 1
#     node.board[y, x - 2] = 1
#     node.board[y, x - 3] = -1

# if x + 3 < game.size:
#     node.board[y, x + 1] = 1
#     node.board[y, x + 2] = 1
#     node.board[y, x + 3] = -1

# if y - 3 >= 0:
#     node.board[y - 1, x] = 1
#     node.board[y - 2, x] = 1
#     node.board[y - 3, x] = -1

# if y + 3 < game.size:
#     node.board[y + 1, x] = 1
#     node.board[y + 2, x] = 1
#     node.board[y + 3, x] = -1

# if y - 3 >= 0 and x - 3 >= 0:
#     node.board[y - 1, x - 1] = 1
#     node.board[y - 2, x - 2] = 1
#     node.board[y - 3, x - 3] = -1

# if y + 3 < game.size and x + 3 < game.size:
#     node.board[y + 1, x + 1] = 1
#     node.board[y + 2, x + 2] = 1
#     node.board[y + 3, x + 3] = -1

# if y - 3 >= 0 and x + 3 < game.size:
#     node.board[y - 1, x + 1] = 1
#     node.board[y - 2, x + 2] = 1
#     node.board[y - 3, x + 3] = -1

# if y + 3 < game.size and x - 3 >= 0:
#     node.board[y + 1, x - 1] = 1
#     node.board[y + 2, x - 2] = 1
#     node.board[y + 3, x - 3] = -1

# game.print_node(node)
# value, capture_mask = game.point_eval(node, position)
# print(value, capture_mask)
# if value != None:
#     game.print_node(game.new_node(node, position, value, capture_mask))

node = root
# node.board[(2,2)] = -1
# node.board[(2,6)] = -1
# node.board[(3,4)] = 1
# node.board[(3,5)] = 1
# node.board[(3,6)] = 1
# node.board[(5,3)] = 1
# node.board[(5,4)] = -1
# node.board[(5,5)] = -1
# node.board[(5,6)] = -1
# node.board[(5,7)] = -1

node.board = np.asarray(
[[0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,-1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,1,1,0,1,0,0,0],
 [0,0,0,1,-1,-1,-1,0,0],
 [0,0,0,-1,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0]])
position = (5,7)
node.player = -1
node.key = 3238605086810496957

# value, capture_mask = game.point_eval(node, position)
# print(value, capture_mask)

game.children(node)