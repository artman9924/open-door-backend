from textblob import TextBlob

MODERATION_KEYWORDS = ['suicide', 'kill', 'abuse', 'hate', 'die', 'harm']

def analyze_emotion(message):
    polarity = TextBlob(message).sentiment.polarity
    if polarity > 0.4:
        return "hopeful"
    elif polarity > 0.1:
        return "relieved"
    elif polarity < -0.4:
        return "angry"
    elif polarity < -0.1:
        return "sad"
    else:
        return "neutral"
