from TicTacToe.Player import Player
from MCTS import MCTS
import numpy as np

def evaluate_network(p1, p2, game, args):
    score = 0
    p1.reset_mcts()
    p2.reset_mcts()
    for i in range(int(args['evaluation_games'] / 2)):
        score -= game.evaluation_play(p1, p2)
        print("---- game : %d / %d | score : %d" % (i*2 + 1, args['evaluation_games'], score))
        score += game.evaluation_play(p2, p1)
        print("---- game : %d / %d | score : %d" % (i*2 + 2, args['evaluation_games'], score))
    score = (score / (int(args['evaluation_games']/2) * 2)) / 2 + 0.5
    return score