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
          login_url = ''
          redirect_url = ''

          # WebDriver Path for Windows 10 
          browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

          # Parent URL
          #browser.get("https://www.texasassessment.com/administrators/")
          
          # Click on STAAR Portal
          #element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='link-group']//a[contains(.,'STAAR System')]")))
          #element.click();

          # Credentials NEEDS TO BE ENCRYPTED AND NOT BAKED INTO THE SCRIPT NEEDS UNIT TEST
          #username = browser.find_element_by_id("userid")
          #password = browser.find_element_by_id("pass")
          #username.send_keys(config['user']['name'])
          #password.send_keys(config['user']['password'])
          #browser = webdriver.Chrome()
          browser.get("https://www.texasassessment.com/administrators/")
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='link-group']//a[contains(.,'STAAR System')]")))
          element.click()
          WebDriverWait(browser,10).until(EC.number_of_windows_to_be(2))
          browser.switch_to.window(browser.window_handles[-1])
          username =WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID,"userid")))
          password =WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID,"pass")))
          username.send_keys(config['user']['name'])
          password.send_keys(config['user']['password'])
          element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='loginButton']")))
          element.click()

          # Authentication submit.click()
          # For XPATH = //*[@id='qa-button-login']
          #element = WebDriverWait(browser, 20).until(
          #                EC.element_to_be_clickable((By.XPATH, "//*[@id='qa-button-login']")))
          #element.click();
