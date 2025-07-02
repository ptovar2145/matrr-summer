'''
Author: Paula Tovar
Title: Exploratory Data Analysis
Description: Program that computes summary data.
Date Created: 06/16/25
Date Last Modified: 07/01/25
'''

import pandas as pd

# functions 
def counts(df, column):
    return df.groupby(column).size()

def missing_proportion(df):
    for col in df.columns:
        num_na = df[col].isnull().sum()
        proportion = (num_na / df.shape[0]) * 100
        print(f"{col} {proportion:.2f}%")
    return 

if __name__ == "__main__":
    # read in data
    data_path = "../dat/connected_spreadsheet_MATRR.xlsx"
    data_df = pd.read_excel(data_path)

    # summary data
    print(f"Number of rows: {data_df.shape[0]}")
    print(f"Number of columns: {data_df.shape[1]}")
    print()

    print(counts(data_df, "drinking_category"))
    print()

    print(counts(data_df, "Species"))
    print()

    print(counts(data_df, "sex"))
    print()

    # proportion of NAs per column
    print("Proportion of NAs per column for all monkeys:")
    missing_proportion(data_df)
    print()

    print("Proportion of NAs per column for cyno monkeys:")
    cyno_df = data_df[data_df["Species"] == "cyno"]
    missing_proportion(cyno_df)
    print()

    print("Proportion of NAs per column for rhesus monkeys:")
    rhesus_df = data_df[data_df["Species"] == "rhesus"]
    missing_proportion(rhesus_df)
