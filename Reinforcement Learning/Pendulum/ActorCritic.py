import keras
from keras.layers import Input, Dense, Concatenate
from keras.models import Model
from keras.optimizers import Adam
import tensorflow as tf
import random
from collections import deque
import numpy as np
import os

from Actor import Actor
from Critic import Critic

class DDPGAgent:

    def __init__(self, env, sess, hyperparameters):
        self.env = env
        self.sess = sess
        self.hp = hyperparameters
        self.memory = deque(maxlen=4000)

        self.actor = Actor(self.env, self.sess, self.hp)
        self.critic = Critic(self.env, self.sess, self.hp)

        self.sess.run(tf.global_variables_initializer())

    def _train(self, states, actions, rewards, next_states, dones):
        if len(self.memory) < self.hp.batch_size:
            return

        target_actions = self.actor.target_model.predict(next_states)
        futur_rewards = self.critic.target_model.predict([next_states, target_actions])
        rewards += self.hp.gamma * futur_rewards * (1 - dones)                          #if done, no futur rewards

        predicted_actions = self.actor.model.predict(states)
        grads = self.critic.gradients(states, predicted_actions)
        self.actor.train(states, grads)
        self.critic.train(states, actions, rewards)
    
    def _update_target(self):
        self.actor.update_target()
        self.critic.update_target()

    def replay(self):
        if len(self.memory) < self.hp.batch_size:
            return
        
        samples = np.array(random.sample(self.memory, self.hp.batch_size))

        states = np.stack(samples[:,0]).reshape((samples.shape[0],-1))
        actions = np.stack(samples[:,1]).reshape((samples.shape[0],-1))
        rewards = np.stack(samples[:,2]).reshape((samples.shape[0],-1))
        next_states = np.stack(samples[:,3]).reshape((samples.shape[0],-1))
        dones = np.stack(samples[:,4]).reshape((samples.shape[0],-1))

        self._train(states, actions, rewards, next_states, dones)
        self._update_target()

    def remember(self, state, action, reward, next_state, done):
        self.memory.append([state, action, reward, next_state, done])

    def act(self, state, temp=True):
        self.hp.epsilon *= self.hp.epsilon_decay
        if np.random.random() < self.hp.epsilon and temp:
            return self.actor.model.predict(state) * 2 + np.random.normal()
        return self.actor.model.predict(state) * 2
    
    def one_game_trial(self):
        state = self.env.reset()
        state = state.reshape((1, self.env.observation_space.shape[0]))

        for _ in range(self.hp.max_steps):
            action = self.act(state)
            action = action.reshape((1, self.env.action_space.shape[0]))
            next_state, reward, done, _ = self.env.step(action)
            next_state = next_state.reshape((1, self.env.observation_space.shape[0]))
            self.remember(state, action, reward, next_state, done)
            state = next_state

    def evaluate(self, n_episodes):
        count_array = []
        for _ in range(n_episodes):
            count = 0
            state = self.env.reset()
            for _ in range(self.hp.max_steps):
                action = self.act(state)
                state, reward, _, _ = self.env.step(action)
                count += reward
            count_array += [count]
        return np.asarray(count_array).mean()
    
    def save(self):
        if not os.path.isdir(self.hp.savedir):
            os.mkdir(self.hp.savedir)
        self.actor.save(self.hp.savedir)
        self.critic.save(self.hp.savedir)
        print("models saved")

    def load(self, prefix):
        self.actor.load(self.hp.savedir + prefix)
        self.critic.load(self.hp.savedir + prefix)