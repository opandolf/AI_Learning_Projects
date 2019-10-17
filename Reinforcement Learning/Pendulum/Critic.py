import keras
from keras.layers import Input, Dense, Concatenate
from keras.models import Model
from keras.optimizers import Adam

import tensorflow as tf
import os

class Critic:
    def __init__(self, env, sess, hyperparameters):
        self.env = env
        self.sess = sess
        self.hp = hyperparameters

        self.state_input, self.action_input, self.model = self.create_model()
        _, _, self.target_model = self.create_model()

        self.grads = tf.gradients(self.model.output, self.action_input)

    def create_model(self):
        state_input = Input(self.env.observation_space.shape)
        state_h1 = Dense(500, activation='relu')(state_input)
        state_h2 = Dense(1000)(state_h1)

        action_input = Input(shape=self.env.action_space.shape)
        action_h1 = Dense(500)(action_input)

        merged = Concatenate()([state_h2, action_h1])
        merged_h1 = Dense(500, activation='relu')(merged)
        output = Dense(1, activation='linear')(merged_h1)

        model = Model(input=[state_input, action_input], output=output)

        adam = Adam(self.hp.lr)
        model.compile(loss='mse', optimizer=adam)

        return state_input, action_input, model
    
    def gradients(self, states, predicted_actions):
        grads = self.sess.run(self.grads, feed_dict={
            self.state_input: states,
            self.action_input: predicted_actions
        })[0]
        return grads
    
    def train(self, states, actions, rewards):
        self.model.fit([states, actions], rewards, verbose=0)
    
    def update_target(self):
        weights  = self.model.get_weights()
        target_weights = self.target_model.get_weights()
		
        for i in range(len(target_weights)):
            target_weights[i] = weights[i]*self.hp.tau + target_weights[i]*(1-self.hp.tau)
        self.target_model.set_weights(target_weights)

    def save(self, path):
        self.model.save_weights(path + "critic_model" + ".h5")
        self.target_model.save_weights(path + "target_critic_model" + ".h5")

    def load(self, path):
        if os.path.isfile(path + "critic_model" + ".h5"):
            self.model.load_weights(path + "critic_model" + ".h5")
        if os.path.isfile(path + "target_critic_model" + ".h5"):
            self.target_model.load_weights(path + "target_critic_model" + ".h5")