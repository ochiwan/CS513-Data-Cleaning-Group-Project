
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

# @BEGIN Task3
# @IN filepath_Task2_1 @URI file:CS513-Data-Cleaning-Group-Project/Subtasks/Task_2/2022-Jul-16/Task2.1_quarterly_and_yearly_data_postPandas.csv
# @IN filepath_Task2_2 @URI file:CS513-Data-Cleaning-Group-Project/Subtasks/Task_2/2022-Jul-22/Task2.2_monthly_data_postPandas.csv
# @OUT Task3_quarterly_and_yearly_data.csv @URI file:Task3_quarterly_and_yearly_data.csv
# @OUT Task3_monthly_data.csv @URI file:Task3_monthly_data.csv

# @BEGIN Read_csv
# @PARAM filepath_Task2_1
# @PARAM filepath_Task2_2
# @OUT df_Jul16
# @OUT df_Jul22
shassan_fp = '/Desktop/projects/'#
ochig_fp = '/Documents/Data Cleaning Project CS513/'#
filepath_Jul16 = os.path.expanduser('~'+ochig_fp+'CS513-Data-Cleaning-Group-Project/Subtasks/Task_2/2022-Jul-16/Task2.1_quarterly_and_yearly_data_postPandas.csv')
filepath_Jul22 = os.path.expanduser('~'+ochig_fp+'CS513-Data-Cleaning-Group-Project/Subtasks/Task_2/2022-Jul-22/Task2.2_monthly_data_postPandas.csv')
# Pandas call to read csv
df_Jul16 = pd.read_csv(filepath_Jul16)
df_Jul22 = pd.read_csv(filepath_Jul22)
# @END Read_csv

# @BEGIN fill_NA
# @IN df_Jul16
# @IN df_Jul22
# @OUT df_Jul16_noNA
# @OUT df_Jul22_noNA
df_Jul16 = df_Jul16.fillna('')#
df_Jul22 = df_Jul22.fillna('')#
# @END fill_NA

# Quarterly/yearly import export relations
# @BEGIN getImportExportRelations_ @ DESC Get quarterly/yearly \n import-export relations \n to U.S.A.
# @IN df_Jul16_noNA
# @OUT df_Jul16_0
df_Jul16 = getImportExportRelations(df_Jul16)
# @END getImportExportRelations_

# Stock Market Total
# @BEGIN stock_market_total_ @DESC Compute stock market total \n relation to U.S.
# @IN df_Jul16_0
# @IN df_Jul22_noNA
# @OUT df_july16_2
# @OUT df_jul22_2
stock_market_Jul16 = getStockMarketTotal(df_Jul16)
stock_market_Jul22 = getStockMarketTotal(df_Jul22)
# @END stock_market_total_

# Import Export Relations
# @BEGIN getUSAUnemploymentRate_ @DESC Compute import export relations
# @IN df_july16_2
# @IN df_jul22_2
# @OUT df_jul16_3
# @OUT df_jul22_3
stock_market_Jul16 = getUSAUnemploymentRate(df_Jul16)
stock_market_Jul22 = getUSAUnemploymentRate(df_Jul22)
# @END getUSAUnemploymentRate_

# Clean up the year label
# @BEGIN Clean_Time_Labels
# @IN df_jul16_3
# @IN df_jul22_3
# @OUT df_jul16_4
# @OUT df_jul22_4
stock_market_Jul16['Time'] = stock_market_Jul16['Time'].str.slice(0,4)
stock_market_Jul22['Time'] = stock_market_Jul22['Time'].str.slice(0,4)
# @END Clean_Time_Labels

# Clean up extra index
# @BEGIN Remove_Extra_Index @DESC Remove extra indices \n generated from Pandas operations
# @IN df_jul16_4
# @IN df_jul22_4
# @OUT df_jul16_5
# @OUT df_jul22_5
stock_market_Jul16 = stock_market_Jul16.iloc[:,1:]
stock_market_Jul22 = stock_market_Jul22.iloc[:,1:]
# @END Remove_Extra_Index

# Export the file as csv
# @BEGIN export_as_csv
# @PARAM savePath
# @IN df_jul16_5
# @IN df_jul22_5
# @OUT Task3_quarterly_and_yearly_data.csv
# @OUT Task3_monthly_data.csv
savePath = os.path.expanduser('~'+ ochig_fp + 'CS513-Data-Cleaning-Group-Project/Subtasks/Task_3')
stock_market_Jul16.to_csv(savePath+"/Task3_quarterly_and_yearly_data.csv")
stock_market_Jul22.to_csv(savePath+"/Task3_monthly_data.csv")
# @END export_as_csv

# @END Task3