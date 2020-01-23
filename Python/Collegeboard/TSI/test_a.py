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

#URL Variables
login_url = 'https://www.accuplacer.org/'
redirect_url = 'https://www.accuplacer.org/api/home.html#/'
reports_scheduler_url = 'https://www.accuplacer.org/api/home.html#/reportScheduler'
custom_reports_url = 'https://www.accuplacer.org/api/home.html#/customReports'

#WebDriver Path
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
#Parent URL
browser.get("https://www.accuplacer.org/api/home.html#/customReports")

#Credentials NEEDS TO BE ENCRYPTED AND NOT BAKED INTO THE SCRIPT NEEDS UNIT TEST
username = browser.find_element_by_id("sessionTimeoutUsername")
password = browser.find_element_by_id("sessionTimeoutPassword")
username.send_keys("richard.barrett")
password.send_keys("Energy2020!")
#browser.send_keys(Keys.ENTER)
#browser.send_keys(Keys.RETURN)

#submit.click()
reauthenticate = browser.find_element_by_css_selector('.btn.btn-sm.btn-primary')
reauthenticate.click()
reauthenticate.click()
#NEED TO PUT AN IF FUNCION AND UNIT TEST FOR SESSION TIMEOUTS!!!
#browser.get("https://www.accuplacer.org/api/home.html#/customReports")
#Download the report

#Close the Webbrowser
