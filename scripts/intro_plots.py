'''
Author: Paula Tovar
Title: Introductory Plots
Description: Program that makes initial summary plots. Saves plots to a pre-existing folder. 
Date Created: 03/26/25
Date Last Modified: 06/10/25
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# reading in data
data_path = "../dat/connected_spreadsheet_MATRR.xlsx"
data_df = pd.read_excel(data_path)

# name of folder
folder_path = "../plots/initial plots 2"

# functions 
def boxplot(df, x, y, title):
    sns.boxplot(x = df[x],
                y = df[y],
                hue = data_df["Timepoint"],
                hue_order = ["baseline", "open access 1", "open access 2"])
    plt.title(f"{y} by {title}")
    plt.legend(title = "Timepoint")
    plot_path = os.path.join(folder_path, f"{y}_{title}.png")
    plt.savefig(plot_path)
    plt.show()

if __name__ == "__main__":
    # boxplots by drinking category
    boxplot(data_df, "drinking_category", "NA:", "Drinking Category")       # sodium
    boxplot(data_df, "drinking_category", "GLU:", "Drinking Category")      # glucose
    boxplot(data_df, "drinking_category", "CHOL:", "Drinking Category")     # cholesterol
    boxplot(data_df, "drinking_category", "WBC:", "Drinking Category")      # white blood cells
    boxplot(data_df, "drinking_category", "RBC:", "Drinking Category")      # red blood cells
    boxplot(data_df, "drinking_category", "HGB:", "Drinking Category")      # hemoglobin
    boxplot(data_df, "drinking_category", "PLT:", "Drinking Category")      # platelets

    # boxplots by sex
    boxplot(data_df, "sex", "CHOL:", "Sex")                                 # cholesterol
    boxplot(data_df, "sex", "GLU:", "Sex")                                  # glucose
    boxplot(data_df, "sex", "HGB:", "Sex")                                  # hemoglobin
