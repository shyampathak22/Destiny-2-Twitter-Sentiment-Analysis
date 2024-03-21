import tweepy
import json
import logging
import os
import datetime
from datetime import timedelta
from dotenv import load_dotenv
import random

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

def create_api_client():
    try:
        client = tweepy.Client(bearer_token=BEARER_TOKEN)
        logger.info('API client created successfully')
        return client
    except Exception as e:
        logger.error('Error creating API client', exc_info=True)
        raise e

def collect_tweets(client, query, start_time, end_time, max_tweets=10000, sample_size=10000):
    logger.info(f'Collecting tweets for query: {query}')
    all_tweets = []
    now = datetime.datetime.utcnow()
    start_time = (now - datetime.timedelta(days=2.5)).isoformat("T") + "Z"
    end_time = (now - datetime.timedelta(days=1.5)).isoformat("T") + "Z"
    try:
        for tweet in tweepy.Paginator(client.search_recent_tweets,
                                      query=query,
                                      tweet_fields=['created_at'],
                                      start_time=start_time,
                                      end_time=end_time,
                                      max_results=100).flatten(limit=max_tweets):
            all_tweets.append(tweet.data)

        sampled_tweets = random.sample(all_tweets, min(sample_size, len(all_tweets)))
        logger.info(f'Sampled {len(sampled_tweets)} tweets')
        return sampled_tweets
    except Exception as e:
        logger.error("Error collecting tweets", exc_info=True)
        raise e


def save_tweets(tweets, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(tweets, file, ensure_ascii=False, indent=4)
    logger.info(f'Saved tweets to {filename}')

if __name__ == '__main__':
    query = "Destiny 2 -is:retweet"
    max_tweets = 10
    output_file = "tweets.json"
    client = create_api_client()

    start_time = (datetime.utcnow() - timedelta(days=7)).isoformat("T") + "Z"
    end_time = datetime.utcnow().isoformat("T") + "Z"

    tweets = collect_tweets(client, query, start_time, end_time, max_tweets)
    save_tweets(tweets, output_file)

