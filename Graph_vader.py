import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_csv("sentiment_analysis_results_vl.csv")
top_flags = df['flags'].value_counts().head(20)

df_top_flags = df[df['flags'].isin(top_flags.index)]

sentiment_counts = df_top_flags.groupby(['flags', 'sentiment']).size().unstack(fill_value=0)
sentiment_counts.drop(columns="Positive",inplace=True)
plt.figure(figsize=(12, 8))
sentiment_counts.plot(kind='bar', stacked=False)

plt.title('Sentiment Distribution Across Top 20 Flags - VADER')
plt.xlabel('Flags')
plt.ylabel('Count')
plt.xticks(rotation=45)

plt.legend(title='Sentiment')
plt.tight_layout()
plt.show()
#plt.savefig("vl_figure.png")


