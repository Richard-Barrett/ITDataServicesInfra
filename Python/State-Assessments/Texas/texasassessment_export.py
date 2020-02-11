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

          # WebDriver Path for Windows 10 
          browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

          # Parent URL
          #browser.get("https://www.texasassessment.com/administrators/")
          
          # Click on STAAR Portal
          browser.get("https://www.texasassessment.com/administrators/")
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='link-group']//a[contains(.,'STAAR System')]")))
          element.click()
          
          # Browser Switches to Window
          WebDriverWait(browser,10).until(EC.number_of_windows_to_be(2))
          browser.switch_to.window(browser.window_handles[-1])
          
          # Credential Passoff 
          username =WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID,"userid")))
          password =WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID,"pass")))
          username.send_keys(config['user']['name'])
          password.send_keys(config['user']['password'])
          
          # Authentication submit.click()
          # Login Button XPATH = "//input[@class='loginButton']"
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='loginButton']")))
          element.click()

          # Click on Reports+ Menu Button
          # Report+ XPATH = //*[@id='topNav']/ul/div/li[4]/a
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='topNav']/ul/div/li[4]/a")))
          element.click();
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='topNav']/ul/div/li[4]/a")))
          element.click();

          # Click on Report Access Link
          # Report Access XPATH = //*[@id='subReports']/li[6]/a
          #element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='subReports']/li[6]/a")))
          #element.click();

          # Step 1. 
          # Click on Results Access Link
          # Results XPATH = //*[@id='subReports']/li[5]/a
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='subReports']/li[5]/a")))
          element.click();
          time.sleep(5)

          # Step 2. 
          # Need a Function to Go through and Click the Drop Down Menu and Select Each Score
          # Click on Reporting Admin Drop Down Menu
          # Reporting Admin Drop Down Menu XPATH = //*[@id='reportingAdminCode']
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportingAdminCode']")))
          element.click();
          time.sleep(5)

          # Step 3. 
          # List out Available Indicies, Index ID, & Index Values 
          # Choose First Index 
          # Index First XPath = //*[@id='reportingAdminCode']/option[2]
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportingAdminCode']/option[2]")))
          element.click();
          time.sleep(3)

          # Step 4. 
          # List out available Report Indicies, Report Types, & Report Values
          # Click on Report and Select First Index
          # First Click Drop Down XPATH = //*[@id='reportTypeSelected']
          # Student Data File (Complete) Index 4 NEEDED FOR REPORT XPATH = //*[@id='reportTypeSelected']/option[5]
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportTypeSelected']/option[5]")))
          element.click();
          time.sleep(3)

          # Step 5. 
          # Click on Search Button
          # Search Button XPATH = //*[@id='fetchCountsSearchBtn']
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fetchCountsSearchBtn']")))
          element.click();
          time.sleep(5)

          # Step 6. 
          # Parse Results and Count How Many Are Available
          # List Out Links for Download
          # Download Final Student Data File (Complete) XPATH = //*[@id='resultsTable']/tbody[2]/tr/td[4]/a
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='resultsTable']/tbody[2]/tr/td[4]/a")))
          element.click();
          
          print("Download Successful!")
          print("Please Check the specified folder for the download...")
          time.sleep(10)

          # Delete the Encrypted File
          #if os.path.exists("secrets_test.json"):
          #      os.remove("secrets_test.json")
          #      print("The file was removed and everything is clean!")
          #else:
          #      print("The file does not exist")

          browser.quit()

