"""
    Module to collect tweets for a specific hashtag.
"""
import os
import pandas as pd
import tweepy

"""
Export your
    - Consumer Key as "TWITTER_CONSUMER_KEY"
    - Consumer Key Secret as "TWITTER_CONSUMER_KEY_SECRET"
    - Access Token as "TWITTER_ACCESS_TOKEN"
    - Access Token Secret as as "TWITTER_ACCESS_TOKEN_SECRET"
from your Twitter application dashboard.

example.
    on Linux (bash),
        `export TWITTER_CONSUMER_KEY=<Consumer Key>`
    on Windows (cmd prompt),
        `set TWITTER_CONSUMER_KEY=<Consumer Key>`
"""

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')

ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

class HashtagCollector(object):
    
    tweepy_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    tweepy_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def __init__(self, hashtag):
        api = tweepy.API(auth)
        tweets = pd.DataFrame
        
    def _collect(self):
        """ Collect Tweets """
        pass
    
    @staticmethod
    def _load(filename):
        """ Load Scraped Tweets from <filename> csv to a pandas dataframe """
        pass
    
    @staticmethod
    def _save(filename, tweets):
        """ Save Tweets to <filename> as CSV from a <tweets> pd.DataFrame """
        pass
        
if __name__ == "__main__":
    """ Demo collection, saving and loading tweets """
    pass