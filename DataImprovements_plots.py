# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 16:41:52 2022

@author: ochig
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# Load datasets
loadPath = os.path.expanduser('~/Documents/Data Cleaning Project CS513/CS513-Data-Cleaning-Group-Project/Subtasks/Task_3')
qy_df = pd.read_csv(loadPath+"/Task3_quarterly_and_yearly_data.csv")
monthly_df = pd.read_csv(loadPath+"/Task3_monthly_data.csv")

# Fill NA since empty gets loaded as NaN
qy_df = qy_df.fillna('')
monthly_df = monthly_df.fillna('')

# Extract Export-import ratio for a couple countries
US_exportImport = qy_df.loc[qy_df['Country']=="United States",["Time", "Export-Import Ratio, seas. adj."]]
China_exportImport = qy_df.loc[qy_df['Country']=="China",["Time", "Export-Import Ratio, seas. adj."]]
# Drop empty values
US_exportImport = US_exportImport.replace('', np.nan).dropna().reset_index()
China_exportImport = China_exportImport.replace('', np.nan).dropna().reset_index()
# Take just yearly values
US_exportImport = US_exportImport.loc[4::5,:]
China_exportImport = China_exportImport.loc[0::5,:]
# Get rid of extra column for index
US_exportImport = US_exportImport.iloc[:,[1,2]]
China_exportImport = China_exportImport.iloc[:,[1,2]]


# Plot
# plt.figure(figsize=(12,8))
# plt.plot(US_exportImport["Time"], US_exportImport.iloc[:,1], label='US')
# plt.plot(China_exportImport["Time"], China_exportImport.iloc[:,1], label='China')
# plt.legend()
# plt.ylabel('Import-Export Ratio [unitless]')
# plt.xlabel('Year')
# plt.grid()
# plt.show()


# # Extract Export-import ratio for a couple countries
# US_gdpPercent = qy_df.loc[qy_df['Country']=="United States",["Time", "Industrial Production % of GDP"]]
# China_gdpPercent = qy_df.loc[qy_df['Country']=="China",["Time", "Industrial Production % of GDP"]]
# Germany_gdpPercent = qy_df.loc[qy_df['Country']=="Germany",["Time", "Industrial Production % of GDP"]]
# # Drop empty values
# US_gdpPercent = US_gdpPercent.replace('', np.nan).dropna().reset_index()
# China_gdpPercent = China_gdpPercent.replace('', np.nan).dropna().reset_index()
# Germany_gdpPercent = Germany_gdpPercent.replace('', np.nan).dropna().reset_index()
# # Take just yearly values
# #US_gdpPercent = US_gdpPercent.loc[4::5,:]
# #China_gdpPercent = China_gdpPercent.loc[0::5,:]
# # Get rid of extra column for index
# US_gdpPercent = US_gdpPercent.iloc[:,[1,2]]
# China_gdpPercent = China_gdpPercent.iloc[:,[1,2]]
# Germany_gdpPercent = Germany_gdpPercent.iloc[:,[1,2]]

# # Plot
# plt.figure(figsize=(12,8))
# plt.plot(US_gdpPercent["Time"], US_gdpPercent.iloc[:,1], label='US')
# plt.plot(China_gdpPercent["Time"], China_gdpPercent.iloc[:,1], label='China')
# plt.plot(Germany_gdpPercent["Time"], Germany_gdpPercent.iloc[:,1], label='Germany')
# plt.legend()
# plt.ylabel('Industrial Production Percent of GDP')
# plt.xlabel('Year')
# plt.grid()
# plt.show()


# # Extract data ratio for a couple countries
# US_CPI_relations = qy_df.loc[qy_df['Country']=="United States",["Time", "Core CPI / CPI, not seas. adj."]]
# China_CPI_relations = qy_df.loc[qy_df['Country']=="China",["Time","Core CPI / CPI, not seas. adj."]]
# Germany_CPI_relations = qy_df.loc[qy_df['Country']=="Germany",["Time","Core CPI / CPI, not seas. adj."]]
# # Drop empty values
# US_CPI_relations = US_CPI_relations.replace('', np.nan).dropna().reset_index()
# China_CPI_relations = China_CPI_relations.replace('', np.nan).dropna().reset_index()
# Germany_CPI_relations = Germany_CPI_relations.replace('', np.nan).dropna().reset_index()
# # Take just yearly values
# #US_gdpPercent = US_gdpPercent.loc[4::5,:]
# #China_gdpPercent = China_gdpPercent.loc[0::5,:]
# # Get rid of extra column for index
# US_CPI_relations = US_CPI_relations.iloc[:,[1,2]]
# China_CPI_relations = China_CPI_relations.iloc[:,[1,2]]
# Germany_CPI_relations = Germany_CPI_relations.iloc[:,[1,2]]

# # Plot
# plt.figure(figsize=(12,8))
# plt.plot(US_CPI_relations["Time"], US_CPI_relations.iloc[:,1], label='US')
# plt.plot(China_CPI_relations["Time"], China_CPI_relations.iloc[:,1], label='China')
# plt.plot(Germany_CPI_relations["Time"], Germany_CPI_relations.iloc[:,1], label='Germany')
# plt.legend()
# plt.ylabel('CPI / Core CPI, not seas. adj.')
# plt.xlabel('Year')
# plt.grid()
# plt.show()


# # Extract data ratio for a couple countries
# US_CPI = qy_df.loc[qy_df['Country']=="United States",["Time", "CPI Price, % y-o-y, not seas. adj.,,"]]
# China_CPI_relations = qy_df.loc[qy_df['Country']=="China",["Time", "CPI / US CPI"]]
# Germany_CPI_relations = qy_df.loc[qy_df['Country']=="Germany",["Time", "CPI / US CPI"]]
# # Drop empty values
# US_CPI = US_CPI.replace('', np.nan).dropna().reset_index()
# China_CPI_relations = China_CPI_relations.replace('', np.nan).dropna().reset_index()
# Germany_CPI_relations = Germany_CPI_relations.replace('', np.nan).dropna().reset_index()
# # Take just yearly values
# #US_gdpPercent = US_gdpPercent.loc[4::5,:]
# #China_gdpPercent = China_gdpPercent.loc[0::5,:]
# # Get rid of extra column for index
# US_CPI = US_CPI.iloc[:,[1,2]]
# China_CPI_relations = China_CPI_relations.iloc[:,[1,2]]
# Germany_CPI_relations = Germany_CPI_relations.iloc[:,[1,2]]

# # Plot
# plt.figure(figsize=(12,8))
# plt.plot()
# plt.plot(US_CPI["Time"], US_CPI.iloc[:,1],'--', label='United States (CPI %y-o-y)')
# plt.plot(China_CPI_relations["Time"], China_CPI_relations.iloc[:,1], label='China')
# plt.plot(Germany_CPI_relations["Time"], Germany_CPI_relations.iloc[:,1], label='Germany')
# plt.legend()
# plt.ylabel('CPI / US CPI')
# plt.xlabel('Year')
# plt.grid()
# plt.show()


# # Extract data for a couple countries
# US = qy_df.loc[qy_df['Country']=="United States",["Time", "GDP to Unemployment Rate Correlaton"]]
# France = qy_df.loc[qy_df['Country']=="France",["Time","GDP to Unemployment Rate Correlaton"]]
# Germany = qy_df.loc[qy_df['Country']=="Germany",["Time","GDP to Unemployment Rate Correlaton"]]
# # Drop empty values
# US = US.replace('', np.nan).dropna().reset_index()
# France = France.replace('', np.nan).dropna().reset_index()
# Germany = Germany.replace('', np.nan).dropna().reset_index()
# # Take just yearly values
# #US_gdpPercent = US_gdpPercent.loc[4::5,:]
# #China_gdpPercent = China_gdpPercent.loc[0::5,:]
# # Get rid of extra column for index
# US = US.iloc[:,[1,2]]
# France = France.iloc[:,[1,2]]
# Germany = Germany.iloc[:,[1,2]]

# # Plot
# plt.figure(figsize=(12,8))
# plt.plot(US["Time"], US.iloc[:,1], label='US')
# plt.plot(France["Time"], France.iloc[:,1], label='France')
# plt.plot(Germany["Time"], Germany.iloc[:,1], label='Germany')
# plt.legend()
# plt.ylabel('GDP to Unemployment Rate [normalized quantities]')
# plt.xlabel('Year')
# plt.grid()
# plt.show()


# # Extract data for a couple countries
# US = qy_df.loc[qy_df['Country']=="United States",["Time", "Retail Sales Volume to CPI Correlaton"]]
# France = qy_df.loc[qy_df['Country']=="France",["Time","Retail Sales Volume to CPI Correlaton"]]
# Germany = qy_df.loc[qy_df['Country']=="Germany",["Time","Retail Sales Volume to CPI Correlaton"]]
# # Drop empty values
# US = US.replace('', np.nan).dropna().reset_index()
# France = France.replace('', np.nan).dropna().reset_index()
# Germany = Germany.replace('', np.nan).dropna().reset_index()
# # Take just yearly values
# #US_gdpPercent = US_gdpPercent.loc[4::5,:]
# #China_gdpPercent = China_gdpPercent.loc[0::5,:]
# # Get rid of extra column for index
# US = US.iloc[:,[1,2]]
# France = France.iloc[:,[1,2]]
# Germany = Germany.iloc[:,[1,2]]

# # Plot
# plt.figure(figsize=(12,8))
# plt.plot(US["Time"], US.iloc[:,1], label='US')
# plt.plot(France["Time"], France.iloc[:,1], label='France')
# plt.plot(Germany["Time"], Germany.iloc[:,1], label='Germany')
# plt.legend()
# plt.ylabel('Retail Sales Volume / CPI [normalized quantities]')
# plt.xlabel('Year')
# plt.grid()
# plt.show()

# Extract data for a couple countries
US = qy_df.loc[qy_df['Country']=="United States",["Time", "Import-Export Ratio, seas. adj."]]
China = qy_df.loc[qy_df['Country']=="China",["Time","Export-Import Ratio / US Import-Export Ratio"]]
# Drop empty values
US = US.replace('', np.nan).dropna().reset_index()
China = China.replace('', np.nan).dropna().reset_index()
# Take just yearly values
US = US.loc[4::5,:]
China = China.loc[0::5,:]
# Get rid of extra column for index
US = US.iloc[:,[1,2]]
US = US.iloc[:-1,]
China = China.iloc[:,[1,2]]
China = China.iloc[:-1,]

# Plot
plt.figure(figsize=(12,8))
plt.plot(US["Time"], US.iloc[:,1]*10.0, '--', label='US')
plt.plot(China["Time"], China.iloc[:,1], label='China', color='r')
plt.legend()
plt.ylabel('Export-Import Ratio / US Import-Export Ratio [unitless]')
plt.xticks(rotation=45)
plt.xlabel('Year')
plt.grid()
plt.show()