import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_sentiment_over_time(sentiments_df, output_file):
    plt.figure(figsize=(10,6))
    sentiments_df['timestamp'] = pd.to_datetime(sentiments_df['timestamp'])
    sns.lineplot(data=sentiments_df, x='timestamp', y='compound', label='Player Sentiment Trends', color='blue')
    plt.title('Sentiment Over Time')
    plt.xlabel('Time')
    plt.ylabel('Average Sentiment Score')
    plt.legend(title='Sentiment Types')
    plt.savefig(output_file)
    plt.close()

def plot_sentiment_score_distribution(sentiments_df, output_file):
    plt.figure(figsize=(10, 6))
    sns.histplot(sentiments_df, x='compound', kde=True, bins=30, color='skyblue')
    plt.title('Distribution of Sentiment Scores')
    plt.xlabel('Compound Sentiment Score')
    plt.ylabel('Frequency')
    plt.savefig(output_file)
    plt.close()
