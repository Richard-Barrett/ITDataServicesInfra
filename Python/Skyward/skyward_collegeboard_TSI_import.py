#!/bin/python
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
file_input_tsi = os.path.abspath("C:\Imports\CustomNameNeedsFormatting_02_24_2020_20_14_12_richardbarrett")

# URL Variables 
login_url = ''
redirect_url = ''
reports_scheduler_url = ''
custom_reports_url = ''

# Check for Version of Chrome
              
# Keys Variables
test_upload = 'TSI'

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

# Click and Span Administration Options 
# Adminsitration XPATH = //a[@id='nav_Admin']/span
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@id='nav_Admin']/span")))
element.click();

# Click on Imports Under SkyBuild 
# Imports XPATH = //*[@id='nav_SMADASCIIImports']/span
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='nav_SMADASCIIImports']/span")))
element.click();

# Click on Test Score Import Wizard - TW
# Test Wizard XPATH = //a[@id='tree1-3-link']/span
element = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@id='tree1-3-link']/span")))
element.click();

# Browser Switches to Window
WebDriverWait(browser,10).until(EC.number_of_windows_to_be(2))
browser.switch_to.window(browser.window_handles[-1])

# Send test_upload and oend Keys
# Field XPATH = //*[@id='brTestScoreImportLookupInput']
test_lookup = browser.find_element_by_id("brTestScoreImportLookupInput")
test_lookup.send_keys(test_upload)
test_lookup.send_keys(Keys.RETURN)

# Click on the TSI Master Test Upload Utility in Test Wizard
# TSI Master Upload Utility XPATH = //*[@id='0x000000000008324e']/td[2]/div
element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='0x000000000008324e']/td[2]/div")))
element.click();

# Click on Edit Button, Switch to New Popup
# Edit Button XPATH = //*[@id='bEdit']
element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='bEdit']")))
element.click();

# Upload Test File
# Choose File Button XPATH = //*[@id='file1']
# Window Page Address that Opens = https://skyward-student.del-valle.k12.tx.us/scripts/wsisa.dll/WService=wsEAplus/simptedit000.w?isPopup=true
# Browser Switches to Window
WebDriverWait(browser,20).until(EC.number_of_windows_to_be(3))
browser.switch_to.window(browser.window_handles[-1])

# CSS Selector = #file1 
# Fulll XPATH = /html/body/form[1]/div/div/div[5]/table/tbody/tr/td[1]/fieldset/table/tbody/tr[9]/td/fieldset/table/tbody/tr/td[2]/table/tbody/tr/td[1]/input
#wd.find_element_by_css_selector('a[onclick*="uploadDocument"]').click()
#wd.find_element_by_css_selector('div#UploadDocumentPopup input#documentfile').send_keys(os.getcwd()+"/<filename>")
#wd.find_element_by_css_selector('div#UploadDocumentPopup input[value="Upload"]').click()
element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form[1]/div/div/div[5]/table/tbody/tr/td[1]/fieldset/table/tbody/tr[9]/td/fieldset/table/tbody/tr/td[2]/table/tbody/tr/td[1]/input")))
element.send_keys(file_input_tsi)

#file_input = browser.find_element_by_id("file1")
#file_input.send_keys(file_input_tsi)

#element = WebDriverWait(browser, 30).until(
#            EC.element_to_be_clickable((By.XPATH, "//*[@id='file1']")))
#element.send_keys(file_input_tsi);

#element.send_keys("C:\Imports\CustomNameNeedsFormatting_02_24_2020_20_14_12_richardbarrett");

#upload = browser.find_element_by_xpath("//*[@id='file1']")
#upload.click();


#upload.send_keys(Keys.RETURN)

#element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='file1']")))
#element.send_keys("C:\Imports\CustomNameNeedsFormatting_02_24_2020_20_14_12_richardbarrett")

# File Selection = (Specify Path)
#browser.findElement(By.id("file1")).sendKeys(r'C:\Users\richard.barrett\Downloads\CustomNameNeedsFormatting_02_24_2020_20_14_12_richardbarrett')
#WebElement fileInput = driver.findElement(By.name("file1"));
#fileInput.sendKeys(r"C:\Users\richard.barrett\Downloads\CustomNameNeedsFormatting_02_24_2020_20_14_12_richardbarrett");

# Upload Button XPATH = //*[@id='bUpload']
element = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='bUpload']")))
element.click();

# Check if Button is Checked to Overwrite Scores
# If Not Checked Check Box XPATH = //*[@id='cOverwrite']
# Make Sure Vaildation is Checked XPATH = //*[@id='cValidateStuLinkslabel']

# Save Button XPATH = //*[@id='bSave']
element = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "")))
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
print("The download was successfull!")
#browser.quit()
