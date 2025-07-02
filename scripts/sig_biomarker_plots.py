'''
Author: Paula Tovar
Title: Introductory Plots for Significant Biomarkers
Description: Program that makes plots of significant biomarkers. Saves plots to a pre-existing folder. 
Date Created: 06/10/25
Date Last Modified: 07/02/25
'''

import pandas as pd
from intro_plots import boxplot

if __name__ == '__main__':
    data_path = "../dat/connected_spreadsheet_MATRR.xlsx"
    data_df = pd.read_excel(data_path)

    # name of folder
    folder_path = "../plots/significant biomarker plots/"

    # box plots are plotted by drinking category and timepoint
    boxplot(data_df, "drinking_category", "MCH:", "Drinking Category", folder_path)  # mean corpuscular hemoglobin
    boxplot(data_df, "drinking_category", "TRIG:", "Drinking Category", folder_path)  # triglycerides
    boxplot(data_df, "drinking_category", "MCV:", "Drinking Category", folder_path)  # mean corpuscular volume
    boxplot(data_df, "drinking_category", "BUN:", "Drinking Category", folder_path)  # blood urea nitrogen
    boxplot(data_df, "drinking_category", "AST:", "Drinking Category", folder_path)  # aspartate transaminase
    boxplot(data_df, "drinking_category", "RBC:", "Drinking Category", folder_path)  # red blood cells
