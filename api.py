from flask import Flask, request
from flask_restful import Resource, Api
from config import TwitterConfig


app = Flask(__name__)
api = Api(app)

# data page limit
default_page_limit = 30


# Get tweets by hashtag
class HashTagApi(Resource):
    def __init__(self):
        self.myApp = TwitterConfig()

    def get(self, hashtag):
        return self.myApp.hashtag(hashtag, int(default_page_limit))


# Get user tweets
class TweetsApi(Resource):
    def __init__(self):
        self.myApp = TwitterConfig()

    def get(self, username):
        return self.myApp.newsfeed(username, int(default_page_limit))


# Resource to the API
api.add_resource(HashTagApi, '/hashtags/<string:hashtag>')
api.add_resource(TweetsApi, '/users/<string:username>')


if __name__ == '__main__':
    app.run(debug=True)
