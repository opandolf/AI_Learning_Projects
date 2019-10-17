import argparse
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

pd.options.mode.chained_assignment = None
np.warnings.filterwarnings('ignore')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Display a histogram of the features having a homogeneous distribution of the grades between the different houses")
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

        nb_features = len(column_names) - 1
        line_size = int(math.sqrt(nb_features)) + 1
        fig, ax = plt.subplots(line_size,line_size, figsize=(20,15))
        ax = ax.ravel()

        for i in range(len(ax)):
            if i < nb_features:
                for house in houses:
                    ax[i].hist(num_df.loc[num_df["Hogwarts House"] == house, column_names[i]], alpha=0.5, bins=50, color=color_dict[house], label=house)
                ax[i].set_title(column_names[i])
                ax[i].legend(prop={'size': 6})
                ax[i].get_xaxis().set_visible(False)
                ax[i].get_yaxis().set_visible(False)
            else:
                ax[i].set_visible(False)

    else:

        fig, ax = plt.subplots(1,2, figsize=(20,15))
        ax = ax.ravel()

        for house in houses:
            ax[0].hist(num_df.loc[num_df["Hogwarts House"] == house, "Arithmancy"], alpha=0.5, bins=50, color=color_dict[house], label=house)
            ax[1].hist(num_df.loc[num_df["Hogwarts House"] == house, "Care of Magical Creatures"], alpha=0.5, bins=50, color=color_dict[house], label=house)
        ax[0].set_title("Arithmancy")
        ax[0].legend()
        ax[1].set_title("Care of Magical Creatures")
        ax[1].legend()

    plt.show()