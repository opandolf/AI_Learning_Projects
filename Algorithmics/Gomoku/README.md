# gomoku

Gomoku is a school project realized with Jean Baptiste Austry (https://github.com/jb255).  
We had to make a Min-max algorithm able to beat, in gomoku, a human player in a minimum of step.  
In order to improve minimax exploration we used greedy choice of childrens and transposition table with zobrist keys.  
Our heuristic evaluate position by adding the impact of the stone played to the previous value of the board. We preprocess the pattern calculation before lauching the game.
