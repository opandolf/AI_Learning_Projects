from Npuzzle import Npuzzle
from Node import Node
from simple_ADI import getADIExamples
from tabulate import tabulate
from NNWrapper import NNWrapper
from Astar import Astar

examples = getADIExamples(1000,31,3)
input_states, target_vs = list(zip(*examples))
# print(input_states)
# print(target_vs)
nnet = NNWrapper(3)
nnet.train(examples,20, load=True)

astar = Astar(nnet, Npuzzle(input_states[-1], 3))
len_solution, solution_array = astar.solve()
print(len_solution)

for x in solution_array:
    print(x)
    print()
