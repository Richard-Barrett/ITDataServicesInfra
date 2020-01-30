#!/bin/python
# ===========================================================
# Created By: Richard Barrett
# Organization: DVISD
# DepartmenT: Data Services
# Purpose: Test Score & 3rd Party Website Data Pull Automation
# Date: 01/20/2020
# ===========================================================

import selenium
import shutil
import xlsxwriter
import os
import unittest
import requests
import getpass
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from datetime import date

import json
with open('secrets.json','r') as f:
      config = json.load(f)

# Definitions
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# System Variables
today = date.today()
date = today.strftime("%m/%d/%Y")
username = getpass.getuser()

# URL Variables 
login_url = 'https://www.accuplacer.org/'
redirect_url = 'https://www.accuplacer.org/api/home.html#/'
reports_scheduler_url = 'https://www.accuplacer.org/api/home.html#/reportScheduler'
custom_reports_url = 'https://www.accuplacer.org/api/home.html#/customReports'

# WebDriver Path for Windows 10 
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

# Parent URL
browser.get("https://www.accuplacer.org")

# Credentials NEEDS TO BE ENCRYPTED AND NOT BAKED INTO THE SCRIPT NEEDS UNIT TEST
username = browser.find_element_by_id("login")
password = browser.find_element_by_id("password")
username.send_keys(config['user']['name'])
password.send_keys(config['user']['password'])

# Authentication submit.click()
# For XPATH = //*[@id='loginContainer']/form/footer/button
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='loginContainer']/form/footer/button")))
element.click();

# Navigate to Report
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Reports")))
element.click();

element = WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Custom Reports")))
element.click();

# Make the Report
# Step 1 - Click Dropdown Menu and Load Current Year Query
element = WebDriverWait(browser, 20).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@id='loadSavedQueryCustomReport']/option[text()='All TSI Scores 2020']")))
element.click();

# Step 2 - Create and Load Dynamic Name for Custom Report with System Call to $Date Dependent on OS in Format of TSI_SCORES_$YEAR_$DATE_LAST_RUN
# Powershell Variable = $(Get-Date -Format "yyyy")
# Linux & Mac Variable = $(date +%F)
# Element XPATH = //*[@id="reportDescriptionCustomReport"]
description = browser.find_element_by_id('reportDescriptionCustomReport')
description.send_keys("NameNeedsFormatting")


# Step 3 - Filter by Criteria
# Click Plus Button on Index(1)
element = WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='rptSearchCollapsible']/div[2]/div[1]/h3/a/i[1]")))
element.click();

# Click Calendar Icon
# Element XPATH = //*[@id='collapseFour-1']/div/fieldset/import-date-select/div[1]/div[3]/div/span/button/i
element = WebDriverWait(browser, 20).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@id='collapseFour-1']/div/fieldset/import-date-select/div[1]/div[3]/div/span/button/i")))
element.click();

# Select Current Date !!!NOTE ISSUE ON CURRENT DATE BEING SET!!!
# Set Variable for OS_DATE to be in Format MM/DD/YYYY
# For Powershell $(Get-Date -UFormat %D)
# //*[@id='createdTo']/option[text()='01/27/2020']
#element = WebDriverWait(browser, 20).until(
#                EC.element_to_be_clickable((By.XPATH,"//input[@id='createdTo']")))
#element.send_keys(date);

#NEED TO PUT AN IF FUNCION AND UNIT TEST FOR SESSION TIMEOUTS!!!
#browser.get("https://www.accuplacer.org/api/home.html#/customReports")
#Download the report
# Click Submit Button
element = WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='rptSearchCollapsible']/div[5]/div/button")))
element.click();

# Click Download Button
# Element XPTAH = //*[@id='rptd']/div[2]/a
element = WebDriverWait(browser, 30).until(
                                EC.element_to_be_clickable((By.XPATH, "//*[@id='rptd']/div[2]/a")))
element.click();

# NEED TO PUT AN IF FUNCION AND UNIT TEST FOR SESSION TIMEOUTS!!!
# Quit the Webbrowser
time.sleep(5)
browser.quit()
