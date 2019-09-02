import gym
import random
import numpy as np
from collections import deque
from NeuralNetwork import NeuralNetwork
import matplotlib.pyplot as plt
import argparse
import os

class CartPole():
        def __init__(self):
                self.name = "CartPole-v0"
                self.env = gym.make(self.name)
                self.env.reset()
                self.max_steps = 200
        def evaluation(self, reward, done):
                if done == True:
                        return 0
                else:
                        return reward + 1
        def action_choice(self, probability):
                if probability >= 0.5:
                        return 1
                else:
                        return 0


class Hyperparameters():
        def __init__(self):
                self.learning_rate = 1e-3
                self.epsilon = 0.99
                self.gamma = 0.95
                self.episodes = 250
                self.batch_size = 100
                self.epsilon_min = 0.1
                self.epsilon_decay = 0.995
                self.iters = 10
                self.dirname = "./Models/"

class Agent():
        def __init__(self, game, neural_network, hyperparameters):
                self.game = game
                self.neural_network = neural_network
                self.hp = hyperparameters
                self.memory = deque(maxlen=2000)

        def simulate_one_game(self):
                state = self.game.env.reset()
                for _ in range(self.game.max_steps):
                        action = self.act(state)
                        next_state, reward, done, _ = self.game.env.step(action)
                        self.memory.append((state, action, reward, next_state, done))
                        if done:
                                break
                        state = next_state

        def remember(self):
                pass

        def act(self, state):
                if np.random.rand() < self.hp.epsilon:
                        return self.game.env.action_space.sample()
                # print("state: ", state, ", shape: ", state.shape)
                actions_reward = self.neural_network.predict(state)
                return np.argmax(actions_reward)

        def replay(self):
                minibatch = random.sample(self.memory, self.hp.batch_size)
                for state, action, reward, next_state, done in minibatch:
                        target = reward
                        if not done:
                                target = reward + self.hp.gamma * np.amax(self.neural_network.predict(next_state))
                        targets = self.neural_network.predict(state)
                        targets[action] = target
                        self.neural_network.train(state, targets)
                if self.hp.epsilon > self.hp.epsilon_min:
                        self.hp.epsilon *= self.hp.epsilon_decay

        def evaluate(self, n_episodes):
                count_array = []
                for _ in range(n_episodes):
                        count = 0
                        state = self.game.env.reset()
                        for _ in range(self.game.max_steps):
                                actions_reward = self.neural_network.predict(state)
                                state, reward, done, _ = self.game.env.step(np.argmax(actions_reward))
                                count += reward
                                if done:
                                        break
                        count_array += [count]
                        # print(count_array)
                        # print(count)
                return np.asarray(count_array).mean()

def train(game, hyperparameters, neural_network, agent):
        evals = [agent.evaluate(10)]
        for i in range(hyperparameters.episodes):
                for _ in range(hyperparameters.iters):
                        agent.simulate_one_game()
                agent.replay()
                score = agent.evaluate(10)
                evals += [score]
                print("episode: ", i, "/", hyperparameters.episodes, ", score :", score)
        neural_network.save(game.name)
        # print(evals)
        plt.plot(evals)
        plt.ylabel("scores")
        plt.show()

def play(game, hyperparameters, neural_network, agent):
        neural_network.load(game.name)
        state = game.env.reset()
        count = 0
        for _ in range(game.max_steps):
                game.env.render()
                action = np.argmax(neural_network.predict(state))
                state, reward, done, _ = game.env.step(action)
                count += reward
                if done:
                        break
        if count == game.max_steps:
                print("Victory")
        else:
                print("Defeat")
        

if __name__ == "__main__":

        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--trained', action='store_true', help="load your trained neural network if exist")
        parser.add_argument('-e', '--exemple', action='store_true', help="load an exemple of trained neural network")
        parser.add_argument('-p', '--play', action='store_true', help="skip the train part, just play with the trained neural network selected if exist")
        args = parser.parse_args()

        game = CartPole()
        hyperparameters = Hyperparameters()
        neural_network = NeuralNetwork(hyperparameters)
        agent = Agent(game, neural_network, hyperparameters)

        if args.trained:
                filename = hyperparameters.dirname + game.name + ".h5"
                if not os.path.isfile(filename):
                        print("There is no model saved, start training a new neural network")
                else:
                        neural_network.load(game.name)
        
        if args.exemple:
                filename = hyperparameters.dirname + "Trained-" + game.name + ".h5"
                print(filename)
                if not os.path.isfile(filename):
                        print("There is no exemple for this game, start training a new neural network")
                else:
                        neural_network.load("Trained-" + game.name)
        
        if not args.play:
                train(game, hyperparameters, neural_network, agent)


        play(game, hyperparameters, neural_network, agent)
        game.env.close()
