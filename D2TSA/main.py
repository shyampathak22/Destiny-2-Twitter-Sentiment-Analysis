import argparse
import pandas as pd
from data_collection import create_api_client, collect_tweets
from data_preprocessing import preprocess_text
from sentiment_analysis import SentimentAnalyzer
from visualization import plot_sentiment_score_distribution, plot_sentiment_over_time
from report_generation import generate_detailed_pdf_report
import datetime
from datetime import timedelta

def main(max_tweets, output_file):
    keywords = ['into the light', 'Into The Light', '#IntoTheLight',
                '#intothelight']
    query = ' OR '.join(keywords)

    now = datetime.datetime.utcnow()
    start_time = (now - datetime.timedelta(days=2.5)).isoformat("T") + "Z"
    end_time = (now - datetime.timedelta(days=1.5)).isoformat("T") + "Z"

    api_client = create_api_client()
    raw_tweets = collect_tweets(api_client, query, start_time, end_time, max_tweets)

    processed_tweets = []
    sentiment_analyzer = SentimentAnalyzer()
    for tweet in raw_tweets:
        preprocessed_text = preprocess_text(tweet['text'])
        sentiment = sentiment_analyzer.analyze_sentiment(preprocessed_text)
        processed_tweet = {
            'text': preprocessed_text,
            'sentiment': sentiment,
            'timestamp': tweet['created_at']
        }
        processed_tweets.append(processed_tweet)

    processed_tweets_df = pd.DataFrame({
        'compound': [tweet['sentiment']['compound'] for tweet in processed_tweets],
        'timestamp': pd.to_datetime([tweet['timestamp'] for tweet in processed_tweets])
    })

    plot_sentiment_score_distribution(processed_tweets_df, 'sentiment_distribution.png')
    plot_sentiment_over_time(processed_tweets_df, 'sentiment_over_time.png')

    report_visualizations = ['sentiment_distribution.png', 'sentiment_over_time.png']
    generate_detailed_pdf_report(processed_tweets_df, report_visualizations, output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Destiny 2 Twitter Sentiment Analysis')
    parser.add_argument('--max_tweets', type=int, default=100, help='Maximum number of tweets to collect')
    parser.add_argument('--output_file', type=str, default='report.pdf', help='Output file for the report')

    args = parser.parse_args()
    main(args.max_tweets, args.output_file)

