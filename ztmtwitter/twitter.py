import tweepy
import time

auth = tweepy.OAuthHandler('Ei4ZWm7bE92T7SwtcVKWRB0LX', 'cqoDPvglDvzgozzPJoAh9g0ZMPESOWTw0EpVYdIhm28T5EMqMq')
auth.set_access_token('1092664648535543808-9QNJ3Ixg4iMJodHD0WSK7bz0tEPgJN', 'fFFjnDhzow5yJi751EbC8InycClHUX9a0qQtyHpenwh7l')

api = tweepy.API(auth)
user=api.me()


def limithandle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
            time.sleep(1000)


search= 'python'
numberOfTweets=2

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break