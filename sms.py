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

# ✅ Analyze a single SMS message
sms = input("📩 Enter an SMS message to analyze: ")
result = analyze_sentiment(sms)
print("Sentiment:", result)

# ✅ Analyze a list of sample SMS messages
print("\n--- Bulk SMS Sentiment Analysis ---\n")
sms_list = [
    "I love this phone!",
    "This product is terrible.",
    "I'll think about it.",
    "Worst experience ever",
    "I'm not sure how I feel."
]

results = []
for s in sms_list:
    sentiment = analyze_sentiment(s)
    print(f"Message: {s}")
    print(f"Sentiment: {sentiment}")
    print("---")
    results.append(f"{s} -> {sentiment}")

# ✅ Save results to a file
with open("sentiment_results.txt", "w") as f:
    for line in results:
        f.write(line + "\n")

# ✅ For Google Colab: Download results file
try:
    from google.colab import files
    files.download("sentiment_results.txt")
except:
    print("Download supported only in Google Colab.")
