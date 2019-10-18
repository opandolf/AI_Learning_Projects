from training_algorithm import training_algorithm
from TicTacToe.GameRules import GameRules
from human_play import human_play
import argparse
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

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', action='store_true', help="train the neural network")
    parser.add_argument('-l', '--load', action='store_true', help="load previously trained weights of the neural network")
    parser.add_argument('-p', '--play', action='store_true', help="allow you to play against the AI. Default if no arguments")
    argp = parser.parse_args()

    if argp.train:
        args['train'] = True
    if argp.load:
        args['load_weights'] = True
    if argp.play or len(sys.argv) == 1:
        args['human_play'] = True

    game = GameRules()

    if argp.train == True:
        training_algorithm(game, args)
    if argp.play:
        human_play(game, args)