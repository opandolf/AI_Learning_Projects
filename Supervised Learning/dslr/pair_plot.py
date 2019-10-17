import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.mode.chained_assignment = None
np.warnings.filterwarnings('ignore')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Display a scatter matrix of the features we will use for logistic regression")
    parser.add_argument("-a", "--all", action="store_true", help="display an histogram for each numeric features of the dataset")
    args = parser.parse_args()

    dataset = "resources/dataset_train.csv"
    df = pd.read_csv(dataset, index_col=0, header=0)
    num_df = df.select_dtypes(include="number")

    num_df['Hogwarts House'] = df["Hogwarts House"].copy()

    houses = num_df["Hogwarts House"].unique()
    column_names = num_df.columns.tolist()

    color_dict = {
        'Hufflepuff':'yellow',
        'Ravenclaw':'blue',
        'Slytherin':'green',
        'Gryffindor':'red',
        }
    
    if args.all:
        pd.plotting.scatter_matrix(num_df[column_names], figsize=(20,15))
    
    else:
        droplist = ["Defense Against the Dark Arts", "Arithmancy", "Care of Magical Creatures"]
        better_df = num_df.drop(columns=droplist).dropna()
        column_names = better_df.columns.tolist()
        pd.plotting.scatter_matrix(better_df[column_names], figsize=(20,15))

    plt.show()