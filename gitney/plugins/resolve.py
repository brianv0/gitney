from __future__ import unicode_literals

from client import slack_client as sc
from client import slacker
from pprint import pprint

crontable = []
outputs = []

github_field_id = "Xf2JS7M3C1"
github_user_map = {}

crontable.append([600, "cache_github_ids"])

def process_message(data):
    if github_user_map:
        for item in data['text'].split(" "):
            if item in github_user_map:
                user = github_user_map[item]
                outputs.append([data["channel"], "@" + user["name"]])


def cache_github_ids():
    if not github_field_id:
        team_prof = slacker.team.profile.get().body["profile"]
        for field in team_prof["fields"]:
            print field
            if 'github' in team_prof["fields"][field]['label'].lower():
                github_field = field
                break
        if not github_field_id:
            raise ValueError("No github_field_id")
    
    list_response = slacker.users.list()
    users = list_response.body['members']
    for user in users:
        id = user['id']
        name = user['name']
        profile = slacker.users.profile.get(id).body["profile"]
        # Try to get github name. If no github name, assume user is 
        # using github name
        pprint(profile)
        fields = profile["fields"]
        maybe_github_id = name
        if fields and github_field_id in fields:
            maybe_github_id = fields[github_field_id].get("value", maybe_github_id)
        github_user_map[maybe_github_id] = {"name":name, "id":id}
