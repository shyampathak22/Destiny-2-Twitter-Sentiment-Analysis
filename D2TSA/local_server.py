from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')

def get_bearer_token():
    response = requests.post(
        'https://api.twitter.com/oauth2/token',
        auth=(CONSUMER_KEY, CONSUMER_SECRET),
        data={'grant_type': 'client_credentials'}
    )
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None

def run_server():
    app.run(debug=True, port=8000)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/auth')
def auth():
    bearer_token = get_bearer_token()
    if bearer_token:
        return f'Bearer Token Obtained: {bearer_token}'
    else:
        return 'Failed to Obtain Bearer Token', 400

if __name__ == "__main__":
    run_server()
