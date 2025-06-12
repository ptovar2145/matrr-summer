'''
Author: Paula Tovar
Title: Introductory Plots
Description: Program that makes initial summary plots.
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

# summary data
category_counts = data_df.groupby("drinking_category").size()
print(category_counts, "\n")

species_counts = data_df.groupby("Species").size()
print(species_counts, "\n")

sex_counts = data_df.groupby("sex").size()
print(sex_counts, "\n")

# name of folder
folder_path = "../plots/initial plots 2"

# box plots are plotted by drinking category and timepoint
# sodium
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["NA:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("Sodium (mmol/L) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "sodium_drinking_category.png")
plt.savefig(plot_path)
plt.show()

# glucose
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["GLU:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("Glucose (mg/dL) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "glucose_drinking_category.png")
plt.savefig(plot_path)
plt.show()

# cholesterol
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["CHOL:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("Cholesterol (mg/dL) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "cholesterol_drinking_category.png")
plt.savefig(plot_path)
plt.show()

# white blood cells
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["WBC:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("White Blood Cell Count by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "white_bc_drinking_category.png")
plt.savefig(plot_path)
plt.show()

# red blood cells
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["RBC:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("RBC (10^6/uL) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "red_bc_drinking_category.png")
plt.savefig(plot_path)
plt.show()

# hemoglobin
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["HGB:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("Hemoglobin (g/dL) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "hemoglobin_drinking_category.png")
plt.savefig(plot_path)
plt.show()

# platelets
sns.boxplot(x = data_df["drinking_category"],
            y = data_df["PLT:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("Platelets (10^3/uL) by Drinking Category")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "platelets_drinking_category.png")
plt.savefig(plot_path)
plt.show()

# box plots are plotted by sex and timepoint (biomarkers with a lot of variation)
# cholesterol
sns.boxplot(x = data_df["sex"],
            y = data_df["CHOL:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("CHOL (mg/dL) by Sex")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "cholesterol_sex.png")
plt.savefig(plot_path)
plt.show()

# glucose
sns.boxplot(x = data_df["sex"],
            y = data_df["GLU:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("Glucose (mg/dL) by Sex")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "glucose_sex.png")
plt.savefig(plot_path)
plt.show()

# hemoglobin
sns.boxplot(x = data_df["sex"],
            y = data_df["HGB:"],
            hue = data_df["Timepoint"],
            hue_order = ["baseline", "open access 1", "open access 2"])
plt.title("Hemoglobin (g/dL) by Sex")
plt.legend(title = "Timepoint")
plot_path = os.path.join(folder_path, "hemoglobin_sex.png")
plt.savefig(plot_path)
plt.show()