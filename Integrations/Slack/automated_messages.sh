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

# Use Messages in this command syntax
# curl -X POST -H 'Content-type: application/json' --data '{"text":"MESSAGE TO INSERT"}' $webhook_url

# General Message:
curl -X POST -H 'Content-type: application/json' --data '{"text":"INSERT MESSAGE"}' $webhook_url

# Messages for Handover:
curl -X POST -H 'Content-type: application/json' --data '{"text":"INSERT MESSAGE"}' $webhook_url

# Message for All Change Requests:
curl -X POST -H 'Content-type: application/json' --data '{"text":"INSERT MESSAGE"}' $webhook_url
