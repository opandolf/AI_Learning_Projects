from TicTacToe.Player import Player
from SimpleAlphaZeroNN.NN import NN
from MCTS import MCTS
import os

def human_play(game, args):
    nn = NN(game, args)
    if os.path.isfile(args['save_file']):
        nn.model.load_weights(args['save_file'])
    computer = Player(nn, MCTS(game, nn, args), game.player2_value)
    human = Player(None, None, game.player1_value)
    game.human_play(human, computer)    