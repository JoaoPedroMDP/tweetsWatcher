# coding: utf-8
from logging import getLogger
from typing import List, Any

import tweepy
from tweepy import API
from app.configs.caching import get_cache
logger = getLogger("twitter")

def set_last_tweet_id(last_tweet_id: Any):
    cache = get_cache()
    cache.set("last_tweet_id", last_tweet_id)

def get_last_tweet_id():
    cache = get_cache()

    try:
        last_tweet_id = cache.get("last_tweet_id")
    except Exception as e:
        last_tweet_id = 0

    return last_tweet_id

def get_tweets(api: API, hashtags: List[str]):
    last_tweet_id = get_last_tweet_id()
    # tweets = tweepy.Cursor(api.search_tweets, hashtags, since_id=last_tweet_id).items(20)
    tweets = tweepy.Cursor(api.search_tweets, hashtags).items(20)
    tweet_list = [x for x in tweets]

    if len(tweet_list) == 0:
        return []

    # set_last_tweet_id(tweet_list[-1].id)
    data = []

    for tweet in tweet_list:
        data.append({
            "id": tweet.id,
            "text": tweet.text,
            "username": tweet.author.screen_name,
            "name": tweet.author.name,
            "image": tweet.author.profile_image_url,
        })

    return data