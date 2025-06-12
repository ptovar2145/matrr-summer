'''
Author: Paula Tovar
Title: Introductory Plots for Significant Biomarkers
Description: Program that makes plots of significant biomarkers.
Date Created: 06/10/25
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
folder_path = "../plots/initial plots 3"

# box plots are plotted by drinking category and timepoint
# mean corpuscular hemoglobin
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["MCH:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("MCH (picograms) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "mch.png")
plt.savefig(plot_path)
plt.show()

# triglycerides
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["TRIG:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("Triglycerides (mg/dL) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "triglycerides.png")
plt.savefig(plot_path)
plt.show()

# mean corpuscular volume
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["MCV:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("MCV (fL) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "mcv.png")
plt.savefig(plot_path)
plt.show()

# blood urea nitrogen
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["BUN:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("BUN (mg/dL) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "bun.png")
plt.savefig(plot_path)
plt.show()

# aspartate transaminase
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["AST:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("AST (IU/L) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "ast.png")
plt.savefig(plot_path)
plt.show()

# red blood cells
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["RBC:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("Red Blood Cells (10^6/uL) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "rbc.png")
plt.savefig(plot_path)
plt.show()
