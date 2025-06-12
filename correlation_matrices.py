'''
Author: Paula Tovar
Title: Correlation Matrices
Description: Program that makes correlation matrices for each species.
Date Created: 06/11/25
Date Last Modified: 06/11/25
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# read in data
data_path = "../dat/connected_spreadsheet_MATRR.xlsx"
data_df = pd.read_excel(data_path)

# cynomolgus macaques
cyno_df = data_df[data_df["Species"] == "cyno"]
cyno_df = cyno_df.drop("MATRR ID", axis = 1)
cyno_matrix = cyno_df.corr(method = "pearson",
                           min_periods = 1,
                           numeric_only = True)

# rhesus macaques
rhesus_df = data_df[data_df["Species"] == "rhesus"]
rhesus_df = rhesus_df.drop("MATRR ID", axis = 1)
rhesus_matrix = rhesus_df.corr(method = "pearson",
                               min_periods = 1,
                               numeric_only = True)

# visualization
folder_path = "../plots/initial plots 4"

sns.heatmap(cyno_matrix,
            annot = False,
            cbar = True,
            linewidths = 0.5,
            xticklabels = True,
            yticklabels = True)
plt.title("Correlation Matrix for Cynomolgus Macaques")
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plot_path = os.path.join(folder_path, "cyno_matrix.png")
plt.savefig(plot_path)
plt.show()

sns.heatmap(rhesus_matrix,
            annot = False,
            cbar = True,
            linewidths = 0.5,
            xticklabels = True,
            yticklabels = True)
plt.title("Correlation Matrix for Rhesus Macaques")
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plot_path = os.path.join(folder_path, "rhesus_matrix.png")
plt.savefig(plot_path)
plt.show()