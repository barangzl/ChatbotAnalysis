from enum import Flag
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Duygu Analizi Modeli
nltk.download('vader_lexicon')

df = pd.read_csv("bitext_customer_support.csv")

# Gerekli stunu al
responses = df['response'].tolist()
flags     = df['flags'].tolist()

# Duygu Analizi Modelini Oluştur
sid = SentimentIntensityAnalyzer()

sentiments = []


# Metinlerin Duygusal Skorlarını Hesapla ve flagslare göre ayır
for i, (response, flag) in enumerate(zip(responses, flags), start=1):
    scores = sid.polarity_scores(response)
    # Skorlar
    if scores['compound'] >= 0.01:
        sentiment = "Positive"
    elif scores['compound'] <= -0.01:
        sentiment = "Olumsuz"
    else:
        sentiment = "Neutral"
    sentiments.append(sentiment)

df['sentiment'] = sentiments

output_file = "sentiment_analysis_results_vl.csv"
df.to_csv(output_file, index=False)