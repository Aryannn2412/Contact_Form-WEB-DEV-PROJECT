from textblob import TextBlob

def is_spam(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity < -0.3  # Negative sentiment likely spam
