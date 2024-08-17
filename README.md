# Theater Tweet Sentiment Analysis

This project is designed to analyze tweets related to theater, detect buzzwords, and determine the sentiment of the tweets. The project includes a streaming service to collect tweets, a sentiment analysis module, a buzzword detection module, and a dashboard to visualize the results.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Modules](#modules)
- [Dashboard](#dashboard)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/theater-tweet-sentiment-analysis.git
    cd theater-tweet-sentiment-analysis
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download NLTK data:
    ```sh
    python -m nltk.downloader stopwords punkt
    ```

## Configuration

1. Update the `config.py` file with your credentials, connection strings, and keys.

2. Ensure you have a running instance of MongoDB and Redis.

## Usage

1. Start the Flask application:
    ```sh
    python app.py
    ```

2. Start the Dash dashboard:
    ```sh
    python dashboard.py
    ```

3. Use the `/start_stream` endpoint to start streaming tweets:
    ```sh
    curl -X POST http://127.0.0.1:5000/start_stream -H "Content-Type: application/json" -d '{"keywords": ["theater", "play", "drama"]}'
    ```

## Modules

### `utils.py`

- `preprocess_tweet(tweet, lang='en')`: Preprocesses the tweet by removing URLs, mentions, hashtags, numbers, and stopwords.
- `detect_language(tweet)`: Detects the language of the tweet.
- `send_email_notification(to_email, subject, body)`: Sends an email notification.

### `sentiment_analysis.py`

- `analyze_sentiment_vader(tweet, lang='en')`: Analyzes the sentiment of the tweet using VADER sentiment analysis.

### `buzzword_detection.py`

- `check_buzzwords_ner(tweet, buzzwords, lang='en')`: Detects buzzwords in the tweet using Named Entity Recognition (NER).

### `streaming.py`

- `MyStreamListener`: A custom Tweepy stream listener that processes incoming tweets.
- `process_tweet(tweet)`: Processes the tweet by detecting language, preprocessing, analyzing sentiment, and detecting buzzwords.
- `start_streaming(keywords)`: Starts streaming tweets based on the provided keywords.

### `dashboard.py`

- A Dash application to visualize the sentiment distribution and buzzword frequency of the collected tweets.

### `app.py`

- A Flask application to provide API endpoints for the dashboard and to start the tweet streaming service.

## Dashboard

The dashboard provides a visual representation of the sentiment distribution and buzzword frequency of the collected tweets. It includes a dropdown to filter tweets by sentiment.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
