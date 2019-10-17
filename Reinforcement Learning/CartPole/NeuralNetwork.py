from keras.models import Model
from keras.layers import Dense, Input
from keras.optimizers import Adam

import numpy as np
import os

class NeuralNetwork():
    def __init__(self, hyperparameters):
        # n_inputs = 4

        a = Input(shape=(4,))
        b = Dense(24, activation='relu')(a)
        c = Dense(24, activation='relu')(b)
        d = Dense(2, activation='linear')(c)
        self.model = Model(inputs=a, outputs=d)  

        # self.model = Sequential([
        #     Dense(5, activation="relu", input_shape=(4,)),
        #     Dense(2, activation="linear"),
        # ])
        self.model.compile(loss='mse', optimizer=Adam(lr=hyperparameters.learning_rate))

    def predict(self, inputs):
        # print("shape: ",inputs.shape)
        x = np.asarray(inputs[np.newaxis,:])
        p = self.model.predict(x)
        return p[0]
    
    def train(self, inputs, targets):
        x = np.asarray(inputs[np.newaxis,:])
        y = np.asarray(targets[np.newaxis,:])
        self.model.fit(x = x, y = y, verbose=0)
    
    def save(self, game_name):
        if not os.path.isdir("./Models/"):
            os.mkdir("./Models")
        savefile = "./Models/" + game_name + ".h5"
        self.model.save_weights(savefile)
    
    def load(self, game_name):
        if os.path.isfile("./Models/" + game_name + ".h5"):
            loadfile = "./Models/" + game_name + ".h5"
            self.model.load_weights(loadfile)

