'''
Author: Paula Tovar
Title: Standardize Data
Description: Program that standardizes the biomarker columns to be on a similar scale.
Date Created: 06/23/25
Date Last Modified: 06/23/25
'''

import pandas as pd
from sklearn.preprocessing import StandardScaler

# reading in data
data_path = "../dat/imputed.xlsx"
data_df = pd.read_excel(data_path)

# separating numeric columns
info_df = data_df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]]
numeric_df = data_df.drop(data_df.columns[[0, 1, 2, 3, 4, 5, 6, 7]], axis = 1)

# standardize data
scaler = StandardScaler()
transformed = scaler.fit_transform(X = numeric_df.to_numpy())
tdf = pd.DataFrame(transformed, columns = numeric_df.columns)

# make into one dataframe again
standardized_df = pd.concat([info_df, tdf], axis = 1)

# write to excel spreadsheet
standardized_df.to_excel("../dat/standardized.xlsx", index = False)