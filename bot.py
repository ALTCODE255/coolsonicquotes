import os
import random

from dotenv import load_dotenv
import tweepy

load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
)


def passTweet(tweet: str, log: list[str]) -> bool:
    return (
        True
        if tweet and tweet.strip() and not tweet.startswith("#") and tweet not in log
        else False
    )


def getTweet() -> str:
    limit = 11
    with open("recent.txt", "r", encoding="utf-8") as f:
        log = f.read().splitlines()
        if len(log) < limit:
            log = [""] * (limit - len(log)) + log
    with open("quotes.txt", "r", encoding="utf-8") as f:
        tweets = [tweet for tweet in f.read().splitlines() if passTweet(tweet, log)]
    random_tweet = random.choice(tweets)
    log.pop(0)
    log.append(random_tweet)
    with open("recent.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(log))
    return random_tweet.replace("\\n", "\n")


client.create_tweet(text=getTweet())
