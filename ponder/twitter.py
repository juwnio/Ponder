import tweepy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def post_tweet(created_post):
    # Load Twitter API credentials from environment variables
    consumer_key = os.environ.get('CONSUMER_API_KEY')
    consumer_secret = os.environ.get('CONSUMER_API_SECRET_KEY')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

    # Create Tweepy Client with OAuth 1.0a user context credentials
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    try:
        # Post the tweet using create_tweet() API v2 method
        response = client.create_tweet(text=created_post)
        print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"An error occurred: {e}")
