import numpy as np

class Board:

    def __init__(self, array, player, opponant):
        self.board = array
        self.player = player
        self.opponant = opponant
        
    def __hash__(self):
        return hash(self.state_formating_nn().tostring())
    
    def lost(self):
        """
        Search in board if opponent won the game
        return bolean            
        """
        # line and column check
        for x in range(3):
            line_slice = self.board[x, :]
            col_slice = self.board[:, x]
            if (np.all(line_slice == self.opponant.value) or np.all(col_slice == self.opponant.value)):
                return True
        # diagonal check
        if (np.all(np.diagonal(self.board) == self.opponant.value) or np.all(np.diagonal(np.rot90(self.board)) == self.opponant.value)):
            return True
        return False

    def full(self):
        if np.count_nonzero(self.board) == 9:
            return True
        return False

    def play(self, move):
        new = np.copy(self.board.reshape(9))
        new[move] = self.player.value
        new = new.reshape(3, 3)
        return Board(new, self.opponant, self.player)
    
    def valid_moves(self):
        l = []
        state = self.board.reshape(9)
        for i in range(len(state)):
            if state[i] == 0:
                l.append(i)
        return l
    
    def valid_moves_mask(self):
        l = []
        state = self.board.reshape(9)
        for i in range(len(state)):
            if state[i] == 0:
                l.append(1)
            else:
                l.append(0)
        return l

    def state_formating_nn(self):
        ret = np.copy(self.board)
        ret *= self.player.value
        return ret

    def symetries(self, p):
        ret = []
        copy_b = self.state_formating_nn()
        copy_p = np.asarray(p).reshape(3,3)
        for _ in range(4):
            ret += [[copy_b, copy_p.reshape(9), self.player.value]]
            copy_b = np.copy(np.rot90(copy_b))
            copy_p = np.copy(np.rot90(copy_p))
        return ret

    def print(self):
        print()
        print(" ______")
        for x in self.board:
            print("|", end='')
            for y in x:
                if y == -1:
                    print("X", end='')
                elif y == 0:
                    print(" ", end='')
                else:
                    print("O", end='')
                print("|", end='')
            print()
            print(" ______")
            print()