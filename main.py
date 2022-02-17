import tweepy
import textblob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


api_key = 'SeSHtUbPmmuKvzudEu0sCjwhE'
api_key_secret = 'pNfT1G0W1c8Dm2fUYWGVFDHdImIQTXH9uUtcEWddQsXEY5ZlG0'
access_token = '1424397060573319171-To50fBUUtzEeHUebxwzwgyuhGp4VMl'
access_token_secret = 'KLF8KFFVQUNaUB7ZghgoAKGGSeD3UNRfiHHtgWwf005wY'

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api= tweepy.API (authenticator, wait_on_rate_limit=True)

crypto_currency= "Dogecoin"

search= f'#(crypto currency) -filter: retweets'

tweet_cursor = tweepy.Cursor(api.search_tweets, q=search, Lang='en', tweet_node='extended').items (10)

tweets = [tweet.full_text for tweet in tweet_cursor ]

tweets_df = pd.DataFrame(tweets , columns = ['Tweets'])

for _, row in tweets_df.iterrows():
    row ['tweets'] = re.sub('https\S+','' , row['Tweets'])
    row['tweets'] = re.sub('#\S+', '', row['Tweets'])
    row['tweets'] = re.sub('@\S+', '', row['Tweets'])
    row['tweets'] = re.sub('\\n', '', row['Tweets'])

tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet:textblob.TextBlob(tweet).sentiment.polarity)
tweets_df['Result'] = tweets_df['Polarity'].map(lambda pol:'+' if pol > 0 else '-')

positive = tweets_df[tweets_df.Result == '+'].count()['Tweets']
negative = tweets_df[tweets_df.Result == '-'].count()['Tweets']

plt.bar([0,1], [positive,negative], label=['Positive', 'Negative'], color=['green', 'red'])
plt.legend

plt.show()


