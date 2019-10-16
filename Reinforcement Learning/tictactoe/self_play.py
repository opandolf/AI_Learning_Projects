from MCTS import MCTS
from TicTacToe.Board import Board
import numpy as np
from TicTacToe.Player import Player

def self_play(game, p2, args):
    # mcts = MCTS(game, NN, args)
    # p1 = Player(mcts,game.player1_value)
    p1 = Player(p2.nn, p2.mcts,game.player1_value)
    training_set = []
    for i in range(args['self_plays']):
        print("---- self play: %d / %d" %(i, args['self_plays']))
        training_set += game.training_play(p1, p2)

        # game_records = []
        # board = game.init_board()
        # while not(game.ended(board)):
        #     p = mcts.probabilites(board)
        #     game_records += board.symetries(p)
        #     a = np.random.choice(np.arange(game.movecount), p=p)
        #     board = board.next_board(a)
        # if board.lost():
        #     for i in range(len(game_records)):
        #         game_records[i][2] = 1 if game_records[i][2] != board.player else -1
        # else:
        #     for i in range(len(game_records)):
        #         game_records[i][2] = 0
        # training_set += game_records

    return training_set