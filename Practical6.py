from textblob import TextBlob

# Input text
text = "I love this product, it is amazing!"

# Create object
analysis = TextBlob(text)

# Sentiment
polarity = analysis.sentiment.polarity

# Output
if polarity > 0:
    print("Positive 😊")
elif polarity < 0:
    print("Negative 😠")
else:
    print("Neutral 😐")