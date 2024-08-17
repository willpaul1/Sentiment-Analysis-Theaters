import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from langdetect import detect
from smtplib import SMTP
from email_validator import validate_email, EmailNotValidError

nltk.download('stopwords')
nltk.download('punkt')

stop_words_en = set(stopwords.words('english'))
stop_words_de = set(stopwords.words('german'))

# SMTP server configuration
# Replace with your SMTP server details
def send_email_notification(to_email, subject, body):
    with SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        message = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(SMTP_USERNAME, to_email, message)

def detect_language(tweet):
    try:
        return detect(tweet)
    except:
        return 'unknown'

def preprocess_tweet(tweet, lang='en'):
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'\@\w+|\#','', tweet)
    tweet = tweet.lower()
    tweet = re.sub(r'\d+', '', tweet)
    tweet = tweet.strip()
    
    stop_words = stop_words_de if lang == 'de' else stop_words_en
    tokens = word_tokenize(tweet)
    filtered_words = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(filtered_words)