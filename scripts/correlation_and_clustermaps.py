'''
Author: Paula Tovar
Title: Correlation Matrices and Clustermaps
Description: Program that makes correlation matrices and clustermaps for each species. Each plot is only for specific timepoints.
Date Created: 06/11/25
Date Last Modified: 06/16/25
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# read in data
data_path = "../dat/imputed.xlsx"
data_df = pd.read_excel(data_path)
columns_to_drop = [0 1, 2, 3, 4, 5, 6, 7]

# cynomolgus macaques
cyno_df = data_df[data_df["Species"] == "cyno"]

cyno_df_base_open1 = cyno_df[cyno_df["Timepoint"].isin(["baseline", "open access 1"])]
cyno_df_open1_open2 = cyno_df[cyno_df["Timepoint"].isin(["open access 1", "open access 2"])]
cyno_df_base_open2 = cyno_df[cyno_df["Timepoint"].isin(["baseline", "open access 2"])]

cyno_dataframes = [cyno_df_base_open1, cyno_df_open1_open2, cyno_df_base_open2]
cyno_matrices = []
cyno_cluster_maps = []

for df in cyno_dataframes:
    numeric_df = df.drop(data_df.columns[columns_to_drop], axis = 1)
    matrix = numeric_df.corr(method = "pearson",
                     min_periods = 1)
    cyno_matrices.append(matrix)

    cluster_map = sns.clustermap(numeric_df, cmap = "coolwarm")
    cyno_cluster_maps.append(cluster_map)
    plt.close(cluster_map.fig)

# rhesus macaques
rhesus_df = data_df[data_df["Species"] == "rhesus"]

rhesus_df_base_open1 = rhesus_df[rhesus_df["Timepoint"].isin(["baseline", "open access 1"])]
rhesus_df_open1_open2 = rhesus_df[rhesus_df["Timepoint"].isin(["open access 1", "open access 2"])]
rhesus_df_base_open2 = rhesus_df[rhesus_df["Timepoint"].isin(["baseline", "open access 2"])]

rhesus_dataframes = [rhesus_df_base_open1, rhesus_df_open1_open2, rhesus_df_base_open2]
rhesus_matrices = []
rhesus_cluster_maps = []

for df in rhesus_dataframes:
    numeric_df = df.drop(data_df.columns[columns_to_drop], axis = 1)
    matrix = numeric_df.corr(method = "pearson",
                     min_periods = 1)
    rhesus_matrices.append(matrix)

    cluster_map = sns.clustermap(numeric_df, cmap = "coolwarm")
    rhesus_cluster_maps.append(cluster_map)
    plt.close(cluster_map.fig)

# visualization
folder_path = "../plots/correlation matrices 3/"
timepoint_pairs = [["baseline", "open access 1"], ["open access 1", "open access 2"], ["baseline", "open access 2"]]

for i in range(len(cyno_matrices)):
    sns.heatmap(cyno_matrices[i],
                annot = False,
                cmap = "coolwarm",
                cbar = True,
                linewidths = 0.5,
                xticklabels = True,
                yticklabels = True)
    plt.title(f"Cynomolgus Macaques from {timepoint_pairs[i][0]} to {timepoint_pairs[i][1]}")
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plot_path = os.path.join(folder_path, f"cyno_matrix{i}.png")
    plt.savefig(plot_path)
    plt.show()

for i in range(len(cyno_cluster_maps)):
    cyno_cluster_maps[i].fig.suptitle(f"Cynomolgus Macaques from {timepoint_pairs[i][0]} to {timepoint_pairs[i][1]}",
                                      y = 0.995)
    plot_path = os.path.join(folder_path, f"cyno_cluster_map{i}.png")
    cyno_cluster_maps[i].fig.savefig(plot_path)
    cyno_cluster_maps[i].fig.show()

for i in range(len(rhesus_matrices)):
    sns.heatmap(rhesus_matrices[i],
                annot = False,
                cmap = "coolwarm",
                cbar = True,
                linewidths = 0.5,
                xticklabels = True,
                yticklabels = True)
    plt.title(f"Rhesus Macaques from {timepoint_pairs[i][0]} to {timepoint_pairs[i][1]}")
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plot_path = os.path.join(folder_path, f"rhesus_matrix{i}.png")
    plt.savefig(plot_path)
    plt.show()

for i in range(len(rhesus_cluster_maps)):
    rhesus_cluster_maps[i].fig.suptitle(f"Rhesus Macaques from {timepoint_pairs[i][0]} to {timepoint_pairs[i][1]}",
                                        y = 0.995)
    plot_path = os.path.join(folder_path, f"rhesus_cluster_map{i}.png")
    rhesus_cluster_maps[i].fig.savefig(plot_path)
    rhesus_cluster_maps[i].fig.show()
