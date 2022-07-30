# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:24:09 2022

Accomplishes Task 1 for the CS513 Group Project, which is to transpose the time
columns into rows, and vice versa the rows of statistics into columns.

@author: ochig
"""

# need pandas and numpy for this task
import pandas as pd
import numpy as np
import os

# @BEGIN Task2.2
# @IN filepath @URI file:/OpenRefine/2022-Jul-22/Task2.2_monthly_data_2022Jul22.csv
# @OUT Task2.2_monthly_data_postPandas.csv @URI file:Task2.2_monthly_data_postPandas.csv

# Generic correlation function wrapper
# @BEGIN npy_corrcoef_wrap
# @PARAM x
# @PARAM y
# @RETURN r
def npy_corrcoef_wrap(x,y):
    # x,y are columns of pandas dataframe
    
    # Initialize empty output array for corr coeff R
    R = np.zeros(len(x))
    
    x = x.values
    y = y.values
    
    # Boolean index for if ''
    xBool = (x.astype('object') != '')
    yBool = (y.astype('object') != '')
    
    # Find indices where xBool and yBool are both True
    xyBool = np.zeros(len(x),dtype=bool)
    for ii in range(0,len(x)):
        if xBool[ii] == 1 and yBool[ii] == 1:
            xyBool[ii] = 1
    xyWhere = np.argwhere(xyBool==1)
    
    # Index only the matching not ''
    x = x[xyBool].astype(float)
    y = y[xyBool].astype(float)
    
    # Fill R at specific indices of xyWhere
    x = (x - x.mean()) / x.std()
    y = (y - y.mean()) / y.std()
    R_temp = x/y
    for ii in range(0,len(xyWhere)):
        R[xyWhere[ii]] = R_temp[ii] 
        
    # Make R into df and get change zeros to ''
    R = pd.DataFrame(R)
    R[R.values==0] = ''
    
    return R
# @END correlation_function_wrapper


# Read in the csv
# @BEGIN get_csv_file
# @PARAM filepath
# @OUT df
wFolder = "Data Cleaning Project CS513" # working folder for the project here
filepath = str(os.getcwd()) + '/CS513-Data-Cleaning-Group-Project/OpenRefine/2022-Jul-22/Task2.2-monthly-data-csv.csv'
df = pd.read_csv(filepath)
# @END get_csv_file


# Replace NaNs in certain columns...
# @BEGIN fill_na
# @IN df
# @OUT df_noNA
df = df.fillna('')
df.replace('..', '', inplace=True)
# @END fill_na


# Correlation of GDP to unemployment rate
# @BEGIN GDP_to_unemploymment @DESC Compute normalized GDP / unemployment
# @IN df_noNA
# @OUT df2
df[['GDP to Unemployment Rate Correlaton']] = npy_corrcoef_wrap( df['GDP,current US$,millions,seas. adj.,'],
                                                     df['Unemployment rate,Percent,,,'] )
# @END GDP_to_unemploymment

# Correlation of Retail sales Volume to CPI
# @BEGIN retail_sales_volume_to_CPI @DESC Compute the normalized \n retail sales volume / CPI
# @IN df2
# @OUT df3
df[['Retail Sales Volume to CPI Correlaton']] = npy_corrcoef_wrap( df['Retail Sales Volume,Index,,,'],
                                                     df['CPI Price, % y-o-y, not seas. adj.,,'] )
# @END retail_sales_volume_to_CPI

# Correlation of Stock Market Value to CPI
# @BEGIN stock_market_value_to_CPI @DESC Compute the normalized \n stock markets value / CPI
# @IN df3
# @OUT df_wCorrelations
df[['Stock Market Value to CPI Correlaton']] = npy_corrcoef_wrap( df['Stock Markets, US$, Billions'],
                                                     df['CPI Price, % y-o-y, not seas. adj.,,'] )
# @END stock_market_value_to_CPI
        
        
# Call the permute function on each dataset
#macroecon_qy_df = series_time_permute(macroecon_qy_df)
#macroecon_monthly_df = series_time_permute(macroecon_monthly_df)

# Export the files as csv
# @BEGIN export_as_csv
# @IN df_wCorrelations
# @OUT Task2.2_monthly_data_postPandas.csv
savePath = str(os.getcwd()) + '/CS513-Data-Cleaning-Group-Project/OpenRefine/2022-Jul-22'
df.to_csv(savePath+"/Task2.2_monthly_data_postPandas.csv")
# @END export_as_csv

# @END Task2.2