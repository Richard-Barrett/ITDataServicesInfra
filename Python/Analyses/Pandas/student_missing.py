#!/bin/python
# ===========================================================
# Created By: Richard Barrett
# Organization: DVISD
# DepartmenT: Data Services
# Purpose: Test Score & 3rd Party Website Data Pull Automation
# Date: 02/12/2020
# ===========================================================

import pandas as pd

df1 = pd.read_excel('C:\Users\richard.barrett\Documents\Projects\Automation\Find Missing EOC Student Data\EOCTestTrackerReport (2).xls')
df2 = pd.read_excel('C:\Users\richard.barrett\Documents\Projects\Automation\Find Missing EOC Student Data\SKR3437679V0A1Y4N1321699.xlsx')

difference = df1[df1!=df2]
print difference
