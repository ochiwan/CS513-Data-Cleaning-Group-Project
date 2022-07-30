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
plt.figure(figsize=(12,8))
plt.plot(US_exportImport["Time"], US_exportImport.iloc[:,1], label='US')
plt.plot(China_exportImport["Time"], China_exportImport.iloc[:,1], label='China')
plt.legend()
plt.ylabel('Import-Export Ratio [unitless]')
#plt.grid()
plt.show()
