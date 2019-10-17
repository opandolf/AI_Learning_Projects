import pandas as pd
import numpy as np
import os
import argparse
from MultinomialLogisticRegression import MultinomialLogisticRegression

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prediction part of logistic regression multi-classifier")
    parser.add_argument("dataset", metavar="dataset", action="store", help="Path of the dataset you want to predict the houses")
    parser.add_argument("weights", metavar="weights", action="store", help="Path of the weights")
    args = parser.parse_args()

    df = pd.read_csv(args.dataset, index_col=0, header=0)
    droplist = ["Hogwarts House", "Defense Against the Dark Arts", "Arithmancy", "Care of Magical Creatures"]
    houses_df = df[["Hogwarts House"]].copy()
    better_df = df.drop(columns=droplist).dropna()
    features_df = better_df.select_dtypes(include="number")

    if os.path.isfile(args.weights):
        weights_df = pd.read_csv(args.weights, index_col=0, header=0)
    else:
        print("%s does not exist, initialize weights" % (args.weights))
        weights_df = pd.DataFrame(0, index=['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'], columns=features_df.columns)
        weights_df.to_csv("weights.csv")

    mlr = MultinomialLogisticRegression()

    prediction_df = mlr.predict(features_df, weights_df)

    for x in range(len(prediction_df.index)):
        houses_df.loc[x, "Hogwarts House"] = prediction_df.iloc[x].idxmax()
    houses_df.to_csv("houses.csv")