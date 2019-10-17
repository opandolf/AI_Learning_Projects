import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import keras.backend as K

class NeuralNetwork():
    def __init__(self, input_shape, num_classes, hyperparameters):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(num_classes, activation='softmax'))

        model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
        self.model = model
    
    def train(self, x_train, y_train, x_test, y_test):
        self.model.fit(x_train, y_train, batch_size=hyperparameters.batch_size, epochs=hyperparameters.epochs, verbose=1, validation_data=(x_test, y_test))
    
    def evaluate(self, x_test, y_test):
        score = self.model.evaluate(x_test, y_test, verbose=0)
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])

## hyperparameters
class Hyperparameters():
    def __init__(self):
        self.batch_size = 128
        self.num_classes = 10
        self.epochs = 12
        self.img_rows, self.img_cols = 28, 28


hyperparameters = Hyperparameters()

# load data_sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# reshape and normalize X
x_train = x_train.reshape(x_train.shape[0], hyperparameters.img_rows, hyperparameters.img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], hyperparameters.img_rows, hyperparameters.img_cols, 1)
input_shape = (hyperparameters.img_rows, hyperparameters.img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# convert Y in one-hot vectors
y_train = keras.utils.to_categorical(y_train, hyperparameters.num_classes)
y_test = keras.utils.to_categorical(y_test, hyperparameters.num_classes)


nn = NeuralNetwork(input_shape, hyperparameters.num_classes, hyperparameters)
nn.train(x_train, y_train, x_test, y_test)
nn.evaluate(x_test, y_test)