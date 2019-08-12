import os
import slack

class Slack:
    def __init__(self, user, channel, token='', icon = 'https://img.icons8.com/cotton/2x/server.png'):
        self.channel = channel
        self.user = user
        self.icon= icon
        if token == '':
            self.token = os.getenv("SLACK_TOKEN")
        else:
            self.token = token
        self.client = slack.WebClient(token=self.token)
    #
    def send(self, message, channel='', user='', icon=''):
        if channel == '':
            channel = self.channel
        if user == '':
            user = self.user
        if icon == '':
            icon = self.icon
                
        return(
            self.client.chat_postMessage(
                channel=channel,
                text=message,
                username=user,
                as_user=False,
                icon_url = icon
                )
            )