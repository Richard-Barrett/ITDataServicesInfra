#!/usr/bin/env python

import json

# example dictionary that contains data like you want to have in json
# "slack_target_url": "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXXXXX/XXXXXXXXXXXXXXX"
details = {
  "slack_config": {
    "slack_target_url": "INSERT_URL"
  },
  "slack_messages": {
    "message_1": "SLACK_MESSAGE_1",
    "message_2": "SLACK_MESSAGE_2",
    "message_3": "SLACK_MESSAGE_3"
  }
}

with open('secrets.json', 'w') as json_file:
    json.dump(details, json_file, indent=4)

# get json string from that dictionary
json = json.dumps(details, indent=4)
print("JSON will be STD.OUT to secrets.json")
print("Please check the current working directory for the file.")
print json
