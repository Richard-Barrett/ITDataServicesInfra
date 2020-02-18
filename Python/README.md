## Welcome to ITDataServicesInfra Python
![Image](https://triking-creative.s3.amazonaws.com/Logos/ITDataServicesInfra/ITDataServicesInfra.PNG)

## What is Python
![Image](https://www.python.org/static/img/python-logo@2x.png)

## What are Modules

Python Modules are scripts that normally form one written whole script.
As the script get longer, sometimes it is better to break up the script into specific components for the interactive compiler to call the subscripts that make the bigger whole. These are called modules. If you want to learn more about modules, you can click the link below to learn more about current implementations.

- **[Python Modules](https://docs.python.org/3/tutorial/modules.html)**

## What are the Requirements

Python is obviously a requirement, but a lot of the code is built in mind with security. 
For that very reason you will need to install GnuPGP or some form of PGP. 
In order for credentials to be passed off, you have to create a secrets file for the credetials to load into the login containers.
GnuPGP can be installed on Linux, Mac, or Windows.

If you are unable to use encryption that's fine, the code will still look and use the JSON file you specify with the directory. 
If you wat to use a specific module you must have a **`secrets.gpg`** file within each working directory for you to automate processes and procedures on integrated platforms. 

**How to Create A Secret**
##
1. Download and install GPG 

- **Linux**

**`sudo apt install gnupg`**

- **Mac OS**

**`brew install gnupg`**

- **Windows** 

**`choco install gnupg4win`**

2. Make a secrets.json file using the following template
```
{
  "user": {
    "name": "yourname",
    "password": "password"
  }
}

#FILE SHOULD BE SAVED AS secrets.json and it will not be tracked. 
```
3. Make a passwordless encryption key with gpg at 2048 or 4096 bit encryption
4. Encrypt the secrets.json with a passwordless encryption key

**`gpg --output secrets.json --encrypt secrets.json`**

5. Remove the secrets.json file, if you are using encryption. 

**`rm secerets.json`**

**NOTE SECRETS ARE EXPLICITLY IGNORED WITHIN THE REPO!!!**

## What are the Key Modules

All of the key modules are defined within **`/ITDataServidesInfra/Python/<program_directory>`**. 
This means any system that has a directory within the **`~/Python`** directory within the **ITDataServicesInfra** repository is a module. Some of the key modules are listed below:

- **[ACT](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/ACT)**
- **[Analyses](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/Analyses)**
- **[Cardonex](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/Cardonex)**
- **[Colleboard](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/Collegeboard)**
- **[Eduphoria](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/Eduphoria)**
- **[Frontline](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/Frontline)**
- **[OnDataSuite](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/OnDataSuite)**
- **[SMTP](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/SMTP)**
- **[Selenium](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/Selenium)**
- **[Sharepoint](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/Sharepoint)**
- **[Skyward](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/Skyward)**
- **[State-Assessments](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Python/State-Assessments)** 

## How is Security Managed

Security is managed through the **`.gitignore`** file on the homepage of the **[ITDataServicesInfra](https://github.com/Richard-Barrett/ITDataServicesInfra)** repository. Furthermore, Secrets are explicity ignored. Scripts call the secrets from within a flatfile or **gpg** passwordless file that sits on server itself. This means that any file with a **`.gpg`**, **`.json`**, or **`.yaml`** extension are explicity ignored. You can store them within the Module directory used from each individual integration. 

## Working with Secrets in ITDataServicesInfra

If you want to use **GnuGPG** you will need to create a **GPG Key** to create a key you will need to use the following method to create a key, and the desired encryption method of your choice. 

1. Generate a Key
- **`gpg --full-generate-key`**

At this point you will go through a key creation process. 

2. Choose RSA Key from the following prompt **Option 4**
```
PS C:\Users\username\Git\ITDataServicesInfra\Python> gpg --full-generate-key
gpg (GnuPG) 2.2.17; Copyright (C) 2019 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 4
```

3. Choose what type of keysize you want and hit enter:
```
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048)
```

4. Choose the expiration length or how long you want the key to be valid:
```
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0)
```

If you choose (0) you will recieve a response for y/N. Enter y and click the Enter key on the keyboard.
```
Key does not expire at all
Is this correct? (y/N)
```

5. Enter a Real name, which becomes the Key ID, valid email address, and a comment tag:
```
GnuPG needs to construct a user ID to identify your key.

Real name: Passwordless

Email address: user@test.com
Comment: Test
You selected this USER-ID:
    "Passwordless (Test) <user@test.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit?
```

6. Enter **O** and hit enter for key generation

7. Follow the prompt to generate a key:
```
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
```

**TO LIST OUT CURRENT KEYS AND MANAGE KEYS YOU CAN LIST THEM OUT IN THE FOLLOWING MANNER!!!**
- **`gpg --list-secret-keys --keyid-format LONG`**

For a complete turotial go here:
**[Generating a New GPG Key](https://help.github.com/en/github/authenticating-to-github/generating-a-new-gpg-key)**

## What is Selenium

## How to Use Selenium

## How to Work with Selenium

## Setting up Selenium Drivers

## What is Browser Automation

## How to Record Browser Automation

## Reusable Code
```
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
      
# Parent URL
browser.get("<insert_login_url")

# Credentials NEEDS UNIT TEST
username = browser.find_element_by_id("uname")
password = browser.find_element_by_id("password")
username.send_keys(config['user']['name'])
password.send_keys(config['user']['password'])

# Authentication submit.click()
# For XPATH = //*[@id='submit1']
element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='submit1']")))
element.click();
print("Logging into <insert_program>!")
print("Authenticated")

# Delete Unencrypted JSON File
if os.path.exists("secrets.json"):
  os.remove("secrets.json")
  print("The file was removed and everything is clean!")
else:
  print("The file does not exist")

              
# Close Browser Session Gracefully              
print("The download was successfull!")
#browser.quit()
```
