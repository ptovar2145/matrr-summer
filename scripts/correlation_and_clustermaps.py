'''
Author: Paula Tovar
Title: Correlation Matrices and Clustermaps
Description: Program that makes correlation matrices and clustermaps for each species. Each plot is only for specific timepoints. Saves plots to a
             pre-existing folder. 
Date Created: 06/11/25
Date Last Modified: 07/02/25
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# functions
def timepoint_df(species_df):
  base_open1 = species_df[species_df["Timepoint"].isin(["baseline", "open access 1"])]
  open1_open2 = species_df[species_df["Timepoint"].isin(["open access 1", "open access 2"])]
  base_open2 = species_df[species_df["Timepoint"].isin(["baseline", "open access 2"])]
  return [base_open1, open1_open2, base_open2]

def make_plots(df_list):
  matrices = []
  clustermaps = []
  for df in df_list:
    numeric_df = df.drop(data_df.columns[columns_to_drop], axis = 1)
    matrix = numeric_df.corr(method = "pearson", 
                             min_periods = 1)
    matrices.append(matrix)
    map = sns.clustermap(numeric_df, cmap = "coolwarm")
    clustermaps.append(map)
    plt.close(map.fig)
  return matrices, clustermaps 

def visual_matrix(matrix_list, species_name):
  for i in range(len(matrix_list)):
    sns.heatmap(matrix_list[i],
                annot = False,
                cmap = "coolwarm",
                cbar = True, 
                linewidths = 0.5, 
                xticklabels = True,
                yticklabels = True)
    plt.title(f"{species_name} from {timepoint_pairs[i][0]} to {timepoint_pairs[i][1]}")
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    plot_path = os.path.join(folder_path, f"{species_name}_matrix{i}.png")
    plt.savefig(plot_path)
    plt.show()

def visual_clustermap(clustermap_list, species_name):
  for i in range(len(clustermap_list)):
    clustermap_list[i].fig.suptitle(f"{species_name} from {timepoint_pairs[i][0]} to {timepoint_pairs[i][1]}",
                                    y = 0.995)
    plot_path = os.path.join(folder_path, f"{species_name}_cluster_map{i}.png")
    clustermap_list[i].fig.savefig(plot_path)
    clustermap_list[i].fig.show()

if __name__ == "__main__":
  # read in data
  data_path = "../dat/standardized.xlsx"
  data_df = pd.read_excel(data_path)
  data_df = data_df.set_index(["MATRR ID", "Timepoint"], drop = False)
  columns_to_drop = [0, 1, 2, 3, 4, 5, 6, 7]
  
  # cynomolgus macaques
  cyno_df = data_df[data_df["Species"] == "cyno"]
  cyno_dataframes = timepoint_df(cyno_df)
  cyno_matrices, cyno_cluster_maps = make_plots(cyno_dataframes)

  # rhesus macaques
  rhesus_df = data_df[data_df["Species"] == "rhesus"]
  rhesus_dataframes = timepoint_df(rhesus_df)
  rhesus_matrices, rhesus_cluster_maps = make_plots(rhesus_dataframes)

  # visualization
  folder_path = "../plots/correlation matrices 5/"
  timepoint_pairs = [["baseline", "open access 1"], ["open access 1", "open access 2"], ["baseline", "open access 2"]]

  visual_matrix(cyno_matrices, "Cynomolgus Macaques")
  visual_clustermap(cyno_cluster_maps, "Cynomolgus Macaques")

  visual_matrix(rhesus_matrices, "Rhesus Macaques")
  visual_clustermap(rhesus_cluster_maps, "Rhesus Macaques")
