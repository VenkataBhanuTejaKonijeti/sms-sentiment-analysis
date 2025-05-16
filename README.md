# SMS Sentiment Analysis with TextBlob

A simple Python project that analyzes the sentiment of SMS messages as Positive, Negative, or Neutral using the TextBlob library.

## Features

- Analyze sentiment of a single SMS message input by the user
- Perform bulk sentiment analysis on a list of SMS messages
- Save results to a text file for easy access and sharing
- Compatible with Google Colab for easy running and file download

## How It Works

The sentiment polarity score from TextBlob determines the sentiment:
- Polarity > 0 : Positive 😊
- Polarity < 0 : Negative 😠
- Polarity = 0 : Neutral 😐

## Setup Instructions

1. Install TextBlob and download required corpora:

    ```bash
    pip install textblob
    python -m textblob.download_corpora
    ```

2. Run the Python script or notebook to:
   - Input SMS messages for sentiment analysis
   - Analyze a batch of messages
   - Save and download the results file (in Google Colab)

## Running in Google Colab

To run this project in Google Colab:

1. Open a new Colab notebook.
2. Copy and paste the code into a cell.
3. Install TextBlob and download corpora by running:

    ```python
    !pip install -q textblob
    !python -m textblob.download_corpora
    ```

4. Run the sentiment analysis code cell.
5. Use the provided code to analyze messages interactively or in bulk.
6. Download the sentiment results file using:

    ```python
    from google.colab import files
    files.download("sentiment_results.txt")
    ```

## Sample Usage

```python
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

message = "I love this phone!"
print(f"Message: {message}")
print(f"Sentiment: {analyze_sentiment(message)}")
