#!/bin/python
# ===========================================================
# Created By: Richard Barrett
# Organization: DVISD
# DepartmenT: Data Services
# Purpose: Test Score & 3rd Party Website Data Pull Automation
# Date: 01/24/2020
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

# Definitions
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# Authentication submit.click()

# Define Driver Path
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

# Define Parent URL
browser.get("https://success.act.org/s/")

# Define Login Process
username = browser.find_element_by_id("input-14")
password = browser.find_element_by_id("input-15")
username.send_keys("USERNAME")
password.send_keys("PASSWORD")

# Select ACT Test Scores and Reports

