import tweepy
from rq import Queue
from config import redis_conn
from utils import preprocess_tweet, detect_language, send_email_notification
from sentiment_analysis import analyze_sentiment_vader
from buzzword_detection import check_buzzwords_ner
from config import collection

q = Queue(connection=redis_conn)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        q.enqueue(process_tweet, status.text)
    
    def on_error(self, status_code):
        if status_code == 420:
            return False

def process_tweet(tweet):
    lang = detect_language(tweet)
    clean_tweet = preprocess_tweet(tweet, lang=lang)
    sentiment = analyze_sentiment_vader(clean_tweet, lang=lang)
    buzzwords = ["PERSON", "ORG", "GPE", "DESIGN", "STAGE"]
    buzzwords_found = check_buzzwords_ner(tweet, buzzwords, lang=lang)
    
    result = {
        'tweet': tweet,
        'clean_tweet': clean_tweet,
        'language': lang,
        'sentiment': sentiment,
        'buzzwords': buzzwords_found
    }
    
    collection.insert_one(result)
    
    if sentiment == 'Negative':
        send_email_notification(
            to_email='alert@example.com',
            subject='Negative Sentiment Alert!',
            body=f'Negative tweet detected: {tweet}'
        )
    
    return result

def start_streaming(keywords):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=auth, listener=myStreamListener)
    
    print(f"Starting stream for keywords: {keywords}")
    myStream.filter(track=keywords, languages=["en", "de"])