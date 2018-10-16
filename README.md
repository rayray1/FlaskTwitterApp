# FlaskTwitterApp

 Flask RESTful API  providing data from Twitter

 ## Features

 * Flask 1.02 and Python 3.6
 * Flask-RESTful
 * venv for virtualenv


 ## First-time setup

 1.  Make sure Python 3.6x and virtualenv are already installed
 2.  Clone the repo and configure the virtualenv

 ```
git clone https://github.com/rayray1/FlaskTwitterApp.git
cd FlaskTwitterApp
```

Install required packages from requirements.txt:

    pip install -r requirements.txt

To be able to connect to the Twitter API, make sure to set the credentials:

    * CONSUMER_KEY
    * CONSUMER_SECRET
    * ACCESS_TOKEN
    * ACCESS_TOKEN_SECRET

## Run Application
When everything is configured correctly start the application:

```
python api.py
```

This application has 2 endpoints for retrieving information from Twitter:
* Get tweets by a hashtag: _http://127.0.0.1:5000/hashtags/SomeHashtag/_
* Get user tweets: _http://127.0.0.1:5000/users/Username/_

`?pages_limit` parameter is also accepted and could be used in the following way:

    http://127.0.0.1:5000/users/username?limit=15
