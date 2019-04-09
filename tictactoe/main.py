from training_algorithm import training_algorithm
from TicTacToe.GameRules import GameRules
from human_play import human_play
import sys

if __name__ == "__main__":
    args = {
        'mcts_simulations' : 25,
        'evaluation_games' : 20,
        'neural_network_epochs' : 10,
        'self_plays' : 100,
        'training_phase_iterations' : 10,
        'mcts_cpuct' : 1,
        'save_file' : "save_weights.h5",
        'load_weights' : False,
        'train' : False,
        'human_play' : False
    }

    if "--train" in sys.argv:
        args['train'] = True
    if "--load" in sys.argv:
        args['load_weights'] = True
    if "--human" in sys.argv or len(sys.argv) == 1:
        args['human_play'] = True

    game = GameRules()

    if args['train'] == True:
        training_algorithm(game, args)
    if args['human_play']:
        human_play(game, args)