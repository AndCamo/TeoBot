import requests
from requests_oauthlib import OAuth1
import keys

consumer_key = keys.api_key
consumer_secret = keys.api_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret


# TWEET TRAMITE POST REQUEST

def get_content():
    content = 'Questo è un test, sono un tweet generato da un bot :) (Ma Teodoro non si è laureato)'
    return content


def format_content(content):
    return {"text": "{}".format(content)}


def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
    return url, auth


def main():
    content = get_content()
    payload = format_content(content)
    url, auth = connect_to_oauth(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    request = requests.post(
        auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
    )


if __name__ == "__main__":
    main()
