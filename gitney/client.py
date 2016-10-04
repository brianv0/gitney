from rtmbot import RtmBot
from slacker import Slacker

slack_client = None
slacker = None

def init(config):
    global slack_client
    global slacker
    bot = RtmBot(config)
    slack_client = bot.slack_client
    slacker = Slacker(config["WEB_TOKEN"])
    return bot
