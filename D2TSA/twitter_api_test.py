import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET,
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

try:
    user = api.verify_credentials()
    print("Authentication OK")
    print("User details:", user.name, user.screen_name)
except Exception as e:
    print("Error during authentication:", e)
