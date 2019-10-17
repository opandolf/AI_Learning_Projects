#!/usr/bin/env python3

import sys
from docopt import docopt
from puzzle_generator import create_puzzle
from heuristic.manhattant_distance import manhattan_distance
from heuristic.linear_conflict import linear_conflict_manhattan
from heuristic.wrong_place import wrong_place
from cost_functions.equal_step_cost import equal_step_cost
from cost_functions.uniform_cost import uniform_cost
from init_goal import init_goal
from check_solvability import solvability
from algorithm.fringe_algo import fringe_algo
from print_sol import print_sol, to_array


help = """
Usage:
  n_puzzle.py [<puzzle_file>] [-h --help] [-u --uniform] [-g --greedy] [-i --iter]

Options:
  -h --help
  -u --uniform  Proceed with an Uniform Cost.
  -g --greedy   Proceed with a Greedy Search.
  -i --iter     Wait for user input to display the solution

"""


arguments = docopt(help)

def get_nbr(line, howMany):
    index = 0
    found = 0
    res = []
    while found != howMany and index < len(line):
        if line[index] == " " or line[index] == "\t":
            index += 1
        elif line[index].isdigit():
            startIndex = index
            while index < len(line) and line[index].isdigit():
                index += 1
            found += 1
            res.append(int(line[startIndex:index]))
        else:
            print("Syntax error on line: \"" + line[:-1] + "\"")
            exit(0)
    if found != howMany:
        print("N puzzle not valid! ")
        exit(0)
    return res


if arguments["<puzzle_file>"]:
    fileName = sys.argv[1]
    file = None
    size = None
    puzzle = ""
    validity_test = []
    try:
        file = open(fileName, "r")
    except:
        print("Invalid File Name.")
        exit(0)
    while 1:
        line = file.readline()
        if line == "":
            if not size:
                print("Empty file.")
                exit(0)
            puzzle = puzzle[:-1]
            break
        if not line.startswith("#"):
            if not size:
                res = get_nbr(line, 1)
                size = res[0]
                if size < 3:
                    print("N puzzle too small")
                    exit(0)
            else:
                res = get_nbr(line, size)
                for nbr in res:
                    if 0 <= nbr <= size*size-1 and nbr not in validity_test:
                        validity_test.append(nbr)
                        puzzle += str(nbr) + ","
                    else:
                        print("N puzzle not valid!")
                        exit()

else:
    size = input('Enter a size : ')
    try:
        size = int(size)
    except:
        print("Invalid size.")
        exit(0)
    puzzle = create_puzzle(size)

if not solvability(to_array(puzzle, size), to_array(init_goal(size), size), size):
    print("Ce taquin est insoluble")
    exit()

heuristic = None
heuristics = {"m": manhattan_distance, "l": linear_conflict_manhattan, "w": wrong_place}
while not heuristic:
    func = input('Chose a heuristic (m) for Manhattan Distance, (l) for Linear Conflict , (w) for Wrong Place:')
    heuristic = heuristics.get(func)

if arguments["--uniform"] > 0:
    cost_function = uniform_cost
else:
    cost_function = equal_step_cost

index = 1
puzzle_array = puzzle.split(",")
nbr_len = len(str(size*size))
for nbr in puzzle_array:
    print(" " * (nbr_len - len(str(nbr))) + str(nbr), end="")
    if index % size != 0:
        print(" ", end="")
    else:
        print()
    index += 1

sol, total_opened, max_opened, size_solution = fringe_algo(puzzle, init_goal(size), cost_function, heuristic, size,
                                                           True if arguments["--greedy"] > 0 else False)
print("\nTotal number of states ever selected in the opened set (complexity in time): {0}".format(total_opened))
print("Maximum number of states ever represented in memory at the same time during the search (complexity in size): {0}".format(max_opened))
print("Number of moves required to transition from the initial state to the final state, according to the search: {0}\n".format(size_solution))
print("The solution :")

print_sol(sol, size, init_goal(size), arguments["--iter"])
