import tweepy
import keys

# GET TOKENS:
consumer_key = keys.api_key
consumer_secret = keys.api_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret
bearer_token = keys.bearer_token


def get_content():
    content = 'Questo è un test, sono UN NUOVO un tweet generato tramite Tweepy! (Ma Teodoro non si è laureato)'
    return content


# API authentication
def api():
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    return tweepy.API(auth)


def get_client():
    client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
    return client


def tweet(message: str):
    client = get_client()

    client.create_tweet(text=message)

    print("Tweeted successfully!")


if __name__ == '__main__':
    content = get_content()
    tweet(content)
