#!/bin/python
# ===========================================================
# Created By: Richard Barrett
# Organization: DVISD
# DepartmenT: Data Services
# Purpose: Test Score & 3rd Party Website Data Pull Automation
# Date: 01/20/2020
# ===========================================================

import selenium
import os
import unittest
import requests
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait 

#Definitions
#find_elements_by_name
#find_elements_by_xpath
#find_elements_by_link_text
#find_elements_by_partial_link_text
#find_elements_by_tag_name
#find_elements_by_class_name
#find_elements_by_css_selector

#URL Variables 
login_url = 'https://www.accuplacer.org/'
redirect_url = 'https://www.accuplacer.org/api/home.html#/'
reports_scheduler_url = 'https://www.accuplacer.org/api/home.html#/reportScheduler'
custom_reports_url = 'https://www.accuplacer.org/api/home.html#/customReports'

#WebDriver Path
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
#Parent URL
browser.get("https://www.accuplacer.org")

#Credentials NEEDS TO BE ENCRYPTED AND NOT BAKED INTO THE SCRIPT NEEDS UNIT TEST
username = browser.find_element_by_id("login")
password = browser.find_element_by_id("password")
username.send_keys("USERNAME")
password.send_keys("PASSWORD")

# Authentication submit.click()
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.pull-left")))
element.click();

# Navigate to Report
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Reports")))
element.click();

element = WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Custom Reports")))
element.click();

#Make the report



#NEED TO PUT AN IF FUNCION AND UNIT TEST FOR SESSION TIMEOUTS!!!
#browser.get("https://www.accuplacer.org/api/home.html#/customReports")
#Download the report 

#Close the Webbrowser
