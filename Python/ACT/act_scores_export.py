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

# Authentication Login Button Click
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".slds-button.slds-button_neutral.sfdc_button")))
element.click();

# Select ACT Test Scores and Reports
# By CSS SELECTOR
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".slds-box:nth-child(4) b")))
element.click();

# Click Student Scores (District)
# By XPATH //*[@id="app"]/div[1]/div[3]/div[2]/div[4]/div[2]/div/div/div[1]/div[3]/div/div[1]/div/label/span
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id="app"]/div[1]/div[3]/div[2]/div[4]/div[2]/div/div/div[1]/div[3]/div/div[1]/div/label/span")))
element.click();

# Click Get Report Button
# By CSS SELECTOR .btn.btn-primary
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
element.click();
