#  coding: utf-8
from logging import getLogger

from flask import Blueprint, request, jsonify
import tweepy

from app.twitterBot.lib.benignexception import BenignException
from app.configs.config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_SECRET, ACCESS_TOKEN_KEY
from app.twitterBot.twitter import get_tweets


twitter = Blueprint("twitter", __name__)
logger = getLogger("twitter")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


@twitter.route("/tweets", methods=["GET"])
def get_hashtags():
    logger.debug("Tweets iniciada --------")
    try:
        hashtags = ["#TADS", "#Feira", "#UFPR"]
        #hashtags = ["#CriançaEsperança"]
        hashtag = request.args.to_dict().get("hashtag", None)
        if hashtag is not None:
            hashtags.append(hashtag)

        data = get_tweets(api, hashtags)
        return jsonify(data)
    except BenignException as e:
        logger.error(str(e))
        return jsonify({"message": str(e)}), 400
