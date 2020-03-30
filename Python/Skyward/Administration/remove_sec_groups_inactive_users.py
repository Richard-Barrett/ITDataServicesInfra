#!/bin/usr/env python
# ===========================================================
# Created By: Richard Barrett
# Organization: DVISD
# DepartmenT: Data Services
# Purpose: Test Score & 3rd Party Website Data Pull Automation
# Date: 02/11/2020
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
browser.get("https://skyward-student.del-valle.k12.tx.us/scripts/wsisa.dll/WService=wsEAplus/seplog01.w?nopopup=true")
time.sleep(5)

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
