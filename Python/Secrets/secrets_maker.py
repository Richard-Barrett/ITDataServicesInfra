#!/bin/python

import json

# example dictionary that contains data like you want to have in json
dic={'User': 100, 'name': 'mkyong.com', 'messages': ['msg 1', 'msg 2', 'msg 3']}

# get json string from that dictionary
json=json.dumps(dic, indent=4)
print json
