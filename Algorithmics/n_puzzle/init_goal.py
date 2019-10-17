from misc.array_to_string import doublearray_to_string

def init_goal(n):
    array = [[0 for col in range(n)] for row in range(n)]
    row_begin = 0
    row_end = n
    col_begin = 0
    col_end = n
    i = 1
    while (i < n * n):
        x = col_begin
        while (x < col_end and i < n*n):
            array[row_begin][x] = i
            i += 1
            x += 1
        row_begin += 1
        x = row_begin
        while (x < row_end and i < n*n):
            array[x][col_end -1] = i
            i += 1
            x += 1
        col_end -= 1

        x = col_end - 1
        while (x >= col_begin and i < n*n):
            array[row_end -1][x] = i
            i += 1
            x -= 1
        row_end -= 1

        x = row_end - 1
        while (x >= row_begin and i < n*n):
            array[x][col_begin] = i
            i += 1
            x -= 1
        col_begin += 1
    puzzle = doublearray_to_string(array, ",", ",")
    return puzzle
    # puzzle = ""
    # for lines in array:
    #     for nbr in lines:
    #         puzzle += str(nbr) + ","
    # puzzle = puzzle[:-1]
    # return puzzle