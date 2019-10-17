from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.losses import *
from tensorflow.keras.callbacks import *

class Neuralnetwork:
    def __init__(self, size):

        self.callbacks = TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)
        # input layer
        i = Input(shape=(size,size))
        i_r = Reshape((size,size,1))(i)

        # hidden layers
            # 4 Conv2D
        h_conv1 = Activation('relu')(BatchNormalization(axis=3)(Conv2D(filters=32, kernel_size=3, padding='same')(i_r)))
        h_conv2 = Activation('relu')(BatchNormalization(axis=3)(Conv2D(filters=32, kernel_size=3, padding='same')(h_conv1)))
        h_conv3 = Activation('relu')(BatchNormalization(axis=3)(Conv2D(filters=32, kernel_size=3, padding='same')(h_conv2)))
        h_conv4 = Activation('relu')(BatchNormalization(axis=3)(Conv2D(filters=32, kernel_size=3, padding='same')(h_conv3)))
            # 2 Dense
        h_flat = Flatten()(h_conv4)
        h_d1 = Dropout(0.8)(Activation('relu')(BatchNormalization(axis=1)(Dense(1024)(h_flat))))
        h_d2 = Dropout(0.8)(Activation('relu')(BatchNormalization(axis=1)(Dense(512)(h_d1))))

        #output layer
        v = Dense(1, activation='relu')(h_d2)

        self.model = Model(inputs=i, outputs=v)
        self.model.compile(loss='mean_squared_error', optimizer=Adam(0.01))