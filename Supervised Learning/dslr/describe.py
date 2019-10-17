import argparse
import os
import pandas as pd
import math
import numpy as np

def ft_sum(lst):
    somme = 0
    for x in lst:
        somme += x
    return somme

def ft_variance(lst, mean, count):
        sum_averagedeviation = 0
        for x in lst:
            sum_averagedeviation += (x - mean)**2
        return (sum_averagedeviation / (count - 1))

def ft_minmax(lst):
    return lst[0], lst[-1]

def ft_quantile(lst, percent, count):
    pos = (count - 1) * percent
    p = int(pos)
    frac = pos - p
    return (lst[p] + (lst[p + 1] - lst[p]) * frac)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="display information about all numeric features in the dataset")
    parser.add_argument("dataset", metavar="dataset", action="store", help="Path of the dataset you want to get information in")
    args = parser.parse_args()

    if not os.path.isfile(args.dataset):
        print("Invalid file")
        exit(1)
    
    df = pd.read_csv(args.dataset, header=0, index_col=0)
    num_df = df.select_dtypes(include="number")

    column_names = num_df.columns.tolist()
    describe_df = pd.DataFrame(index=["count","mean","std","min","25%","50%","75%","max"], columns=column_names,dtype=float)

    for name in column_names:
        feature_df = num_df[name].dropna()
        feature_list = sorted(feature_df.tolist())
        feature_count = len(feature_list)
        describe_df[name]["count"] = feature_count
        
        feature_sum = ft_sum(feature_list)
        feature_mean = feature_sum / feature_count
        describe_df[name]["mean"] = feature_mean

        feature_variance = ft_variance(feature_list, feature_mean, feature_count)
        feature_std = math.sqrt(feature_variance)
        describe_df[name]["std"] = feature_std

        feature_min, feature_max = ft_minmax(feature_list)
        describe_df[name]["min"] = feature_min
        describe_df[name]["max"] = feature_max

        describe_df[name]["25%"] = ft_quantile(feature_list, 0.25, feature_count)
        describe_df[name]["50%"] = ft_quantile(feature_list, 0.50, feature_count)
        describe_df[name]["75%"] = ft_quantile(feature_list, 0.75, feature_count)
        

    print(describe_df)