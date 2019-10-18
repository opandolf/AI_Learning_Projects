# N_puzzle

I was interested by [**this solution**](https://arxiv.org/pdf/1805.07470.pdf) of problem solving Reinforcement Learning environment where terminal states are rare.
For example in case of rubik's cube or n_puzzles, a stochastic exploration of solutions have a very low chance of passing by a terminal state.  
To overcome this challenge, they implement autodidactic iterations algorithm. It create dataset exploring by starting from terminal state (here solution state). This increase frequency of solution state in datasets and improve learning efficiency.
