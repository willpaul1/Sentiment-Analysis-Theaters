import redis
import pymongo

#imput your credentials, connectionstrings and keys here... or use .env files... or store them in a secret manager (Recommended)

API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'


SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'


redis_conn = redis.Redis()
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["tweet_sentiment_db"]
collection = db["tweets"]