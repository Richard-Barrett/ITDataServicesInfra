## Welcome to ITDataServicesInfra Python
![Image](https://triking-creative.s3.amazonaws.com/Logos/ITDataServicesInfra/ITDataServicesInfra.PNG)

## What is Python
![Image](https://www.python.org/static/img/python-logo@2x.png)

## What are Modules

## What are the Requirements

Python is obviously a requirement, but a lot of the code is built in mind with security. 
For that very reason you will need to install GnuPGP or some form of PGP. 
In order for credentials to be passed off, you have to create a secrets file for the credetials to load into the login containers.
GnuPGP can be installed on Linux, Mac, or Windows.

If you are unable to use encryption that's fine, the code will still look and use the JSON file you specify with the directory. 
If you wat to use a specific module you must have a **`secrets.gpg`** file within each working directory for you to automate processes and procedures on integrated platforms. 

**How to Create A Secret**
1. Download and install GPG 

**Windows** 

**`brew install gnupg4win`**

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

## How is Security Managed

## Working with Secrets in ITDataServicesInfra

## What is Selenium

## How to Use Selenium

## How to Work with Selenium

## Setting up Selenium Drivers

## What is Browser Automation

## How to Record Browser Automation
