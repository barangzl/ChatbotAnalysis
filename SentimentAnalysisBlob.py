from enum import Flag
import pandas as pd
from textblob import TextBlob


df = pd.read_csv("bitext_customer_support.csv")

# Gerekli stunları al
responses = df['response'].tolist()
flags     = df['flags'].tolist()

# Duygu Analizi Modeli yükle ve oluştur
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Olumlu'
    elif polarity < 0:
        return 'Olumsuz'
    else:
        return 'Nötr'

# Metinlerin Duygusal Skorlarını Hesapla ve flagslare göre ayır
sentiments = [analyze_sentiment(response) for response in responses]

# Sonuçları DataFrame'e ekle
df['sentiment'] = sentiments

output_file = "sentiment_analysis_results.csv"
df.to_csv(output_file, index=False) # Yeni dataframe i kayıt et

# Metinlerin Duygusal Skorlarını Hesapla ve flagslere göre ayır
sentiments = [analyze_sentiment(response) for response in responses]

# Olumsuz sayısını hesapla
negative_count = sentiments.count("Olumsuz")

print("Olumsuz durumlardaki metin sayısı:", negative_count)
