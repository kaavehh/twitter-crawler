import sys
from tweepy import API, OAuthHandler
import json
from twitter_oath_settings import consumer_key, consumer_secret, access_token, access_secret

def twitter_auth():
    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
    except:
        sys.stderr.write("Could not authorize API access.\n")
    return auth

def activate_client():
    auth = twitter_auth()
    api = API(auth)
    return api
    
if __name__ == "__main__":
    tweet_json = []
    api = activate_client()
    tweets = api.user_timeline(screen_name='realDonaldTrump', tweet_mode='extended', count=25)
    for tweet in tweets:
        tweet_json.append(tweet._json)
    data_dict = {"tweets": tweet_json}
    try:
        with open('twitter_data.json', 'w') as file:
            json.dump(data_dict, file)
    except:
        sys.stderr.write("Could not write to JSON file.\n")
