# ![Image](https://brandpalettes.com/wp-content/uploads/2019/03/slack_logo_colors-300x77.png)
# Slack Integrations and Automations
In order to integrate with Slack you will need to generate a JSON payload in order to send particular messages to your desired channel destination. 

**secrets.json**
```json
{
  "slack_config": {
    "slack_target_url": "INSERT_URL"
  },
  "slack_messages": {
    "message_1": "SLACK_MESSAGE_1",
    "message_2": "SLACK_MESSAGE_2",
    "message_3": "SLACK_MESSAGE_3"
  }
}
```

What this does is it stores all of the informatin needed to autheticate with Slack, establish a session, and target a desired set of channels. 
Furthermore, it allows you to customize the message you want to send. 
After you have successfully published a message to a hannel you can scheudle it with **Task-Scheduler** or make a **Cronjob**.
You can make a **secrets.json** by using the following command to generate a template within the current working directory. 
```python
python secrets_json_slack_int_maker.py
```

**Before The Script is Ran:**
```bash
├── README.md
├── automated_messages.py
├── automated_messages.sh
└── secrets_json_slack_int_maker.py
```

**Output:**
```bash
 richardbarret@1152-MacBook-Pro  ~/Git/SalesforceCLI/Integration/Slack   master  python secrets_json_slack_int_maker.py                                 ✔  1054  13:24:56
JSON will be STD.OUT to secrets.json
Please check the current working directory for the file.
{
  "slack_config": {
    "slack_target_url": "INSERT_URL"
  },
  "slack_messages": {
    "message_1": "SLACK_MESSAGE_1",
    "message_2": "SLACK_MESSAGE_2",
    "message_3": "SLACK_MESSAGE_3"
  }
}
```

**After The Script is Ran:**
```bash
├── README.md
├── automated_messages.py
├── automated_messages.sh
├── secrets.json
└── secrets_json_slack_int_maker.py
```
