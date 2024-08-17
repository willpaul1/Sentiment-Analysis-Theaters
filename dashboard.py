import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["tweet_sentiment_db"]
collection = db["tweets"]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Theater Tweet Sentiment Dashboard"),
    dcc.Dropdown(
        id='sentiment-filter',
        options=[
            {'label': 'All', 'value': 'All'},
            {'label': 'Positive', 'value': 'Positive'},
            {'label': 'Neutral', 'value': 'Neutral'},
            {'label': 'Negative', 'value': 'Negative'},
        ],
        value='All',
        clearable=False
    ),
    dcc.Graph(id='sentiment-graph'),
])

@app.callback(
    Output('sentiment-graph', 'figure'),
    [Input('sentiment-filter', 'value')]
)
def update_graph(selected_sentiment):
    if selected_sentiment == 'All':
        tweets = list(collection.find())
    else:
        tweets = list(collection.find({'sentiment': selected_sentiment}))
    
    sentiments = [tweet['sentiment'] for tweet in tweets]
    buzzwords = [bw for tweet in tweets for bw in tweet['buzzwords']]

    fig = px.histogram(
        x=sentiments,
        labels={'x': 'Sentiment', 'y': 'Count'},
        title=f"Sentiment Distribution (Filtered by {selected_sentiment})"
    )

    buzzword_fig = px.histogram(
        x=buzzwords,
        labels={'x': 'Buzzwords', 'y': 'Count'},
        title="Buzzword Frequency"
    )

    fig.update_layout(showlegend=False)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
