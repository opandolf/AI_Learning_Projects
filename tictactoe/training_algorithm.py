from SimpleAlphaZeroNN.NN import NN
from self_play import self_play
from evaluate_newtork import evaluate_network
from TicTacToe.Player import Player
from MCTS import MCTS
import os

def training_algorithm(game, args):
    
    nn1 = NN(game,args)
    nn2 = nn1.__class__(game,args)
    
    # if os.path.isfile(args['save_file']):
    #     nn.model.load_weights(args['save_file'])
    
    p1 = Player(nn1, MCTS(game,nn1,args),game.player1_value)
    p2 = Player(nn2, MCTS(game,nn2,args),game.player2_value)

    # p2.nn.model.load_weights(args['save_file'])

    print("TRAINING PHASE STARTING")
    for i in range(args['training_phase_iterations']):
        print("-- training iteration : %d / %d" %(i, args['training_phase_iterations']))
        p1.nn.model.save_weights(args['save_file'])
        p2.nn.model.load_weights(args['save_file'])
        
        training_set = self_play(game, p2, args)
        print("-- neural network training")
        p2.nn.train(training_set)

        print("-- evaluation")
        score = evaluate_network(p1, p2, game, args)

        if score >= 0.5:
            print("new best player: ", score)
            p2.nn.model.save_weights(args['save_file'])
            p1.nn.model.load_weights(args['save_file'])
        else:
            print("not better: ", score)