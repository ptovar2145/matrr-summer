'''
Author: Paula Tovar
Title: Introductory Plots
Description: Program that makes initial summary plots. Saves plots to a pre-existing folder. 
Date Created: 03/26/25
Date Last Modified: 07/02/25
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# functions 
def boxplot(df, x, y, title, folder):
    sns.boxplot(x = df[x],
                y = df[y],
                hue = data_df["Timepoint"],
                hue_order = ["baseline", "open access 1", "open access 2"])
    plt.title(f"{y} by {title}")
    plt.legend(title = "Timepoint")
    plot_path = os.path.join(folder, f"{y}_{title}.png")
    plt.savefig(plot_path)
    plt.show()

if __name__ == "__main__":
    # reading in data
    data_path = "../dat/connected_spreadsheet_MATRR.xlsx"
    data_df = pd.read_excel(data_path)

    # name of folder
    folder_path = "../plots/initial plots 2"
    
    # boxplots by drinking category
    boxplot(data_df, "drinking_category", "NA:", "Drinking Category", folder_path)       # sodium
    boxplot(data_df, "drinking_category", "GLU:", "Drinking Category", folder_path)      # glucose
    boxplot(data_df, "drinking_category", "CHOL:", "Drinking Category", folder_path)     # cholesterol
    boxplot(data_df, "drinking_category", "WBC:", "Drinking Category", folder_path)      # white blood cells
    boxplot(data_df, "drinking_category", "RBC:", "Drinking Category", folder_path)      # red blood cells
    boxplot(data_df, "drinking_category", "HGB:", "Drinking Category", folder_path)      # hemoglobin
    boxplot(data_df, "drinking_category", "PLT:", "Drinking Category", folder_path)      # platelets

    # boxplots by sex
    boxplot(data_df, "sex", "CHOL:", "Sex", folder_path)                                 # cholesterol
    boxplot(data_df, "sex", "GLU:", "Sex", folder_path)                                  # glucose
    boxplot(data_df, "sex", "HGB:", "Sex", folder_path)                                  # hemoglobin
