#!/bin/python 
# ===========================================================
# Created By: Richard Barrett
# Organization: DVISD
# DepartmenT: Data Services
# Purpose: Dynamic Excel Diff Comparison Report
# Date: 02/28/2020
# ===========================================================

import getpass
import json
import logging
import numpy as np 
import os 
import pandas as pd
import platform  
import shutil 
import subprocess
import threading
import time
import unittest
import xlsxwriter
from datetime import date

# System Variables
today = date.today()
date = today.strftime("%m/%d/%Y")
node = platform.node()
system = platform.system()
username = getpass.getuser()
version = platform.version()
working_directory = os.getcwd()

# File Variables on Relative Path within CWD
file_1 = "ExportPOSStudents.xlsx"
file_2 = "ExportNutrikidsSkywardCompare.xlsx"

# Column Variables to Compare
e_code = "Eligibility Code"
e_date = "Effective Date"
f_name = "First Name"
l_name = "Last Name"

# Logging Variables 

# Ensure that the Files Exist
if os.path.exists(file_1) and os.path.exists(file_2):
    print("The Files Exist.")
else:
    print("One of the files might not exist.")

# Create Dataframes
df1 = pd.read_excel(file_1)
df2 = pd.read_excel(file_2)

print(df1)
print(df2)

# Check to See if Files are Same Size
df1.equals(df2)
if print(df1.equals(df2)) is False:
    print("Dataframes are not the same size.")
else:
    print("Dataframes are the same size.")

df1[e_date].equals(df2[e_date])
if print(df1[e_date].equals(df2[e_date])) is False:
    print("The Entries are not the same within column for e_date.")
else:
    print("The Entries are the same within the columns for e_date.")

#comparison_values = df1.values == df2.values
#print(comparison_values)
#if df2.equals(df1) == False:
#    print("Datframes are not of the the same size.")
#else df2.equals(df1) == True: 
#    print("Dataframes are of the same size.")

# If Files are Not Same Size Check Indexes and Column Names and Format

# Check Indexes and Size 

# Compare Dataframe Values
#if comparison_values = df1.values == df2.values
#    print(comparison_values)
#else:
#    print("Cannot compare Dataframes.")

# Get-Index of Cell with Parameter == False
#rows,cols=np.where(comparison_values==False)

# Iterate over Cells and Update (df1) value to display changed value in second dataframe (df2)
#for item in zip(rows,cols):
#    df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.i

# Export to Excel after df1(Old Value) --> df2(New Value)
#df1.to_excel('./excel_diff.xlsx',index=False,header=True)

