import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LTSM


class RecurrentNeuralNetwork:
    def __init__(self, size):
        

        model = Sequential()

        model.add(LTSM(128, input_shape=(3,3), activation='relu', return_sequences=True))
        model.add(Dropout(0.2))

        model.add(LTSM(128, activation='relu'))
        model.add(Dropout(0.2))

        model.add(Dense(32, activation='relu'))
        model.add(Dropout(0.2))

        model.add(Dense(32, activation='softmax'))


        opt= tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)

        model.compile(loss='sparse_categorical_crossentropy', optimizers=opt, metrics=['accuracy'])
    
        