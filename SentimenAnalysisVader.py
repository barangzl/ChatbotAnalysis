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

output_file = "results.txt"


with open(output_file, "w", encoding="utf-8") as file: # Output doysanını oluştur
    # Metinlerin Duygusal Skorlarını Hesapla ve flagslare göre ayır
    for i, (response, flag) in enumerate(zip(responses, flags), start=1):
        scores = sid.polarity_scores(response)
        file.write(f"{i}. \"{response}\"\n")
        file.write("   Duygusal Skorlar: " + str(scores) + "\n")
        
        # Skorlar
        if scores['compound'] >= 0.05:
            file.write("   Yorum: Olumlu\n")
        elif scores['compound'] <= -0.009:
            file.write("   Yorum: Olumsuz\n")
        else:
            file.write("   Yorum: Nötr\n")
        
        # Flagsler
        file.write("   Flags: " + str(flag) + "\n")
        file.write("\n")
