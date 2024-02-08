import praw
import os
import time
from dotenv import load_dotenv

load_dotenv()

# Load your environment variables
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
username = os.getenv("username")
password = os.getenv("password")

# Create a Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    redirect_uri="https://effective-yodel-749j6rr66vpf469-8000.app.github.dev/",
    user_agent="<iRobotModeration 1.00>",
    api_request_delay=1.0
)

subreddit_name = "roomba"  # Name of the subreddit you want to monitor
moderators = ['GroundbreakingCar633', 'oxlialt', 'Used-Macbook', 'Brandi_yyc', 'iRobot_MOD_BOT']
modmail = reddit.inbox.unread()

for conversation in modmail:
    if isinstance(conversation, praw.models.Message) and conversation.is_assigned:
        continue

    for message in conversation.messages:
        if message.author == 'iRobot_MOD_BOT' and not conversation.replies:
            auto_reply1 = '''Thank you for talking to our support team. This is an automated message sent by u/iRobot_MOD_BOT. We need the following details from you, this is an automated response but once this occurs a mod will reach out.
            ...
            '''
            conversation.reply(auto_reply1)

            auto_reply2 = '''Hi there! Thank you for reaching out. We want to assure you that your message is our top priority. We are currently working on improving our subreddit and may be a bit slow in responding to modmails. We kindly request your patience during this time.
            ...
            '''
            conversation.reply(auto_reply2)

            message.mark_read()

        if message.author in moderators and message.distinguished == 'moderator' and message.body.strip().lower() == '!closemod':
            closing_message = "Thank you for contacting us. Goodbye."
            conversation.reply(closing_message, internal=False)
            message.mark_read()