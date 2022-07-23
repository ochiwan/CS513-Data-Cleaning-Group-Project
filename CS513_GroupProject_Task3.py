# -*- coding: utf-8 -*-
"""
Created on 

Accomplishes Task 3 for the CS513 Group Project

@author: shassan
"""

# need pandas and numpy for this task
import pandas as pd
import numpy as np
import os
print(pd.__version__)
dir = str(os.getcwd())

# Read in the csv
username = "shassan"                      # your username here (windows)
wFolder = "Data Cleaning Project CS513" # working folder for the project here
filepath_Jul16 = dir + '/OpenRefine/2022-Jul-16/Task2.1_quarterly_and_yearly_data_postPandas.csv'
filepath_Jul22 = dir + '/OpenRefine/2022-Jul-22/Task2.2_monthly_data_postPandas.csv'

df_Jul16 = pd.read_csv(filepath_Jul16)
df_Jul22 = pd.read_csv(filepath_Jul22)

df_Jul16 = df_Jul16.fillna('')
df_Jul22 = df_Jul22.fillna('')

stock_market_Jul16 = df_Jul16
stock_market_Jul22 = df_Jul22

def getStockMarketTotal(df):
    US_stockMarket_thisYear = 0
    index = 0
    for i in range(0, len(df)-10):   
        if i > 0 and ((i + 1) % 10) == 0:
            index = i+10
        US_stockMarket_thisYear = df.loc[index, 'Stock Markets, US$, Billions']

        if isinstance(US_stockMarket_thisYear, str) or isinstance(df.loc[i,'Stock Markets, US$, Billions'],str):
            df.loc[i,'US Stock Market to Stock Market'] = ''
        else:
            df.loc[i,'US Stock Market to Stock Market'] = US_stockMarket_thisYear / df.loc[i,'Stock Markets, US$, Billions']
        
    df = df.fillna('')
    return df

stock_market_Jul16 = getStockMarketTotal(stock_market_Jul16)
stock_market_Jul22 = getStockMarketTotal(stock_market_Jul22)

def getImportExportRelations(df):
    US_importExport_thisYear = 0
    US_exportImport_thisYear = 0

    importExport = 'Import-Export Ratio, seas. adj.'
    exportImport = 'Export-Import Ratio, seas. adj.'
    
    index = 0
    for i in range(0, len(df)-10):   
        if i > 0 and ((i + 1) % 10) == 0:
            index = i + 10
        US_importExport_thisYear = df.loc[index, importExport]
        US_exportImport_thisYear = df.loc[index, exportImport]

        if isinstance(US_importExport_thisYear, str) or isinstance(df.loc[i, importExport],str):
            df.loc[i,'Import/Export'] = ''
        else:
            df.loc[i,'Import/Export'] = US_importExport_thisYear / df.loc[i, exportImport]
            df.loc[i,'Export/Import'] = US_exportImport_thisYear / df.loc[i, importExport]
        
    df = df.fillna('')
    return df

stock_market_Jul16 = getImportExportRelations(stock_market_Jul16)
stock_market_Jul22 = getImportExportRelations(stock_market_Jul22)

print(stock_market_Jul16)

# 13

# 14