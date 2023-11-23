import praw
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
username = os.getenv("username")
password = os.getenv("password")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="<iRobotModeration 1.00>",
    api_request_delay=1.0  # Delay between API requests to avoid rate limits
)

subreddit_name = "roomba"  # Name of the subreddit you want to monitor

subreddit = reddit.subreddit(subreddit_name)

for modmail in subreddit.modmail.stream():
    if modmail.unread:
        modmail.reply("hello")  # Modify the message content as needed
        modmail.mark_read()
        modmail.archive()