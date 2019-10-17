from keras.layers import Input, Dense
from keras.models import Model
from keras.optimizers import Adam

import tensorflow as tf
import os

class Actor:
    def __init__(self, env, sess, hyperparameters):
        self.env = env
        self.sess = sess
        self.hp = hyperparameters

        self.state_input, self.model = self.create_model()
        _, self.target_model = self.create_model()

        self.critic_grad = tf.placeholder(tf.float32, [None, self.env.action_space.shape[0]])

        model_weights_vars = self.model.trainable_weights
        self.grads = tf.gradients(self.model.output, model_weights_vars, -self.critic_grad) #negative because we want to do gradient ascent
        grads_and_vars = zip(self.grads, model_weights_vars)
        self.optimize = tf.train.AdamOptimizer(self.hp.lr).apply_gradients(grads_and_vars)

    def create_model(self):
        state_input = Input(shape=self.env.observation_space.shape)
        h1 = Dense(500, activation='relu')(state_input)
        h2 = Dense(1000, activation='relu')(h1)
        h3 = Dense(500, activation='relu')(h2)
        output = Dense(self.env.action_space.shape[0], activation='tanh')(h3)

        model = Model(input=state_input, output=output)
        adam = Adam(lr=self.hp.lr)

        model.compile(loss='mse', optimizer=adam)
        
        return state_input, model
    
    def train(self, states, grads):

        self.sess.run(self.optimize, feed_dict={
            self.state_input: states,
            self.critic_grad: grads
        })
    
    def update_target(self):
        weights  = self.model.get_weights()
        target_weights = self.target_model.get_weights()
		
        for i in range(len(target_weights)):
            target_weights[i] = weights[i]*self.hp.tau + target_weights[i]*(1-self.hp.tau)
        self.target_model.set_weights(target_weights)

    def save(self, path):
        self.model.save_weights(path + "actor_model" + ".h5")
        self.target_model.save_weights(path + "target_actor_model" + ".h5")

    def load(self, path):
        if os.path.isfile(path + "actor_model" + ".h5"):
            self.model.load_weights(path + "actor_model" + ".h5")
        if os.path.isfile(path + "target_actor_model" + ".h5"):
            self.target_model.load_weights(path + "target_actor_model" + ".h5")