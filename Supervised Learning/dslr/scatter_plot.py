import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.mode.chained_assignment = None
np.warnings.filterwarnings('ignore')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Display a scatter plot of the features having a correlation between them")
    parser.add_argument("-a", "--all", action="store_true", help="display an scatter plot for each numeric features of the dataset")
    parser.add_argument("-c", "--colors", action="store_true", help="display different colors to show houses repartitions")
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
        line_size = nb_features
        fig, ax = plt.subplots(line_size,line_size, figsize=(20,15), sharex="col", sharey="row")
        ax = ax.ravel()

        for i in range(len(ax)):
            x_feature = i % line_size
            y_feature = int(i / line_size)
            if x_feature != y_feature:
                if args.colors:
                    for house in houses:
                        ax[i].scatter(num_df.loc[num_df["Hogwarts House"] == house, column_names[x_feature]], num_df.loc[num_df["Hogwarts House"] == house, column_names[y_feature]], alpha=0.5, color=color_dict[house], label=house)
                else:
                    ax[i].scatter(num_df[column_names[x_feature]], num_df[column_names[y_feature]], alpha=0.1)
                if y_feature == line_size - 1:
                    ax[i].set_xlabel(column_names[x_feature], rotation=45, ha='right')
                    ax[i].set_xticklabels([])
                if x_feature == 0:
                    ax[i].set_ylabel(column_names[y_feature], rotation=45, ha='right')
                    ax[i].set_yticklabels([])
            else:
                ax[i].set_visible(False)
    
    else:
        if args.colors:
            for house in houses:
                plt.scatter(num_df.loc[num_df["Hogwarts House"] == house, "Defense Against the Dark Arts"], num_df.loc[num_df["Hogwarts House"] == house, "Astronomy"], alpha=0.5, color=color_dict[house], label=house)
        else:
            num_df.plot(kind='scatter', x="Defense Against the Dark Arts", y="Astronomy", alpha=0.1)
    
    plt.show()