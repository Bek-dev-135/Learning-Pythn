import tweepy

auth = tweepy.OAuthHandler('Ei4ZWm7bE92T7SwtcVKWRB0LX', 'cqoDPvglDvzgozzPJoAh9g0ZMPESOWTw0EpVYdIhm28T5EMqMq')
auth.set_access_token('1092664648535543808-9QNJ3Ixg4iMJodHD0WSK7bz0tEPgJN', 'fFFjnDhzow5yJi751EbC8InycClHUX9a0qQtyHpenwh7l')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)