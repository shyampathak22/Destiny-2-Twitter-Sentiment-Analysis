import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import json
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        return self.analyzer.polarity_scores(text)

def save_sentiment_data(sentiment_data, filename="tweets_sentiment.json"):
    with open(filename, 'w') as file:
        json.dump(sentiment_data, file, indent=4)
        print(f"Sentiment data successfully saved to {filename}")

