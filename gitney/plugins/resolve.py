from __future__ import unicode_literals

from client import slack_client as sc
from client import slacker
from pprint import pprint

crontable = []
outputs = []

def process_message(data):
    profile = slacker.users.profile.get("U244W3692", True).body["profile"]
    pprint(profile)
    if 'print users' in data['text']:
        for user in sc.api_call("users.list")["members"]:
            print(user["name"], user["id"])
