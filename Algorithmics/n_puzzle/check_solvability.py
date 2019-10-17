def find_nbr(state, size, nbr):
    for x in range(size):
        for y in range(size):
            if str(state[x][y]) == str(nbr):
                return x, y


def permutation_parity(puzzle, goal, size):
    tmp_puzzle = puzzle
    nbr = 0
    while (tmp_puzzle != goal):
        for x in range(size):
            for y in range(size):
                if (tmp_puzzle[x][y] != goal[x][y]):
                    coord_x, coord_y = find_nbr(tmp_puzzle, size, goal[x][y])
                    tmp_puzzle[coord_x][coord_y] = tmp_puzzle[x][y]
                    tmp_puzzle[x][y] = goal[x][y]
                    nbr += 1
    return nbr


def void_parity(puzzle, goal, size):
    x_a, y_a = find_nbr(puzzle, size, 0)
    x_b, y_b = find_nbr(goal, size, 0)
    nbr = abs(x_a - x_b) + abs(y_a - y_b)
    return nbr


def solvability(puzzle, goal, size):
    if permutation_parity(puzzle, goal, size) % 2  == void_parity(puzzle, goal, size) % 2:
        return True
    else:
        return False
