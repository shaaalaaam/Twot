from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import csv

tweets = []

with open('twitter_dataset.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        tweet = row[5]  # Get the tweet text from the 6th column
        tweets.append(tweet)

# print(tweets)


# Replace with your API key and endpoint
key = "50020ee4adeb4029bb7144f5579b9150"
endpoint = "https://languageinstanceforsentimentanalysis.cognitiveservices.azure.com/"

# Authenticate the client
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Sample list of tweets
tweets = [
    "This product is amazing!",
    "I'm so disappointed with the customer service.",
    "Just had the best experience with this company.",
]

# Call the sentiment analysis function on the tweets
response = client.analyze_sentiment(tweets)

# Process the results of the sentiment analysis
for idx, doc in enumerate(response):
    print("Tweet: {}".format(tweets[idx]))
    print("Sentiment: {}".format(doc.sentiment))
    print("Confidence scores: Positive={:.2f}; Neutral={:.2f}; Negative={:.2f}\n".format(
        doc.confidence_scores.positive,
        doc.confidence_scores.neutral,
        doc.confidence_scores.negative,
    ))
