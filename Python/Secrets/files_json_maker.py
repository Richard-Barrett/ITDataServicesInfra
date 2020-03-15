#!/bin/python
#!/bin/python

import json

# example dictionary that contains data like you want to have in json
details = {
  "get_files": {
    "file_1": "<absolute_path>",
    "file_2": "<absolute_path>",
    "file_3": "<absolute_path>",
    "file_4": "<absolute_path>",
    "file_5": "<absolute_path>"
  },
  "put_files": {
    "file_1": "<absolute_path>",
    "file_2": "<absolute_path>",
    "file_3": "<absolute_path>",
    "file_4": "<absolute_path>",
    "file_5": "<absolute_path>"
  }
}

## File Template for files.json

with open('files.json', 'w') as json_file:
    json.dump(details, json_file, indent=4)

# get json string from that dictionary
json = json.dumps(details, indent=4)
print("JSON will be STD.OUT to files.json")
print("Please check the current working directory for the file.")
print json
