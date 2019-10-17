from misc.array_to_string import array_to_string
from algorithm.astar import astar
from algorithm.Node import Node

def set_new_goal(goal, size):
    fringe_goal = goal.copy()
    new_goal = []
    if size % 2 == 0:
        ref_line = 0
        ref_col = size - 1
    else:
        ref_line = size - 1
        ref_col = 0
    for i in range(len(fringe_goal)):
        if (not (int(i % size) == ref_col or int(i / size) == ref_line)):
            new_goal.append(str(fringe_goal[i]))
            fringe_goal[i] = 'x'
    return fringe_goal, new_goal

def set_new_start(start, size):
    new_start = []
    if size % 2 == 0:
        ref_line = 0
        ref_col = size - 1
    else:
        ref_line = size - 1
        ref_col = 0
    for i in range(len(start)):
        if (not (int(i % size) == ref_col or int(i / size) == ref_line)):
            new_start.append(str(start[i]))
    return new_start


def fringe_algo(start, goal, cost_function, heuristic_function,size,greedy):
    tmp_size = size
    new_goal = goal.split(",")
    new_start = start.split(",")
    complexity_time = 0
    complexity_size = 0
    size_solution = 0
    solutions = []
    while(tmp_size > 3):
        fringe_goal, new_goal = set_new_goal(new_goal, tmp_size)
        # print(array_to_string(new_goal,","))
        sol, total_opened, max_opened = astar(Node(array_to_string(new_start, ",")), array_to_string(fringe_goal, ","), cost_function, heuristic_function, tmp_size, greedy)
        if (len(sol) > 1):
            sol = sol[1:]
        solutions.append(sol)
        complexity_time += total_opened
        if (max_opened > complexity_size):
            complexity_size = max_opened
        size_solution += len(sol)
        new_start = set_new_start(sol[-1].split(","), tmp_size)
        tmp_size -= 1
    sol, total_opened, max_opened = astar(Node(array_to_string(new_start, ",")), array_to_string(new_goal, ","), cost_function, heuristic_function, 3, greedy)
    if (len(sol) > 1):
        sol = sol[1:]
    solutions.append(sol)
    complexity_time += total_opened
    if (max_opened > complexity_size):
        complexity_size = max_opened
    size_solution += len(sol)
    return solutions, complexity_time, complexity_size, size_solution
