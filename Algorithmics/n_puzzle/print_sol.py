def to_array(goal, size):
    puzzle_array = goal.split(",")
    res = []
    i = 0
    y = -1
    while i < len(puzzle_array):
        if i % size == 0:
            res.append([])
            y += 1
        res[y].append(puzzle_array[i])
        i += 1
    return res


def print_sol(sol, size, goal, iter):
    nbr_len = len(str(size*size))
    goal = to_array(goal, size)
    layer = len(sol)
    for actual_layer in reversed(range(1, layer+1)):
        if actual_layer == layer:
            for puzzle in sol[0]:
                if iter:
                    input()
                index = 1
                puzzle_array = puzzle.split(",")
                for nbr in puzzle_array:
                    print(" " * (nbr_len - len(str(nbr))) + str(nbr), end="")
                    if index % size != 0:
                        print(" ", end="")
                    else:
                        print()
                    index += 1
                print()
            print()
        else:
            layer_size = layer-actual_layer
            if layer_size % 2 == 1:
                start_bottom = 1
            else:
                start_bottom = 0
            top_right_size = int((layer_size+1)/2)
            if start_bottom == 0:
                bottom_left_size = top_right_size
            else:
                bottom_left_size = top_right_size - 1

            if layer % 2 == 1:
                tmp = bottom_left_size
                bottom_left_size = top_right_size
                top_right_size = tmp

            for puzzle in sol[layer_size]:
                if iter:
                    input()
                i = 0
                index = 1
                x = 0
                y = 0
                puzzle_array = puzzle.split(",")
                while x < size * size:
                    if (x%size) > size - top_right_size - 1 or y < top_right_size or (x%size) < bottom_left_size or y > size - bottom_left_size - 1:
                        print(" " * (nbr_len - len(str(goal[y][x%size]))) + str(goal[y][x%size]), end="")
                    else:
                        if i >= len(puzzle_array):
                            print()
                        print(" " * (nbr_len - len(str(puzzle_array[i]))) + str(puzzle_array[i]), end="")
                        i += 1
                    if index % size != 0:
                        print(" ", end="")
                    else:
                        y += 1
                        print()
                    x += 1
                    index += 1
                print()
            print()