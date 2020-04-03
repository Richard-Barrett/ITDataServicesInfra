#!/bin/usr/env python
# ===========================================================
# Created By: Richard Barrett
# Organization: DVISD
# DepartmenT: Data Services
# Purpose: Skyward Administration
# Date: 04/01/2020
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
file_input_inactive_users = os.path.abspath("C:\Imports\CustomNameNeedsFormatting_02_24_2020_20_14_12_richardbarrett")

# URL Variables 
login_url = ''
redirect_url = ''
reports_scheduler_url = ''
custom_reports_url = ''

# Check for Version of Chrome

# WebDriver Path for System
if platform.system() == ('Windows'):
    browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
elif platform.system() == ('Linux'):
    browser = webdriver.Chrome(executable_path='/home/rbarrett/Drivers/Google/Chrome/chromedriver_linux64/chromedriver')
elif platform.system() == ('Darwin'):
    browser = webdriver.Chrome(executable_path='~/Drivers/Google/Chrome/chromedriver_mac64/chromedriver')
else:
    print("Are you sure you have the Selenium Webdriver installed in the correct path?")
      
# tearDown Method
def tearDown(self):
    self.browser.close()

# shutDown Method 
def shutDown(self):
    self.browser.quit()

# Parent URL
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
print("Logging into <insert_program>!")
print("Authenticated")

# Click and Span Skyward Contact Access
# Adminsitration XPATH = //*[@id='nav_ContactAccess']/span
element = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='nav_ContactAccess']/span")))
element.click();

# Click on Secured Users
# XPATH = //a[@id='nav_SecuredUsers']/span
element = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='nav_SecuredUsers']/span")))
element.click();

# Load users.json File 
with open('users.json','r') as f:
          config = json.load(f)

# Send Keys to Lookup 
# XPATH = //*[@id='brSecuredUsersLookupInput']
target_user = WebDriverWait(browser, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='brSecuredUsersLookupInput']")))
target_user.send_keys(config['sec_group_removal']['name_key']);
target_user.send_keys(Keys.RETURN);
time.sleep(2)

# Expand Button on Element Needing Sec Group Removal
# Class "bd_open"
print("fault 1")
time.sleep(2)
element = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "bd_closed")))
element.click()
time.sleep(2)
print("post fault 1")
time.sleep(2)

# Click on Remove All Groups By Link Text
# find_elements_by_link_text
print("fault 2")
time.sleep(2)
element = WebDriverWait(browser, 20).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Remove All Groups")))
element.click()
time.sleep(2)
print("post fault 2")
time.sleep(2)
# Browser Switches to New Window Alert for Verification
# Browser Switches to Window
#WebDriverWait(browser,10).until(EC.number_of_windows_to_be(2))
#browser.switch_to.window(browser.window_handles[-1])

# Click Ok by ID
# XPATH //*[@id='msgBtn1'] 
time.sleep(2)
element = WebDriverWait(browser, 20).until(
                            EC.element_to_be_clickable((By.XPATH, "//*[@id='msgBtn1']")))
element.click()
time.sleep(2)
