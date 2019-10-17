import pandas as pd
import numpy as np
import os
import argparse
from MultinomialLogisticRegression import MultinomialLogisticRegression

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Training part of logistic regression multi-classifier")
    parser.add_argument("dataset", metavar="dataset", action="store", help="Path of the dataset you want to train on")
    args = parser.parse_args()

    # dataset = "resources/dataset_train.csv"
    df = pd.read_csv(args.dataset, index_col=0, header=0)
    droplist = ["Defense Against the Dark Arts", "Arithmancy", "Care of Magical Creatures"]
    better_df = df.drop(columns=droplist).dropna()
    features_df = better_df.select_dtypes(include="number")

    target_df = better_df["Hogwarts House"]
    target_onehot_df = pd.get_dummies(target_df)

    if os.path.isfile("weights.csv"):
        weights_df = pd.read_csv("weights.csv", index_col=0, header=0)
    else:
        print("weights.csv does not exist, initializing weights to 0")
        weights_df = pd.DataFrame(0, index=target_onehot_df.columns, columns=features_df.columns)
        weights_df.to_csv("weights.csv")

    mlr = MultinomialLogisticRegression()
    weights_df = mlr.train(features_df, target_onehot_df, weights_df)
    weights_df.to_csv("weights.csv")