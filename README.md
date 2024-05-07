# Sentiment Analysis with Vaderlexicon and TextBlob

This repository contains code for sentiment analysis performed on the Bitext dataset using two popular sentiment analysis models - Vaderlexicon and TextBlob. The goal of this project is to analyze the sentiment of text data from the Bitext dataset and compare the performance of the two models.

## Dataset

The dataset contains chatbot conversations with the following columns:

- `flags`: Flags associated with each conversation.
- `instruction`: Instructions or commands given during the conversation.
- `category`: Categorization of the conversation.
- `intent`: Intent behind the conversation.
- `response`: Responses provided by the chatbot during the conversation.

The dataset comprises various chatbot interactions and serves as the basis for sentiment analysis using Vaderlexicon and TextBlob models.

## Dependencies

- Python 3.x
- pandas
- nltk
- TextBlob
- vaderSentiment

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt

## Usage

1. **Data Preparation**: Download the Bitext dataset.

2. **Sentiment Analysis with Vaderlexicon**: Run the `SentimentAnalysisVader.py` script to perform sentiment analysis using the Vaderlexicon model. This script will generate sentiment scores for each text instance in the dataset.

3. **Sentiment Analysis with TextBlob**: Run the `SentimentAnalysisBlob.py` script to perform sentiment analysis using the TextBlob model. This script will generate sentiment scores for each text instance in the dataset.

4. **Evaluation (Work in Progress)**: The evaluation of the sentiment analysis models with each other and categorize the results for further evaluation. Results will be provided once the evaluation is complete.


## Results

The results of the sentiment analysis for Vaderlexicon are provided in the `results.txt` file, and for TextBlob, they are provided in the `sentiment_analysis_results.csv` file.

