import numpy as np

value_array = [0, 35, 800, 15000, 80000, np.inf]

def qtuple_value(qtuple):
        white = 0
        black = 0
        for x in qtuple:
            if x == 1:
                white += 1
            elif x == -1:
                black += 1
        if white > 0 and black > 0:
            return 0, 0
        if white > 0:
            return value_array[white], white
        if black > 0:
            return -value_array[black], -black
        return 0, 0

def preprocess_line_eval(line, pos):
        qtuple = [0]*5
        score = 0
        max_size = 0
        left_capture = 0
        right_capture = 0
        count = 0
        if len(line) > 4:
            for i in range(len(line) - 4):
                for x in range(5):
                    qtuple[x] = line[i + x]
                value, size = qtuple_value(qtuple)
                score += value
                max_size = max(max_size, size * line[pos])
                if size * line[pos] == 3:
                    count += 1
        
        else:
            score = 0
            max_size = 0
        if pos - 3 >= 0 and line[pos] == line[pos - 3] == -line[pos - 2] == -line[pos - 1] != 0:
            left_capture = 1
        if pos + 3 < len(line) and line[pos] == line[pos + 3] == -line[pos + 2] == -line[pos + 1] != 0:
            right_capture = 1
        capture = (left_capture, right_capture)
        return score , True if (max_size == 3 and count > 1) else False, capture

def preprocess_values(regle):
        dict_values = {}
        for size in range(1, 10):
            array = [0] * size
            for i in range(3 ** size):
                if i == 120:
                    i = i
                for b in range(size):
                    array[b] = int(i / 3 ** (size - 1 - b)) % 3 - 1
                for pos in range(max(0, size - 5), min(9, 0 + 5, size)):
                    value, free_three, capture = preprocess_line_eval(array, pos)
                    if regle != "42":
                        free_three = False
                        capture = (0,0)
                    dict_values[(str(array), pos)] = {'value': value, 'free_three': free_three, 'capture': capture}
        return dict_values

