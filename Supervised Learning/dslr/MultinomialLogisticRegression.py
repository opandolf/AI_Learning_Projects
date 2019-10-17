from BinaryLogisticRegression import BinaryLogisticRegression
# from DataSetCsv import DataSetCsv
# from tranpose_list import transpose_list
import pandas as pd
import numpy as np

class MultinomialLogisticRegression:
    
    def _standardize(self, X):
        normalized = (X - X.mean())/ X.std()
        return normalized


    def train(self, X, Y, W, lr=1e-3, iters=1000):
        X = self._standardize(X)
        for i in range(len(W.index)):
            blr = BinaryLogisticRegression()
            W.iloc[i] = blr.train(X.to_numpy(), Y.iloc[:,i].to_numpy(), W.iloc[i].to_numpy(), lr, iters)
        return W

    def predict(self, X, W):
        X = self._standardize(X)
        P = pd.DataFrame(index=X.index, columns=W.index, dtype=float)
        for i in range(len(W.index)):
            blr = BinaryLogisticRegression()
            P.iloc[:,i] = blr.predict(X.to_numpy(), W.iloc[i].to_numpy())
        return P
