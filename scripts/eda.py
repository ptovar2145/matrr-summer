'''
Author: Paula Tovar
Title: Exploratory Data Analysis
Description: Program that computes summary data.
Date Created: 06/16/25
Date Last Modified: 06/16/25
'''

import pandas as pd

# read in data
data_path = "../dat/connected_spreadsheet_MATRR.xlsx"
data_df = pd.read_excel(data_path)

# summary data
print(f"Number of rows: {data_df.shape[0]}")
print(f"Number of columns: {data_df.shape[1]}")
print()

category_counts = data_df.groupby("drinking_category").size()
print(category_counts)
print()

species_counts = data_df.groupby("Species").size()
print(species_counts)
print()

sex_counts = data_df.groupby("sex").size()
print(sex_counts)
print()

# proportion of NAs per column
print("Proportion of NAs per column for all monkeys:")
for col in data_df.columns:
    num_na = data_df[col].isnull().sum()
    proportion = (num_na / data_df.shape[0]) * 100
    print(f"{col} {proportion:.2f}%")
print()

print("Proportion of NAs per column for cyno monkeys:")
cyno_df = data_df[data_df["Species"] == "cyno"]
for col in cyno_df.columns:
    num_na = cyno_df[col].isnull().sum()
    proportion = (num_na / cyno_df.shape[0]) * 100
    print(f"{col} {proportion:.2f}%")
print()

print("Proportion of NAs per column for rhesus monkeys:")
rhesus_df = data_df[data_df["Species"] == "rhesus"]
for col in rhesus_df.columns:
    num_na = rhesus_df[col].isnull().sum()
    proportion = (num_na / rhesus_df.shape[0]) * 100
    print(f"{col} {proportion:.2f}%")

