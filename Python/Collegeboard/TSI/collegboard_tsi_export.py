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
username.send_keys("richard.barrett")
password.send_keys("Energy2020!")
#browser.send_keys(Keys.ENTER)
#browser.send_keys(Keys.RETURN)

#submit.click()
browser.find_element_by_css_selector('.btn.btn-lg.btn-primary').click()

#Navigate to CustomReports XPATH=//*[@id="leftNav"]/ul/li[11]/ul/li[9]/a
#browser.find_element_by_xpath('//*[@id="leftNav"]/ul/li[11]').click()
browser.find_element_by_partial_link_text("Custom Reports").click()


#element.send_keys(password)
#element.send_keys(Keys.RETURN)
#element.close()
#Setting the value of email input field
#driver.execute_script(f'var element = document.getElementById("email"); element.value = "{username}";')

#Setting the value of password input field
#driver.execute_script(f'var element = document.getElementById("password"); element.value = "{password}";')

#Submitting the form or click the login button also
#driver.execute_script(f'document.getElementsByClassName("login_form")[0].submit();')

#print(driver.page_source)

#Make the report

#NEED TO PUT AN IF FUNCION AND UNIT TEST FOR SESSION TIMEOUTS!!!
#browser.get("https://www.accuplacer.org/api/home.html#/customReports")
#Download the report 

#Close the Webbrowser
