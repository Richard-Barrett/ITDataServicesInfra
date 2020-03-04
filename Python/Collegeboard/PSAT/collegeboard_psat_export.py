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
import subprocess
import getpass
import platform
import logging
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from datetime import date

decrypt = "gpg --output secrets.json --decrypt secrets.gpg" 

if os.path.exists("secrets.gpg"):
      returned_value = subprocess.call(decrypt, shell=True)
else:
        print("The file does not exist")

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
          login_url = ''
          redirect_url = ''

          # WebDriver Path for Windows 10 
          browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

          # Parent URL
          browser.get("https://k12reports.collegeboard.org/login")

          # Credentials NEEDS TO BE ENCRYPTED AND NOT BAKED INTO THE SCRIPT NEEDS UNIT TEST
          username = browser.find_element_by_id("view4__username_pro")
          password = browser.find_element_by_id("view4__password_pro")
          username.send_keys(config['user']['name'])
          password.send_keys(config['user']['password'])

          # Authentication submit.click()
          # For XPATH = //*[@id='view4__SignInForm']/div[3]/button
          element = WebDriverWait(browser, 20).until(
                          EC.element_to_be_clickable((By.XPATH, "//*[@id='view4__SignInForm']/div[3]/button")))
          element.click();
          time.sleep(5)
      
          # Select School District from Drop Down and Click Sign In 
          # For School District XPATH = //*[@id='orgId']/option[2]
          # For Sign-In XPATH = //*[@id='view-holder']/div/div/div/div/form/button
          element = WebDriverWait(browser, 20).until(
                          EC.element_to_be_clickable((By.XPATH, "//*[@id='orgId']/option[2]")))
          element.click();
          
          element = WebDriverWait(browser, 20).until(
                          EC.element_to_be_clickable((By.XPATH, "//*[@id='view-holder']/div/div/div/div/form/button")))
          element.click();
          time.sleep(3)
      
          # Handle Tour Pop Up Window Click Don't Show Again Checkbox and Click Close Button
          # Don't Show Again Checkbox XPATH = //*[@id='dontShowTour'], ID = dontShowTour
          # Close Button XPATH = //*[@id='start_tour_container']/div/div/div[2]/button
          # Browser Switches to Window
          WebDriverWait(browser,10).until(EC.number_of_windows_to_be(2))
          browser.switch_to.window(browser.window_handles[-1])
          element = WebDriverWait(browser, 20).until(
                          EC.element_to_be_clickable((By.XPATH, "//*[@id='dontShowTour']")))
          element.click();
          time.sleep(2)
          element = WebDriverWait(browser, 20).until(
                          EC.element_to_be_clickable((By.XPATH, "//*[@id='start_tour_container']/div/div/div[2]/button")))
          element.click();
          time.sleep(2)
           
      
          # Click on the Downloads Menu and Select Raw Data Files for Your System 
          # Downloads Drop Down XPATH = //*[@id='navigation-region']/div/nav[1]/div/div/div/ul/li[2]/a
          # Select RAW Data Files for System XPATH = //*[@id='navigation-region']/div/nav/div/div/div/ul/li[2]/ul/li[3]/a/span
          element = WebDriverWait(browser, 20).until(
                          EC.element_to_be_clickable((By.XPATH, "//*[@id='navigation-region']/div/nav[1]/div/div/div/ul/li[2]/a")))
          element.click();
          
          element = WebDriverWait(browser, 20).until(
                          EC.element_to_be_clickable((By.XPATH, "//*[@id='navigation-region']/div/nav/div/div/div/ul/li[2]/ul/li[3]/a/span")))
          element.click();
      
          # NEED TO PUT AN IF FUNCION AND UNIT TEST FOR SESSION TIMEOUTS!!!
          # Quit the Webbrowser
          time.sleep(5)

          # Delete the Encrypted File
          if os.path.exists("secrets.json"):
                    os.remove("secrets.json")
                    print("The file was removed and everything is clean!")
          else:
                     print("The file does not exist")

print("The download was successfull!")
#browser.quit()
