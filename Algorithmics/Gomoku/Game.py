import time
import numpy as np
from Zobrist import Zobrist
from Node import Node
from preprocess import preprocess_values


class Game:
    def __init__(self, children_size, timelimit, regle="42", size=19):
        # self.value_array = [0, 35, 800, 15000, 80000, np.inf]
        # self.counter_value_array = [15, 400, 1800, 100000]

        # initialisation des values des 9tuples
        self.capture_value = [0, 35, 800, 15000, 80000, np.inf]
        self.size = size
        self.zobrist = Zobrist(self.size)
        self.tt = {}
        self.children_size = children_size
        self.timelimit = timelimit
        self.dict_values = preprocess_values(regle)
        self.regle = regle

    def init(self):
        return Node(np.zeros((self.size, self.size), dtype=int), self.zobrist.board, -1, 0, 0, 0, None, 1)

    def end(self, node):
        if node.value == np.inf * node.player:
            return True
        elif node.value == -np.inf * node.player:
            children = self.children(node)
            if abs(children[0].value) != np.inf:
                return False
            if node.player == 1:
                if node.black_capture >= 5:
                    return True
                if node.white_capture == 4 and self.check_capture(node):
                    return False
                else:
                    return True
            else:
                if node.white_capture >= 5:
                    return True
                if node.black_capture == 4 and self.check_capture(node):
                    return False
                else:
                    return True
                
        if np.count_nonzero(node.board) == self.size ** 2:
            return True
        return False

    def capture_remove_score(self, board, player, pos):
        score = 0
        score += self.horizontal_eval(board, player, pos, True, self.xy_limits(pos))[0]
        score += self.vertical_eval(board, player, pos, True, self.xy_limits(pos))[0]
        score += self.leftdiagonal_eval(board, player, pos, True, self.xy_limits(pos))[0]
        score += self.rightdiagonal_eval(board, player, pos, True, self.xy_limits(pos))[0]
        return score

    def capture_eval(self, board, player, capture_mask, position, key):
        
        total_score = 0

        if capture_mask[0] == 1:

            pos = (position[0], position[1] - 1)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

            pos = (position[0], position[1] - 2)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

        if capture_mask[1] == 1:
            
            pos = (position[0], position[1] + 1)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

            pos = (position[0], position[1] + 2)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

        if capture_mask[2] == 1:

            pos = (position[0] - 1, position[1])
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

            pos = (position[0] - 2, position[1])
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0            

        if capture_mask[3] == 1:
            
            pos = (position[0] + 1, position[1])
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

            pos = (position[0] + 2, position[1])
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

        if capture_mask[4] == 1:
            
            pos = (position[0] - 1, position[1] - 1)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

            pos = (position[0] - 2, position[1] - 2)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

        if capture_mask[5] == 1:
            
            pos = (position[0] + 1, position[1] + 1)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

            pos = (position[0] + 2, position[1] + 2)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

        if capture_mask[6] == 1:
            
            pos = (position[0] - 1, position[1] + 1)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

            pos = (position[0] - 2, position[1] + 2)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

        if capture_mask[7] == 1:
            
            pos = (position[0] + 1, position[1] - 1)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

            pos = (position[0] + 2, position[1] - 2)
            score = self.capture_remove_score(board, player, pos)
            key = self.zobrist.next_board(key, pos, board[pos])
            total_score += score
            board[pos] = 0

        return total_score, key


    def sub_values(self, a, b):
        if (a == np.inf and b == np.inf) or (a == -np.inf and b == -np.inf):
            return 0
        else:
            return a - b
            
    def add_values(self, a, b):
        if a == np.inf and b == -np.inf:
            return -np.inf
        elif a == -np.inf and b == np.inf:
            return np.inf
        else:
            return a + b

    def qtuple_eval(self, qtuple, player, pos, capture_bool):
        old_value = self.dict_values[(str(qtuple), pos)]["value"]
        
        # print(qtuple)
        # print(self.dict_values[(str(qtuple), pos)])

        if capture_bool == False:
            qtuple[pos] = player
        else:
            qtuple[pos] = 0

        # print("qtuple: ", qtuple, "pos: ", pos)
        # print(self.dict_values[(str(qtuple), pos)])

        new_value = self.dict_values[(str(qtuple), pos)]["value"]

        if capture_bool == False:
            free_three = self.dict_values[(str(qtuple), pos)]["free_three"]
            capture = self.dict_values[(str(qtuple), pos)]["capture"]
            if capture == (1,0):
                time.sleep(0)
        else:
            free_three = 0
            capture = (0,0)

        score = self.sub_values(new_value, old_value)

        # print(score, free_three, capture)

        return score, free_three, capture

    def horizontal_eval(self, board, player, position, capture_bool, xylimits):
        
        y,x = position

        if position == (4,5):
            time.sleep(0)

        xmin, xmax = xylimits[0:2]

        qtuple_size = xmax - xmin + 1
        qtuple = [0] * qtuple_size
        pos = x - xmin
        for i in range(qtuple_size):
            qtuple[i] = board[y, xmin + i]
        
        return self.qtuple_eval(qtuple, player, pos, capture_bool)

    
    def vertical_eval(self, board, player, position, capture_bool, xylimits):

        y,x = position

        ymin, ymax = xylimits[2:4]

        qtuple_size = ymax - ymin + 1
        qtuple = [0] * qtuple_size
        pos = y - ymin
        for i in range(qtuple_size):
            qtuple[i] = board[ymin + i, x]

        return self.qtuple_eval(qtuple, player, pos, capture_bool)

    def leftdiagonal_eval(self, board, player, position, capture_bool, xylimits):

        y,x = position

        xmin,xmax,ymin,ymax = xylimits

        qtuple_size = min(xmax - x, ymax - y) + min(x - xmin, y - ymin) + 1
        qtuple = [0] * qtuple_size
        pos = min(x - xmin, y - ymin)
        for i in range(qtuple_size):
            qtuple[i] = board[y - min(y - ymin, x - xmin) + i, x - min(y - ymin, x - xmin) + i]

        return self.qtuple_eval(qtuple, player, pos, capture_bool)

    def rightdiagonal_eval(self, board, player, position, capture_bool, xylimits):

        y,x = position

        xmin,xmax,ymin,ymax = xylimits

        qtuple_size = min(xmax - x, y - ymin) + min(x - xmin, ymax - y) + 1
        qtuple = [0] * qtuple_size
        pos = min(xmax - x, y - ymin)
        for i in range(qtuple_size):
            qtuple[i] = board[y - min(y - ymin, xmax - x) + i, x + min(y - ymin, xmax - x) - i]

        return self.qtuple_eval(qtuple, player, pos, capture_bool)


    def xy_limits(self, position):
        y,x = position


        xmin = max(0, x - 4)
        xmax = min(self.size - 1, x + 4)
        ymin = max(0, y - 4)
        ymax = min(self.size - 1, y + 4)

        return xmin, xmax, ymin, ymax

    def point_eval(self, node, position):
        key = self.zobrist.next_board(node.key, position, node.player)
        if key in self.tt:
            value, valid = self.tt[key]
            if valid != 1:
                return None, None
            return (self.sub_values(value, node.value)) * node.player, [0, 0, 0, 0, 0, 0, 0, 0]

        total_score = 0

        # if position == (5,7):

        # xmin = max(0, x - 4)
        # xmax = min(self.size - 1, x + 4)
        # ymin = max(0, y - 4)
        # ymax = min(self.size - 1, y + 4)

        xylimits = self.xy_limits(position)

        freethree_count = 0
        capture_mask = [0] * 8

        ## horizontal
        score, freethree, capture = self.horizontal_eval(node.board, node.player, position, False, xylimits)
        
        total_score += score
        freethree_count += freethree
        capture_mask[0:2] = capture

        # if position == (5,7):
        #     print("h:", score, freethree, capture, capture_mask)

        ## vertical
        score, freethree, capture = self.vertical_eval(node.board, node.player, position, False, xylimits)
        
        total_score += score
        freethree_count += freethree
        capture_mask[2:4] = capture

        # if position == (5,7):
        #     print("v:", score, freethree, capture, capture_mask)
    

        ## left diagonal
        score, freethree, capture = self.leftdiagonal_eval(node.board, node.player, position, False, xylimits)
        
        total_score += score
        freethree_count += freethree
        capture_mask[4:6] = capture

        # if position == (5,7):
        #     print("d1:", score, freethree, capture, capture_mask)

        ## right diagonal
        score, freethree, capture = self.rightdiagonal_eval(node.board, node.player, position, False, xylimits)
        
        total_score += score
        freethree_count += freethree
        capture_mask[6:8] = capture

        # if position == (5,7):
        #     print("d2:", score, freethree, capture, capture_mask)

        if freethree_count >= 2:
            self.tt[key] = [0,0]
            return None, capture_mask

        # print("sum mask:", sum(capture_mask))
        # print()

        if sum(capture_mask) > 0:
            board_copy = np.copy(node.board)
            board_copy[position] = node.player
            capture_score, key = self.capture_eval(board_copy, node.player, capture_mask, position, key)
            total_score += capture_score
            if node.player == 1:
                if node.white_capture + sum(capture_mask) > 5:
                    capture_value = self.capture_value[-1]
                else:
                    capture_value = self.capture_value[node.white_capture + sum(capture_mask)] - self.capture_value[node.white_capture]
            else:
                if node.black_capture + sum(capture_mask) > 5:
                    capture_value = self.capture_value[-1]
                else:
                    capture_value = -self.capture_value[node.black_capture + sum(capture_mask)] - (-self.capture_value[node.black_capture])
            total_score += capture_value
        else:
            self.tt[key] = [self.add_values(node.value, total_score), 1]
    
        return total_score * node.player, capture_mask

    def proximity(self, node, position):
        y = position[0]
        x = position[1]

        if x - 1 >= 0:
            if node.board[y, x - 1] != 0:
                return True
        if x + 1 < self.size:
            if node.board[y, x + 1] != 0:
                return True
        if y - 1 >= 0:
            if x - 1 >= 0:
                if node.board[y - 1, x - 1] != 0:
                    return True
            if node.board[y - 1, x] != 0:
                return True
            if x + 1 < self.size:
                if node.board[y - 1, x + 1] != 0:
                    return True
        if y + 1 < self.size:
            if x - 1 >= 0:
                if node.board[y + 1, x - 1] != 0:
                    return True
            if node.board[y + 1, x] != 0:
                return True
            if x + 1 < self.size:
                if node.board[y + 1, x + 1] != 0:
                    return True
        return False

    def valid_moves(self, node):
        if node.key == self.zobrist.board:
            return [(int(self.size / 2), int(self.size / 2))]

        ret = []
        for y in range(self.size):
            for x in range(self.size):
                if self.regle == "pro" and node.turn_count == 3:
                    if int(self.size/2) - 2 <= y <= int(self.size/2) + 2 and int(self.size/2) - 2 <= x <= int(self.size/2) + 2:
                        continue
                if self.regle == "longpro" and node.turn_count == 3:
                    if int(self.size/2) - 3 <= y <= int(self.size/2) + 3 and int(self.size/2) - 3 <= x <= int(self.size/2) + 3:
                        continue
                if node.board[y, x] == 0 and self.proximity(node, (y, x)):
                    ret += [(y, x)]
        if self.regle == "pro" and node.turn_count == 3 and ret == []:
            ret += [(int(self.size/2), int(self.size/2) - 3)]
            ret += [(int(self.size/2), int(self.size/2) + 3)]
            ret += [(int(self.size/2) - 3, int(self.size/2))]
            ret += [(int(self.size/2) + 3, int(self.size/2))]
        if self.regle == "longpro" and node.turn_count == 3 and ret == []:
            ret += [(int(self.size/2), int(self.size/2) - 4)]
            ret += [(int(self.size/2), int(self.size/2) + 4)]
            ret += [(int(self.size/2) - 4, int(self.size/2))]
            ret += [(int(self.size/2) + 4, int(self.size/2))]  
        return ret

    def new_node_capture(self, board, position, capture_mask, key):
        

        if capture_mask[0] == 1:
            pos = (position[0], position[1] - 1)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0
            pos = (position[0], position[1] - 2)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0

        if capture_mask[1] == 1:
            pos = (position[0], position[1] + 1)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0
            pos = (position[0], position[1] + 2)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0

        if capture_mask[2] == 1:
            pos = (position[0] - 1, position[1])
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0
            pos = (position[0] - 2, position[1])
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0

        if capture_mask[3] == 1:            
            pos = (position[0] + 1, position[1])
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0
            pos = (position[0] + 2, position[1])
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0

        if capture_mask[4] == 1:            
            pos = (position[0] - 1, position[1] - 1)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0
            pos = (position[0] - 2, position[1] - 2)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0

        if capture_mask[5] == 1:            
            pos = (position[0] + 1, position[1] + 1)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0
            pos = (position[0] + 2, position[1] + 2)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0

        if capture_mask[6] == 1:            
            pos = (position[0] - 1, position[1] + 1)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0
            pos = (position[0] - 2, position[1] + 2)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0

        if capture_mask[7] == 1:            
            pos = (position[0] + 1, position[1] - 1)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0
            pos = (position[0] + 2, position[1] - 2)
            key = self.zobrist.next_board(key, pos, board[pos])
            board[pos] = 0

        return board, key   

    def new_node(self, node, position, value, capture_mask):
        board = np.copy(node.board)
        board[position] = node.player
        key = self.zobrist.next_board(node.key, position, node.player)
        white_capture = node.white_capture
        black_capture = node.black_capture
        if sum(capture_mask) > 0:
            if node.player == 1:
                white_capture += sum(capture_mask)
            else:
                black_capture += sum(capture_mask)
            board, key = self.new_node_capture(board, position, capture_mask, key)
        return Node(board, key, -node.player, self.add_values(node.value, value * node.player), white_capture, black_capture, position, node.turn_count + 1)

    def children(self, node):

        valid_moves = self.valid_moves(node)

        best = []
        for position in valid_moves:
            value, capture_mask = self.point_eval(node, position)
            if value != None:
                if not(value * node.player == -node.value and abs(node.value) == np.inf and sum(capture_mask) == 0):
                    best += [[position, value, capture_mask]]
        
        # print(node.board)
        # print(node.key)
        # for a in best:
        #     print(a)
        # print()
        

        best.sort(key=lambda x: x[1], reverse=True)
        best = best[:4]

        # for a in best:
        #     print(a)
        # print()


        children = []
        for position, value, capture_mask in best:
            children += [self.new_node(node, position, value, capture_mask)]

        # if len(children) == 0:
        #     self.print_node(node)
        return children

    def check_capture(self, node):
        valid_moves = self.valid_moves(node)

        for position in valid_moves:
            value, capture_mask = self.point_eval(node, position)
            if value != None and sum(capture_mask) > 0:
                return True
        
        return False
            

    def print_node(self, node):
        print("   ", end="")
        for i in range(len(node.board)):
            print("%2d" % i, end="")
        print()
        for y in range(len(node.board)):
            print("%2d " % y, end="")
            for point in node.board[y]:
                if point == 1:
                    print(" O", end="")
                elif point == -1:
                    print(" X", end="")
                else:
                    print("  ", end="")
            print("\n", end="")

    def player_move(self, node, position):
        y,x = position
        if not (0 <= y < self.size and 0 <= x < self.size and node.board[position] == 0):
            return None
        if self.regle == "pro" and node.turn_count == 3:
            if int(self.size/2) - 2 <= y <= int(self.size/2) + 2 and int(self.size/2) - 2 <= x <= int(self.size/2) + 2:
                return None
        if self.regle == "longpro" and node.turn_count == 3:
            if int(self.size/2) - 3 <= y <= int(self.size/2) + 3 and int(self.size/2) - 3 <= x <= int(self.size/2) + 3:
                return None        
        value, capture_mask = self.point_eval(node, position)
        if value != None:
            return self.new_node(node, position, value, capture_mask)
        else:
            return None