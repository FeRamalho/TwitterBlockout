import os
from flask import Flask, render_template, request, url_for
import oauth2 as oauth
import urllib.request
import urllib.parse
import urllib.error
import json
from dotenv import load_dotenv

def request_token():
    #app_callback_url = url_for('callback', _external=True)


    consumer = oauth.Consumer(
        get_env_vars("API_KEY"), get_env_vars("API_KEY_SECRET"))
    client = oauth.Client(consumer)
    resp, content = client.request(request_token_url, "POST", body=urllib.parse.urlencode({
                                   "oauth_callback": app_callback_url}))
    return True

def get_env_vars(envName):
    load_dotenv()
    return os.getenv(envName)