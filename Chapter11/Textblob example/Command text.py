from textblob import TextBlob
text = 'Tomorrow will be a great weekend for us'
blob = TextBlob(text)

blob.detect_language()
chinese = blob.translate(to = 'zh')
chinese
spanish = blob.translate(to = 'es')
spanish

# Polarity: -1.0 (Negative) to 1.0 (Positive)
# Subjectivity : 0.0 (Objective) to 1.0 (Subjective)
blob.sentiment

text1 = 'Yesterday was a beautiful day but today looks like bad weather'
blob1 = TextBlob(text1)
blob1.sentiment
