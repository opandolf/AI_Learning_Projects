# gomoku

Gomoku is a school project done with Jean Baptiste Austry (https://github.com/jb255).  
We had to make a Min-max algorithm able to beat, in gomoku, a human player in a minimum of step.  
In order to improve minimax exploration we used an iterative deepening wrapper, greedy choice of childrens and transposition table with zobrist keys.  
Our heuristic evaluates position by adding the impact of the stone played to the previous value of the board. We preprocess the pattern calculation before lauching the game.

# Usage

usage: main.py [-h] [-b] [file [file ...]]
  
positional arguments:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file  
  
optional arguments:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-h, --help        show this help message and exit  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-b, --board_size  change the board size  
