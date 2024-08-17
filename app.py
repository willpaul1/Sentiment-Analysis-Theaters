from flask import Flask, request, jsonify
from config import collection
from streaming import start_streaming
from rq import Queue
from config import redis_conn

app = Flask(__name__)
q = Queue(connection=redis_conn)

@app.route('/dashboard', methods=['GET'])
def get_dashboard_data():
    tweets = list(collection.find().sort('_id', -1).limit(100))
    for tweet in tweets:
        tweet['_id'] = str(tweet['_id'])
    return jsonify(tweets)

@app.route('/start_stream', methods=['POST'])
def start_stream():
    keywords = request.json.get('keywords')
    if not keywords:
        return jsonify({'error': 'No keywords provided'}), 400
    
    q.enqueue(start_streaming, keywords)
    return jsonify({'status': 'Stream started', 'keywords': keywords})

if __name__ == "__main__":
    app.run(debug=True, port=5000)