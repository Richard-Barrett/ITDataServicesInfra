#!/usr/bin/env python2
import json
import requests
import os
import platform

decrypt = "gpg --output secrets.json --decrypt secrets.gpg"

if os.path.exists("secrets.gpg"):
      returned_value = subprocess.call(decrypt, shell=True)
else:
        print("The file does not exist")

with open('secrets.json','r') as f:
      config = json.load(f)

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
# webhook_url = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
# slack_data = {'text': "BODY"}
webhook_url = (config['slack_config']['slack_target_url'])
slack_message_1={'text': config['slack_messages']['message_1']}
slack_message_2={'text': config['slack_messages']['message_2']}
slack_message_3={'text': config['slack_messages']['message_3']}

# Send message_1
response = requests.post(
    webhook_url, data=json.dumps(slack_message_1,slack_message_2,slack_message_3),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )

# Send message_2
response = requests.post(
    webhook_url, data=json.dumps(slack_message_2),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )

# Send message_3
response = requests.post(
    webhook_url, data=json.dumps(slack_message_3),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
