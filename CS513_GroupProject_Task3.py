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
    field =  'Stock Markets, US$, Billions'

    index = 0
    for i in range(0, len(df)-10):   
        if i > 0 and ((i + 1) % 10) == 0:
            index = i+10
        US_stockMarket_thisYear = df.loc[index, field]

        if isinstance(US_stockMarket_thisYear, str) or isinstance(df.loc[i,field],str):
            df.loc[i,'US Stock Market to Stock Market'] = ''
        else:
            df.loc[i,'US Stock Market to Stock Market'] = df.loc[i,field] / US_stockMarket_thisYear
        
    df = df.fillna('')
    return df

stock_market_Jul16 = getStockMarketTotal(stock_market_Jul16)
stock_market_Jul22 = getStockMarketTotal(stock_market_Jul22)

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

stock_market_Jul16 = getImportExportRelations(stock_market_Jul16)
stock_market_Jul22 = getImportExportRelations(stock_market_Jul22)

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

stock_market_Jul16 = getUSAUnemploymentRate(stock_market_Jul16)
stock_market_Jul22 = getUSAUnemploymentRate(stock_market_Jul22)

print(stock_market_Jul22)