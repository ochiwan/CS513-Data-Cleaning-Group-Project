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

dir = str(os.getcwd())

# Read in the csv
#username = "shassan"
#wFolder = "Data Cleaning Project CS513" # working folder for the project here

# @BEGIN Task3
# @IN filepath @URI file:~/Desktop/projects/CS513-Data-Cleaning-Group-Project/Subtasks/Task_2/2022-Jul-22/Task2.2_monthly_data_postPandas.csv#
# @OUT Task3_quarterly_and_yearly_data.csv @URI file:Task3_quarterly_and_yearly_data.csv
filepath_Jul16 = os.path.expanduser('~/Desktop/projects/CS513-Data-Cleaning-Group-Project/Subtasks/Task_2/2022-Jul-16/Task2.1_quarterly_and_yearly_data_postPandas.csv')
filepath_Jul22 = os.path.expanduser('~/Desktop/projects/CS513-Data-Cleaning-Group-Project/Subtasks/Task_2/2022-Jul-22/Task2.2_monthly_data_postPandas.csv')

df_Jul16 = pd.read_csv(filepath_Jul16)
df_Jul22 = pd.read_csv(filepath_Jul22)

df_Jul16 = df_Jul16.fillna('')
df_Jul22 = df_Jul22.fillna('')

stock_market_Jul16 = df_Jul16
stock_market_Jul22 = df_Jul22

# Get stock market total
# @BEGIN getStockMarketTotal
# @PARAM stock_market_df
# @OUT stockMarketTotal
def getStockMarketTotal(stock_market_df):
    US_stockMarket_thisYear = 0
    field =  'Stock Markets, US$, Billions'

    index = 0
    for i in range(0, len(stock_market_df)-10):   
        if i > 0 and ((i + 1) % 10) == 0:
            index = i+10
        US_stockMarket_thisYear = stock_market_df.loc[index, field]

        if isinstance(US_stockMarket_thisYear, str) or isinstance(stock_market_df.loc[i,field],str):
            stock_market_df.loc[i,'US Stock Market to Stock Market'] = ''
        else:
            stock_market_df.loc[i,'US Stock Market to Stock Market'] = stock_market_df.loc[i,field] / US_stockMarket_thisYear
        
    stock_market_df = stock_market_df.fillna('')
    return stock_market_df
# @END getStockMarketTotal

# Read in the csv
# @BEGIN getImportExportRelations
# @PARAM stock_market_df
# @OUT importExportRelations
def getImportExportRelations(df):
    US_importExport_thisYear = 0
    US_exportImport_thisYear = 0
    US_retail_sales = 0
    US_industrialProductionGDP = 0
    US_coreCPI = 0

    importExport = 'Import-Export Ratio, seas. adj.'
    exportImport = 'Export-Import Ratio, seas. adj.'
    retailSales = 'Retail Sales Volume,Index,,,'
    industrialProductionGDP = 'Industrial Production, constant US$,,,'
    coreCPI = 'Core CPI,not seas.adj,,,'
    
    index = 0
    for i in range(0, len(df)-10):   
        if i > 0 and ((i + 1) % 10) == 0:
            index = i + 10
        US_importExport_thisYear = df.loc[index, importExport]
        US_exportImport_thisYear = df.loc[index, exportImport]
        US_retail_sales = df.loc[index, retailSales]
        US_industrialProductionGDP = df.loc[index, industrialProductionGDP]
        US_coreCPI = df.loc[index, coreCPI]
        
        # import/export
        if isinstance(US_importExport_thisYear, str) or isinstance(df.loc[i, importExport],str):
            df.loc[i,'Import/Export'] = ''
        else:
            df.loc[i,'Import/Export'] = df.loc[i, exportImport] / US_importExport_thisYear
            df.loc[i,'Export/Import'] = df.loc[i, importExport] / US_exportImport_thisYear

        # retail sales
        if isinstance(US_retail_sales, str) or isinstance(df.loc[i, retailSales],str):
            df.loc[i,'Retail Sales'] = ''
        else:
            df.loc[i,'Retail Sales'] = df.loc[i, retailSales] / US_retail_sales

        # industrial prod GDP
        if isinstance(US_industrialProductionGDP, str) or isinstance(df.loc[i, industrialProductionGDP],str):
            df.loc[i,'Industrial Production GDP'] = ''
        else: 
            df.loc[i,'Industrial Production GDP'] = df.loc[i, industrialProductionGDP] / US_industrialProductionGDP
        
        # core CPI
        if isinstance(US_coreCPI, str) or isinstance(df.loc[i, coreCPI],str):
            df.loc[i,'Core CPI'] = ''
        else:
            df.loc[i,'Core CPI'] = df.loc[i, coreCPI] / US_coreCPI
            
        
    df = df.fillna('')
    return df
# @END getImportExportRelations

# Correlation of GDP to unemployment rate
# @BEGIN getUSAUnemploymentRate @DESC Get unemployment rate for USA
# @PARAM stock_market_Jul16
# @OUT USAUnemploymentRateJul16
def getUSAUnemploymentRate(df):
    US_unemployment_thisYear = 0
    field =  'Unemployment rate,Percent,,,'

    index = 0
    for i in range(0, len(df)-10):   
        if i > 0 and ((i + 1) % 10) == 0:
            index = i + 10
        US_unemployment_thisYear = df.loc[index, field]

        if isinstance(US_unemployment_thisYear, str) or isinstance(df.loc[i,field],str):
            df.loc[i,'US Unemployment as leading/trailing'] = ''
        else:
            df.loc[i,'US Unemployment as leading/trailing'] = df.loc[i,field] / US_unemployment_thisYear 
        
    df = df.fillna('')
    return df
# @END getUSAUnemploymentRate

# Stock Market Total
# @BEGIN stock_market_total_jul16 @DESC Compute stock market total for July 16
# @IN df_jul16
# @OUT df_jul16_2
stock_market_Jul16 = getStockMarketTotal(stock_market_Jul16)
# @END stock_market_total_jul16

# Stock Market Total
# @BEGIN stock_market_total_jul22 @DESC Compute stock market total for July 22
# @IN df_jul22
# @OUT df_jul22_2
stock_market_Jul22 = getStockMarketTotal(stock_market_Jul22)
# @END stock_market_total_jul22

# Import Export Relations
# @BEGIN import_export_relations_jul16 @DESC Compute import export relations for July 16
# @IN df_jul16_2
# @OUT df_jul16_3
# stock_market_Jul16 = getImportExportRelations(stock_market_Jul16)
# @END import_export_relations_jul16

# Import Export Relations
# @BEGIN import_export_relation_jul22 @DESC Compute import export relations for July 22
# @IN df_jul22_2
# @OUT df_jul22_3
# stock_market_Jul22 = getImportExportRelations(stock_market_Jul22)
# @END import_export_relation_jul22

# Import Export Relations
# @BEGIN USAUnemploymentRate_jul16 @DESC Compute import export relations for July 22
# @IN df_july16_3
# @OUT df_jul16_4
stock_market_Jul16 = getUSAUnemploymentRate(stock_market_Jul16)
# @END USAUnemploymentRate_jul16

# Import Export Relations
# @BEGIN USAUnemploymentRate_jul22 @DESC Compute import export relations for July 22
# @IN df_jul22_3
# @OUT df_jul22_4
stock_market_Jul22 = getUSAUnemploymentRate(stock_market_Jul22)
# @END USAUnemploymentRate_jul22

savePath = os.path.expanduser('~/Desktop/projects/CS513-Data-Cleaning-Group-Project/Subtasks/Task_3')

# Export the file as csv
# @BEGIN export_as_csv
# @IN df1
# @OUT Task3_quarterly_and_yearly_data.csv
stock_market_Jul16.to_csv(savePath+"/Task3_quarterly_and_yearly_data.csv")
# @END export_as_csv

# Export the file as csv
# @BEGIN export_as_csv
# @IN df2
# @OUT Task3_monthly_data.csv
stock_market_Jul22.to_csv(savePath+"/Task3_monthly_data.csv")
# @END export_as_csv

# @END Task3