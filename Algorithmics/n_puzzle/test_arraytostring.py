from fringe_algo import fringe_algo
from init_solution import init_solution
from misc.array_to_string import doublearray_to_string
from puzzle_generator import create_puzzle
from heuristic_set.manhattant_distance import manhattan_distance_set
from heuristic_set.linear_conflict_set import linear_conflict_manhattan
from cost_functions.equal_step_cost import equal_step_cost


size = 4
goal = init_solution(size)
puzzle = "12,1,5,3,9,11,13,4,2,8,14,6,0,10,15,7"

# size = 5
# goal = init_solution(size)
# puzzle = "8,13,11,9,21,2,23,19,3,18,5,6,10,1,16,15,4,14,17,20,0,7,12,24,22"

print("goal: " + goal)
print("start: " + puzzle)

fringe_algo(puzzle, goal,equal_step_cost, linear_conflict_manhattan, size)