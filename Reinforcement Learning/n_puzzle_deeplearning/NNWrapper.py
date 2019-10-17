import numpy as np
from NeuralNetwork import Neuralnetwork

class NNWrapper():
    def __init__(self, size):
        self.nnet = Neuralnetwork(size)
        self.size = size

    def train(self, examples, epoch=100, load=False):

        if load == True:
            self.nnet.model.load_weights('npuzzle'+str(self.size)+'.h5')
        i, v = list(zip(*examples))
        
        # Tensorflow demande des numpy array en input
        i = np.asarray(i).reshape(len(i),self.size, self.size)
        v = np.asarray(v)

        hist = self.nnet.model.fit(x = i, y = v, epochs=epoch, callbacks=[self.nnet.callbacks])
        self.nnet.model.save_weights('npuzzle'+str(self.size)+'.h5')
        # print(hist.history['acc'])
    
    def predict(self, state):

        i = np.asarray(state).reshape(1, self.size, self.size)
        v = self.nnet.model.predict(i)
        return v[0]
    
    def evaluate(self, evaluations):

        i, v = list(zip(*evaluations))

        i = np.asarray(i).reshape(len(i),self.size, self.size)
        v = np.asarray(v)

        blabla = self.nnet.model.evaluate(x = i, y = v)
        print(blabla)