'''
Author: Paula Tovar
Title: Monkey Biochemistry Spreadsheets
Description: Program that connects biochemistry spreadsheets to ID information.
Date Created: 02/19/25
Date Last Modified: 6/10/25
'''

import pandas as pd

# reading in data
biochem_data_path = "../dat/AllCohorts_Blood_hematology_biochemistry_copy.xlsx"
id_data_path = "../dat/MonkeyDataAcrossCohorts_With_INIA.csv"

biochem_df = pd.read_excel(biochem_data_path)
id_df = pd.read_csv(id_data_path)

# cleaning up columns
biochem_df.drop(labels = ["Unnamed: 44", "Unnamed: 45"], axis = 1, inplace = True)

# removing unnecessary timepoints to remain with "baseline" and "open access 1/2"
timepoints = ["baseline", "open access 1", "open access 2"]
filtered_biochem = biochem_df[biochem_df["Timepoint"].isin(timepoints)]

# adding drinking category as column to filtered_biochem on matching ID
connected_df = pd.merge(filtered_biochem, id_df[["monkey_id", "drinking_category"]],
                        left_on = "MATRR ID", right_on = "monkey_id")

# drop redundant monkey_id column
connected_df.drop(columns = ["monkey_id"], inplace = True)

# adding sex as column to filtered_biochem on matching ID
connected_df = pd.merge(connected_df, id_df[["monkey_id", "sex"]],
                        left_on = "MATRR ID", right_on = "monkey_id")

# drop redundant monkey_id column (again)
connected_df.drop(columns = ["monkey_id"], inplace = True)

# moving drinking_category and sex to a more readable position
col_list = list(connected_df.columns)
col_list.insert(3, col_list.pop(col_list.index("drinking_category")))
col_list.insert(4, col_list.pop(col_list.index("sex")))
connected_df = connected_df[col_list]

# check first row 
print(connected_df.iloc[0])

# making connected dataframe into Excel spreadsheet
connected_df.to_excel('../dat/connected_spreadsheet_MATRR.xlsx', index = False)