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
    user_agent="<iRobotModeration 1.00>",
    api_request_delay=1.0  # Delay between API requests to avoid rate limits
)

subreddit_name = "roomba"  # Name of the subreddit you want to monitor
subreddit = reddit.subreddit(subreddit_name)

processed_modmail_ids = []  # List to store IDs of processed modmails

while True:
    for conversation in subreddit.modmail.conversations(state="new"):
        for modmail in conversation.messages:
            author_name = modmail.author.name if modmail.author else None
            if modmail.id not in processed_modmail_ids and author_name != subreddit_name:
                # Reply to the modmail
                conversation.reply(body="Hello! Your message is queued.")

                # Archive the modmail
                conversation.archive()

                # Add the modmail ID to the processed list
                processed_modmail_ids.append(modmail.id)

    # Delay between checking for new modmails
    time.sleep(300)  # Delay for 300 seconds (5 minutes) before checking again