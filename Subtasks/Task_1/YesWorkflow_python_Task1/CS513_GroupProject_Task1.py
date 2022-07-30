
# need pandas and numpy for this task
import pandas as pd
import numpy as np
import os

# Make a function for permuting the axes so time is the row and statistics
# are listed across the columns of the row
def series_time_permute(df):
    
    # Get list of time values
    times = df.columns[2:]
    
    # Get list of countries in order found in Country column
    countries = np.unique(df["Country"].values)
    
    # List of statistic names found in series column
    stats = df.loc[0:30,"Series"].values
    
    # Initialize an empty dataframe with series as the column names
    colNames = np.r_[["Time","Country"], stats]
    df_perm = pd.DataFrame(columns=colNames)
    
    # For each time step, and each country, list all stats
    # [time, country, stat1:statN]
    for time in times:
        for country in countries:
        
            # Two boolean indexes to match country and the time, return pd array
            cIndex = df.columns == time
            new_row = df.loc[df["Country"]==country, cIndex].T
            
            # Tack country on
            new_row.loc[time,"Country"] = country
            
            # Shuffle the columns so country is first
            cols = new_row.columns.tolist()
            cols = cols[-1:] + cols[:-1]
            new_row = new_row[cols]
            
            # Make the time index a column
            #new_row.loc[time,"Time"] = time
            new_row = new_row.reset_index()
            
            # Rename columns to match above
            new_row.columns = colNames
            
            # Place in primary df
            df_perm = pd.concat([df_perm, new_row])
    
    return df_perm

# @BEGIN CS513_GroupProject_Task1
# @IN filepath @URI file:Economic_Indicators_2022_25Years.csv
# @OUT macroecon_qy_df.csv @URI file:Task1_quarterly_and_yearly_data.csv
# @OUT macroecon_monthly_df.csv @URI file:Task1_monthly_data.csv

# Read in the csv
# @BEGIN get_csv_file
# @PARAM username
# @PARAM wFolder
# @PARAM filepath
# @OUT macroecon_df
username = "ochig"                      # your username here (windows)
wFolder = "Data Cleaning Project CS513" # working folder for the project here
filepath = os.path.expanduser("~"+username+"/documents/"+wFolder+"/Economic_Indicators_2022_25Years.csv")
macroecon_df = pd.read_csv(filepath)
# @END get_csv_file


# @BEGIN drop_columns_and_NA
# @IN macroecon_df
# @OUT macroecon_df2
# Country code and series code are unecessary, drop them
macroecon_df = macroecon_df.drop(columns=["Country Code","Series Code"])
# Drop rows with nans (bottom of df)
macroecon_df = macroecon_df.dropna(axis=0)
# @END drop_columns_and_NA

# @BEGIN split_monthly_quarterly_yearly
# @IN macroecon_df2
# @OUT macroecon_qy_df
# @OUT macroecon_monthly_df
# Split the datasets into quarterly and yearly statistics, and monthly statistics
is_monthly = ["M" in s for s in macroecon_df.columns]   # identify columns that have an M
is_qy = [not x for x in is_monthly.copy()]              # is quarterly/yearly is opposite        
is_monthly[0:1+1] = [True, True]    # Reset Country and Series to keep them
is_qy[0:1+1] = [True, True]         # " "
# Now use the boolean indices to split
macroecon_qy_df = macroecon_df.loc[:,is_qy].copy()
macroecon_monthly_df = macroecon_df.loc[:,is_monthly].copy()
# @END split_quarterly_yearly
   
        
# Call the permute function on each dataset
# @BEGIN quarterly_series_time_permute
# @IN macroecon_qy_df
# @OUT macroecon_qy_df_permuted
macroecon_qy_df = series_time_permute(macroecon_qy_df)
# @END quarterly_series_time_permute

# @BEGIN monthly_series_time_permute
# @IN macroecon_monthly_df
# @OUT macroecon_monthly_df_permuted
macroecon_monthly_df = series_time_permute(macroecon_monthly_df)
# @END monthly_series_time_permute


# Export the files as csv
# @BEGIN export_as_csv
# @IN macroecon_qy_df_permuted
# @IN macroecon_monthly_df_permuted
# @OUT macroecon_qy_df.csv
# @OUT macroecon_monthly_df.csv
savePath = 'C:/Users/ochig/documents/Data Cleaning Project CS513/CS513-Data-Cleaning-Group-Project'
macroecon_qy_df.to_csv(savePath+"/Task1_quarterly_and_yearly_data.csv")
macroecon_monthly_df.to_csv(savePath+"/Task1_monthly_data.csv")
# @END export_as_csv

# @END CS513_GroupProject_Task1

    