#!/bin/usr/env python
# ===========================================================
# Created By: Richard Barrett
# Organization: DVISD
# DepartmenT: Data Services
# Purpose: Skyward Reports
# Date: 04/03/2020
# ===========================================================
import selenium
import shutil
import xlsxwriter
import os
import unittest
import requests
import subprocess
import getpass
import platform
import socket
import ssl
import pynput
import logging
import time 
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from datetime import date

decrypt = "gpg --output secrets.json --decrypt secrets.gpg" 

if os.path.exists("secrets.gpg"):
      returned_value = subprocess.call(decrypt, shell=True)
else:
        print("The file does not exist!")
        print("You should probably create a secret!")
        print("gpg --output filename.gpg --encrypt filename.json")
            
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
node = platform.node()
system = platform.system()
username = getpass.getuser()
version = platform.version()
keyboard = Controller()

# Upload Path Variables 
file_input_inactive_users = os.path.abspath("<insert_file_path>")

# URL Variables 
login_url = ''
redirect_url = ''
reports_scheduler_url = ''
custom_reports_url = ''

# Check for Version of Chrome

# WebDriver Path for OS.System
if platform.system() == ('Windows'):
    browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
elif platform.system() == ('Linux'):
    browser = webdriver.Chrome(executable_path='/home/rbarrett/Drivers/Google/Chrome/chromedriver_linux64/chromedriver')
elif platform.system() == ('Darwin'):
    browser = webdriver.Chrome(executable_path='~/Drivers/Google/Chrome/chromedriver_mac64/chromedriver')
else:
    print("Are you sure you have the Selenium Webdriver installed in the correct path?")
      
# TearDown Method
def tearDown(self):
    self.browser.close()

# ShutDown Method 
def shutDown(self):
    self.browser.quit()

# Parent URL
#browser.get(config['URL']['target_url'])
#browser.get("https://skyward-student.del-valle.k12.tx.us/scripts/wsisa.dll/WService=wsEAplus/seplog01.w?nopopup=true")
#options.addArguments("--ignore-certificate-errors")
browser.get("https://skyward-dev.del-valle.k12.tx.us/scripts/wsisa.dll/WService=wsEAplusTrn/seplog01.w?nopopup=true")
time.sleep(5)

# Click on Advanced Button for Certificate Error
# XPATH //*[@id='details-button']
element = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='details-button']")))
element.click();

# Click on Proceed
# XPATH //*[@id'proceed-link']
element = WebDriverWait(browser, 20).until(
                    EC.element_to_be_clickable((By.ID, "proceed-link")))
element.click();
time.sleep(10)

# Credentials NEEDS UNIT TEST
username = browser.find_element_by_id("login")
password = browser.find_element_by_id("password")
username.send_keys(config['user']['name'])
password.send_keys(config['user']['password'])

# Authentication submit.click()
# For XPATH = //*[@id='bLogin']
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='bLogin']")))
element.click();
print("Logging into Skyward!")
print("Authenticated")

# Click and Span Skyward Contact Family Access
# Adminsitration XPATH = //*[@id='nav_ContactAccess']/span
element = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='nav_FamilyAccessSuperUser']/span")))
element.click();

# Click on id="browsetool_export"
# Opens Options to Download Report
# XPATH = //*[@id='browsetool_export']
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='browsetool_export']")))
element.click();

# Click on .CSV Radio Button
# XPATH = //*[@id='ExCOptCSV']
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='ExCOptCSV']")))
element.click();

# Click on Export Button
# XPATH = //*[@id='bExport']
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='bExport']")))
element.click();

# Click on id="browsetool_export"
# Opens Options to Download Report
# XPATH = //*[@id='browsetool_export']
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='browsetool_export']")))
element.click();

# Click on .xlsx Radio Button
# XPATH = //*[@id='ExCOptXLSX']
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='ExCOptXLSX']")))
element.click();

# Click on Export Button 
# XPATH  = //*[@id='bExport']
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='bExport']")))
element.click();

# Click on Run Button 
# Run Button XPATH = 
# Delete Unencrypted JSON File
if os.path.exists("secrets.json"):
  os.remove("secrets.json")
  print("The file was removed and everything is clean!")
else:
  print("The file does not exist")

              
# Close Browser Session Gracefully              
print("The Export was successfull!")
#browser.quit()
