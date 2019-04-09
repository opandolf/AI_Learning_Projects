import tensorflow
from tensorflow.keras.layers import Conv2D, Dropout, Dense, Input, Reshape, Activation, BatchNormalization, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model
import numpy as np

class NN:

    """
    Graph model class
    """
    
    def __init__(self, game, args):
        self.game = game
        self.epochs = args['neural_network_epochs']
        # I am not using residual layers in this model. Residual layers are used for limiting the vanishing gradients problem when layers go deep
        # I use batchnormalization instead.

        inputs = Input(shape=self.game.shape)

        # reshape inputs to fit model
        inputs_reshaped = Reshape((self.game.shape[0],self.game.shape[1], 1))(inputs)

        # add 3 convolutional layers which are the Core of NN
        h_conv1 = Activation('relu')(BatchNormalization()(Conv2D(filters=32, kernel_size=3, padding='same')(inputs_reshaped)))
        h_conv2 = Activation('relu')(BatchNormalization()(Conv2D(filters=32, kernel_size=3, padding='same')(h_conv1)))
        h_conv3 = Activation('relu')(BatchNormalization()(Conv2D(filters=32, kernel_size=3, padding='same')(h_conv2)))

        # Flatten for Dense layers
        h_flat = Flatten()(h_conv3)

        # policy head
        pi = Activation('softmax')(Dense(self.game.movecount, name='p')(h_flat))

        #value head
        v = Activation('tanh')(Dense(1, name='v')(h_flat))

        self.model = Model(inputs=inputs, outputs=[pi, v])
        self.model.compile(loss=['categorical_crossentropy','mean_squared_error'], optimizer=Adam(lr=1e-3, decay=1e-5), metrics=['accuracy'])

    def predict(self, board):
        
        state = board.state_formating_nn()

        # Resize board (1, x, y)
        state = state[np.newaxis,:,:]

        pi, v = self.model.predict(state)

        # Only keep available moves and normalize probabilities
        pi = pi[0] * board.valid_moves_mask()
        pi = pi / sum(pi)
        
        return pi, v[0][0]
    
    def train(self, training_set):

        boards,target_pis,target_vs = list(zip(*training_set))

        boards = np.asarray(boards)
        target_pis = np.asarray(target_pis)
        target_vs = np.asarray(target_vs)

        self.model.fit(x = boards, y = [target_pis, target_vs], epochs=self.epochs, verbose=0)