import json
from json import JSONDecodeError
from flask import request

import pytest
from tweepy import TweepError


from FlaskTwitterApp import app
from config import TwitterConfig



def test_hashtag_value_not_specified_in_url(client):
    response = client.get('/hashtags/')
    assert response.status_code == 404


def test_hashtag_request_returns_200_status_code(client):
    response = client.get('/hashtags/Python/')
    assert response.status_code == 200


def test_hashtag_request_context_check():
    with app.test_request_context('/hashtags/Python?limit=3'):
        assert request.method == 'GET'
        assert request.path == '/hashtags/Python'
        assert request.args['pages_limit'] == '3'


def test_hashtag_request_returns_valid_json_response(client):
    response = client.get('/hashtags/Python/')
    assert response.is_json is True


def test_hashtag_request_with_invalid_pages_limit_value_returns_json_with_error(client):
    response = client.get('/hashtags/HelloWorld/?limit=nan')
    error = json.loads(response.data)
    assert error['error'] == ERRORS['CONVERSION']


def test_username_value_not_specified_in_url(client):
    response = client.get('/users/')
    assert response.status_code == 404


def test_user_request_returns_200_status_code(client):
    response = client.get('/users/Twitter/')
    assert response.status_code == 200


def test_user_request_returns_json_with_valid_data(client):
    response = client.get('/users/Twitter/')
    data = json.loads(response.data)
    assert len(data['page 1']) > 0
