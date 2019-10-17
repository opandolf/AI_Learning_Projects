# import math
import numpy as np

class BinaryLogisticRegression:

    def _sigmoid(self, Z):
        return (1 / (1 + np.exp(-Z)))

    def _prediction_vector(self, X, W):
        return (self._sigmoid(X @ W))
    
    def _error_vector(self, P, Y):
        return (P - Y)
    
    def _gradiants_vector(self, S, X):
        return (S @ X)
    
    def _update_weights(self, W, X, Y, lr):
        P = self._prediction_vector(X, W)
        S = self._error_vector(P, Y)
        G = self._gradiants_vector(S, X)
        return(W - (G * (1/len(Y) * lr)))

    def train(self, X, Y, W, lr=1e-3, iters=1000):
        for _ in range(iters):
            W = self._update_weights(W, X, Y, lr)
        return W

    def predict(self, X, W):
        return self._prediction_vector(X, W)