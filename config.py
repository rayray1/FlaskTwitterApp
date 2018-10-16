import tweepy

# Initialize Twitter API connection
class TwitterConfig(object):
    def __init__(self):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)


    def hashtag(self, hashtag, default_page_limit):
        result = []
        for tweet in tweepy.Cursor(self.api.search, q = '#' + hashtag, tweet_mode = 'extended', result_type ='recent').items(default_page_limit):
            status = self.api.get_status(tweet.id)
            msg = {
                    "hashtags": ["#%s" % hashtag],
                    "account": {
                        "fullname" : tweet.user.name,
                        "href" : tweet.user.url,
                        "id": tweet.user.id
                    },
                    "id": tweet.id,
                    "text": tweet.full_text,
                    "screen_name": tweet.user.screen_name,
                    "date": tweet.created_at.strftime("%I:%M %p - %d %b %Y"),
                    "like": tweet.favorite_count,
                    "retweets": tweet.retweet_count
            }
            result.append(msg)
        return result


    def newsfeed(self, username, default_page_limit):
        result = []
        for user_feed in tweepy.Cursor(self.api.user_timeline, screen_name = '@'+ username, tweet_mode = 'extended', result_type = 'recent').items(default_page_limit):
            status = self.api.get_status(user_feed.id)
            msg = {
                    "account": {
                        "fullname" : user_feed.user.name,
                        "href" : user_feed.user.url,
                        "id": user_feed.user.id
                    },
                    "date": user_feed.created_at.strftime("%I:%M %p - %d %b %Y"),
                    "text": user_feed.full_text,
                    "retweets": user_feed.retweet_count,
                    "like": user_feed.favorite_count
            }
            result.append(msg)
        return result


# Twitter api keys - Should be kept in secret in production
CONSUMER_KEY = '1BgZ8412n4pEdgdrqLmnTJZ6m'
CONSUMER_SECRET = 'jznmWOD4Gg2muE2AsZL3WAppuZdP9N2sXlZHCaAwMsx3TEjmWy'
ACCESS_TOKEN = '617522164-rFIKgfhMh3Rvctt6kHcwBANoaKtcJqCYBcWphVbI'
ACCESS_TOKEN_SECRET = 'BY0RJd7g4XgNEyHEjwIhZBSQUw2TOKwIapzrNLBPnvdoR'
