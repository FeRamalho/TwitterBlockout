import os
from flask import Flask, render_template, request, url_for
import oauth2 as oauth
import urllib.request
import urllib.parse
import urllib.error
import json
from dotenv import load_dotenv

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'
#show_user_url = 'https://api.twitter.com/1.1/users/show.json'
app_callback_url = 'http://127.0.0.1:5000'

def request_token():
    #app_callback_url = url_for('callback', _external=True)

    consumer = oauth.Consumer(get_env_vars("API_KEY"), get_env_vars("API_KEY_SECRET"))
    client = oauth.Client(consumer)
    resp, content = client.request(request_token_url, "POST", body=urllib.parse.urlencode({
                                   "oauth_callback": app_callback_url}))
    
    if resp['status'] != '200':
        error_message = 'Invalid response, status {status}, {message}'.format(
            status=resp['status'], message=content.decode('utf-8'))
        return error_message
    
    request_token = dict(urllib.parse.parse_qsl(content))
    confirm_callback = request_token[b'oauth_callback_confirmed'].decode('utf-8')
    if not confirm_callback:
        return "Invalid callback url"
    oauth_token = request_token[b'oauth_token'].decode('utf-8')
    oauth_token_secret = request_token[b'oauth_token_secret'].decode('utf-8')
    
    return request_token

def get_env_vars(envName):
    load_dotenv()
    return os.getenv(envName)

def redirect_user(request_token):
    return 0