import tweepy
import textblob
import pandas as pd
import matplotlib.pyplot as plt
import re
from array import *
from selenium import webdriver
from selenium.common.exceptions import *

driver = webdriver.Chrome("C:/Users/aryan/Downloads/chromedriver_win32 (2)/chromedriver.exe")
from selenium.webdriver.common.keys import Keys
import time
#set chromodriver.exe path
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.google.com/")
#identify search box
m = driver.find_element_by_name("q")
#enter search text
s=input(print("enter match"))
m.send_keys(s)
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)

api_key = 'SeSHtUbPmmuKvzudEu0sCjwhE'
api_key_secret = 'pNfT1G0W1c8Dm2fUYWGVFDHdImIQTXH9uUtcEWddQsXEY5ZlG0'
access_token = '1424397060573319171-To50fBUUtzEeHUebxwzwgyuhGp4VMl'
access_token_secret = 'KLF8KFFVQUNaUB7ZghgoAKGGSeD3UNRfiHHtgWwf005wY'

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

c=[]
b=array('i',[])
for i in range(3):
    a=input(print("enter player name"))
    c.append(a)
    search= f'#{a} -filter:retweets lang:en'

    tweet_cursor = tweepy.Cursor(api.search_tweets, q=search, tweet_mode='extended').items(100)

    tweets = [tweet.full_text for tweet in tweet_cursor]

    tweets_df = pd.DataFrame(tweets, columns=['Tweets'])

    for _, row in tweets_df.iterrows():
        row['tweets'] = re.sub('https\S+', '', row['Tweets'])
        row['tweets'] = re.sub('#\S+', '', row['Tweets'])
        row['tweets'] = re.sub('@\S+', '', row['Tweets'])
        row['tweets'] = re.sub('\\n', '', row['Tweets'])
    #print(tweets_df)
    #print(tweets)


    tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
    tweets_df['Result'] = tweets_df['Polarity'].map(lambda pol: '+' if pol > 0 else '-')

    positive = tweets_df[tweets_df.Result == '+'].count()['Tweets']
    negative = tweets_df[tweets_df.Result == '-'].count()['Tweets']
#    print(b)
    b.append(positive)
    print(positive)
    #print(negative)

    langs = ['Positive', 'Negative']
    students = [positive,negative]
    a=plt.bar(langs,students)
    a[0].set_color('g')
    a[1].set_color('r')

    plt.xlabel("Tweet Sentiment")
    plt.ylabel("No. of Tweets")
    plt.title("Sentiment Analysis")
    plt.legend

    plt.show()

if (b[0] >= b[1]) and (b[0] >= b[2]):
   largest = b[0]
elif (b[1] >= b[0]) and (b[1] >=b[2]):
   largest = b[1]
else:
   largest = b[2]

if(largest==b[0]):
    {
        print('Player 1 is best')

    }
elif(largest==b[1]):
    {
        print('player 2 is th e best')

    }

else:
    {
        print('player 3 is the best')

    }


# creating the dataset
data = {c[0]: b[0], c[1]: b[1], c[2]: b[2]}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='green',
        width=0.4)

plt.ylabel("Positivity score")
plt.title("Comparison of player fan sentiment")
plt.show()

