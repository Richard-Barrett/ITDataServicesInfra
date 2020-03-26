#!/bin/bash
# ===========================================================
# Created By: Richard Barrett
# Organization: Del Valle ISD
# Department: Data Services 
# Purpose: Send Message to Slack Channel
# Date: 03/26/2020
# ===========================================================

# System Variables
webhook_url=$(cat secrets.json | jq ".slack_config.slack_target_url" | tr -d \")
echo $webhook_url
printf "Webhook Variable is Working.\n"

message_1=$(cat secrets.json | jq ".slack_messages.message_1" | tr -d \")
message_2=$(cat secrets.json | jq ".slack_messages.message_2" | tr -d \")
message_3=$(cat secrets.json | jq ".slack_messages.message_3" | tr -d \")

# Use Messages in this command syntax
# Example without using the secrets.json file to hold messages
# curl -X POST -H 'Content-type: application/json' --data '{"text":"TEST TEXT BODY"}' $webhook_url

# Usage with secrets.json
# curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$message_#\"}" $webhook_url

# Messages for message_1:
curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$message_1\"}" $webhook_url

# Messages for message_2:
curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$message_2\"}" $webhook_url

# Messages for message_3:
curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$message_3\"}" $webhook_ur
