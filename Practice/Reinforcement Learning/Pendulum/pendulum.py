import gym
from ActorCritic import DDPGAgent
import tensorflow as tf
import keras
import keras.backend as K
import matplotlib.pyplot as plt
import os
import argparse



class Pendulum():
    def __init__(self):
        self.name = "Pendulum-v0"
        self.env = gym.make(self.name)
        self.env.reset()
        # self.max_steps = 500

class Hyperparameters():
        def __init__(self):
                self.lr = 1e-4
                self.lr_actor = 1e-4
                self.lr_critic = 1e-4

                self.epsilon = 0.9
                self.gamma = 0.90
                self.episodes = 10
                self.batch_size = 256
                self.epsilon_min = 0
                self.epsilon_decay = 0.99995
                self.iters = 10
                self.savedir = "./Models/"
                self.max_steps = 200

                self.tau = .01


def train(hyperparameters, agent):
    for i in range(hyperparameters.episodes):
        for _ in range(hyperparameters.iters):
            agent.one_game_trial()
            for _ in range(40):
                agent.replay()
        print("episode: ", i + 1, "/", hyperparameters.episodes)
        play(hyperparameters, agent)
        agent.save()



def play(hyperparameters, agent):
        # agent.load()
        state = agent.env.reset()
        
        score = 0
        for _ in range(500):
                state = state.reshape((1, agent.env.observation_space.shape[0]))
                agent.env.render()
                action = agent.act(state, temp=False)
                action = action.reshape((1, agent.env.action_space.shape[0]))
                state, reward, _, _ = agent.env.step(action)
                score += reward
        print(score)

def main(args):
    sess = tf.Session()
    K.set_session(sess)
    game = Pendulum()
    hp = Hyperparameters()
    # hp.max_steps = game.max_steps
    agent = DDPGAgent(game.env, sess, hp)

    if args.trained:
        agent.load("")
    
    if args.exemple:
        agent.load("Trained-")
    if not args.play:
        train(hp, agent)

    play(hp,agent)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--trained', action='store_true', help="load your trained neural networks if exist")
    parser.add_argument('-e', '--exemple', action='store_true', help="load an exemple of trained neural networks")
    parser.add_argument('-p', '--play', action='store_true', help="skip the train part, just play with the trained neural networks selected if exist")
    args = parser.parse_args()

    main(args)
    # test()