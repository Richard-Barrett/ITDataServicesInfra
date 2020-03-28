#!/bin/python

import json

# example dictionary that contains data like you want to have in json
# "slack_target_url": "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXXXXX/XXXXXXXXXXXXXXX"
details = {
  "sftp_credential": {
    "host": "<hostname>",
    "username": "<username>",
    "password": "password",
    "port_num": "<port>",
    "key_file": "<direct_path>"
  }
}

with open('secrets.json', 'w') as json_file:
    json.dump(details, json_file, indent=4)

# get json string from that dictionary
json = json.dumps(details, indent=4)
print("JSON will be STD.OUT to secrets.json")
print("Please check the current working directory for the file.")
print(json)
